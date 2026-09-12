class Accommodation:

    def __init__(
        self,
        accommodation_id=None,
        destination_id=None,
        name="",
        accommodation_type="",
        price_per_night=0,
        rating=0,
        facilities=""
    ):
        self.accommodation_id = accommodation_id
        self.destination_id = destination_id
        self.name = name
        self.accommodation_type = accommodation_type
        self.price_per_night = price_per_night
        self.rating = rating
        self.facilities = facilities

    def to_dict(self):
        return {
            "accommodation_id": self.accommodation_id,
            "destination_id": self.destination_id,
            "name": self.name,
            "type": self.accommodation_type,
            "price_per_night": self.price_per_night,
            "rating": self.rating,
            "facilities": self.facilities
        }