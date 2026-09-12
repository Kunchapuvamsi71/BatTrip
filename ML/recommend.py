import pickle


# Load the trained tourism model
with open("saved_models/tourism_model.pkl", "rb") as file:
    model = pickle.load(file)


data = model["data"]
vectorizer = model["vectorizer"]
similarity_matrix = model["similarity_matrix"]


def recommend_places(place_name, number_of_places=5):

    # Find the selected place
    matches = data[
        data["Name"].str.lower() == place_name.lower()
    ]

    if matches.empty:
        print("Place not found!")
        return

    place_index = matches.index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity_matrix[place_index])
    )

    # Sort by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Places")
    print("==========================")

    count = 0

    for index, score in similarity_scores:

        # Don't recommend the same place
        if index == place_index:
            continue

        print(
            data.iloc[index]["Name"],
            "-",
            data.iloc[index]["Destination"],
            "| Similarity:",
            round(score * 100, 2),
            "%"
        )

        count += 1

        if count == number_of_places:
            break


# Test recommendation
recommend_places("Munnar", 5)