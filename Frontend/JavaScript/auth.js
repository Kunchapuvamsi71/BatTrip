// BatTrip & SpiderRoam
// Frontend ↔ Backend API Connection

const API_BASE_URL = window.BATTRIP_API_BASE || "http://127.0.0.1:5000";

async function getDestinations() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/destinations`);

        if (!response.ok) {
            throw new Error("Failed to fetch destinations");
        }

        const destinations = await response.json();

        console.log("Destinations received from backend:");
        console.log(destinations);

        return destinations;
    } catch (error) {
        console.error("Backend connection error:", error);
        return [];
    }
}
