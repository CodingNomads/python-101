# Build a CLI RPG game following the instructions from the course.

import sys

# Ask the player for their name.
name = input("Enter your name: ")
# Display a message that greets them and introduces them to the game world.
print(f"Hello {name}! Welcome.")
sword = False
dragon = True
continue_playing = True
# Present them with a choice between two doors.
while continue_playing:
    choice = input("Choose 'left' or 'right' door by typing 'l' or 'r': ")
    # If they choose the left door, they'll see an empty room.
    if choice == 'l':
        go_back = None
        while not go_back == "y":
            go_back = input("You're in an empty room... Do you want to go back? y/n: ")
            if go_back == "y":
                print("You returned to the previous room.")
                break
            look = input("Do you want to look around? y/n: ")
            if look == "y":
                if not sword:
                    took_sword = input("You found a sword! Take it? y/n: ")
                    if took_sword == "y":
                        print("You took the sword.")
                        sword = True
                else:
                    print("There's nothing here...")
                
    # If they choose the right door, then they encounter a dragon.
    elif choice == 'r':
        go_back = None
        while not go_back == "y":
            if not dragon:
                print("The room is empty now.")
                stop = input("Do you want to stop playing? y/n: ")
                if stop == "y":
                    sys.exit()
            go_back = input("You've encountered a dragon! Do you want to go back? y/n: ")
            if go_back == "y":
                print("You returned to the previous room.")
                break
            fight = input("Do you want to fight the dragon? y/n: ")
            if fight == "y":
                if sword:
                    print("Your sword broke, but you defeated the dragon!")
                    sword = False
                    dragon = False
                else:
                    print("The dragon ate you whole...")
                    continue_playing = False
                    sys.exit()
            
    # In both cases, they have the option to return to the previous room or interact further.


    # When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

    # When encountering the dragon, they have the choice to fight it.


    # If they have the sword from the other room, then they will be able to defeat it and win the game.

    # If they don't have the sword, then they will be eaten by the dragon and lose the game.
