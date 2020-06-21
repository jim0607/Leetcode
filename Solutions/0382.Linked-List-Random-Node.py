382. Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();


"""
solution 1: reservoir sampling: O(1), O(n). It is good for really large linkedlist and the linkedlist dynamically changing length
"""

import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        curr = self.head
        res = -1
        cnt = 0
        while curr:
            cnt += 1
            rand_idx = random.randrange(cnt)
            if rand_idx == 0:    # 这里不一定random_idx == 0, 我们用random_idx等于啥都行，我们需要的只是等于某一个数的概率是1/m
                res = curr.val
            curr = curr.next
            
        return res


"""
solution 2: O(n), O(1) just use an arr to store all the node vals
"""

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        rand_idx = random.randrange(len(self.nums))
        return self.nums[rand_idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
