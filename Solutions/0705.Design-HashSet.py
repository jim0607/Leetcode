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
Seperate chaining to resolve hash collision. 
Time complexity for seach/put/get is O(n/m) where m is the talbe size, n is number of keys in the table.
"""
class ListNode:
    
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    # (Robert Sedgewick) In seperate-chaining, our goal is to choose the table size to be suffciently small so that we do not waste too much memory,
    # but sufficiently large so that we do not waste time searching through along hte chains.
    SIZE = 100007   # 如果改成10007就会有test case TLE. 这是因为如果size太小，collision就会很多，time complexity就会增加
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [ListNode(-1) for _ in range(self.SIZE)]

    def add(self, key: int) -> None:
        head = self.hashset[key % self.SIZE]
        curr = head
        while curr.next:
            if curr.next.key == key:    # search hit
                break
            curr = curr.next
        curr.next = ListNode(key)       # seach miss

    def remove(self, key: int) -> None:
        head = self.hashset[key % self.SIZE]
        curr = head
        while curr.next:
            if curr.next.key == key:    # search hit
                curr.next = curr.next.next
                break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        head = self.hashset[key % self.SIZE]
        curr = head
        while curr.next:
            if curr.next.key == key:    # search hit
                return True
        return False    # search miss

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
