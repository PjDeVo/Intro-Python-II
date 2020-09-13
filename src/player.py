# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item

class Player(Room):
    def __init__(self, name, currentRoom, inventory):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []


    def walk(self, direction):

        print(self.currentRoom)

        try:    

            nextRoom = getattr(self.currentRoom, f"{direction}_to")

            if nextRoom == None:
                print('SORRY, YOU CAN NOT GO THAT WAY')
            else:
                self.currentRoom = nextRoom
                print(self.currentRoom)
            

        except:
            AttributeError

        
    def pickUpItem(self,item):
        self.inventory = self.inventory.append(item)

    def dropItem(self, item):
        self.inventory = self.inventory.remove(Item)

            

             