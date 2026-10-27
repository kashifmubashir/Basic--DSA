def first_last(a, x):
    first = last = -1

    for i in range(len(a)):
        if a[i] == x:
            if first == -1:
                first = i

            last = i

    return first, last


print(first_last([1, 2, 3, 2, 2, 4], 2))
print(first_last([1, 2, 3], 7))