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
