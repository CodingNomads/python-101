# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

num = int(input("Enter a number up to 1mil: "))

found = False
guess = 0
while not found:
    if guess == num:
        found = True
    else:
        guess += 1

print(f"Found it: {num} == {guess}")