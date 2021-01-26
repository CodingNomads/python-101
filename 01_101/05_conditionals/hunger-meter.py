# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.


# hunger = 2
hunger = "small"

if type(hunger) != str:
    print("You're confused! Please enter a string")
elif hunger == "big":
    print("Eat the pizza")
elif hunger == "medium":
    print("Eat the joghurt")
elif hunger == "small":
    print("Eat the apple")
else:
    print("Don't eat anything")