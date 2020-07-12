705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)



"""
There are two key questions that one should address, in order to implement the HashSet data structure, 
namely hash function and collision handling.
Here, we use seperate chaining for resolve hash collision.
"""
class ListNode:
    
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    SIZE = 10007   # 为什么改成1007就不行呢？
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [ListNode(-1) for _ in range(self.SIZE)]

    def add(self, key: int) -> None:
        idx = key % self.SIZE
        head = self.hashset[idx]
        curr = head.next
        if not curr:
            head.next = ListNode(key)       # 注意只有.next才能成功新建一个ListNode到linked list中
        else:
            if curr.key == key:
                return
            while curr.next:
                if curr.key == key:
                    return
                curr = curr.next
            curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % self.SIZE
        head = self.hashset[idx]
        prev, curr = head, head.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.SIZE
        head = self.hashset[idx]
        curr = head.next
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
