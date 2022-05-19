num = int(input("Enter numerator: \n"))
den = int(input("Enter denominator: \n"))


def divide(a, b):
    if num == 0:
        raise ValueError("Denominator cannot be zero")
    else:
        return a / b


try:
    print(divide(num, den))
except ZeroDivisionError:
    print("Wrong value")
else:
    print("You finally got something right")
finally:
    print("I run everytime")
