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
"""
分三步：
1. construct a dictoinary of adjacency list for the graph
2. get in_degree information for all nodes
3. topological sort - bfs
step I: initialze q by putting all in_degree = 0 into q
step II: keep adding in_degree = 0 node into q and pop out while updating res
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. construct a dictoinary of adjacency list for the graph
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)      # topological sorting 针对有向图, so do not append v to u!!
            
        # 2. get in_degree information for all nodes
        in_degrees = collections.defaultdict(int)
        for u, v in prerequisites:
            if v not in in_degrees:
                in_degrees[v] = 0
            in_degrees[u] += 1
            
        # 3. topological sort - bfs
        # step I: initialze q by putting all in_degree = 0 into q
        q = collections.deque()
        for node, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(node)
        
        # step II: keep adding in_degree = 0 node into q and pop out while updating res
        res = []
        while len(q) > 0:
            curr_node = q.popleft()
            res.append(curr_node)       # update res after each pop
            for next_node in graph[curr_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:  # **Always append all the inDegree=0 items in the queue
                    q.append(next_node)
                    
        return len(res) == len(graph)
