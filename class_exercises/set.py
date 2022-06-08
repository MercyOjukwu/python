set_one = [1,2,3,4,5]
set_two = [2,3,5,6,7]
new_set = []
for elements in set_one:
    if elements not in set_two:
        new_set.append(elements)
