from flask import Blueprint, jsonify, request
import requests


location_bp = Blueprint("location", __name__)


@location_bp.route("/api/location", methods=["GET"])
def get_location():

    place = request.args.get("place", "").strip()

    if not place:
        return jsonify({
            "message": "Please provide a location",
            "status": "error"
        }), 400

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "BatTrip-SpiderRoam"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    if response.status_code != 200:
        return jsonify({
            "message": "Location service unavailable",
            "status": "error"
        }), 500

    results = response.json()

    if not results:
        return jsonify({
            "message": "Location not found",
            "status": "error"
        }), 404

    location = results[0]

    return jsonify({
        "name": location.get("display_name"),
        "latitude": float(location.get("lat")),
        "longitude": float(location.get("lon")),
        "status": "success"
    })