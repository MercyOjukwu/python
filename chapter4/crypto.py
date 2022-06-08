four_digits = list(input("Enter a four-digit number: "))
for digit in four_digits:
    four_digits[0] = int(four_digits[0] * 7) % 10
    four_digits[1] = int(four_digits[0] * 7) % 10
    four_digits[2] = int(four_digits[0] * 7) % 10
    four_digits[3] = int(four_digits[0] * 7) % 10
    four_digits[0] = four_digits[2]
    four_digits[1] = four_digits[3]
print(four_digits)
