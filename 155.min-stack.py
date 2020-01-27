class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x - self.min)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        if not self.stack:
            return
        tmp = self.stack.pop()
        if tmp < 0:
            self.min -= tmp

    def top(self) -> int:
        if not self.stack:
            return
        tmp = self.stack[-1]
        if tmp < 0:
            return self.min
        else:
            return self.min + tmp

    def getMin(self) -> int:
        return self.min


if __name__ == '__main__':
    ret = MinStack()
    ret.push(-2)
    ret.push(0)
    ret.push(-3)
    print(ret.getMin())
    ret.pop()
    print(ret.top())
    ret.pop()
