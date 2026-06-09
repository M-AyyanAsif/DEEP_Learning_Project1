import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    
    # Load model only once
    model = load_model("trained_model.h5")

    def __init__(self, filename):
        self.filename = filename

    def predict(self):

        test_image = image.load_img(
            self.filename,
            target_size=(224, 224)
        )

        test_image = image.img_to_array(test_image)

        # IMPORTANT: normalize image
        test_image = test_image / 255.0

        test_image = np.expand_dims(test_image, axis=0)

        prediction_probs = self.model.predict(test_image)

        print("Prediction Probabilities:", prediction_probs)

        result = np.argmax(prediction_probs, axis=1)

        print("Predicted Class:", result)

        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]