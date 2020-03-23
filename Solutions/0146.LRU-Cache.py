146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4



"""solution 1: use a queue to store the time-linear data and a dictionary to store the cache number, very straight forward.
a cache实际上就是一个hashmap/dictionary"""
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = {}
        self.q = collections.deque()    # 保存key，最recently used放在最后面，最least used放在最前面。
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.q.remove(key)      # O(N)
            self.q.append(key)
            return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:       # if key not in cache, put it in cache and q, and also check the size of q
            self.cache[key] = value
            self.q.append(key)
            if len(self.q) > self.capacity:
                leastUsedKey = self.q.popleft()
                del self.cache[leastUsedKey]
        else:                           # if key is in cache, then renew it's corresponding value
            self.cache[key] = value
            self.q.remove(key)      # O(N)
            self.q.append(key)



"""solution 2: OrderedDict
python中的orderedDict其实就是solution 3中类似的linkedlist实现的，相当于直接使用封装好的函数了.
orderedDict直接就存在一个orderedDict.move_to_end(key)操作，和orderedDict.popitem(last = False)操作"""
# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.orderedDict = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.orderedDict:
            return -1
        else:
            self.orderedDict.move_to_end(key)
            return self.orderedDict[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.orderedDict:
            self.orderedDict[key] = value
            if len(self.orderedDict) > self.capacity:
                self.orderedDict.popitem(last = False)
            self.orderedDict.move_to_end(key)
        else:
            self.orderedDict[key] = value
            self.orderedDict.move_to_end(key)




"""solution 3: use a double linked list and a dictionary to implment the ordereddict in solution 2
Double linkedlist: newest node append to tail, eldest node remove from head, so that the operation is O(1)
Hashmap: key is key, value is 以key为key的一个double linkedlist node"""
class DLLNode:
    # define a double-linked-list node, with four properties
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}     # key is key, val is the corresponding node
        self.capacity = capacity
        
        self.dummyHead = DLLNode(0, 0)      # 定义一个dummy tail 和一个 dummy head
        self.dummyTail = DLLNode(0, 0)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        
    def removeNode(self, node: DLLNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insertToTail(self, node: DLLNode):
        self.dummyTail.prev.next = node
        node.prev = self.dummyTail.prev
        
        self.dummyTail.prev = node
        node.next = self.dummyTail
        
    def moveToTail(self, node: DLLNode):
        self.removeNode(node)
        self.insertToTail(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.moveToTail(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.moveToTail(self.cache[key])
        else:
            newNode = DLLNode(key, value)
            self.cache[key] = newNode
            self.insertToTail(newNode)
            if len(self.cache) > self.capacity:
                eldestNode = self.dummyHead.next
                self.removeNode(eldestNode)
                del self.cache[eldestNode.key]
                
                
/*
 * @lc app=leetcode id=146 lang=csharp
 *
 * [146] LRU Cache
 */

// @lc code=start

public class DLLNode {
    public int key;
    public int val;
    public DLLNode prev;
    public DLLNode next;
    
    public DLLNode(int key, int value) {
        this.key = key;
        this.val = value;
        this.prev = null;
        this.next = null;
    }
}

public class LRUCache {
    public int capac;
    public Dictionary<int, DLLNode> cache;
    public DLLNode dummyHead;
    public DLLNode dummyTail;
        
    public LRUCache(int capacity) {
        this.cache = new Dictionary<int, DLLNode>();
        this.capac = capacity;

        this.dummyHead = new DLLNode(0, 0);
        this.dummyTail = new DLLNode(0, 0);
        this.dummyHead.next = this.dummyTail;
        this.dummyTail.prev = this.dummyHead;
    }

    public void removeNode(DLLNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public void insertToTail(DLLNode node) {
        this.dummyTail.prev.next = node;
        node.prev = this.dummyTail.prev;
        this.dummyTail.prev = node;
        node.next = this.dummyTail;
    }

    public void moveToTail(DLLNode node) {
        removeNode(node);
        insertToTail(node);
    }
    
    public int Get(int key) {
        if (this.cache.ContainsKey(key)) {
            moveToTail(this.cache[key]);
            return this.cache[key].val;
        } else {
            return -1;
        }
    }
    
    public void Put(int key, int value) {
        if (this.cache.ContainsKey(key)) {
            this.cache[key].val = value;
            moveToTail(this.cache[key]);
        } else {
            DLLNode newNode = new DLLNode(key, value);
            this.cache[key] = newNode;
            insertToTail(newNode);
            if (this.cache.Count() > this.capac) {
                DLLNode eldestNode = this.dummyHead.next;
                removeNode(eldestNode);
                this.cache.Remove(eldestNode.key);
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end
