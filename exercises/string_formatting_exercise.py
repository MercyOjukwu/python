
print("Welcome to Q-Mart, I'll take your order.")

a = input("First product? \n")
b = input("Second product? \n")
c = input("Would you like anything else? \n")
print()
print()
print("I'll take the quantity of those now...\n")

quantity_one = input("Quantity of first product?\n")
quantity_one = int(quantity_one)

quantity_two = input("Quantity of second product?\n")
quantity_two = int(quantity_two)

quantity_three = input("Quantity of third product?\n")
quantity_three = int(quantity_three)

price_one = 2
price_two = 20
price_three = 10

total_one = (quantity_one * 2)
total_two = quantity_two * 20
total_three = quantity_three * price_three

final_total = total_one + total_two + total_three

print()
print()

print("Alright then I'll get you your receipt and your goods will be at the exit for you...")
print()

print("***************************************")
print("\nFLorence & Sons Group of Company")
print("312 Herbert Macaulay Way , Sabo Yaba")
print("     07014014013 florence@gmail.com")
print("\n*****************************************")

print("SKU      Qty    Price      Total")
print(f"{a}      {quantity_one}      {price_one}           {total_one}".format(a, quantity_one, price_one, total_one))
print(f"{b}      {quantity_two}      {price_two}          {total_two}".format(b, quantity_two, price_two, total_two))
print(f"{c}      {quantity_three}      {price_three}          {total_three}".format(c, quantity_three, price_three, total_three))
print(f"                              TOTAL: {final_total}".format(final_total))

print("\n*****************************************")
print("\n          Thanks for your patronage :)")
print("\n*****************************************")
