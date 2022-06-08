asterisk = '*'
number = 0
count = 0

while number < 30:
    number += 1
    if number % 5 == 0:
        print(number)
        for count in asterisk:
            print(asterisk * number)
