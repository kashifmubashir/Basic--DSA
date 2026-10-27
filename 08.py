def hanoi(n, source, helper, target):
    if n == 1:
        print(source, "->", target)
        return

    hanoi(n - 1, source, target, helper)
    print(source, "->", target)
    hanoi(n - 1, helper, source, target)


hanoi(3, "A", "B", "C")