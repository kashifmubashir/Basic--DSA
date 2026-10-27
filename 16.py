def valid_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)

        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


print(valid_parentheses("({[]})"))
print(valid_parentheses("([)]"))