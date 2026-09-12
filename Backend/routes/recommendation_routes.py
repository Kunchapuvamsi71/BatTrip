from flask import Blueprint, jsonify, request

from services.recommendation_service import get_recommendations


recommendation_bp = Blueprint("recommendation", __name__)


@recommendation_bp.route("/api/recommendations", methods=["GET"])
def get_recommendation_api():
    destination = request.args.get("place", "").strip()
    interest = request.args.get("interest", "").strip() or None
    budget_raw = request.args.get("budget", "").strip()

    if not destination:
        return jsonify({
            "status": "error",
            "message": "Please provide a destination"
        }), 400

    budget = None

    if budget_raw:
        try:
            budget = float(budget_raw)
        except ValueError:
            return jsonify({
                "status": "error",
                "message": "Budget must be a valid number"
            }), 400

    recommendations = get_recommendations(
        destination,
        interest,
        budget
    )

    return jsonify({
        "status": "success",
        "place": destination,
        "interest": interest,
        "budget": budget,
        "recommendations": recommendations
    })