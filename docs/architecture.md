# BatTrip & SpiderRoam – System Architecture

## 1. Frontend

The frontend is developed using:

- HTML
- CSS
- JavaScript

It provides the user interface for trip planning, recommendations, stays, bike rentals and food.

## 2. Backend

The backend is developed using:

- Python
- Flask

The backend provides REST APIs for:

- Destinations
- Trip planning
- Recommendations
- Location services
- Budget calculation
- Itinerary generation

## 3. Database

MySQL is used to store:

- Users
- Destinations
- Tourist places
- Accommodations
- Bike rentals
- Food places
- Trips
- Recommendations

## 4. AI/ML

The recommendation system uses:

- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity

The ML component recommends tourist places based on tourism-related features.

## 5. External Services

The project can use:

- OpenStreetMap / Nominatim for location search
- OSRM for road-distance calculation
- Open-Meteo for weather information

## 6. Overall Flow

User
↓
Frontend
↓
Flask Backend
↓
Services
↓
MySQL Database / ML Model / External APIs
↓
Recommendation and Trip Result