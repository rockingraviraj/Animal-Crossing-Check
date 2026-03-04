import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# dataset load
data = pd.read_csv("data/csi_data.csv")

# features and labels
X = data[["signal"]]
y = data["label"]

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestClassifier()

# training
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)

# confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("Confusion Matrix:")
print(cm)

# save model
joblib.dump(model, "models/model.pkl")

print("Model saved successfully")