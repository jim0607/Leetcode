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
代码看上去很长，但是逻辑很简单
"""
class DLLNode:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cnt = 0
        self.capacity = k
        self.head = DLLNode(-1)     # create a dummy head and a dummy tail
        self.tail = DLLNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.cnt == self.capacity:
            return False
        
        new_node = DLLNode(value)
        
        # below we will insert the new_node right after the dummy head,注意事项insert到dummy head后面而不是前面
        next_node = self.head.next
        new_node.next = next_node
        next_node.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        
        self.cnt += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.cnt == self.capacity:
            return False
        
        new_node = DLLNode(value)
        prev_node = self.tail.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.tail
        self.tail.prev = new_node
        
        self.cnt += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.cnt == 0:
            return False
        
        next_node = self.head.next
        next_next_node = next_node.next
        self.head.next = next_next_node
        next_next_node.prev = self.head
        
        self.cnt -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.cnt == 0:
            return False
        
        prev_node = self.tail.prev
        prev_prev_node = prev_node.prev
        prev_prev_node.next = self.tail
        self.tail.prev = prev_prev_node
        
        self.cnt -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.cnt == 0 else self.head.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.cnt == 0 else self.tail.prev.val

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
