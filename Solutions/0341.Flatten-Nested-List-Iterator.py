"""
341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """



"""
用一个辅助函数把nested_list flatten掉存到一个q中就可以了，用递归去flatten既可以了
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = collections.deque()
        self._flatten(nestedList)
        
    def _flatten(self, nested_lst):
        for lst in nested_lst:
            if lst.isInteger():
                self.q.append(lst.getInteger())
            else:
                self._flatten(lst.getList())
        
    def next(self) -> int:
        if self.hasNext:
            return self.q.popleft()
    
    def hasNext(self) -> bool:
         return len(self.q) > 0


            

""" Implement using q """
class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.q = deque()
        for lst in nested_list:
            self.q.append(lst)
    
    def next(self) -> int:
        if self.hasNext():
            return self.q.popleft()
    
    def hasNext(self) -> bool:
        if len(self.q) == 0:
            return False
        
        while len(self.q) > 0:
            if self.q[0].isInteger():
                return True

            top_item = self.q.popleft()
            for item in top_item.getList()[::-1]:
                self.q.appendleft(item)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


                
"""
solution 3: use a stack
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        # put every item in the nestedList into a stack with reversed order
        for item in nestedList[::-1]:
            self.stack.append(item)
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    # 注意这类问题的主程序一般都写在hasNext里面！
    def hasNext(self) -> bool:
        while self.stack:
            topItem = self.stack[-1]
            if topItem.isInteger():
                return True
            else:            # if it is a nestedList, 就展开。
                self.stack = self.stack[:-1] + topItem.getList()[::-1]
                
        return False



