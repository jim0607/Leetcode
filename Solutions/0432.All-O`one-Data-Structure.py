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
        self.prev = None
        self.next = None
        self.key_set = set()

    def get_one_key(self):
        key = self.key_set.pop()
        self.key_set.add(key)
        return key


class DoubleLinkedList:

    def __init__(self):
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_after(self, n1, n2):
        """
        insert n2 after n1
        """
        n1.next.prev = n2
        n2.next = n1.next
        n1.next = n2
        n2.prev = n1

    def insert_before(self, n1, n2):
        """
        insert n2 before n1
        """
        n1.prev.next = n2
        n2.prev = n1.prev
        n1.prev = n2
        n2.next = n1


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoubleLinkedList()
        self.key_cnt = defaultdict(int)
        self.cnt_node = {0: self.dll.dummy_head}  # key is cnt, value is node

    def remove_key(self, cnt, key):
        node = self.cnt_node[cnt]
        node.key_set.remove(key)
        if not node.key_set:
            self.dll.remove(node)
            self.cnt_node.pop(cnt)

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.key_cnt[key] += 1
        cnt = self.key_cnt[key]

        if cnt not in self.cnt_node:
            self.cnt_node[cnt] = Node()
            self.dll.insert_after(self.cnt_node[cnt - 1], self.cnt_node[cnt])
        self.cnt_node[cnt].key_set.add(key)

        if cnt - 1 > 0:  
            self.remove_key(cnt - 1, key)       # remove old (cnt, key) pair

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.key_cnt:
            return

        self.key_cnt[key] -= 1
        cnt = self.key_cnt[key]

        if cnt == 0:
            self.key_cnt.pop(key)
        else:
            if cnt not in self.cnt_node:
                self.cnt_node[cnt] = Node()
                self.dll.insert_before(self.cnt_node[cnt + 1], self.cnt_node[cnt])
            self.cnt_node[cnt].key_set.add(key)

        self.remove_key(cnt + 1, key)       # remove old (cnt, key) pair

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.dll.dummy_head.next == self.dll.dummy_tail:
            return ''
        return self.dll.dummy_tail.prev.get_one_key()

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.dll.dummy_head.next == self.dll.dummy_tail:
            return ''
        return self.dll.dummy_head.next.get_one_key()
