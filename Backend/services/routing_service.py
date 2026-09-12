import requests


def get_route_distance(start_lat, start_lon, end_lat, end_lon):
    """
    Get approximate road distance using OSRM.
    """

    url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{start_lon},{start_lat};{end_lon},{end_lat}"
        f"?overview=false"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("code") != "Ok":
        return None

    distance_meters = data["routes"][0]["distance"]
    distance_km = distance_meters / 1000

    return round(distance_km, 2)