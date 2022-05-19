print("You would make use of three integers for this program.\n")

first_input = int(input("Enter first number: \n"))
second_input = int(input('Enter second number: \n'))
third_input = int(input('Enter third number: \n'))

smallest_value = 0


sum_of_numbers = first_input + second_input + third_input
product = first_input * second_input * third_input


print(f"> Sum of numbers is: {sum_of_numbers}")
print(f"> Average of numbers is: {sum_of_numbers / 3}")
print("> The largest number is:", max(first_input, second_input, third_input))
print("> The smallest value is:", min(first_input, second_input, third_input))
