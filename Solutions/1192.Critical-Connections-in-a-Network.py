1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.


Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 
Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.


"""
solution 1: brutal force: 每次都是尝试去掉一条边，然后看去掉之后connected comonents的个数是不是还是只有一个 - O(E^2).
solution 2: Tarjan's algorithm. In Tarjan's algorithm we keep a list low[i].
low[i]: 表示节点i所见到过的除了目前的父节点parent之外的所有节点中步数最小的那一个。
eg: [[0,1],[1,2],[2,3],[3,0],[2,4]]. 节点2第一次被访问到的时候是作为节点1的next, 那时候节点2的low[2]没有被更新过，
所以我们继续访问节点2; 节点2第二次被访问到的时候是作为节点3的next, 那时候节点2的low[2]已经被更新过了，
说明2已经被访问过了，那就不继续访问了
We use dfs to scan all the node, at each node, we update the low[node]. 需要传入curr node and prev node
In the example [[0,1],[1,2],[2,0],[1,3]], we start from 0 and do dfs, then the two lists are:
low = [0, 0, 0, 3]
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        low = [-1 for _ in range(n)]
        
        def dfs(curr, prev, step):      # 需要传入curr node and prev node
            low[curr] = step
            
            for next in graph[curr]:
                if next == prev:
                    continue
                if low[next] == -1:       # if not visited
                    dfs(next, curr, step+1)
                    
                if low[next] > step:    # 说明next只能通过curr访问到，那就是critical bridge了 
                    res.append([curr, next])
                else:                   # 说明next不仅可以通过curr访问到，而且还可以通过别的渠道访问到
                    low[curr] = min(low[curr], low[next])

        res = []
        dfs(0, -1, 0)
        return res
