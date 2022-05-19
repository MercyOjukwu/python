# lst = []
#
# user = [lst.append(chr(i))for i in range(65, 91)]
#
# print(lst)

# multiply = lambda x, y: x * y
# print(multiply(2, 3))

# def mult(a, b):
#     return a * b
#
#
# def operate(x, y, fn):
#     return fn(x, y, )
#
#
# print(operate(2, 3, mult))

# def multiple(x, function):
#     return function(x)
#
#
# print(multiple(2, lambda x: x * 2))
# # print(multiple(3, lambda x: x * 3))
# print(all([1, 2, 3, 4]))
# print(any([1, 0, 2]))
#
# names = ["Me", "Myself", "I", "you"]
#
# print(all(name.istitle() for name in names))
#



# any([person["age"] <= 20 for person in people])
#
# lst = list(map(lambda x: x ** 2, range(1, 10)))
# print("1.", lst)

# # print("2. ", lst_two)
# map_object = map(lambda x: x ** 1, range(1, 10))
# lst_two = list(map_object)
#
# print("2. ", lst_two)
# def isEven(x):
#     return x % 2 == 0
#
#
# filter_obj = list(filter(isEven, range(1, 20)))
# print("Even numbers include: ", filter_obj)

# new_tuple = ((1, 2, 3), (4, 5, 6))
# for numbers in new_tuple:
#     arithmetic_one = sum(new_tuple[0])
#     arithmetic_two = sum(new_tuple[1])
# print("Sum of the members of the first nested tuple: ", arithmetic_one)
# print("Sum of the members of the second nested tuple: ", arithmetic_two)

numbers = [4, 3, 2, 1]
new_lst = numbers[:]
numbers.sort()
print(numbers)

