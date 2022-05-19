first_input = int(input("Enter first number: \n"))
second_input = int(input("Enter second number: \n"))
third_input = int(input("Enter third number: \n"))

sum_of_numbers = first_input + second_input + third_input
average = sum_of_numbers // 3
product = first_input * second_input * third_input

largest_value = first_input
if second_input > first_input:
    largest_value = second_input
elif third_input > first_input:
    largest_value = third_input
else:
    largest_value = first_input

smallest_value = first_input
if second_input < first_input:
    smallest_value = second_input
elif third_input < first_input:
    smallest_value = third_input
else:
    smallest_value = first_input


print(f"*Sum of numbers = {sum_of_numbers}\n*Average of numbers = {average}\n*Product of numbers is = {product}\n*Smallest number = {smallest_value}\n*Largest number = {largest_value}\n")


















