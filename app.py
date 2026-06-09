import os
import tempfile
import traceback
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from cnn_classifier.utils.common import decodeImage
from cnn_classifier.pipeline.prediction import PredictionPipeline

# Ensure standard UTF-8 text streaming environments
os.environ["LANG"] = "en_US.UTF-8"
os.environ["LC_ALL"] = "en_US.UTF-8"

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    # Using python executable safety flag in cloud containers
    exit_code = os.system("python main.py")
    if exit_code != 0:
        return jsonify({"error": "Training pipeline failed execution"}), 500
    return "Training completed successfully"

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    try:
        data = request.get_json()

        if not data or "image" not in data:
            return jsonify({"error": "No image data found in request"}), 400

        image_data = data["image"]

        # Create a dynamic, thread-safe secure temp file inside the OS container storage layer
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_img:
            temp_filename = temp_img.name

        try:
            
            decodeImage(image_data, temp_filename)

            # Instantiate the prediction pipeline safely per-request
            classifier = PredictionPipeline(temp_filename)
            result = classifier.predict()

            return jsonify(result)

        finally:
            # Clean up the container space instantly after inference to prevent memory leaks
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    except Exception as e:
        
        print("\n" + "="*50)
        print("!!! INFERENCE CRASH DETECTED !!!")
        print(traceback.format_exc())
        print("="*50 + "\n")
        
        return jsonify({"error": f"Inference Pipeline Error: {str(e)}"}), 500

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)