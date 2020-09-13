# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, description, message, items = None):
        self.description = description
        self.message = message
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        if items is None:
            self.items = []
        else: self.items = items

    def __str__(self):
        return f"Room Description: {self.description}"

