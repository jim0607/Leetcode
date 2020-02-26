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


”“”所有的topological sort 都是两步：
1. 从数字关系求出 indegrees 和 neighbors
2. 然后 BFS“”“


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        # 找到所有节点的inDegree值
        inDegrees = collections.defaultdict(int)
        inDegrees = self.getInDegrees(numCourses, prerequisites)
        
        # 用一个hashmap存储边/邻居
        neighbors = collections.defaultdict(list)
        for u, v in prerequisites:
            neighbors[v].append(u)
            
        # BFS
        res = []
        q = collections.deque()
        for node, inDegree in inDegrees.items():
            if inDegree == 0:
                q.append(node)
                res.append(node)
                
        while q:
            currNode = q.popleft()
            for neighbor in neighbors[currNode]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    q.append(neighbor)
                    res.append(neighbor)
                    
        return res if len(res) == numCourses else []
    
    def getInDegrees(self, numCourses, prerequisites):
        inDegrees = collections.defaultdict(int)
        for n in range(numCourses):
            inDegrees[n] = 0
            
        for u, v in prerequisites:
            inDegrees[u] += 1
            
        return inDegrees
