"""
You wake up in a maze of `if` statements and you need
to find the path to get out:

.--.--.--.  .--.--.
|     |        |  |
:  :--:  :  :  :  :
|  |     |  |     |
:  :  :  :--:--:--:
|  |  |           |
:  :  :--:--:--:  :
|  |   You  |  |  |
:  :--:--:  :  :  :
|     |     |  |  |
:--:  :  :--:  :  :
|        |        |
:--:--:--:--:--:--:

However, this maze has a BIG limitation!
There are only two actions you can take, you can only ADD
either one of the following lines of code:

    flag = True
    flag = False

You can add as many of them as you want to, but you can't change any of the code
that is already there.

Add the code so when you run it, it will print out all directions necessary
so you can get out of the maze!
"""

flag = True

if flag == True:
    flag = False  # TODO: remove this line
    print("left")

if flag == False:
    print("straight ahead")

if flag == True:
    print("left")

if flag == False:
    flag = True  # TODO: remove this line
    print("straight ahead")

if flag == True:
    print("straight ahead")

if flag == True:
    flag = False  # TODO: remove this line
    print("straight ahead")

if flag == True:
    print("DEAD END")

if flag == True:
    print("left")

if flag == False:
    flag = True  # TODO: remove this line
    print("right")

if flag == True:
    flag = False  # TODO: remove this line
    print("straight ahead")

if flag == False:
    flag = True  # TODO: remove this line
    print("straight ahead")

if flag == False:
    print("DEAD END")

if flag == True:
    print("right")

if flag == True:
    flag = False  # TODO: remove this line
    print("straight ahead")

if flag == True:
    print("left")

if flag == False:
    print("EXIT!!")

if flag == True:
    print("DEAD END")
