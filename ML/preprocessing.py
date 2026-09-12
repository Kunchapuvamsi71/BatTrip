import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# Load tourism dataset
data = pd.read_csv("dataset/tourism_dataset.csv")


# Combine important text information
data["features"] = (
    data["Name"].fillna("") + " " +
    data["Destination"].fillna("") + " " +
    data["State"].fillna("") + " " +
    data["Type"].fillna("") + " " +
    data["Interest"].fillna("") + " " +
    data["Description"].fillna("")
)


# Convert text features into numerical values
vectorizer = TfidfVectorizer(stop_words="english")

feature_matrix = vectorizer.fit_transform(data["features"])


print("===================================")
print("BatTrip & SpiderRoam")
print("Tourism Data Preprocessing")
print("===================================")

print("Dataset loaded successfully!")
print("Number of tourist places:", len(data))
print("Number of features:", feature_matrix.shape[1])
print("Preprocessing completed successfully!")