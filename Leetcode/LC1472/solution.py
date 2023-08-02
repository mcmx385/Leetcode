# print(self.at, self.list, None)
# print(self.at, self.list, self.list[self.at])


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

###############################################


class BrowserHistory:
    def __init__(self, homepage: str):
        self.list = [homepage]
        self.at = 0

    def visit(self, url: str) -> None:
        self.list = self.list[: self.at + 1]
        self.list.append(url)
        self.at += 1

    def back(self, steps: int) -> str:
        x = len(self.list)
        return_steps = steps if self.at - steps >= 0 else self.at
        self.at -= return_steps
        return self.list[self.at]

    def forward(self, steps: int) -> str:
        x = len(self.list)
        forward_steps = steps if self.at + steps < x else x - 1 - self.at
        self.at += forward_steps
        return self.list[self.at]


###############################################


class BrowserHistory:
    def __init__(self, homepage: str):
        self.list = [homepage]
        self.at = 0
        self.len = 1

    def visit(self, url: str) -> None:
        self.list = self.list[: self.at + 1]
        self.list.append(url)
        self.at += 1
        self.len = len(self.list)

    def back(self, steps: int) -> str:
        return_steps = steps if self.at - steps >= 0 else self.at
        self.at -= return_steps
        return self.list[self.at]

    def forward(self, steps: int) -> str:
        forward_steps = steps if self.at + steps < self.len else self.len - 1 - self.at
        self.at += forward_steps
        return self.list[self.at]


###############################################


class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.at = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.at.next = ListNode(url, self.at)
        self.at = self.at.next

    def back(self, steps: int) -> str:
        while self.at.prev and steps:
            self.at = self.at.prev
            steps -= 1
        return self.at.val

    def forward(self, steps: int) -> str:
        while self.at.next and steps:
            self.at = self.at.next
            steps -= 1
        return self.at.val


###############################################


class BrowserHistory:
    def __init__(self, homepage: str):
        self.list = [homepage]
        self.at = 0

    def visit(self, url: str) -> None:
        self.list = self.list[: self.at + 1] + [url]
        self.at += 1

    def back(self, steps: int) -> str:
        return self.list[max(0, self.at - steps)]

    def forward(self, steps: int) -> str:
        return self.list[min(len(self.list) - 1, self.at + steps)]
