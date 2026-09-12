from flask import Blueprint, jsonify, request

from database.db_connection import get_db_connection


accommodation_bp = Blueprint("accommodation", __name__)


@accommodation_bp.route("/api/accommodations", methods=["GET"])
def get_accommodations():

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
                a.id,
                a.name,
                d.name AS destination,
                a.stay_type,
                a.price_per_night,
                a.rating,
                a.facilities
            FROM accommodations a
            LEFT JOIN destinations d
                ON a.destination_id = d.id
            WHERE LOWER(d.name) = LOWER(%s)
            ORDER BY a.rating DESC
        """

        cursor.execute(query, (destination,))
        accommodations = cursor.fetchall()

        return jsonify({
            "status": "success",
            "destination": destination,
            "accommodations": accommodations
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