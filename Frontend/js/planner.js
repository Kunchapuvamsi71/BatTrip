// BatTrip & SpiderRoam
// JavaScript compatibility shim for lowercase paths on static hosting.

if (typeof window !== "undefined") {
    const script = document.currentScript || null;
    if (script && script.src) {
        console.info("Loaded planner compatibility shim.");
    }
}
