
def func(lst):
    from collections import defaultdict
    counter = defaultdict(int)

    for element in lst:
        counter[element] += 1

    return [k for k, _ in sorted(counter.items(), key=lambda x: x[1], reverse=True)]


print(func("matthew"))
