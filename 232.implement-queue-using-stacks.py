class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack0 = []
        self.stack1 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack0:
            self.stack1.append(self.stack0.pop())
        self.stack0.append(x)
        while self.stack1:
            self.stack0.append(self.stack1.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack0.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack0[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack0) == 0


# Your MyQueue object will be instantiated and called as such:


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print('pop1 = {}, pop2 = {}, pop3 = {}, empty = {}'.format(obj.pop(), obj.pop(), obj.pop(), obj.empty()))
