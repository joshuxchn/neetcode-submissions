class Node:
    def __init__(self, val=0, key=0):
        self.next = None
        self.prev = None
        self.used = 0
        self.val = val
        self.key = key


class LFUCache:
    # MRU is at the front; LRU is at the back
    def __init__(self, capacity: int):
        # key -> node
        self.keys_ = {}

        # frequency -> list of nodes
        self.freq_ = {}

        # Dummy nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keys_:
            return -1

        x = self.keys_[key]

        # FIX 1: Remove x from its old frequency bucket
        old_frequency = x.used
        self.freq_[old_frequency].remove(x)

        # FIX 2: Remove empty frequency buckets
        if not self.freq_[old_frequency]:
            del self.freq_[old_frequency]

        # Increase its frequency and add it to the new bucket
        x.used += 1
        self.freq_.setdefault(x.used, []).append(x)

        # FIX 3: Accessed node becomes MRU, so move it to the front
        self.remove(x)
        self.insert_front(x)

        return x.val

    def put(self, key: int, value: int) -> None:

        # FIX 5: Updating an existing key doesn't increase size
        if key in self.keys_:
            self.keys_[key].val = value

            # A put on an existing key increases its frequency
            self.get(key)
            return

        # FIX 6: Evict before inserting when already at capacity
        if self.size == self.capacity:
            # LFU means the minimum frequency
            lowest_frequency = min(self.freq_)

            # FIX 7: Search from the back because LRU is at the back
            victim = self.tail.prev

            while victim != self.head:
                if victim.used == lowest_frequency:
                    break
                victim = victim.prev

            # FIX 8: Remove victim from all three structures
            self.remove(victim)
            del self.keys_[victim.key]

            self.freq_[lowest_frequency].remove(victim)
            if not self.freq_[lowest_frequency]:
                del self.freq_[lowest_frequency]

            self.size -= 1

        # Create the new node with frequency 1
        x = Node(value, key)
        x.used = 1

        # Add it to both hash maps
        self.keys_[key] = x
        self.freq_.setdefault(1, []).append(x)

        # FIX 9: A new node is MRU, so insert it at the front
        self.insert_front(x)
        self.size += 1

    def insert_front(self, node):
        # Insert between head and the current first node
        first = self.head.next

        node.prev = self.head
        node.next = first

        self.head.next = node
        first.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        # Optional cleanup
        node.prev = None
        node.next = None