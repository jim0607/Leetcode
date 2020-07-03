886. Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false




        
"""
Assign the first person RED, then anyone the first person doesn't like should be assigned BLUE. Then anyone those BLUE person don't like should be RED.
If a person has to be both BLUE and RED, then it is impossible. 
Solution 1: dfs - Time: O(V+E); Space: O(V+E)
"""
"""
Assign the first person RED, then anyone the first person doesn't like should be assigned BLUE. Then anyone those BLUE person don't like should be RED.
If a person has to be both BLUE and RED, then it is impossible. 
"""
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:       # change list of edges representation to adjacency list representation 
            graph[u].append(v)
            graph[v].append(u)
            
        
        RED, BLUE = set(), set()
        
        # 这里的should_be_red时每一层必须携带的信息，不能用全局变量，必须传到参数里！一般没把握的话最好是传到参数里，传到参数里一定可以保证每一层得到正确的信息。
        # 就像bfs能用层序遍历一定可以保证是对的，不用层序遍历的普通bfs不一定能接所有题，比如这一题不用层序遍历bfs就解不了。
        def dfs(curr, should_be_red):   
            should_be_red = not should_be_red
            for next in graph[curr]:
                if should_be_red:
                    if next in BLUE:
                        return False
                    if next in RED:
                        continue
                    RED.add(next)
                    if not dfs(next, should_be_red):
                        return False
                elif not should_be_red:
                    if next in RED:
                        return False
                    if next in BLUE:
                        continue
                    BLUE.add(next)
                    if not dfs(next, should_be_red):
                        return False
                    
            return True
                
        
        # 注意这里不能只从单一节点1出发，因为1可能只和2连在一起，2也只和1连在一起，而后面还有一堆
        # 比如[[1,2],[3,4],[4,5],[5,3]], [1,2]和后面完全脱钩了，如果只从1出发的话就遍历不到3,4,5了
        for i in range(1, N + 1):
            if i not in RED and i not in BLUE:
                RED.add(i)
                if not dfs(i, True):
                    return False
                
        return True




"""
Assign the first person RED, then anyone the first person doesn't like should be assigned BLUE. Then anyone those BLUE person don't like should be RED.
If a person has to be both BLUE and RED, then it is impossible. 
Soluiton 2: bfs - Time: O(V+E); Space: O(V+E)
"""
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:       # change list of edges representation to adjacency list representation 
            graph[u].append(v)
            graph[v].append(u)
            
        
        RED, BLUE = set(), set()
        def bfs(i):
            q = collections.deque()
            q.append(i)
            RED.add(i)
            should_be_red = True
            while q:
                lens = len(q)
                should_be_red = not should_be_red
                for _ in range(lens):
                    curr = q.popleft()      # 注意因为是带层序遍历的bfs, 妄想简单改成q.pop()来实现dfs是不行的！
                    for next in graph[curr]:
                        if should_be_red:
                            if next in BLUE:
                                return False
                            if next in RED:
                                continue
                            q.append(next)
                            RED.add(next)
                        elif not should_be_red:
                            if next in RED:
                                return False
                            if next in BLUE:
                                continue
                            q.append(next)
                            BLUE.add(next)
                        
            return True  
        
        # 注意这里不能只从单一节点1出发，因为1可能只和2连在一起，2也只和1连在一起，而后面还有一堆
        # 比如[[1,2],[3,4],[4,5],[5,3]], [1,2]和后面完全脱钩了，如果只从1出发的话就遍历不到3,4,5了
        for i in range(1, N + 1):
            if i not in RED and i not in BLUE:
                if not bfs(i):
                    return False
                
        return True