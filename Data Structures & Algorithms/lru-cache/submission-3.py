class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = self.tail = None
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        
        if prev:
            prev.next = next
        else:
            #this means it was the head
            self.head = next
        if next:
            next.prev = prev
        else:
            #this means it was the tail
            self.tail = prev

    def insert(self, node):
        prev = self.tail
        node.next = None
        node.prev=prev

        if self.tail:
            prev.next = node
        else: #shits empty
            self.head = node

        self.tail = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key] #fetches pair, not val (like java)
            self.remove(node)
            self.insert(node)
            return(node.val)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #putting counts as using
        node = Node(key, value)
        self.insert(node)
        self.cache[key]=node

        if len(self.cache) > self.capacity:
            lru = self.head
            self.remove(self.head)
            del self.cache[lru.key]
        
