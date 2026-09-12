CREATE DATABASE IF NOT EXISTS battrip_spiderroam;

USE battrip_spiderroam;


-- Users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Destinations
CREATE TABLE IF NOT EXISTS destinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL
);


-- Tourist Places
CREATE TABLE IF NOT EXISTS tourist_places (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    state VARCHAR(100),
    destination_id INT,
    type VARCHAR(100),
    rating DECIMAL(2,1),
    popularity INT,
    cost DECIMAL(10,2),
    duration INT,
    interest VARCHAR(255),
    description TEXT,

    FOREIGN KEY (destination_id)
        REFERENCES destinations(id)
        ON DELETE SET NULL
);


-- Accommodation
CREATE TABLE IF NOT EXISTS accommodations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    destination_id INT,
    stay_type VARCHAR(50),
    price_per_night DECIMAL(10,2),
    rating DECIMAL(2,1),
    facilities VARCHAR(255),

    FOREIGN KEY (destination_id)
        REFERENCES destinations(id)
        ON DELETE SET NULL
);


-- Bike Rentals
CREATE TABLE IF NOT EXISTS bike_rentals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    shop_name VARCHAR(150) NOT NULL,
    destination_id INT,
    bike_type VARCHAR(100),
    price_per_day DECIMAL(10,2),
    rating DECIMAL(2,1),
    address VARCHAR(255),
    contact VARCHAR(50),

    FOREIGN KEY (destination_id)
        REFERENCES destinations(id)
        ON DELETE SET NULL
);


-- Food Places
CREATE TABLE IF NOT EXISTS food_places (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    destination_id INT,
    food_type VARCHAR(100),
    average_cost DECIMAL(10,2),
    rating DECIMAL(2,1),
    speciality VARCHAR(255),
    address VARCHAR(255),

    FOREIGN KEY (destination_id)
        REFERENCES destinations(id)
        ON DELETE SET NULL
);


-- User Preferences
CREATE TABLE IF NOT EXISTS user_preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    interest VARCHAR(100),
    budget DECIMAL(10,2),
    preferred_transport VARCHAR(100),

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);


-- Trips
CREATE TABLE IF NOT EXISTS trips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    start_location VARCHAR(150),
    days INT,
    people INT,
    budget DECIMAL(10,2),
    transport VARCHAR(100),
    mileage DECIMAL(10,2),
    fuel_price DECIMAL(10,2),
    total_cost DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);


-- Trip Places
CREATE TABLE IF NOT EXISTS trip_places (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT,
    tourist_place_id INT,
    visit_day INT,

    FOREIGN KEY (trip_id)
        REFERENCES trips(id)
        ON DELETE CASCADE,

    FOREIGN KEY (tourist_place_id)
        REFERENCES tourist_places(id)
        ON DELETE CASCADE
);


-- Recommendations
CREATE TABLE IF NOT EXISTS recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    tourist_place_id INT,
    score DECIMAL(5,2),
    reason TEXT,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    FOREIGN KEY (tourist_place_id)
        REFERENCES tourist_places(id)
        ON DELETE CASCADE
);