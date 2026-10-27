def subset_sum(a, target, i=0):
    if target == 0:
        return True

    if i == len(a):
        return False

    return (
        subset_sum(a, target - a[i], i + 1)
        or subset_sum(a, target, i + 1)
    )


print(subset_sum([3, 4, 5, 2], 9))
print(subset_sum([3, 4, 5, 2], 20))