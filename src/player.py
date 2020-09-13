# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(Room):
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom


    def walk(self, direction):

        print(self.currentRoom)

        try:    

            nextRoom = getattr(self.currentRoom, f"{direction}_to")

            if nextRoom == None:
                print('sorry, you can not go that way')
            else:
                self.currentRoom = nextRoom
                print(self.currentRoom)
            

        except:
            AttributeError
            

             