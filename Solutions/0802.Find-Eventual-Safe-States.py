802. Find Eventual Safe States

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].



"""
所谓safe的意思，就是再没有向外的边，即没有出度，像上面例子中的结点5和6就是出度为0，因为graph[5]和graph[6]均为空。
那么我们分析题目中的例子，除了没有出度的结点5和6之外，结点2和4也是安全状态结点，为啥呢，我们发现结点2和4都只能到达结点5，而结点5本身就是安全状态点，
所以2和4也就是安全状态点了，所以我们可以得出的结论是，若某结点唯一能到达的结点是安全状态结点的话，那么该结点也同样是安全状态结点。
那么我们就可以从没有出度的安全状态往回推，比如结点5，往回推可以到达结点4和2，先看结点4，此时我们先回推到结点4，那么此时结点4出度为0，
则标记结点4也为安全状态结点，同理，回推到结点2，此时结点2虽然入度仍为2，但是出度为0了，标记结点2也为安全状态结点。
所以这里其实就是topological sort for out_degree!
"""
class Solution:
    def eventualSafeNodes(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for i, edge in enumerate(edges):
            for node in edge:       # 注意这里append顺序，我们需要反着箭头走
                graph[node].append(i)
            
        out_degrees = collections.defaultdict(int)
        for i, edge in enumerate(edges):
            out_degrees[i] += len(edge)
            
        q = collections.deque()
        for node, out_deg in out_degrees.items():
            if out_deg == 0:
                q.append(node)
                
        res = []
        while len(q) > 0:
            curr_node = q.popleft()
            res.append(curr_node)
            for next_node in graph[curr_node]:
                out_degrees[next_node] -= 1
                if out_degrees[next_node] == 0:
                    q.append(next_node)
                    
        return sorted(res)
