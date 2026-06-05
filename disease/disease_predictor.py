import pickle
import pandas as pd

model = pickle.load(
    open("models/training_disease_model.pkl", "rb")
)

# Load training columns
df = pd.read_csv("data/Training.csv")

symptoms = df.columns[:-1]

def predict_disease(selected_symptoms):

    input_data = [0] * len(symptoms)

    for symptom in selected_symptoms:

        if symptom in symptoms:

            index = list(symptoms).index(symptom)

            input_data[index] = 1

    prediction = model.predict([input_data])

    return prediction[0]