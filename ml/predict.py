import joblib
from config.settings import MODEL_PATH
# this is for the prediction for the model
model = joblib.load(MODEL_PATH)

def predict(features):

    prediction = model.predict([features])

    return prediction[0]
