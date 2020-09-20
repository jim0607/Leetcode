"""
302. Smallest Rectangle Enclosing Black Pixels

An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6
"""



"""
solution 1: simple dfs visit every balck pixel, and update the max_i, max_j, min_i, min_j during dfs. - O(mn)
"""
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        self.min_i, self.max_i = x, x
        self.min_j, self.max_j = y, y
        self._dfs(image, x, y)
        return (self.max_i - self.min_i + 1) * (self.max_j - self.min_j + 1)
    
    def _dfs(self, image, curr_i, curr_j):
        image[curr_i][curr_j] = "0"
        self.min_i = min(self.min_i, curr_i)
        self.min_j = min(self.min_j, curr_j)
        self.max_i = max(self.max_i, curr_i)
        self.max_j = max(self.max_j, curr_j)
        for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_i, next_j = curr_i + delta_i, curr_j + delta_j
            if 0 <= next_i < len(image) and 0 <= next_j < len(image[0]):
                if image[next_i][next_j] == "1":
                    self._dfs(image, next_i, next_j)                
                
                
                
"""
solution 2: 我们需要知道Black出现的最大的i和最小的i, 所以我们可以求出每一行的第一个Black和最后一个Black的idx, 
就是我们想求的最大的i和最小的i了，转换成了OOXX问题了. 这题可以用binary search的原因是有且只有一个Black的岛屿，
所以每一行都是一个先上后下的mountain array. - O(mlogn+nlogm)
特别注意我们在某一行扫binary search的时候范围是start, end = 0, self.min_j 
"""
"""
https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/discuss/75127/C%2B%2BJavaPython-Binary-Search-solution-with-explanation
In a word, the algorithm is doing following:
top = search row [0...x], find first row contain 1,
bottom = search row[x+1, row], find first row contian all 0
left = search col[0...y], find first col contain 1,
right = search col[y+1, col], find first col contain all 0
"""
class Solution:
    BLACK = "1"
    WHITE = "0"
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        self.max_i, self.min_i = x, x
        self.max_j, self.min_j = y, y
        
        for row in range(len(image)):
            self._binary_search_in_row(image, row)
        for col in range(len(image[0])):
            self._binary_search_in_col(image, col)
            
        # 特别注意这里要扫两次binary search, why?
        # 因为比如说扫到某一行的时候有的1是拐着弯从下面过来的，所以binary search时可能是[01100000011111]
        # 第一次binary search的时候self.min_j在位置9, 从位置9开始binary search会错过位置1上的1
        # 为了避免错过，我们第一遍先把min_j更新到位置2 (在某一行一定会更新到位置2, 因为图是联通的), 
        # 这样第二遍从位置2开始binary search就不会错过了位置1上的1了
        for row in range(len(image)):
            self._binary_search_in_row(image, row)
        for col in range(len(image[0])):
            self._binary_search_in_col(image, col)
            
        print(self.max_i, self.min_i)
        print(self.max_j, self.min_j)

        return (self.max_i - self.min_i + 1) * (self.max_j - self.min_j + 1)
    
    
    def _binary_search_in_row(self, image, row):
        # step 1: search for first_j
        start, end = 0, self.min_j       
        while start + 1 < end:      # binary search for the first 1 in arr [000000011111]
            mid = start + (end - start) // 2
            if image[row][mid] == self.BLACK:
                end = mid
            else:
                start = mid
        self.min_j = start if image[row][start] == self.BLACK else end
        
        # step 2: search for the last_j
        start, end = self.max_j, len(image[0]) - 1
        while start + 1 < end:      # binary search for the last 1 in arr [111110000000]
            mid = start + (end - start) // 2
            if image[row][mid] == self.BLACK:
                start = mid
            else:
                end = mid
        self.max_j = end if image[row][end] == self.BLACK else start
        
        
    def _binary_search_in_col(self, image, col):
        # step 1: search for first_i
        start, end = 0, self.min_i       
        while start + 1 < end:      # binary search for the first 1 in arr [000000011111]
            mid = start + (end - start) // 2
            if image[mid][col] == self.BLACK:
                end = mid
            else:
                start = mid
        self.min_i = start if image[start][col] == self.BLACK else end
        
        # step 2: search for the last_i
        start, end = self.max_i, len(image) - 1
        while start + 1 < end:      # binary search for the last 1 in arr [111110000000]
            mid = start + (end - start) // 2
            if image[mid][col] == self.BLACK:
                start = mid
            else:
                end = mid
        self.max_i = end if image[end][col] == self.BLACK else start
