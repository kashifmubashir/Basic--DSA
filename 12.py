def count_occurrences(a, x):
    count = 0

    for value in a:
        if value == x:
            count += 1

    return count


print(count_occurrences([1, 2, 2, 2, 3, 4], 2))