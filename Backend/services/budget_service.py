def calculate_budget(
    fuel_cost,
    accommodation_cost,
    food_cost,
    transport_cost,
    activity_cost,
    budget
):
    total_cost = (
        fuel_cost
        + accommodation_cost
        + food_cost
        + transport_cost
        + activity_cost
    )

    remaining_budget = budget - total_cost

    if remaining_budget >= 0:
        status = "Within Budget"
    elif abs(remaining_budget) <= budget * 0.10:
        status = "Slightly Over Budget"
    else:
        status = "Over Budget"

    return {
        "fuel_cost": fuel_cost,
        "accommodation_cost": accommodation_cost,
        "food_cost": food_cost,
        "transport_cost": transport_cost,
        "activity_cost": activity_cost,
        "total_cost": total_cost,
        "remaining_budget": remaining_budget,
        "status": status
    }