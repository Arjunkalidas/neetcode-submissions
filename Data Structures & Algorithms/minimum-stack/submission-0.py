class MinStack:

    stack = []

    def __init__(self):
        self.stack = []                                                  

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        lowest = float('inf')
        for n in self.stack:
            lowest = min(n, lowest)
        return lowest
