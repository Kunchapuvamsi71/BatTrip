from flask import Blueprint, jsonify, request

from services.itinerary_service import create_itinerary
from services.budget_service import calculate_budget
from utils.validators import validate_trip_data
from database.db_connection import get_db_connection


trip_bp = Blueprint("trip", __name__)


# ==========================================
# CREATE / SAVE TRIP
# ==========================================

@trip_bp.route("/api/trip", methods=["POST"])
def create_trip():

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Trip data is required",
            "status": "error"
        }), 400


    try:

        days = int(data.get("days", 0))
        people = int(data.get("people", 0))
        budget = float(data.get("budget", 0))

    except (ValueError, TypeError):

        return jsonify({
            "message": "Invalid trip numbers",
            "status": "error"
        }), 400


    destinations = data.get("destinations", [])

    validation = validate_trip_data(
        days,
        people,
        budget
    )


    if not validation["valid"]:

        return jsonify({
            "message": "Invalid trip data",
            "errors": validation["errors"],
            "status": "error"
        }), 400


    # ==========================================
    # CREATE ITINERARY
    # ==========================================

    itinerary = create_itinerary(
        destinations,
        days
    )


    # ==========================================
    # CALCULATE BUDGET
    # ==========================================

    fuel_cost = float(data.get("fuel_cost", 0))
    accommodation_cost = float(
        data.get("accommodation_cost", 0)
    )
    food_cost = float(
        data.get("food_cost", 0)
    )
    transport_cost = float(
        data.get("transport_cost", 0)
    )
    activity_cost = float(
        data.get("activity_cost", 0)
    )


    budget_result = calculate_budget(
        fuel_cost,
        accommodation_cost,
        food_cost,
        transport_cost,
        activity_cost,
        budget
    )


    # ==========================================
    # USER ID
    # ==========================================

    user_id = data.get("user_id")


    # ==========================================
    # SAVE TRIP TO DATABASE
    # ==========================================

    connection = None
    cursor = None

    try:

        connection = get_db_connection()
        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO trips
            (
                user_id,
                start_location,
                days,
                people,
                budget,
                total_cost
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            """,
            (
                user_id,
                data.get("start_location", ""),
                days,
                people,
                budget,
                budget_result.get("total_cost", 0)
            )
        )


        trip_id = cursor.lastrowid

        connection.commit()


        return jsonify({

            "status": "success",

            "message": "Trip created successfully",

            "trip_id": trip_id,

            "days": days,

            "people": people,

            "destinations": destinations,

            "itinerary": itinerary,

            "budget": budget_result

        })


    except Exception as error:

        if connection:
            connection.rollback()

        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500


    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()



# ==========================================
# GET MY TRIPS
# ==========================================

@trip_bp.route("/api/trips/<int:user_id>", methods=["GET"])
def get_my_trips(user_id):

    connection = None
    cursor = None

    try:

        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )


        cursor.execute(
            """
            SELECT
                id,
                user_id,
                start_location,
                days,
                people,
                budget,
                total_cost,
                created_at
            FROM trips
            WHERE user_id = %s
            ORDER BY id DESC
            """,
            (user_id,)
        )


        trips = cursor.fetchall()


        return jsonify({

            "status": "success",

            "trips": trips

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