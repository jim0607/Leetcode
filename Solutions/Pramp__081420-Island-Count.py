Island Count
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.

Example:

input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

output: 6 # since this is the number of islands in binaryMatrix.
          # See all 6 islands color-coded below.



def get_number_of_islands(binaryMatrix):
  m, n = len(binaryMatrix), len(binaryMatrix[0])
  cnt = 0   # number of islands
  for i in range(m):
    for j in range(n):
      if binaryMatrix[i][j] == 1:
        helper(binaryMatrix, i, j)
        cnt += 1
  return cnt

def helper(binaryMatrix, x, y):
  binaryMatrix[x][y] = 0
  m, n = len(binaryMatrix), len(binaryMatrix[0])
  # go to visit neighbors
  for delta_x, delta_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    next_x, next_y = x + delta_x, y + delta_y
    if 0 <= next_x < m and 0 <= next_y < n:
      if binaryMatrix[next_x][next_y] == 1:
        helper(binaryMatrix, next_x, next_y)
        
        
matrix = [ [0,    1,    0,    1,    0],
[0,    0,    1,    1,    1],
[1,    0,    0,    1,    0],
[0,    1,    1,    0,    0],
[1,    0,    1,    0,    1]]
print(get_number_of_islands(matrix))
print(matrix)




两点不好的地方需要改进：
1. should we ask yourself a question before implementing the code for dfs?
answer should be: we want to avoid visiting the same node again and again,
one way is to use a set to mark the visited nodes, the other way to modify the matrix in-place.

2. 一定要在代码结束之后主动run test case, 首先需要run test case orally. 然后写一个print()出来打印结果像上面那样！！

知识点：
For Python, when we pass variables into function, for immutable variables such as string, int and so on, we pass the variable itself and store them in a stack,
so the variables won't be changed outside the function.
But if the variable is for muttable variable such as matrix or arr, instead of passing the values and locations of the variable, 
we pass the reference of the variables (to save tons of space), so if we change the variables inside the function, it will also be changed outside the funciton.
This iis handled by Python implicitly.



