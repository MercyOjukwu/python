
first_input = int(input("Enter a number: \n"))
second_input = int(input('Enter another number: \n'))

print("First number tripled is a multiple of second number doubled: ", (first_input * 3) % (second_input * 2) == 0)
