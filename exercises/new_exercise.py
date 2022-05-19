# def add(a: int = 2, b: str = "Deji my boy") -> [int, str]:
#     print(a, b)
#
#
# print(add())


# def play_around(*numbers):
#     for number in numbers:
#         total = 0
#         total += number
#     return total
#
#
# print(play_around(1, 2, 3, 4, 5, 6, 7))

# def pack_and_unpack(*args, **kwargs):
#     print("Args", args)
#     print("KwArgs", kwargs)
#
#
# pack_and_unpack(1, 2, 3, 4, name='Deji', age='undefined', relationship_status='uninterested')

# first_word = "Hi"
# second_word = "Everyone"
# print(first_word + " " + second_word)
#
# word_one = "goal"
# word_one = "f" + word_one[1:]
# print(word_one)
#
# print(f"Hello {second_word}".format(second_word))

# first_input = int(input("Enter a number: \n"))
# second_input = int(input('Enter another number: \n'))
# product = first_input * second_input
# print(f"The product of {first_input} and {second_input} is: {product}".format(first_input, second_input, product))

# name = "Zaphira"
# hands = 2
# legs = 2

# print(name + " has " + str(hands) + " hands and " + str(legs) + " legs.")

# print(f"{name} has {hands} hands and {legs} legs".format(name, hands, legs))

#
# name = "Elephant  is a big animal"
# for letters in name:
#     print(letters)
#
# a = 2
# b = 3
# print(f"{a} multiplied by {b} is {a*b}".format(a, b))


# #0.2 kg is the weight of the newt.
#
# #
# weight = float(0.2)
# animal = "newt"
# print(f"Thw weight of the {animal} is {weight} kg")


# One of the most useful string methods is
#
# sentence = "One of the most useful string methods "
# print(sentence.find("useful"))
# print(sentence.find("One"))
# print(sentence.find("ijukreanf"))
#
# print("One of the most useful string methods ".find("most"))


# print("One of the most useful string methods ".find("most"))
#
#
#
# print("MY NEW HOUSE IS HUGE".isdecimal())
#
#
# # the following code shows how to replace
# phrase = "the following code shows how to replace"
#
# print(phrase.replace("replace", "cook soup"))
#
#
#
# letters = "AAA"
#
# print(letters.find("a"))

# new = "Somebody said something to Samantha."
#
# print(new.replace("s", "x"))
# print(new.replace("S", "X"))
#
#
# input = input("Enter a word: \n")
# print(input.find("a"))
#
# def replace_multiply_letters_with_digits(str):
#     str.replace("a", "1")
#     str.replace("e", "2")
#     str.replace("i", "3")
#     str.replace("o", "4")
#     str.replace("u", "5")
#
#
# print(replace_multiply_letters_with_digits("Hi, I'm a new student at this school"))
#
# num1 = 25_000_000
# num2 = 25000000
# print( num1, "\n", num2 )

# print(175e3)

#
# Enter a base: 1.2
# Enter an exponent: 3
# 1.2 to the power of 3 = 1.7279999999999


# first_input = int(input("Enter a base: \n"))
# second_input = int(input("Enter an exponent: \n"))
#
# print(f"The result of {first_input} raised to the power of {second_input} is : {first_input ** second_input}")


# Enter a number: 5.432
# 5.432 rounded to 2 decimal places is 5.43
#
# user_input = float(input("Enter a number: \n"))
# print(round(user_input, 2))

# Enter a number: -10
# The absolute value of -10 is 10.0

# user_input = int(input("Enter a number: "))
# print(abs(user_input))


# Enter a number: 1.5
# Enter another number: .5
# The difference between 1.5 and .5 is an integer? True!
#
# first_input = int(input("Enter a number: "))
# second_input = int(input("Enter another number: "))
#
# print(f"The difference between {first_input} and {second_input} is an interger ; ", first_input - second_input == int)
#

#
# balance = 2000.0
# spent = 256.35
# remaining = balance - spent
#
# print(f"After spending {spent} at the supermarket, my balance was {balance}...now I'm left with {remaining:,.2f}")

# print("$" + str(150) + "," + str("000") + "," + str("000") + " ")

#
# def multiply(x, y):
#     product = x * y
#     return product
#
#
# print(multiply(2, 5))

# def cube(x):
#     return x**3
#
#
# print(cube(3))
#
#
# def say_hello(x):
#     print("hello", x)
#
#
# print(say_hello("Jonathan"))
#
# num = 1
# while num < 10:
#     num += 1
#     print(num)


# def double_number(x):
#     return x + x
#
#
# print(double_number(55))

# def invest(amount, rate, years):
#     return "$" + str(amount * rate * years)
#
#
# print(invest(100, 2, 1))
#
# for i in range(1, 4):
#     j = i * 2
#     print(f"i is {i} and j is {j}")


# a = 4
# b = 16
# print(a == b)
# print(a <= b)
# print(a != b and a > b)

# print(1 <= 1)
# print(1 == 1)
# print(1 != 2)
# print("good" != "bad")
# print("good" != "Good")
# print(123 != "123")


print(3 != 4)
print(10 != 5)
print("jack" != "jill")
print(42 != "42")








