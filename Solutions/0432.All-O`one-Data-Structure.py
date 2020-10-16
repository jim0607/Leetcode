"""
432. All O`one Data Structure

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. 
           If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""


"""
use a Double Linked list, a hashmap to store (key, cnt) pair, use a hashmap to store (cnt, node) pair.  
node is a DLL node, there is a node.key_set = set() which stores all the keys with that cnt.  
The rest is to update the dll, the two hashmaps in each method call. similar with LRU.
"""
class Node:
           
    def __init__(self):
        self.key_set = set()
        self.prev = None
        self.next = None
        
    def add(self, key):
        self.key_set.add(key)
    
    def remove(self, key):
        self.key_set.remove(key)
    
    def get_one_key(self):
        key = self.key_set.pop()
        self.key_set.add(key)
        return key
    
           
class DoubleLinkedList:
           
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_after(self, n1, n2):     # insert node2 after node1
        temp = n1.next
        
        n1.next = n2
        n2.prev = n1
        
        n2.next = temp
        temp.prev = n2
        
    def insert_before(self, n1, n2):
        temp = n1.prev
        
        temp.next = n2
        n2.prev = temp
        
        n1.prev = n2
        n2.next = n1
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoubleLinkedList()
        self.counter = collections.defaultdict(int)
        self.node_val = {0: self.dll.head}      # key is cnt, value is node
        
    def remove_key(self, v, key):
        node = self.node_val[v]
        node.remove(key)
        if not node.key_set:
            self.dll.remove(node)
            self.node_val.pop(v)
        
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.counter[key] += 1
        v = self.counter[key]
        
        if v not in self.node_val:
            self.node_val[v] = Node()
            self.dll.insert_after(self.node_val[v-1], self.node_val[v])
        self.node_val[v].add(key)
        
        if v - 1 > 0:       # remove old (v, key) pair
            self.remove_key(v-1, key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.counter:
            return
        
        self.counter[key] -= 1
        v = self.counter[key]
        
        if v == 0:
            self.counter.pop(key)
        else:
            if v not in self.node_val:
                self.node_val[v] = Node()
                self.dll.insert_before(self.node_val[v+1], self.node_val[v])
            self.node_val[v].add(key)
        
        self.remove_key(v+1, key)
        
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.dll.head.next == self.dll.tail:
            return ''
        return self.dll.tail.prev.get_one_key()

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.dll.head.next == self.dll.tail:
            return ''
        return self.dll.head.next.get_one_key()
