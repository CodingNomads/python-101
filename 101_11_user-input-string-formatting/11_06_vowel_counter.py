# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

text = input("Say something: ")

for v in "aeiou":
    n = text.count(v)
    print(v, n)