import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# load dataset
df = pd.read_csv("data/Training.csv")

print(df.columns)

# features & target
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2,
    random_state=42
)

# model training
# model = DecisionTreeClassifier()
model = RandomForestClassifier(n_estimators=200)
# fit the model
model.fit(X_train, y_train)

# model prediction
predictions = model.predict(X_test)

# model evaluation
accuracy = accuracy_score(y_test, predictions)

# result
print(f"Accuracy Score Prediction: {accuracy * 100:.2f}%")

# save the model
pickle.dump(model, open("models/training_disease_model.pkl", "wb"))

# print the result
print("Disease Prediction Model Saved!")