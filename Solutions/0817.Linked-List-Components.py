"""
817. Linked List Components

We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.
"""

"""
直接遍历linked list, 如果curr.val in nums_set and curr.next.val in nums_set, 那就disjoint_cnt -= 1
O(N + M), where N is how many nodes are there in liked list, M = len(nums)
"""
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        nums_set = set(nums)
        disjoint_cnt = len(nums)
        curr = head
        while curr and curr.next:
            if curr.val in nums_set and curr.next.val in nums_set:
                disjoint_cnt -= 1
            curr = curr.next
        return disjoint_cnt


"""
find connected components, union find is good for that
O(N + M^2) where N is how many nodes are there in liked list, M = len(nums)
"""
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        # step 1: build the graph
        graph = defaultdict(int)
        curr = head
        while curr and curr.next:
            graph[curr.val] = curr.next.val
            curr = curr.next

        # step 2: do union if two values are connected
        uf = UnionFind(nums)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] in graph and graph[nums[i]] == nums[j] or (nums[j] in graph and graph[nums[j]] == nums[i]):
                    uf.union(nums[i], nums[j])
        return uf.disjoint_cnt
    
    
class UnionFind:
    
    def __init__(self, nums):
        self.father = defaultdict(int)
        self.disjoint_cnt = 0
        for num in nums:
            self.father[num] = num
            self.disjoint_cnt += 1
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.disjoint_cnt -= 1
