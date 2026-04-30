from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

data = pd.read_csv("data/csi_dataset.csv")

X = data[["mean","std","max","min","energy"]]
y = data["label"]

pred = model.predict(X)

print("Accuracy:", accuracy_score(y, pred))
print("Confusion Matrix:\n", confusion_matrix(y, pred))