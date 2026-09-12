def create_itinerary(destinations, total_days):
    """
    Create a simple day-by-day itinerary
    for multiple destinations.
    """

    if not destinations:
        return []

    base_days = total_days // len(destinations)
    extra_days = total_days % len(destinations)

    itinerary = []
    day_number = 1

    for index, destination in enumerate(destinations):

        days_for_destination = base_days

        if index < extra_days:
            days_for_destination += 1

        for _ in range(days_for_destination):

            itinerary.append({
                "day": day_number,
                "destination": destination,
                "activity": f"Explore popular places in {destination}"
            })

            day_number += 1

    return itinerary