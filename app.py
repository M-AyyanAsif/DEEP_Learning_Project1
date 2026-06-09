import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from cnn_classifier.utils.common import decodeImage
from cnn_classifier.pipeline.prediction import PredictionPipeline

# Ensure standard UTF-8 text streaming environments
os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


clApp = ClientApp()

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training completed successfully"

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    try:
        data = request.get_json()

        if not data or "image" not in data:
            return jsonify({"error": "No image found in request"}), 400

        image_data = data["image"]

        # Safely extract and save binary payload
        decodeImage(image_data, clApp.filename)

        # Execute Deep Learning model inference
        result = clApp.classifier.predict()

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)