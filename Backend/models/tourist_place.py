class TouristPlace:

    def __init__(
        self,
        place_id=None,
        destination_id=None,
        name="",
        place_type="",
        rating=0,
        popularity=0,
        cost=0,
        duration="",
        interest="",
        description=""
    ):
        self.place_id = place_id
        self.destination_id = destination_id
        self.name = name
        self.place_type = place_type
        self.rating = rating
        self.popularity = popularity
        self.cost = cost
        self.duration = duration
        self.interest = interest
        self.description = description

    def to_dict(self):
        return {
            "place_id": self.place_id,
            "destination_id": self.destination_id,
            "name": self.name,
            "type": self.place_type,
            "rating": self.rating,
            "popularity": self.popularity,
            "cost": self.cost,
            "duration": self.duration,
            "interest": self.interest,
            "description": self.description
        }