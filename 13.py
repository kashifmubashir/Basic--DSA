def floor_ceil(a, x):
    floor_value = None
    ceil_value = None

    for value in a:
        if value <= x:
            floor_value = value

        if value >= x and ceil_value is None:
            ceil_value = value

    return floor_value, ceil_value


print(floor_ceil([1, 3, 5, 7, 9], 6))
print(floor_ceil([1, 3, 5, 7, 9], 0))