766. Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].




"""
solution: 遍历整个matrix, 每次都与其右下角的数进行比较
"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                
        return True
        
        
Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
solution: Compare half of 1 row with half of the next/previous row.

What if the matrix is so large that you can only load up a partial row into the memory at once?
Solution: This is the general solution to this kind of question: 
If you are not allowed to operate upon the entire matrix, you hash the maximum allowable chunks of the matrix sequentially and operate upon them , 
assuming we are able to operate upon different discontiguous hashed chunks of our matrix without too much buffering.
So the solution for this questions is: Hash 2 rows (so only 1 element needs to be loaded at a time) by applysing hash function to the elements in the two rows,
and then compare to see if should return False.  But if there is hash collision, then this algorithm doesn't work.

Follow up3: follow up 3是在memory没限制的情况下设计高效的parallel算法

1-101 分给一台机器
100-201 分给另外一台机器
.
.
.
依次类推，要注意 boarder, boarder 需要有重叠，因为需要比较前后两行才能知道是不是要 return False
