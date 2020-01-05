#
# @lc app=leetcode id=444 lang=python3
#
# [444] Sequence Reconstruction
#
# https://leetcode.com/problems/sequence-reconstruction/description/
#
# algorithms
# Medium (21.14%)
# Likes:    198
# Dislikes: 696
# Total Accepted:    20.9K
# Total Submissions: 99K
# Testcase Example:  '[1,2,3]\n[[1,2],[1,3]]'
#
# Check whether the original sequence org can be uniquely reconstructed from
# the sequences in seqs. The org sequence is a permutation of the integers from
# 1 to n, with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common
# supersequence of the sequences in seqs (i.e., a shortest sequence so that all
# sequences in seqs are subsequences of it). Determine whether there is only
# one sequence that can be reconstructed from seqs and it is the org sequence.
# 
# Example 1:
# 
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
# 
# Output:
# false
# 
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because
# [1,3,2] is also a valid sequence that can be reconstructed.
# 
# 
# 
# Example 2:
# 
# Input:
# org: [1,2,3], seqs: [[1,2]]
# 
# Output:
# false
# 
# Explanation:
# The reconstructed sequence can only be [1,2].
# 
# 
# 
# Example 3:
# 
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
# 
# Output:
# true
# 
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original
# sequence [1,2,3].
# 
# 
# 
# Example 4:
# 
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
# 
# Output:
# true
# 
# 
# 
# 
# UPDATE (2017/1/8):
# The seqs parameter had been changed to a list of list of strings (instead of
# a 2d array of strings). Please reload the code definition to get the latest
# changes.
# 
#
"""举个例子理解题意：
org: [1,2,3], seqs: [[1,2],[1,3]]
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
所以存在后面的元素对前面的元素有依赖关系。可以用topological sort
所有的topological sort 都是两步：
1. 从数字关系求出 indegrees 和 neighbors
2. 然后 BFS

这个题目要做三个判断：
1. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素即可
2. 判断seqs的拓扑排序是否存在，只需判断len(order) 是否等于len(hashmap used for store neighbors)
3. 最后判断这个唯一的拓扑排序order是否等于org
"""
# @lc code=start
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not org and not seqs:
            return True
        if not org or not seqs:
            return False
        
        # 求出inDegrees
        inDegrees = {}
        inDegrees = self.get_inDegree(seqs)

        # 构建hashmap求出neighbors
        edges = collections.defaultdict(list)
        for seq in seqs:
            for i in range(len(seq) - 1):
                edges[seq[i]].append(seq[i+1])

        # BFS
        q = collections.deque()
        for n, val in inDegrees.items():
            if val == 0:
                q.append(n)
        order = []
        while q:
            # 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素即可
            if len(q) > 1:
                return False
            currNode = q.popleft()
            order.append(currNode)
            for neighbor in edges[currNode]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    q.append(neighbor)
        # 首先判断seqs的拓扑排序是否存在，然后判断这个唯一的拓扑排序是否等于org
        return len(order) == len(edges) and order == org

    def get_inDegree(self, seqs):
        inDegrees = collections.defaultdict()
        # initialize
        for seq in seqs:
            for item in seq:
                inDegrees[item] = 0
        
        for seq in seqs:
            for i in range(1, len(seq)):
                inDegrees[seq[i]] += 1

        return inDegrees

        
# @lc code=end

