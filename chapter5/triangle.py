asterisk = '*'
number = 0
count = 0
number_two = 7

while number < 7:
    number += 1
    for count in asterisk:
        print(asterisk * number)
print()
while number_two > 0:
    number_two -= 1
    for count in asterisk:
        print(asterisk * number_two)
