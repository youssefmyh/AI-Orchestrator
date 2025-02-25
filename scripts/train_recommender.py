import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([[101, 102], [201, 202], [301, 302], [401, 402], [501, 502]])

model = RandomForestClassifier()
model.fit(X_train, y_train)
joblib.dump(model, "recommender_service/model.pkl")
print("✅ Recommender model trained!")
