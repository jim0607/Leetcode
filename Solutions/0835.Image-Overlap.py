835. Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.


"""
step 1: create a list of positions for A and B where 1s are located
step 2: use a counter to remember the cnt of (delta_i, delta_j)
O(N^4), O(N^2)
"""
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        lens = len(A)
        A_pos = [(i, j) for i in range(lens) for j in range(lens) if A[i][j] == 1]
        B_pos = [(i, j) for i in range(lens) for j in range(lens) if B[i][j] == 1]
        
        res = 0
        counter = collections.defaultdict(int)
        for A_i, A_j in A_pos:          # O(N^2)
            for B_i, B_j in B_pos:      # O(N^2)
                delta_i, delta_j = A_i - B_i, A_j - B_j
                counter[(delta_i, delta_j)] += 1
                res = max(res, counter[(delta_i, delta_j)])
                
        return res
