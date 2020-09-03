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
2. 然后 BFS"""


"""
这个题目要做三个判断：
1. 判断seqs的拓扑排序是否存在，只需判断len(res) 是否等于len(graph) or len(inDegrees), 如果小于说明有孤立节点，如果大于说明有环，两者都不存在拓扑排序
2. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素, 即每一层只有一个选择: if len(q)>1: return False
3. 最后判断这个唯一的拓扑排序res是否等于org
"""

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # 1. construct the graph
        graph = collections.defaultdict(list)
        for seq in seqs:
            for i in range(len(seq)-1):
                curr, next = seq[i], seq[i+1]
                graph[curr].append(next)
                
        # 2. get in_degrees
        in_degrees = collections.defaultdict(int)
        for seq in seqs:
            for node in seq:
                in_degrees[node] = 0    # 注意这一步的初始化很重要，不然in_degrees里就没有in_degree=0的node了
        for seq in seqs:
            for node in seq[1:]:
                in_degrees[node] += 1   # 注意一个node的in_degree值代表的是有多少node指向它
                
        # 3. bfs: I. put all in_degree = 0 nodes into q
        q = collections.deque()
        for node, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(node)
                
        # 3. bfs: II. keep appending the in_degree = 0 and pop wile updating res
        res = []
        while len(q) > 0:
            if len(q) > 1:   # 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素，即每一层只有一个选择
                return False
            
            curr_node = q.popleft()
            res.append(curr_node)       # 不要忘了update res every time we pop
            
            for next_node in graph[curr_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    q.append(next_node)

        # 首先判断seqs的拓扑排序是否存在，然后判断这个唯一的拓扑排序是否等于org
        return len(res) == len(graph) and res == org
