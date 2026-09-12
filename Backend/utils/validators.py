def validate_trip_data(days, people, budget):
    """
    Validate basic trip planning information.
    """

    errors = []

    if days <= 0:
        errors.append("Number of days must be greater than 0.")

    if people <= 0:
        errors.append("Number of people must be greater than 0.")

    if budget < 0:
        errors.append("Budget cannot be negative.")

    if errors:
        return {
            "valid": False,
            "errors": errors
        }

    return {
        "valid": True,
        "errors": []
    }