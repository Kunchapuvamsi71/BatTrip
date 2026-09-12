def calculate_fuel_cost(distance_km, mileage, fuel_price):
    """
    Calculate fuel required and fuel cost.
    """

    if mileage <= 0:
        return {
            "fuel_litres": 0,
            "fuel_cost": 0
        }

    fuel_litres = distance_km / mileage
    fuel_cost = fuel_litres * fuel_price

    return {
        "fuel_litres": round(fuel_litres, 2),
        "fuel_cost": round(fuel_cost, 2)
    }


def calculate_rental_cost(price_per_day, days):
    """
    Calculate vehicle rental cost.
    """

    return round(price_per_day * days, 2)