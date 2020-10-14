"""
1203. Sort Items by Groups Respecting Dependencies

There are n items each belonging to zero or one of m groups where group[i] is the group 
that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. 
The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing 
all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 
Constraints:

1 <= m <= n <= 3*10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m-1
0 <= beforeItems[i].length <= n-1
0 <= beforeItems[i][j] <= n-1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
"""


"""
step 1: put -1 into idependent groups;
step 2: build the item_graph and item_degrees, and group_graph and group_degrees;
step 3: topological sort for the two graphs we built;
step 4: get the res: 先宏观有序，再微观有序
"""
class Solution:
    def sortItems(self, n: int, m: int, groups: List[int], beforeItems: List[List[int]]) -> List[int]:
        # step 1: put -1 into idependent groups
        for item, group in enumerate(groups):
            if group == -1:
                groups[item] = m
                m += 1
        
        # step 2: build the graphs and in_degrees
        item_graph = defaultdict(list)      # items are nodes in the graph
        group_graph = defaultdict(list)     # groups are nodes in the graph
        item_indegrees = defaultdict(int)
        group_indegrees = defaultdict(int)
        for item in range(n):     # 注意topological sort的indegrees initialization很容易被遗忘
            item_indegrees[item] = 0
        for group in groups:        
            group_indegrees[group] = 0
        for item, befores in enumerate(beforeItems):
            group = groups[item]
            for before_item in befores:
                item_graph[before_item].append(item)
                item_indegrees[item] += 1
                before_group = groups[before_item]
                if before_group != group:
                    group_graph[before_group].append(group)
                    group_indegrees[group] += 1

        # step 3: topological sort for the two graphs we built
        ordered_items = self.topo_sort(item_graph, item_indegrees)
        ordered_groups = self.topo_sort(group_graph, group_indegrees)
        if len(ordered_items) == 0 or len(ordered_groups) == 0:     # 如果没有valid的拓扑排序
            return []
        
        # step 4: get the res: 先宏观有序，再微观有序
        res = []
        group_items = defaultdict(list)     # put the already ordered items into groups,
        for item in ordered_items:          # so that the items in each group are sorted
            group = groups[item]
            group_items[group].append(item)
        for group in ordered_groups:        # output the res in the order of each group - 宏观有序
            res += group_items[group]       # in each group_items[group], 都是微观有序的
        return res
    
    
    def topo_sort(self, graph, indegrees):
        q = deque()
        for node, indegree in indegrees.items():
            if indegree == 0:
                q.append(node)
        
        res = []
        while len(q) > 0:
            curr_node = q.popleft()
            res.append(curr_node)
            for next_node in graph[curr_node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    q.append(next_node)

        return res if len(res) == len(graph) else []    # 注意判断有没有valid的拓扑排序
