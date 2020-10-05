"""
562. Longest Line of Consecutive One in Matrix

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""


"""
each time we meet a 1, we explore horizontally, vertically and diagonally.
Use set to store the nodes that were horizontally visited, vertically visited and diagonally visited. 
"""
class Solution:
    def longestLine(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        h_visited = set()   # store the nodes that were horizontally visited
        v_visited = set()
        d_visited = set()
        ad_visited = set()  # store the nodes that were anti-diagonally visited
        m, n = len(matrix), len(matrix[0])
        max_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if (i, j) not in h_visited:
                        p, q = i, j
                        while p < m and matrix[p][q] == 1:
                            h_visited.add((p, q))
                            p += 1
                        max_len = max(max_len, p - i)
                    
                    if (i, j) not in v_visited:
                        p, q = i, j
                        while q < n and matrix[p][q] == 1:
                            v_visited.add((p, q))
                            q += 1
                        max_len = max(max_len, q - j)
                    if (i, j) not in d_visited:
                        p, q = i, j
                        while p < m and q < n and matrix[p][q] == 1:
                            d_visited.add((p, q))
                            p += 1
                            q += 1
                        max_len = max(max_len, p - i)
                    if (i, j) not in ad_visited:
                        p, q = i, j
                        while p < m and q >= 0 and matrix[p][q] == 1:
                            ad_visited.add((p, q))
                            p += 1
                            q -= 1
                        max_len = max(max_len, p - i)
        return max_len
        
        
"""
也可以用四个dp数组来做 - O(MN)
"""
