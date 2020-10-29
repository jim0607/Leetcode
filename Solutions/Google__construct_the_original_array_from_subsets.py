"""
Given a list of subsets from an array A, construct the original array. The original array may contain duplicate elements.
[ 
1
2
3
1 2 
1 3
2 2
2 3
1 2 2
1 2 3
2 2 3
]

return original arr: [1, 2, 2, 3]
"""

"""
solution: topological sort. 如果len(q) > 1 就不是唯一解
graph[1] = [2, 3]
graph[2] = [2, 3]
grpah[3] = []

in_degrees[1] = 0
in_degrees[2] = 1
in_degrees[3] = 1 + 1 = 2
"""
