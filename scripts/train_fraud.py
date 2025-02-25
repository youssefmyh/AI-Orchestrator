import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

X_train = np.array([[100, 14, 1], [5000, 2, 0], [20, 18, 1], [3000, 23, 0]])
y_train = np.array([0, 1, 0, 1])  

model = RandomForestClassifier()
model.fit(X_train, y_train)
joblib.dump(model, "fraud_detection_service/model.pkl")
print("✅ Fraud detection model trained!")
