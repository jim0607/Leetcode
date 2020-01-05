#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (37.37%)
# Likes:    1444
# Dislikes: 99
# Total Accepted:    198.8K
# Total Submissions: 530.3K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]

        # 用一个hashmap存储边/邻居
        edges = {x: [] for x in range(numCourses)}
        for u, v in prerequisites:
            edges[v].append(u)
            
        # 找到所有节点的inDegree值
        inDegree = {}
        inDegree = self.get_inDegree(numCourses, prerequisites)

        # Topological sort - BFS
        q = collections.deque()
        for n, val in inDegree.items():
            if val == 0:
                q.append(n)
        order = []
        while q:
           currNode = q.popleft()
           order.append(currNode)
           for neighbor in edges[currNode]:
               inDegree[neighbor] -= 1
               if inDegree[neighbor] == 0:
                   q.append(neighbor)

        if len(order) == numCourses:
            return order
        else:
            return []

    def get_inDegree(self, numCourses, prerequisites):
        inDegree = collections.defaultdict()
        # initialize the dict
        for i in range(numCourses):
            inDegree[i] = 0
        
        for u, v in prerequisites:
            inDegree[u] += 1
        
        return inDegree

# @lc code=end

