# BatTrip & SpiderRoam API Documentation

## Base URL

http://127.0.0.1:5000

## 1. Test API

GET /api/test

## 2. Destinations

GET /api/destinations

Returns the available destinations.

## 3. Recommendations

GET /api/recommendations?place=Munnar

Returns recommended tourist places.

## 4. Location

GET /api/location?place=Munnar

Returns latitude and longitude of a location.

## 5. Create Trip

POST /api/trip

Creates a trip using the provided travel details.

## Project Status

Backend APIs are being developed using Flask.