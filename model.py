# model.py

import numpy as np
from keras.models import load_model

# Load the saved model
model = load_model('heart_model.h5')

# Prediction function
def predict(input_list):
    # Make sure input has 10 features
    data = np.array(input_list).reshape(1, 10)  # Shape: (1, 10)
    prediction = model.predict(data)
    return 'Risk' if prediction[0][0] > 0.5 else 'No Risk'

