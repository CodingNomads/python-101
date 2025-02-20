# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

has_sword = True

print("Welcome to the Dungeon!")
name = input("What is your name, adventurer? ")

while True:
    print(name + ", you are in a hallway. Before you are two doors.")
    choice = ""
    while choice != "left" and choice != "right":
        choice = input("Will you choose left, or right (left/right)? ")

    if choice == "left":
        print("This room is seemingly empty.")
        choice = ""
        while choice != "look" and choice != "leave":
            choice = input("Will you look around, or leave (look/leave)? ")
        if choice == "look":
            print("In the corner of the room, behind some debris, there lies a sword.")
            choice = ""
            while choice != "take" and choice != "leave":
                choice = input("Will you take it around, or leave (take/leave)? ")
            if choice == "take":
                has_sword = True
                print("You now have a servicable sword.")

    else:  # if choice == "right":
        print("There is a large red dragon sleeping in the center of the room.")
        choice = ""
        while choice != "fight" and choice != "leave":
            choice = input("Will you fight the dragon, or leave (fight/leave)? ")
        if choice == "fight":
            if has_sword:
                print("You strike a mortal blow against the dragon, killing it!")
            else:
                print(
                    "Points for bravery, which are outweighed by stupidity. The dragon eats you!"
                )
            break
