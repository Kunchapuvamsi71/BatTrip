from flask import Flask, jsonify
from flask_cors import CORS

from routes.destination_routes import destination_bp
from routes.recommendation_routes import recommendation_bp
from routes.location_routes import location_bp
from routes.trip_routes import trip_bp
from routes.auth_routes import auth_bp
from routes.accommodation_routes import accommodation_bp
from routes.bike_routes import bike_bp
from routes.food_routes import food_bp

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register all routes
app.register_blueprint(destination_bp)
app.register_blueprint(recommendation_bp)
app.register_blueprint(location_bp)
app.register_blueprint(trip_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(accommodation_bp)
app.register_blueprint(bike_bp)
app.register_blueprint(food_bp)


@app.route("/")
def home():
    return jsonify({
        "project": "BatTrip & SpiderRoam",
        "message": "Backend is working!",
        "status": "success"
    })


@app.route("/api/test")
def test():
    return jsonify({
        "message": "API connection successful!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
