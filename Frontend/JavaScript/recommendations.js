// BatTrip & SpiderRoam
// Location API Connection

const LOCATION_API_URL = window.BATTRIP_API_BASE || "http://127.0.0.1:5000";

async function searchLocation(placeName) {
    try {
        const response = await fetch(
            `${LOCATION_API_URL}/api/location?place=${encodeURIComponent(placeName)}`
        );

        const result = await response.json();

        if (!response.ok) {
            console.error("Location API error:", result);
            return null;
        }

        console.log("Location received:");
        console.log(result);

        return result;
    } catch (error) {
        console.error("Backend connection error:", error);
        return null;
    }
}
