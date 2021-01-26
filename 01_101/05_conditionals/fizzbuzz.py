# Suppose we have a number n.
# We have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write Fizz instead of the number
# - If the number is divisible by 5, write Buzz instead of the number
# - If the number is divisible by 3 and 5 both, write FizzBuzz instead of the number

number = 100

for n in range(number):
    if (n % 5 == 0) and (n % 3 == 0):
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
