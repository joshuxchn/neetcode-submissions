class Node:
    def __init__(self, val=0, key=0):
        self.key = key
        self.next = None
        self.prev = None
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.curr_size = 0

        self.head = Node()
        self.tail = Node() #dummy
        self.tail.prev, self.head.next = self.head, self.tail
        
    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        
        self.curr_size += 1
        if self.curr_size <= self.capacity:
            x = Node(value, key)
            self.insert(x)
            self.cache[key] = x
            return 
        
        #case 3 - evict LRU
        x = self.head.next
        self.remove(x)
        del self.cache[x.key]

        x = Node(value, key)
        self.insert(x)
        self.cache[key]=x

        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        temp = self.tail.prev

        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node




        
