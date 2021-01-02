"""
1042. Flower Planting With No Adjacent

You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. 
In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. 
The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

Example 1:
Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:
Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:
Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
"""


"""
start from garden 1, do dfs, assign along the way the correponding color,
assign which color? the color that is not in the exclude_color list
"""
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        def dfs(curr_node):
            for next_node in graph[curr_node]:
                if res[next_node] == -1:
                    exclude_color = []
                    for neigb_node in graph[next_node]:
                        exclude_color.append(res[neigb_node])
                        
                    for next_color in [1, 2, 3, 4]:
                        if next_color not in exclude_color:
                            res[next_node] = next_color
                    dfs(next_node)
        
        
        graph = defaultdict(list)
        for u, v in paths:
            graph[u - 1].append(v - 1)  # 实在受不了不从0开始
            graph[v - 1].append(u - 1)
            
        res = [-1 for _ in range(n)]
        for node in range(n):       # 注意为了防止有的node没有跟其他的点连一起，需要遍历所有的node
            if res[node] == -1:
                res[node] = 1
                dfs(node)
        return res
