import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load tourism dataset
data = pd.read_csv("dataset/tourism_dataset.csv")


# Combine important information
data["features"] = (
    data["Name"].fillna("") + " " +
    data["Destination"].fillna("") + " " +
    data["State"].fillna("") + " " +
    data["Type"].fillna("") + " " +
    data["Interest"].fillna("") + " " +
    data["Description"].fillna("")
)


# Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words="english")

feature_matrix = vectorizer.fit_transform(data["features"])


# Calculate similarity between tourist places
similarity_matrix = cosine_similarity(feature_matrix)


# Save the trained model data
model = {
    "data": data,
    "vectorizer": vectorizer,
    "similarity_matrix": similarity_matrix
}


with open("saved_models/tourism_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("===================================")
print("BatTrip & SpiderRoam")
print("ML Model Training")
print("===================================")

print("Dataset loaded successfully!")
print("Tourist places:", len(data))
print("Feature matrix created!")
print("Similarity matrix created!")
print("Model saved successfully!")
print("===================================")