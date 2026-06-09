import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    
    def __init__(self, filename):
        self.filename = filename
        
        # 1. Anchor the path dynamically to the root directory where 'trained_model.h5' sits
        # Go up 4 levels from this file (src/cnn_classifier/pipeline/prediction.py) to reach the root
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.abspath(os.path.join(current_dir, "../../../.."))
        model_path = os.path.join(root_dir, "trained_model.h5")
        
        # 2. Safety Check: Fallback to local root if path resolution acts up in Docker
        if not os.path.exists(model_path):
            model_path = "trained_model.h5"
            
        # 3. Load model instance safely for this execution context
        self.model = load_model(model_path)

    def predict(self):
        # Load the target image payload
        test_image = image.load_img(
            self.filename,
            target_size=(224, 224)
        )

        test_image = image.img_to_array(test_image)

        # Normalize pixel values
        test_image = test_image / 255.0

        # Expand dimensions to match batch size input shape: (1, 224, 224, 3)
        test_image = np.expand_dims(test_image, axis=0)

        # Run deep learning inference
        prediction_probs = self.model.predict(test_image)
        print("Prediction Probabilities:", prediction_probs)

        # Get class index with highest probability
        result = np.argmax(prediction_probs, axis=1)
        print("Predicted Class:", result)

        # Match label map thresholds
        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]