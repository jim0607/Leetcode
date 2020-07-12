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
Some of the questions which can be asked to the interviewer before implementing the solution

For simplicity, are the keys integers only?
For collision resolution, can we use chaining?
Do we have to worry about load factors?
Can we assume inputs are valid or do we have to validate them?
Can we assume this fits memory?
"""

"""
Seperate chaining to resolve hash collision.
"""
class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None        
        
        
class MyHashMap:
    
    SIZE = 100007   # 不知道为什么改成10007就过不了某个test case

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = [ListNode(-1, -1) for _ in range(self.SIZE)]     # store linked list head in the arr,ListNode(-1, -1)是一个dummy node, 方便后续操作

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.SIZE
        head = self.hashmap[idx]
        if not head.next:
            head.next = ListNode(key, value)
            
        else:
            curr = head.next
            if curr.key == key:
                curr.val = value
                return
            
            while curr.next:
                if curr.key == key:
                    curr.val = value    # update the (key-val) pair
                    return
                curr = curr.next
        
            curr.next = ListNode(key, value)  # if search miss, create a new node at the end            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.SIZE
        head = self.hashmap[idx]
        if not head.next:
            return -1
        
        curr = head.next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.SIZE
        head = self.hashmap[idx]
        if not head.next:
            return

        prev, curr = head, head.next    # constructor里面初始化一些dummy head是为了这里更方便remove
        while curr:
            if curr.key == key:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


"""
由于题目说明了keys are in range [0, 1000000], so the below array method works. But don't do that in an interview.
Because we are supposed to use seperate chaining or open addressing for hashing collision resolution.
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.SIZE = 1000001
        self.hashmap = [None for _ in range(self.SIZE)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashmap[key % self.SIZE] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.hashmap[key % self.SIZE] == None:   # 不能用not self.hashmap[key % self.SIZE], 因为self.hashmap[key % self.SIZE]有可能等于0
            return -1
        return self.hashmap[key % self.SIZE]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hashmap[key % self.SIZE] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
