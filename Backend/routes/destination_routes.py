from flask import Blueprint, jsonify

from database.db_connection import get_db_connection

destination_bp = Blueprint("destination", __name__)


@destination_bp.route("/api/destinations", methods=["GET"])
def get_destinations():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT id, name, state FROM destinations ORDER BY name"
        )

        destinations = cursor.fetchall()

        return jsonify({
            "status": "success",
            "destinations": destinations
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