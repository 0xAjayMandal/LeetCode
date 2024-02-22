class MinStack:

    def __init__(self):
        self.mainStack = []
        self.auxStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if len(self.auxStack) == 0 or val <= self.auxStack[-1]:
            self.auxStack.append(val)

    def pop(self) -> None:
        topValue = self.mainStack.pop()
        if topValue == self.auxStack[-1]:
            self.auxStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.auxStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()