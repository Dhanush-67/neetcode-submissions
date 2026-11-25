class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        Prev, Next = node.prev, node.next
        Prev.next = Next
        Next.prev = Prev

    def insert(self,node):
        Prev = self.right.prev
        Prev.next = node
        node.next = self.right
        node.prev = Prev
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.storage:
            node = self.storage[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.remove(self.storage[key])
        node = Node(key,value)
        self.insert(node)
        self.storage[key] = node

        if len(self.storage) > self.capacity:
            trash = self.left.next
            del self.storage[trash.key]
            self.remove(trash)

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)