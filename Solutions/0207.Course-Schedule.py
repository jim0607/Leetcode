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
"""分三步：1. collect the inDegree of each node
2. collect the neighbors information
3. topological sort - BFS"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or not prerequisites:
            return True
        
        inDegrees = collections.defaultdict(int)
        inDegrees = self.getInDegrees(numCourses, prerequisites)
        print(inDegrees)
        
        # 用一个hashmap来存储相邻节点
        neighbors = collections.defaultdict(list)
        for u, v in prerequisites:
            neighbors[v].append(u)    # topological sorting 针对有向图, so do not append v to u!!
            
        q = collections.deque()
        visited = set()
        for node, inDegree in inDegrees.items():
            if inDegree == 0:
                q.append(node)
                visited.add(node)       # 孪生兄弟
                
        while q:
            currNode = q.popleft()
            for neighbor in neighbors[currNode]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    q.append(neighbor)
                    visited.add(neighbor)       # 孪生兄弟
                    
        return len(visited) == numCourses
    
    def getInDegrees(self, numCourses, prerequisites):
        inDegrees = collections.defaultdict(int)
        for node in range(numCourses):      # initialize
            inDegrees[node] = 0
        
        for u, v in prerequisites:
            inDegrees[u] += 1
            
        return inDegrees
