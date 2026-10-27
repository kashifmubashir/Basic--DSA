def next_greater(a):
    result = [-1] * len(a)
    stack = []

    for i, value in enumerate(a):
        while stack and a[stack[-1]] < value:
            result[stack.pop()] = value

        stack.append(i)

    return result


print(next_greater([4, 5, 2, 10, 8]))