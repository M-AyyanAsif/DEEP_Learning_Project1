import numpy as np
import os
<<<<<<< HEAD
import tensorflow as tf
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    
    def __init__(self, filename):
        self.filename = filename
        
        # 1. Resolve path
        model_path = "trained_model.h5"
        if not os.path.exists(model_path):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            root_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
            model_path = os.path.join(root_dir, "trained_model.h5")
            if not os.path.exists(model_path):
                model_path = "/home/user/app/trained_model.h5"
            
        print(f"Loading raw weights from: {model_path}")
        
        
        base_model = tf.keras.applications.VGG16(
            include_top=False, 
            weights=None, 
            input_shape=(224, 224, 3)
        )
        
        # Re-attach your custom classification top layers
        x = tf.keras.layers.Flatten()(base_model.output)
        prediction_layer = tf.keras.layers.Dense(units=2, activation="softmax")(x)
        
        
        self.model = tf.keras.models.Model(inputs=base_model.input, outputs=prediction_layer)
        
        
        self.model.load_weights(model_path, by_name=True, skip_mismatch=True)
        print("Model weights successfully bound to structure!")

    def predict(self):
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        prediction_probs = self.model.predict(test_image)
        result = np.argmax(prediction_probs, axis=1)

=======
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    
    # Load model only once
    model = load_model(os.path.join("model", "trained_model.h5"))

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

>>>>>>> 578e7f68f7edccf75be8a865a97f6e32673e9426
        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]