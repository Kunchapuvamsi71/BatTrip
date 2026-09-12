class User:

    def __init__(
        self,
        user_id=None,
        name="",
        email="",
        password=""
    ):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }