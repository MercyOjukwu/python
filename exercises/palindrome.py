import math


def calculate_factorial(n):
    return math.factorial(n)


user_input = int(input("Enter a number: "))

fact = calculate_factorial(user_input)
print("The factorial of " , user_input, " is ", fact)
