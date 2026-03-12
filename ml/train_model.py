import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("data/csi_dataset.csv")

X = data[["mean","std","max","min","energy"]]
y = data["label"]

model = RandomForestClassifier(n_estimators=100)

model.fit(X,y)

joblib.dump(model,"models/model.pkl")

print("Model trained and saved")