# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script
word = "hello"
guessed = False
counter = 10
# Print an explanation to the user
print("Guess the word.")
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
blank = ""
for c in word:
    blank += "_"
    print(f"_", end=" ")
print()
# Ask for user input
while not guessed and counter > 0:
    guess = input("\nEnter a single character: ")
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
    counter -= 1
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
    if guess in word:
        blank = ""
        for c in word:
            if c == guess:
                blank += c
            else:
                blank += "_"
    for c in blank:
        print(c, end=" ")
        
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it