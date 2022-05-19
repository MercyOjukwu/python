user_input = input("Enter a five digit number: ")

if len(user_input) < 5 or len(user_input) > 5:
    print("I said enter a FIVE digit number!")
else:
    print()
    for digit in user_input:
        print(digit)
