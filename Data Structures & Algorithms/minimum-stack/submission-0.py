class MinStack:

    def __init__(self):
        self.s = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return -1
