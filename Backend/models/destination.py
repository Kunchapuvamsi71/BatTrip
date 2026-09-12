class Destination:

    def __init__(
        self,
        destination_id=None,
        name="",
        state=""
    ):
        self.destination_id = destination_id
        self.name = name
        self.state = state

    def to_dict(self):
        return {
            "destination_id": self.destination_id,
            "name": self.name,
            "state": self.state
        }