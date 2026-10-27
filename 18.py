class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        self.stack.append(x)

        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        x = self.stack.pop()

        if x == self.mins[-1]:
            self.mins.pop()

        return x

    def get_min(self):
        return self.mins[-1]


s = MinStack()

s.push(5)
s.push(2)
s.push(7)

print(s.get_min())

s.pop()
s.pop()

print(s.get_min())