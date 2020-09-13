from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item('sword', 'a weapon of destruction for a warrior')),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item('candle', 'a tool to light your way')),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item('shovel', 'This could be useful...')),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

directions = ['n','s','e','w']



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Player1', room["outside"], [])

# print(player1.name)
# print(player1)

startingPoint = 0
currentRoom = player1.currentRoom

active = True

while active == True:

    print(f'The player is currently in {player1.currentRoom}')
    if player1.currentRoom.items:
        print(f"In This Room You Find a {player1.currentRoom.items.name}")
        print(f'If you would like to pick up {player1.currentRoom.items.name} type P')
 
    print(f"{player1.name} is now holding {player1.inventory}")
    
    for i, d in enumerate(directions):
       print("  " + str(i+1) + ": " + directions[i]) 


    print("  " + "q" + ": " + "quit")


    selection = input('what way would you like to go to?')

    print(len(player1.inventory))
   

    try:
        
        if selection == "q":
            print('quitting')
            active = False
        elif selection == 'p':
            if player1.currentRoom.items != None:
                player1.inventory.append(player1.currentRoom.items.name)
            else:
                print('there are no items to pick up')
        elif selection == "d":
            if len(player1.inventory)> 0:
                selection = input('what item would you to drop?')
                try:
                    player1.inventory.remove(selection)
                    print(f'you have dropped your {selection}')
                except: 
                    print('that item is not in your inventory')
                
            
        elif int(selection) > 0 and int(selection) <= len(directions) + 1:
            player1.walk(directions[int(selection) -1])
        
            
            # active = False

    except ValueError:
        print('please try again')

