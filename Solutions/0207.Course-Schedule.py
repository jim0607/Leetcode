#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (40.23%)
# Likes:    2615
# Dislikes: 134
# Total Accepted:    301.4K
# Total Submissions: 747.7K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
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
"""分两步：1. collect the inDegree of each node
2. topological sort - BFS"""
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        if not prerequisites:
            return True
        
        # 用一个hashmap来存储相邻节点
        edges = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
            
        inDegree = {}
        inDegree = self.get_inDegree(numCourses, prerequisites)

        # BFS 模板
        q = collections.deque()
        for n, cnt in inDegree.items():
            if cnt == 0:
                q.append(n)
        cntCourses = 0
        while q:
            currNode = q.popleft()
            cntCourses += 1
            for neighbor in edges[currNode]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)

        return cntCourses == numCourses

    def get_inDegree(self, numCourses, prerequisites):
        inDegree = collections.defaultdict()
        # initialize
        for i in range(numCourses):
            inDegree[i] = 0

        for u, v in prerequisites:
            inDegree[u] += 1
        
        return inDegree

# @lc code=end

