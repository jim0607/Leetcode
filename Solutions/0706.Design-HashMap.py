"""
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""



"""
There are two main issues that we should tackle, in order to design an efficient hashmap data structure: 
1). hash function design and 2). collision handling.
hashing的冲突解决方法：
(Robert Sedgewick) The first component of a hashing algorithm is hasing function.  A hash function converts keys into array indices. 
The second component of hasing algorithm is collision resolution: a strategy for handling the case when more than one key are hased to the same index.

Seperate chaining
A straightfoward and general approach to resolve collision resoluiton is to build, for each of the m array indeices, 
a linked list of the key-val pairs whose kwys hash to that index.  
This mehtod is known as seperate chaining because items that collide are chained together in separate linked lists.  
The basic idea is to choose m to be sufficiently large that the lists are sufficiently short to enable efficient search throught a two-step process: 
hash to find hte list that could contain the key, then sequentially search through that list for hte key.

Open addressing
Another approach to resove collision is to store n key-val pairs in a hash table of m > n size, relying on empty entries in the table to help with collision resolution.   
Such method are called open addressing.
The simpliest open addressing is called Linear probing: when there is a collision, then we just check the next entry in the table (by incrementing the index).  
hash_table_size是固定的，采取取模的方式，如果出现冲突，比如8%7 = 1,将8放到地址1，下一个进来15%7 也是1，这个时候就把15放到紧接着的后面那个地址也就是2
"""
"""
Some of the questions which can be asked to the interviewer before implementing the solution

For simplicity, are the keys integers only?
For collision resolution, can we use chaining?
Do we have to worry about load factors?
Can we assume inputs are valid or do we have to validate them?
Can we assume this fits memory?
"""

"""
Seperate chaining to resolve hash collision. 
Time complexity for seach/put/get is O(n/m) where m is the talbe size, n is number of keys in the table.
"""
class ListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.val = value    # ******注意定义的ListNode既有key, 也有val
        self.next = None
        

class MyHashMap:
    
    # (Robert Sedgewick) In seperate-chaining, our goal is to choose the table size to be suffciently small so that we do not waste too much memory,
    # but sufficiently large so that we do not waste time searching through along hte chains.
    SIZE = 100007   # need to define the size of hashtable.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # store linked list head in the arr,ListNode(-1, -1)是一个dummy node, 方便后续操作
        self.map = [ListNode(-1, -1) for _ in range(self.SIZE)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.SIZE     # this is hash function - take MOD
        head = self.map[idx]
        curr = head
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value    # update the value if search hit
                break
            curr = curr.next
            
        if not curr.next:       # if search miss, we append the new key-value pair to the tail
            curr.next = ListNode(key, value)
            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.SIZE
        head = self.map[idx]
        curr = head
        while curr.next:
            if curr.next.key == key:    # search hit
                return curr.next.val    
            curr = curr.next
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.SIZE
        head = self.map[idx]
        curr = head
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # if search hit, then remove
                break
            curr = curr.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
