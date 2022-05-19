number = 0

while number <= 100:
    number += 1
    if number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 15 == 0:
        print("fizz buzz")
    else:
        print(number)
