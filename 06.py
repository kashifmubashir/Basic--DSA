def is_sorted(a, i=0):
    if i >= len(a) - 1:
        return True

    if a[i] > a[i + 1]:
        return False

    return is_sorted(a, i + 1)


print(is_sorted([1, 2, 3, 5]))
print(is_sorted([1, 4, 3, 5]))