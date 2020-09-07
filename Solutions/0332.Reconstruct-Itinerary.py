"""
332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order. 
"""



"""
Recurssive backtracking.  Worst case: O(E^d), where E is # of edges, d is is the maximum number of flights from an airport.
"""  
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtrack(curr_node, curr_path):
            if len(cnt) == 0:   # when all tickets are used and there is not tickets remaining
                res.append(curr_path.copy())
                return 
            for next_node in graph[curr_node]:
                if (curr_node, next_node) not in cnt:
                    continue
                cnt[(curr_node, next_node)] -= 1
                if cnt[(curr_node, next_node)] == 0:  # 注意要delete掉if the ticket all (curr_node, next_node) have been used
                    del cnt[(curr_node, next_node)]
                curr_path.append(next_node)
                backtrack(next_node, curr_path)
                curr_path.pop()
                cnt[(curr_node, next_node)] += 1
            
            
        graph = collections.defaultdict(list)
        cnt = collections.defaultdict(int)   # store how many tickets are there (u --> v), 
                           # normally we use viisted set, but there are duplicated tickets in input
        for u, v in tickets:
            graph[u].append(v)
            cnt[(u, v)] += 1
            
        for lst in graph.values():  
            lst.sort()      # you should return the itinerary that has the smallest lexical order
            
        res = []
        visited = set()
        backtrack("JFK", ["JFK"])
        return res[0]
    
  
  
"""
Solution 2: 因为只需要输出一种包含所有边的路径，所以可以用另一种图的解法 Eulerian Path - every edge is visited exactly once. 
Eulerian path 使用的算法叫做 Hierholzer algorithm. Hierholzer algorithm 不做backtrack, 所以每一条边只访问一次，所以时间复杂度是O(E), where E is the # of edges.
"""  

Hierholzer algorithm 模板：

path = []
dfs(source):
    while u 存在未被访问的边 e[u, v]:
        mark 边e[u, v] 为访问过        # 保证每条边being visited exactly once.
        dfs(v)
        
    path.pushleft(u)


    
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # step 1: build a graph
        graph = collections.defaultdict(list)
        for dep, des in tickets:
            graph[dep].append(des)
            
        # step 2: sort the des in the graph reversely
        for dep in graph.keys():
            graph[dep].sort(reverse = True)
            
        # do a dfs using Hieholzer algorithm, not backtracking algorithm
        self.res = []
        source = "JFK"
        self.dfs(graph, source)
        
        return self.res[::-1]
    
    def dfs(self, graph, source):
        while graph[source]:
            nextSource = graph[source].pop()  # pop出来不再append进去就相当于mark这条边为访问过了
            self.dfs(graph, nextSource)     # 这里不做backtrack, 所以每一条边只访问一次，所以时间复杂度是O(E), where E is the # of edges.
            
        self.res.append(source)   # 想想append的顺序，应该是谁先出while循环先append谁，len(graph[v])=0最先出while循环，所以先append v, 也就是最先append终点机场
    
    
    
"""
iterative way for solution 2 
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)       
        for dep, des in tickets:      # the key of graph is departure airport, while the value is a list of destination
            graph[dep].append(des)
            
        for dep in graph.keys():
            graph[dep].sort(reverse = True)     # sort reversly, so that when we pop, we pop the smallest one
            
        stack = ["JFK"]
        res = []
        while stack:
            airport = stack[-1]
            
            # Check if elem in graph as there may be a case when there is no out edge from an airport 
            # In that case it won't be present as a key in graph.  If present, then append it's smallest to the stack
            if airport in graph and len(graph[airport]) > 0:
                stack.append(graph[airport].pop())
                
            # If there is no further children to traverse then add that airport to res
            # This airport should be the last to go since we can't anywhere from this
            # That's why we return the reverse of the result
            else:
                res.append(stack.pop())
                
        return res[::-1]
