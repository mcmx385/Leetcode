class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0
        self.used = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.used.removeNode(key)
        self.used.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.used.removeNode(key)
            self.used.append(key)
            self.cache[key] = value
            return
        if self.count < self.capacity:
            self.count += 1
            self.used.append(key)
            self.cache[key] = value
            return
        del self.cache[self.used[0]]
        self.used.pop(0)
        self.used.append(key)
        self.cache[key] = value
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prevNode = None
        self.nextNode = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.nextNode = self.tail
        self.tail.prevNode = self.head

    def removeNode(self, node):
        node.prevNode.nextNode = node.nextNode
        node.nextNode.prevNode = node.prevNode

    def addNode(self, node):
        node.prevNode = self.head
        node.nextNode = self.head.nextNode

        self.head.nextNode.prevNode = node
        self.head.nextNode = node

    def popTail(self):
        node = self.tail.prevNode
        self.removeNode(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeNode(node)
        self.addNode(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addNode(node)
            node.value = value
            return
        if self.count < self.capacity:
            self.count += 1
            node = Node(key, value)
            self.addNode(node)
            self.cache[key] = node
            return
        node = self.popTail()
        del self.cache[node.key]
        node = Node(key, value)
        self.addNode(node)
        self.cache[key] = node
        return


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict[key] = self.dict.pop(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                self.dict.pop(list(self.dict.keys())[0])
        self.dict[key] = value
