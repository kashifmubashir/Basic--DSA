def subsequences(s, i=0, current=""):
    if i == len(s):
        print(current if current else '""')
        return

    subsequences(s, i + 1, current)
    subsequences(s, i + 1, current + s[i])


subsequences("ab")