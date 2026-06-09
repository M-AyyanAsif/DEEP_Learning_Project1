import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    
    def __init__(self, filename):
        self.filename = filename
        
        # 1. Start with a direct fallback path
        model_path = "trained_model.h5"
        
        # 2. If it's not found in the immediate working directory, resolve the path dynamically
        if not os.path.exists(model_path):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up 3 levels from src/cnn_classifier/pipeline/prediction.py to reach the root dir
            root_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
            model_path = os.path.join(root_dir, "trained_model.h5")
            
            # Double fallback check: if path calculation is off, force local root reference
            if not os.path.exists(model_path):
                model_path = "/home/user/app/trained_model.h5"
            
        print(f"Attempting to load model from verified path: {model_path}")
        
        # 3. CRITICAL FIX: compile=False bypasses structural metadata mismatches (e.g., 'batch_shape')
        self.model = load_model(model_path, compile=False)

    def predict(self):
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        # Scale pixel values down to [0, 1] exactly how it was trained
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        prediction_probs = self.model.predict(test_image)
        result = np.argmax(prediction_probs, axis=1)

        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]