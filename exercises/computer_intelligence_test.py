
user_input = input("What is your problem ? \n")
second_input = input("Have you had this problem before ? \n")

if second_input == "Yes" or second_input == "yes":
    print("Well you have it again.")
elif second_input == "No" or second_input == "no":
    print("Well, you have it now.")
else:
    print("Sorry dear, you'll be fine")
