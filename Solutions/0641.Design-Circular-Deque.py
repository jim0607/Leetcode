"""
641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
"""

"""
代码看上去很长，但是逻辑很简单
"""
class DoubleListNode:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.dummyhead = DoubleListNode(-1)
        self.dummytail = DoubleListNode(-1)
        self.cnt = 0
        self.capacity = k
        
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        # below we insert the new_node right after the dummy head,注意事项insert到dummy head后面而不是前面
        new_node = DoubleListNode(value)
        self.dummyhead.next.prev = new_node
        new_node.next = self.dummyhead.next
        self.dummyhead.next = new_node
        new_node.prev = self.dummyhead
        
        self.cnt += 1

        return True
    
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        new_node = DoubleListNode(value)
        self.dummytail.prev.next = new_node
        new_node.prev = self.dummytail.prev
        self.dummytail.prev = new_node
        new_node.next = self.dummytail        

        self.cnt += 1
        
        return True
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.dummyhead.next = self.dummyhead.next.next
        self.dummyhead.next.prev = self.dummyhead
        
        self.cnt -= 1
        
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.dummytail.prev = self.dummytail.prev.prev
        self.dummytail.prev.next = self.dummytail
        
        self.cnt -= 1
        
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.dummyhead.next.val 

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.dummytail.prev.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cnt == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cnt == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
