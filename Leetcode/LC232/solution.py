# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue:
    def __init__(self):
        self.stack = []
        self.arr = []

    def push(self, x: int) -> None:
        n = len(self.stack)
        for i in range(n):
            self.arr.append(self.stack.pop())
        self.stack.append(x)
        for i in range(n):
            self.stack.append(self.arr.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        self.size += 1

    def pop(self) -> int:
        if not self.head:
            return None
        result = self.head.val
        self.head = self.head.next
        self.size -= 1
        return result

    def peek(self) -> int:
        if not self.head:
            return None
        return self.head.val

    def empty(self) -> bool:
        return self.size == 0


class MyQueue:
    def __init__(self):
        self.stack = deque()
        self.arr = deque()

    def push(self, x: int) -> None:
        n = len(self.stack)
        for i in range(n):
            self.arr.append(self.stack.pop())
        self.stack.append(x)
        for i in range(n):
            self.stack.append(self.arr.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


class MyQueue:
    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        return self.arr.pop(0)

    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        return len(self.arr) == 0


class MyQueue:
    def __init__(self):
        self.stack = []
        self.arr = []

    def swap(self):
        n = len(self.stack)
        for i in range(n):
            self.arr.append(self.stack.pop())

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.arr:
            self.swap()
        return self.arr.pop()

    def peek(self) -> int:
        if not self.arr:
            self.swap()
        return self.arr[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.arr) == 0
