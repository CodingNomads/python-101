# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay

collab_story = """You would never guess""".lower()

word = ""
for c in collab_story:
    if c == " ":
        print(word[1:] + word[0] + "ay")
        word = ""
    else:
        word += c

print(word[1:] + word[0] + "ay")