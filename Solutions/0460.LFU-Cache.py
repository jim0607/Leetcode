"""
460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.


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
                








class LFUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = collections.defaultdict(int)   # key is key, val is freq  
        
        # key is freq, val is a list of keys corresponding to the freq.  In order to maintain the list ordered, we use DLL (ordered dictionary)
        # in the ordered dictionary, key is key, val is value corresponding to the key. We put the LRU key at the beginning of the DLL.
        self._freqs = collections.defaultdict(lambda: collections.OrderedDict())    
        self._min_freq = 0      # the smallest freq in the cache 

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        
        self._update(key, None)
        
        return self._freqs[self._cache[key]][key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        
        if key in self._cache:
            self._update(key, value)
        else:
            if len(self._cache) == self.capacity:       # if cache is full, remove the LFU key
                # del the least used key from the cache, as well as it's coreesponding freq in the ordered dictonary
                # the leased frequenctly used num should have min freq
                
                remove_key = self._freqs[self._min_freq].popitem(last = False)[0]    # ordered dictionary pop a key value pair (key, val) from the beginning of the DLL: .popitem(last = False)
                del self._cache[remove_key]                                          # pop出来的是一个(key, value) pair
                
            # add the new key
            self._min_freq = 1
            self._cache[key] = 1
            self._freqs[1][key] = value    # OrderedDict添加到末尾, 新放进去的都默认放到最后面
            
    def _update(self, key, value):
        """
        1. update freq, freq+=1
        2. update val 
        3. update min_freq if neccessarry
        """
        freq = self._cache[key] 
        val = self._freqs[freq].pop(key)    # remove current key and get the val - pop(key) is O(1) for OrderedDict
        
        if self._min_freq == freq and not self._freqs[freq]:        # 3. update min_freq if neccessarry
            self._min_freq = freq + 1    
            
        freq += 1
        self._cache[key] = freq       # 1. update freq, freq+=1
        self._freqs[freq][key] = value if value != None else val        # 2. update val - OrderedDict添加到末尾

        

"""
非常常考的题套路就是先给一个题求Kth largest, 然后follow up是data stream, 这个问题的solution 是LFU - O(1)
July 2020 的Google 面经就有:
Given logs from a YouTube service, and an Integer K. Return K most searched strings from the logs. 
Discussed creating map of unique strings and counts and going over the map to find the K strings with highest counts by sorting the unique strings by their count. 
Talked about improving the sort from O(NlogN) to O(NlogK) by using a min heap to sort.
Heap O(NlogK)
Quick Select O(N)
Follow ups: How would you change your code for a stream of logs, Interviewer said that my points and solution were acceptable.
Solution: LFU - O(1)
"""
