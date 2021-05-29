# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

flag = False
extension = ""
for c in filename:
    if flag:
        extension += c
    if c == ".":
        flag = True

if extension == "pdf":
    print(True)