from flask import Blueprint, jsonify, request
from database.db_connection import get_db_connection

food_bp = Blueprint("food", __name__)


@food_bp.route("/api/food", methods=["GET"])
def get_food():
    destination = request.args.get("destination", "").strip()

    if not destination:
        return jsonify({
            "status": "error",
            "message": "Please provide a destination"
        }), 400

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                f.id,
                f.name,
                d.name AS destination,
                f.food_type,
                f.average_cost,
                f.rating,
                f.speciality,
                f.address
            FROM food_places f
            LEFT JOIN destinations d
                ON f.destination_id = d.id
            WHERE LOWER(d.name) = LOWER(%s)
            ORDER BY f.rating DESC
        """

        cursor.execute(query, (destination,))
        food_places = cursor.fetchall()

        return jsonify({
            "status": "success",
            "destination": destination,
            "food": food_places
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()