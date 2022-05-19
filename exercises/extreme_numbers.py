name = input("Enter a user name: ")
print()
print(f"Hello {name}, let's help you find the lowest and highest values in your quiz.")

lst = []
num_of_elements = int(input("How many elements should be in list: \n"))

for i in range(num_of_elements):
    lst.append(int(input("Enter a value: \n")))
minimum = min(lst)
maximum = max(lst)

print("Good job!")
print()
print(" >The minimum value is: ", minimum)
print(" >The maximum value is: ", maximum)
