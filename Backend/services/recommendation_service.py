import os
import pickle


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

ML_DIR = os.path.join(BASE_DIR, "ML")

MODEL_PATH = os.path.join(
    ML_DIR,
    "saved_models",
    "tourism_model.pkl"
)


def load_model():
    if not os.path.exists(MODEL_PATH):
        return None

    try:
        with open(MODEL_PATH, "rb") as file:
            return pickle.load(file)

    except Exception as error:
        print("ML model loading error:", error)
        return None


def get_recommendations(destination, interest=None, budget=None, number_of_places=5):

    model = load_model()

    if model is None:
        return []

    try:
        data = model["data"]
        similarity_matrix = model["similarity_matrix"]

        destination = destination.strip().lower()

        places = data[
            data["Destination"].astype(str).str.lower()
            == destination
        ].copy()

        if places.empty:
            return []

        recommendations = []

        for index in places.index:

            score = 0

            rating_score = (
                float(data.loc[index, "Rating"]) / 5
            ) * 30

            popularity_score = (
                float(data.loc[index, "Popularity"]) / 100
            ) * 20

            interest_score = 0

            if interest:
                place_interests = str(
                    data.loc[index, "Interest"]
                ).lower()

                if interest.lower() in place_interests:
                    interest_score = 20

            budget_score = 0

            if budget is not None:

                try:
                    place_cost = float(
                        data.loc[index, "Cost"]
                    )

                    if place_cost <= float(budget):
                        budget_score = 15

                except (ValueError, TypeError):
                    pass

            ml_score = 0

            similarity_scores = list(
                enumerate(similarity_matrix[index])
            )

            similarity_scores.sort(
                key=lambda x: x[1],
                reverse=True
            )

            for similar_index, similarity in similarity_scores:

                if similar_index != index:
                    ml_score = float(similarity) * 10
                    break

            score = (
                rating_score
                + popularity_score
                + interest_score
                + budget_score
                + ml_score
            )

            if score > 100:
                score = 100

            if interest and interest.lower() in str(
                data.loc[index, "Interest"]
            ).lower():

                reason = (
                    f"Matches your {interest} interest, "
                    "with strong rating and popularity."
                )

            elif budget is not None and float(
                data.loc[index, "Cost"]
            ) <= float(budget):

                reason = (
                    "Fits your activity budget "
                    "and has a good rating."
                )

            else:

                reason = (
                    "Highly rated and popular "
                    "tourist attraction."
                )

            recommendations.append({
                "name": data.loc[index, "Name"],
                "destination": data.loc[index, "Destination"],
                "state": data.loc[index, "State"],
                "type": data.loc[index, "Type"],
                "rating": float(data.loc[index, "Rating"]),
                "popularity": int(data.loc[index, "Popularity"]),
                "cost": float(data.loc[index, "Cost"]),
                "duration": int(data.loc[index, "Duration"]),
                "interest": data.loc[index, "Interest"],
                "description": data.loc[index, "Description"],
                "score": round(score, 2),
                "reason": reason
            })

        recommendations.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return recommendations[:number_of_places]

    except Exception as error:

        print("ML recommendation error:", error)

        return []