"""由于需要实现popMax函数，所以只能用O(N)的时间复杂度了，反正需要O(N)时间，索性就用一个数组"""
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        maxItem = max(self.stack)
        for i in range(len(self.stack) - 1, -1, -1):
            if maxItem == self.stack[i]:
                self.stack = self.stack[:i] + self.stack[i + 1:]
                break
        
        return maxItem

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


Follow up:
we can use double linked list and TreeMap to make it O(logN)
Using structures like Array or Stack will never let us popMax quickly. We turn our attention to tree and linked-list structures that have a lower time complexity for removal, with the aim of making popMax faster than O(N) time complexity.

Say we have a double linked list as our "stack". This reduces the problem to finding which node to remove, since we can remove nodes in O(1) time.

We can use a TreeMap mapping values to a list of nodes to answer this question. TreeMap can find the largest value, insert values, and delete values, all in O(log N) time.
