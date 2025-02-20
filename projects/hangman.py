# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

word_to_guess = "apple"
display_word = "_____"
letters_guessed = ""
guesses_left = 6

print("Welcome to Hangman!")
print("Guess a letter at a time to guess a word.")

while display_word != word_to_guess and guesses_left > 0:

    print(f"You have {guesses_left} tries remaining.")
    print(f"You've already tried: {letters_guessed}")
    print(f"The word is: {display_word}")
    letter = ""
    while True:
        letter = input("Guess a single letter: ").lower()
        if len(letter) != 1:
            print(f"Your guess, '{letter}', is too long.")
            continue
        if letter in letters_guessed:
            print("You already guessed that letter.")
            continue
        break

    letters_guessed += letter
    display_word = ""
    for ch in word_to_guess:
        if ch in letters_guessed:
            display_word += ch
        else:
            display_word += "_"

    if letter in word_to_guess:
        print("Good guess!")
    else:
        print("Sorry, that'll cost you.")
        guesses_left -= 1


if guesses_left == 0:
    print(f"You lost! The word was '{word_to_guess}'.")
else:
    print(f"You won! You had {guesses_left} guesses remaining")
