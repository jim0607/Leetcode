"""
Given an Iterator class interface with methods: next() and hasNext(), 
design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.#         """
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
   
    
"""
solutoin 1: use a q to store the peek 了但是不需要remove掉的nums
"""
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.q = deque()
        self.iter = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.q) > 0:
            return self.q[0]
        else:
            self.q.append(self.iter.next())
            return self.q[0]

    def next(self):
        """
        :rtype: int
        """
        if len(self.q) > 0:
            return self.q.popleft()
        else:
            return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0 or self.iter.hasNext()
    
    
"""
solution 2: 我们看到solution 1中只用到了q[0], 所以其实可以用一个参数self.next_item来代替q[0]就可以了
"""
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_item = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_item

    def next(self):
        """
        :rtype: int
        """
        top = self.next_item
        self.next_item = self.iterator.next() if self.iterator.hasNext() else None
        return top

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_item != None
