// ==========================================
// BatTrip & SpiderRoam
// My Trips JavaScript
// ==========================================

const TRIPS_API_URL = "http://127.0.0.1:5000";


// ==========================================
// LOAD MY TRIPS
// ==========================================

async function loadMyTrips() {

    const tripsContainer =
        document.getElementById("tripsContainer");


    // Get logged-in user

    const storedUser =
        localStorage.getItem("loggedInUser");


    // ==========================================
    // CHECK LOGIN
    // ==========================================

    if (!storedUser) {

        tripsContainer.innerHTML = `
            <div class="card">

                <h2>🔐 Please Login</h2>

                <p>
                    You need to login to view your saved trips.
                </p>

                <a href="login.html" class="btn">
                    Login
                </a>

            </div>
        `;

        return;
    }


    let user;

    try {

        user = JSON.parse(storedUser);

    } catch (error) {

        console.error(
            "Invalid user data:",
            error
        );

        localStorage.removeItem("loggedInUser");

        window.location.href = "login.html";

        return;
    }


    // Check user ID

    if (!user.id) {

        tripsContainer.innerHTML = `
            <div class="card">

                <h2>Unable to identify your account</h2>

                <p>
                    Please login again.
                </p>

                <a href="login.html" class="btn">
                    Login Again
                </a>

            </div>
        `;

        return;
    }


    // ==========================================
    // FETCH TRIPS FROM FLASK
    // ==========================================

    try {

        const response = await fetch(
            `${TRIPS_API_URL}/api/trips/${user.id}`
        );


        const result = await response.json();


        console.log(
            "My Trips response:",
            result
        );


        if (result.status !== "success") {

            tripsContainer.innerHTML = `
                <div class="card">

                    <h2>Unable to load trips</h2>

                    <p>
                        ${result.message || "Something went wrong."}
                    </p>

                </div>
            `;

            return;
        }


        // ==========================================
        // NO TRIPS
        // ==========================================

        if (!result.trips || result.trips.length === 0) {

            tripsContainer.innerHTML = `
                <div class="card">

                    <h2>🧳 No trips saved yet</h2>

                    <p>
                        Create your first trip using the Trip Planner.
                    </p>

                    <a href="planner.html" class="btn">
                        🚀 Plan My Trip
                    </a>

                </div>
            `;

            return;
        }


        // ==========================================
        // DISPLAY TRIPS
        // ==========================================

        let html = "";


        result.trips.forEach(function (trip) {

            html += `

                <div class="card">

                    <h2>
                        🗺️ Trip #${trip.id}
                    </h2>


                    <p>
                        <strong>📍 Starting Location:</strong>
                        ${trip.start_location || "Not specified"}
                    </p>


                    <p>
                        <strong>📅 Days:</strong>
                        ${trip.days || 0}
                    </p>


                    <p>
                        <strong>👥 People:</strong>
                        ${trip.people || 0}
                    </p>


                    <p>
                        <strong>💰 Budget:</strong>
                        ₹${Number(trip.budget || 0).toFixed(2)}
                    </p>


                    <p>
                        <strong>💵 Total Cost:</strong>
                        ₹${Number(trip.total_cost || 0).toFixed(2)}
                    </p>


                    <p>
                        <strong>🕒 Created:</strong>
                        ${formatDate(trip.created_at)}
                    </p>

                </div>

            `;

        });


        tripsContainer.innerHTML = html;


    } catch (error) {

        console.error(
            "My Trips connection error:",
            error
        );


        tripsContainer.innerHTML = `

            <div class="card">

                <h2>❌ Backend Connection Error</h2>

                <p>
                    Make sure Flask is running.
                </p>

                <button
                    onclick="loadMyTrips()"
                    class="btn"
                >
                    🔄 Try Again
                </button>

            </div>

        `;
    }
}



// ==========================================
// FORMAT DATE
// ==========================================

function formatDate(dateValue) {

    if (!dateValue) {
        return "Not available";
    }


    const date = new Date(dateValue);


    if (isNaN(date.getTime())) {
        return dateValue;
    }


    return date.toLocaleString();
}



// ==========================================
// START
// ==========================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        loadMyTrips();

    }
);