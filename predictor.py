from seeds_classifier.seed_classifier import SeedClassifier
import numpy as np

class PythonPredictor:
    def __init__(self, config):
        self.model = SeedClassifier()

    def predict(self, payload):
        area = payload["area"]
        perimeter = payload["perimeter"]
        compactness = payload["compactness"]
        length = payload["length"]
        width = payload['width']
        asymmetry = payload["asymmetry"]
        kernel_length = payload['kernel length']
        x_data = np.array([area, perimeter, compactness, length, width, asymmetry, kernel_length]).reshape(1,-1)
        return str((self.model.classify(x_data)))