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

       
       
"""
Solution 3: union find
"""
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:       # change list of edges representation to adjacency list representation 
            graph[u].append(v)
            graph[v].append(u)
            
        uf = UnionFind(graph)
        
        visited = set()     # 用visited标记一下不然会超时, 每次做union就标记visited一下
        for node in graph:
            for dislike_node in graph[node]:
                if uf.connected(node, dislike_node):
                    return False
                if dislike_node in visited:
                    continue
                for dis_dislike_node in graph[dislike_node]:    # 敌人的敌人是朋友
                    uf.union(node, dis_dislike_node)
                    visited.add(node)
                    visited.add(dis_dislike_node)
                    
        return True
        
        
class UnionFind:
    
    def __init__(self, graph):
        self.father = collections.defaultdict()
        for node in graph:
            self.father[node] = node
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b


         
"""
follow up 1是有几种不同的分组方法，dfs解之。follow up 2是如何将两个组的人数尽可能分的一样多，在面试官提醒下逐步推导出dp的方法，具体不记得了。
"""
follow up 1: dfs 找可能的组合方法，然后找闲云野鹤，闲云野鹤就是没有人dislike他，也不去dislike别人的人。
Consider from 闲云野鹤 the persons who can go into both A and B group.  闲云野鹤 = n, then we have 2**n different组合方式?

Follow up2:
本质竟然是dp 背包问题
S1-S2=diff.
S1 
S2
https://leetcode.com/problems/tallest-billboard/



Connected component.

Delta possible

1         2
A <-> B C
1        2
D<-> X Y

-1   -2 
1    0
      0
      2

A: b 
B: a

a: 2
b: 3
diff = b-a = 1

最后问题变成了：
nums = [1, 1, 2, 2, 10, 9], nums里面存这个idx下的人dislike的人数。
然后去找怎样把nums分成两个子数组，使得他们的和最接近 -- 背包问题！！！
sums = sum(nums)
find a subsequence which has closet value to sums / 2
有点像416. Partition Equal Subset Sum 



TF: F[I][D]=F[I-1][D-abs(Right-Left)] || F[I-1][D+abs(right-left)]
std::min(abs(D) | D ~ delta values that are possible).


// All connected components have been processed.  We are looking for std::min(abs(I) | I ~ delta values that are possible).

2X * X=2X^2.
-X X total number of people.
X 

DP[N]
-1 OK.
1 OK
A <-> B C



D<-> X Y

(A,D) (BCXY)  -> (A X Y) (B C D)	 

Follow up2:

https://leetcode.com/problems/tallest-billboard/
