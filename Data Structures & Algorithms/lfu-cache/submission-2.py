class Node:
    def __init__(self, val=0, key=-1):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        self.used = 0

class LFUCache:
    def __init__(self, capacity):
        self.freq = {} #map of LRUcaches
        self.keys = {} #key to node
        self.capacity = capacity
        self.size = 0



    def get(self, key):
        if key not in self.keys: return -1

        node = self.keys[key]
        self.put(key, node.val) #update frequency
        return node.val


    def put(self, key, val):
        #if key is valid: 
            #remove from F[x]. Add to F[x+1]. Used += 1
        
        if key in self.keys:
            node = self.keys[key]

            node.val = val
            self.remove(node)
            node.used += 1

            #instantiate LRU cache, dummy head and tail
            if node.used not in self.freq: self.makeLRU(node.used)
            self.insert_back(self.freq[node.used][1], node)
                
        
        #Not valid: new node, add to F[x]
            #Create new key to dict

        else:
            #if size >= capacity, evict
            self.size += 1
            if self.size > self.capacity:
                #fix for O(1)
                minLRU = min(self.freq)

                del self.keys[self.freq[minLRU][0].next.key] #delete key from keys
                self.remove(self.freq[minLRU][0].next) #remove head, LRU
                self.size -=1

            node = Node(val, key)
            if node.used not in self.freq: self.makeLRU(node.used)

            self.insert_back(self.freq[node.used][1], node)
            self.keys[key] = node

        return

    #helpers
    def makeLRU(self, used):
        dummyHead = Node(-1)
        dummyTail = Node(-1)
        dummyHead.next = dummyTail
        dummyTail.prev = dummyHead
        self.freq[used] = [dummyHead, dummyTail]
        
    def insert_back(self, tail, node):
        #X -> Node -> dummy
        tail.prev.next = node
        node.next = tail

        # X <- Node <- Dummy
        node.prev = tail.prev
        tail.prev = node
        

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        #if removal means the LRUcache is empty, del from freq
        if node.prev.val == -1 and node.next.val == -1:
            del self.freq[node.used]

#logic
#frequency map of LRUcaches. Front is LRU, back is MRU (makes sense, we are adding to tail)