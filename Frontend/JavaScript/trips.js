// BatTrip & SpiderRoam
// Recommendations API Connection

const RECOMMENDATION_API_URL = window.BATTRIP_API_BASE || "http://127.0.0.1:5000";

async function getBackendRecommendations(placeName) {
    try {
        const response = await fetch(
            `${RECOMMENDATION_API_URL}/api/recommendations?place=${encodeURIComponent(placeName)}`
        );

        const result = await response.json();

        if (!response.ok) {
            console.error("Recommendation API error:", result);
            return [];
        }

        console.log("Recommendations received:");
        console.log(result);

        return result.recommendations || [];
    } catch (error) {
        console.error("Backend connection error:", error);
        return [];
    }
}
