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


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        
        # 1. construct a dictoinary of adjacency list for the graph
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)      # topological sorting 针对有向图, so do not append v to u!!
            
        # 2. get in_degree information for all nodes
        in_degrees = collections.defaultdict(int)
        for n in range(numCourses):
            in_degrees[n] = 0
        for u, v in prerequisites:
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
                    
        return res if len(res) == len(graph) else []
