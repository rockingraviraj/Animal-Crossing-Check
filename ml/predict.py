import joblib
from config.settings import MODEL_PATH

model = joblib.load(MODEL_PATH)

def predict(features):

    prediction = model.predict([features])

    return prediction[0]