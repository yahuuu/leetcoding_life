# -*- coding:utf-8 -*-
# Created data: 20210624

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top_stack = list()
        self.num_stack = list()

    def push(self, val: int) -> None:
        if not self.num_stack:
            self.top_stack.append(val)
            self.num_stack.append(val)
            return
        self.num_stack.append(val)
        self.top_stack.append(min(self.top_stack[-1], val))

    def pop(self) -> None:
        if not self.num_stack:
            return
        self.num_stack.pop(-1)
        self.top_stack.pop(-1)

    def top(self) -> int:
        return self.num_stack[-1]

    def getMin(self) -> int:
        return self.top_stack[-1]

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())

