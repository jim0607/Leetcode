"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n-1 and n-1 roads such that 
there is only one way to travel between two different cities (this network form a tree). 
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. 
Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 

Constraints:

2 <= n <= 5 * 10^4
connections.length == n-1
connections[i].length == 2
0 <= connections[i][0], connections[i][1] <= n-1
connections[i][0] != connections[i][1]
"""



"""
问题等价于原来0不能到达所有的nodes, 现在需要改变一些connections使得0可以到达所有nodes.
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # step 1: construct the graph using adjacency list
        graph = collections.defaultdict(list)   
        anti_graph = collections.defaultdict(list)   
        for u, v in connections:
            graph[u].append(v)          
            anti_graph[v].append(u)    # 注意建anti-directions图的时候要反过来
            
        
        def dfs(curr_node):
            """
            从0出发，先在anti_graph里面找next_node一直往前走，
            然后从graph里面找next_node, 从graph里面找说明需要反向，所以self.cnt += 1
            """
            if len(visited) == n:
                return
            visited.add(curr_node)
            
            for next_node in anti_graph[curr_node]:
                if next_node not in visited:
                    dfs(next_node)
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    self.cnt += 1
                    dfs(next_node)
        
        
        self.cnt = 0
        visited = set()
        dfs(0)      # since 题目说了graph是一个tree, 所以不会重复visit同一个点
        return self.cnt
