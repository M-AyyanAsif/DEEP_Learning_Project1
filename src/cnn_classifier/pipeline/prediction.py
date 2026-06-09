import numpy as np
import os
import h5py
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def patch_h5_model(model_path):
    """
    Strips out incompatible Keras 3 metadata keywords from legacy h5 layer configurations
    to prevent deserialization TypeErrors.
    """
    try:
        with h5py.File(model_path, 'r+') as f:
            if 'model_config' in f.attrs:
                config_data = json.loads(f.attrs['model_config'])
                
                # Dig into the layers configuration list
                if 'config' in config_data and 'layers' in config_data['config']:
                    modified = False
                    for layer in config_data['config']['layers']:
                        # Focus directly on the problematic InputLayer or dense setups
                        if 'config' in layer:
                            layer_config = layer['config']
                            # Remove the keys crashing the Keras engine
                            for bad_key in ['batch_shape', 'optional', 'quantization_config']:
                                if bad_key in layer_config:
                                    del layer_config[bad_key]
                                    modified = True
                    
                    if modified:
                        # Write the sanitized configuration back to the file
                        f.attrs['model_config'] = json.dumps(config_data).encode('utf-8')
                        print("Successfully sanitized model layer configuration attributes.")
    except Exception as e:
        print(f"Self-healing patch skipped or unneeded: {str(e)}")

class PredictionPipeline:
    
    def __init__(self, filename):
        self.filename = filename
        
        model_path = "trained_model.h5"
        
        if not os.path.exists(model_path):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            root_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
            model_path = os.path.join(root_dir, "trained_model.h5")
            
            if not os.path.exists(model_path):
                model_path = "/home/user/app/trained_model.h5"
            
        print(f"Attempting to load model from verified path: {model_path}")
        
        # Run the validation sanitization patch before passing to Keras load_model
        patch_h5_model(model_path)
        
        self.model = load_model(model_path, compile=False)

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