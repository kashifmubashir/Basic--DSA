def search_insert(a, target):
    for i in range(len(a)):
        if a[i] >= target:
            return i

    return len(a)


print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 7))