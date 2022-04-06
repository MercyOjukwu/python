number = 0

while number <= 100:
    counter = number + 1
    print(counter)
    if number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 15 == 0:
        print("fizz buzz")
