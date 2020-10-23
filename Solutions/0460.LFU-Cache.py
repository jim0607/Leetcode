"""
460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, 
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. 
This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""




"""
Use a dictionary to store (key, freq) pair.
Use another dicitonary to store (freq, list of key) pair, where list of key is OrderedDict like LRU to enable O(1) operations.
"""
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_freq = defaultdict(int)               # key --> freq
        self.freq_to_orddict = defaultdict(OrderedDict)   # freq --> orddict (key --> val)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        
        freq = self.key_to_freq[key]
        val = self.freq_to_orddict[freq][key]
        self.update(key, val)
        
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.key_to_freq:
            self.update(key, value)
        
        else:
            if len(self.key_to_freq) == self.capacity:    # first remove LFU if oversized 
                min_key, min_val = self.freq_to_orddict[self.min_freq].popitem(last = False)  # del the coreesponding freq in the ordered dictonary
                del self.key_to_freq[min_key]     # del the least used key from the cache
            
            self.min_freq = 1                             # then update key_to_freq, freq_to_orddict and min_freq
            self.key_to_freq[key] = 1
            self.freq_to_orddict[1][key] = value
            
    def update(self, key, value):
        """
        Update key --> value pair for an already exsited key
        1. update freq, freq += 1
        2. update value
        3. update min_freq if neccessarry
        """
        freq = self.key_to_freq[key]
        
        if self.min_freq == freq and len(self.freq_to_orddict[freq]) == 1:  # update min_freq if neccessary
            self.min_freq += 1
            
        self.freq_to_orddict[freq].pop(key)     # first delete the key --> val pair in orddict
        freq += 1                               
        self.key_to_freq[key] = freq            # then update key_to_freq and freq_to_orddict using the new freq
        self.freq_to_orddict[freq][key] = value


"""
非常常考的题套路就是先给一个题求Kth largest, 然后follow up是data stream, 这个问题的solution 是LFU - O(1)
July 2020 的Google 面经: Given logs from a YouTube service, and an Integer K. Return K most searched strings from the logs.
Solution: Heap O(NlogK), or Quick Select O(N).

Follow ups: How would you change your code for a stream of logs?
Let's re-state the problem: 
Implement the TopKFreq class:
TopKFreq(K): Initializes the object with the capacity of the data structure.
int get(): return the K most frequently searched strings in a data stream
void put(s): Sets or inserts the value if the s is not already present. When the cache reaches its capacity, 
it should invalidate the least frequently used item before inserting a new item. For this problem, 
when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be evicted. 
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
"""
class TopKFreq:

    def __init__(self, K):
        self.K = K   # keep the size of str_to_freq to be K, so that all the strings in str_to_freq are top K frequently searched
        self.str_to_freq = defaultdict(int)
        self.freq_to_set(OrderedSet)        # 这里只需要OrderedSet, 不需要ordered dictionary, 因为key是string, 没有val
        self.min_freq = 0

    def search(self, s):
        if s in self.str_to_freq:
            freq = self.str_to_freq[s]

            if freq == self.min_freq and len(self.freq_to_set[freq]) == 1:
                self.min_freq += 1

            self.freq_to_set[freq].remove(s)  # since we need to remove, we cannot just use a list, instead, we have to use OrderedSet (actually DLL)
            freq += 1
            self.str_to_freq[s] = freq
            self.freq_to_set[freq].insert_to_end(s)

        else:
            # When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item
            if len(self.str_to_freq) == self.K:
                min_s = self.freq_to_set[self.min_freq].pop_first()
                del self.str_to_freq[min_s]
            self.min_freq = 1
            self.str_to_freq[s] = 1
            self.freq_to_set[1].append(s)

    def get(self):
        """
        Return the K most frequently searched strings. Here we don't update frequency.
        """
        return [s for s in self.str_to_freq]


def DLLNode:

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


def OrderedSet:

    def __init__(self):
        """
        实现OrderedSet需要两个数据结构：
        1. A DLL, so that we can move a node to end, and pop first node in O(1) time
        2. A dictionary, for fast key --> node look up
        """
        self.key_to_node = defaultdict(DLLNode)

        self.dummy_head = DLLNode(-1, -1)
        self.dummy_tail = DLLNode(-1, -1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def remove(self, key):
        """
        Remove an already existed node from the DDL
        """
        node = self.key_to_node[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.key_to_node[key]

    def insert_to_end(self, key):
        """
        Insert a new node to the end of the DDL
        """
        new_node = DLLNode(key)
        self.key_to_node[key] = new_node

        self.dummy_tail.prev.next = new_node
        new_node.prev = self.dummy_tail.prev
        new_node.next = self.dummy_tail
        self.dummy_tail.prev = new_node

    def pop_first(self, key):
        """
        Pop the first node in the DLL (return the key)
        """
        first_node = self.dummy_head.next
        first_node_key = first_node.key
        self.remove_node(first_node_key)
        return first_node_key
