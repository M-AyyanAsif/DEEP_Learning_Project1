import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    
    def __init__(self, filename):
        self.filename = filename
        
        
        model_path = "trained_model.h5"
        
        
        if not os.path.exists(model_path):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            
            root_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
            model_path = os.path.join(root_dir, "trained_model.h5")
            
        print(f"Attempting to load model from verified path: {model_path}")
        self.model = load_model(model_path)

    def predict(self):
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        prediction_probs = self.model.predict(test_image)
        result = np.argmax(prediction_probs, axis=1)

        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]