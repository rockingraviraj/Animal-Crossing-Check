import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.feature_extraction import extract_features

X = np.load("data/X.npy")
y = np.load("data/y.npy")

X_features = np.array([extract_features(sample) for sample in X])

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X_features, y_encoded, test_size=0.2, random_state=42
)

rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
print(classification_report(y_test, y_pred))

pickle.dump(rf_model, open("models/rf_model.pkl", "wb"))
pickle.dump(encoder, open("models/label_encoder.pkl", "wb"))

print("Random Forest Model Saved Successfully!")