from flask import Blueprint, jsonify, request
from database.db_connection import get_db_connection

bike_bp = Blueprint("bike", __name__)


@bike_bp.route("/api/bikes", methods=["GET"])
def get_bikes():
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
                b.id,
                b.shop_name,
                d.name AS destination,
                b.bike_type,
                b.price_per_day,
                b.rating,
                b.address,
                b.contact
            FROM bike_rentals b
            LEFT JOIN destinations d
                ON b.destination_id = d.id
            WHERE LOWER(d.name) = LOWER(%s)
            ORDER BY b.rating DESC
        """

        cursor.execute(query, (destination,))
        bikes = cursor.fetchall()

        return jsonify({
            "status": "success",
            "destination": destination,
            "bikes": bikes
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