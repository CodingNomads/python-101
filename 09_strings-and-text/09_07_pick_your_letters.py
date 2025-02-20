# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
space = word[-1]
print(
    word[1:3]
    + space
    + word[-2]
    + word[2:4]
    + space
    + word[0]
    + word[-3]
    + word[2:4]
    + word[-2]
)
