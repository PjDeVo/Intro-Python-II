# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(Room):
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self,):
        return f"{super().__str__()}"
             