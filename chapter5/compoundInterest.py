import math

principal = 1000.0
rate = 0.05

print("Year     Amount on deposit")

year = 0
while year <= 10:
    year += 1
    rate += 1
    amount = principal * (1.0 + rate ** year)
    print(f"{year}        {amount}")
