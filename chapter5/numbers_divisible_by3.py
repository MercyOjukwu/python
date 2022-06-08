count_of_divisible = 0
print("Numbers between 1 - 30 are: ")

number = 0
while number < 30:
    number += 1
    print(number)
    if number % 3 == 0:
        count_of_divisible += number
print(f"The sum of numbers divisible by three are {count_of_divisible}.")
