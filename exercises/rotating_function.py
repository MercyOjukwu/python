def rotate_list(lst, k):
    for k in lst:
        while k in lst:
            print(lst[k])


print(rotate_list([1, 2, 3], 2))
