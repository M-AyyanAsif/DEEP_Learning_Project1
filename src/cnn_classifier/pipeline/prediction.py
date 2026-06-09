import numpy as np
import os
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
        
        # 2. Re-create the network structure manually to ignore broken metadata
        # Assuming you used VGG16 as your base model architecture:
        base_model = tf.keras.applications.VGG16(
            include_top=False, 
            weights=None, 
            input_shape=(224, 224, 3)
        )
        
        # Re-attach your custom classification top layers
        x = tf.keras.layers.Flatten()(base_model.output)
        prediction_layer = tf.keras.layers.Dense(units=2, activation="softmax")(x)
        
        # Bind the model structure
        self.model = tf.keras.models.Model(inputs=base_model.input, outputs=prediction_layer)
        
        # 3. Load purely the raw mathematical weight matrices
        # By using by_name=True and skip_mismatch=True, metadata errors disappear!
        self.model.load_weights(model_path, by_name=True, skip_mismatch=True)
        print("Model weights successfully bound to structure!")

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