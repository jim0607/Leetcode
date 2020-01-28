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
        if key not in self.cache:
            self.cache[key] = value
            self.q.append(key)
            if len(self.q) > self.capacity:
                leastUsedKey = self.q.popleft()
                del self.cache[leastUsedKey]
        else:
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
class DLinkedList:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dummyHead = DLinkedList(0, 0)    # 定义一个dummy tail 和一个 dummy head
        self.dummyTail = DLinkedList(0, 0)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

        self.cache = {}
        self.capacity = capacity

    # remove a node
    def remove_node(self, node: DLinkedList):
        node.prev.next = node.next
        node.next.prev = node.prev

    # insert a node to tail
    def insert_to_tail(self, node: DLinkedList):
        self.dummyTail.prev.next = node
        node.prev = self.dummyTail.prev

        node.next = self.dummyTail
        self.dummyTail.prev = node


    # move a node to tail
    def move_to_tail(self, node: DLinkedList): 
        self.remove_node(node)
        self.insert_to_tail(node)
    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move_to_tail(node)
            return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            newNode = DLinkedList(key, value)
            self.cache[key] = newNode
            self.insert_to_tail(newNode)
            if len(self.cache) > self.capacity:
                eldestNode = self.dummyHead.next
                self.remove_node(eldestNode)
                del self.cache[eldestNode.key]
        else:
            existedNode = self.cache[key]       # 注意newNode 不能直接定义一个newNode为DListNode(key, value)，因为会丢失原来那个node在链表中的位置。
            existedNode.val = value   # 更新existed node
            self.cache[key] = existedNode
            self.move_to_tail(existedNode)
