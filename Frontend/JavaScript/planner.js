// BatTrip & SpiderRoam
// Complete Trip Planner + Flask Backend Connection

const PLANNER_API_URL = "http://127.0.0.1:5000";


// =========================
// SEND TRIP TO BACKEND
// =========================

async function sendTripToBackend(tripData) {

    // Get logged-in user
    const storedUser = localStorage.getItem("loggedInUser");

    if (storedUser) {

        try {

            const user = JSON.parse(storedUser);

            if (user.id) {
                tripData.user_id = user.id;
            }

        } catch (error) {

            console.error(
                "User data error:",
                error
            );
        }
    }


    try {

        const response = await fetch(
            `${PLANNER_API_URL}/api/trip`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(tripData)
            }
        );


        const result = await response.json();


        if (!response.ok) {

            console.error(
                "Trip API error:",
                result
            );

            return null;
        }


        console.log(
            "Trip result received from backend:"
        );

        console.log(result);


        return result;

    }

    catch (error) {

        console.error(
            "Backend connection error:",
            error
        );

        return null;
    }
}


// =========================
// ADD DESTINATION
// =========================

function addPlace() {

    let input =
        document.getElementById("destination");

    let name =
        input.value.trim();


    if (name === "") {

        alert("Enter a destination");

        return;
    }


    places.push(name);

    input.value = "";

    showPlaces();
}


// =========================
// SHOW DESTINATIONS
// =========================

function showPlaces() {

    let list =
        document.getElementById("list");

    list.innerHTML = "";


    for (
        let i = 0;
        i < places.length;
        i++
    ) {

        let div =
            document.createElement("div");

        div.className =
            "destination";


        div.innerHTML =
            (i + 1) +
            ". " +
            places[i] +
            ' <button class="remove-btn" onclick="removePlace(' +
            i +
            ')">Remove</button>';


        list.appendChild(div);
    }
}


// =========================
// REMOVE DESTINATION
// =========================

function removePlace(index) {

    places.splice(index, 1);

    showPlaces();
}


// =========================
// CURRENT LOCATION
// =========================

function useCurrentLocation() {

    let status =
        document.getElementById(
            "locationStatus"
        );


    if (!navigator.geolocation) {

        status.innerHTML =
            "❌ Location is not supported. Please enter your starting location manually.";

        return;
    }


    status.innerHTML =
        "📍 Getting your current location...";


    navigator.geolocation.getCurrentPosition(

        function (position) {

            let latitude =
                position.coords.latitude;

            let longitude =
                position.coords.longitude;


            status.innerHTML =
                "✅ Location detected: " +
                latitude.toFixed(4) +
                ", " +
                longitude.toFixed(4);
        },


        function (error) {

            status.innerHTML =
                "❌ Location permission denied. Please enter your starting location manually.";
        }

    );
}


// =========================
// GEOCODING
// =========================

async function getCoordinates(place) {

    let url =
        "https://nominatim.openstreetmap.org/search?q=" +
        encodeURIComponent(place) +
        "&format=json&limit=1";


    try {

        let response =
            await fetch(url);

        let data =
            await response.json();


        if (data.length === 0) {

            return null;
        }


        return {

            lat:
                parseFloat(data[0].lat),

            lon:
                parseFloat(data[0].lon)
        };

    }

    catch (error) {

        console.error(
            "Geocoding error:",
            error
        );

        return null;
    }
}


// =========================
// ROAD DISTANCE
// =========================

async function getDistance(
    start,
    destinations
) {

    let totalDistance = 0;

    let current = start;


    for (
        let i = 0;
        i < destinations.length;
        i++
    ) {

        let next =
            await getCoordinates(
                destinations[i]
            );


        if (!next) {

            continue;
        }


        let url =
            "https://router.project-osrm.org/route/v1/driving/" +
            current.lon +
            "," +
            current.lat +
            ";" +
            next.lon +
            "," +
            next.lat +
            "?overview=false";


        try {

            let response =
                await fetch(url);

            let data =
                await response.json();


            if (
                data.routes &&
                data.routes.length > 0
            ) {

                totalDistance +=
                    data.routes[0].distance /
                    1000;
            }

        }

        catch (error) {

            console.log(
                "Routing error:",
                error
            );
        }


        current = next;
    }


    return totalDistance;
}


// =========================
// BUILD TRIP
// =========================

async function buildTrip() {

    let output =
        document.getElementById(
            "output"
        );


    let startName =
        document
            .getElementById("startLocation")
            .value
            .trim();


    let days =
        parseInt(
            document
                .getElementById("days")
                .value
        );


    let people =
        parseInt(
            document
                .getElementById("people")
                .value
        );


    let budget =
        parseFloat(
            document
                .getElementById("budget")
                .value
        );


    let mileage =
        parseFloat(
            document
                .getElementById("mileage")
                .value
        );


    let petrol =
        parseFloat(
            document
                .getElementById("petrol")
                .value
        );


    let food =
        parseFloat(
            document
                .getElementById("food")
                .value
        );


    let activity =
        parseFloat(
            document
                .getElementById("activity")
                .value
        );


    let stay =
        parseFloat(
            document
                .getElementById("stay")
                .value
        );


    let transport =
        document
            .getElementById("transport")
            .value;


    let interest =
        document
            .getElementById("interest")
            .value;


    // =========================
    // VALIDATION
    // =========================

    if (startName === "") {

        alert(
            "Please enter starting location."
        );

        return;
    }


    if (places.length === 0) {

        alert(
            "Please add at least one destination."
        );

        return;
    }


    if (
        !days ||
        days <= 0
    ) {

        alert(
            "Please enter valid travel days."
        );

        return;
    }


    if (
        !people ||
        people <= 0
    ) {

        alert(
            "Please enter valid number of people."
        );

        return;
    }


    if (
        !budget ||
        budget <= 0
    ) {

        alert(
            "Please enter a valid budget."
        );

        return;
    }


    output.innerHTML =
        '<div class="result">' +
        '⏳ Building your trip... Please wait.' +
        '</div>';


    // =========================
    // GET START LOCATION
    // =========================

    let start =
        await getCoordinates(
            startName
        );


    if (!start) {

        output.innerHTML =
            '<div class="error">' +
            '❌ Starting location not found. Please check the name.' +
            '</div>';

        return;
    }


    // =========================
    // GET ROAD DISTANCE
    // =========================

    let distance =
        await getDistance(
            start,
            places
        );


    // =========================
    // TRANSPORT COST
    // =========================

    let fuelCost = 0;

    let rentalCost = 0;

    let transportCost = 0;


    if (
        transport === "Own Bike" ||
        transport === "Own Car"
    ) {

        let fuelNeeded =
            mileage > 0
                ? distance / mileage
                : 0;


        fuelCost =
            fuelNeeded * petrol;
    }


    else if (
        transport === "Rental Bike"
    ) {

        let fuelNeeded =
            mileage > 0
                ? distance / mileage
                : 0;


        fuelCost =
            fuelNeeded * petrol;


        rentalCost =
            700 * days;
    }


    else if (
        transport === "Rental Car"
    ) {

        let fuelNeeded =
            mileage > 0
                ? distance / mileage
                : 0;


        fuelCost =
            fuelNeeded * petrol;


        rentalCost =
            2500 * days;
    }


    else if (
        transport === "Public Transport"
    ) {

        transportCost =
            distance * 4;
    }


    // =========================
    // ACCOMMODATION
    // =========================

    let nights =
        Math.max(
            days - 1,
            1
        );


    let stayCost =
        stay *
        people *
        nights;


    // =========================
    // FOOD
    // =========================

    let foodCost =
        food *
        people *
        days;


    // =========================
    // ACTIVITIES
    // =========================

    let activityCost =
        activity *
        people;


// =================