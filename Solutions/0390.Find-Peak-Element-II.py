"""
390 Find Peak Element II

There is an integer matrix which has the following features:
The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:
A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.
Example
Given a matrix:
[ [1 ,2 ,3 ,6 ,5], [16,41,23,22,6], [15,17,24,21,7], [14,18,19,20,10], [13,14,11,10,9] ]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])
Challenge
Solve it in O(n+m) time.
If you come up with an algorithm that you thought it is O(n log m) or O(m log n), can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?
Solution
"""


"""
Solution 1:
once the max col idx in the row is found, we can use one comparism to choose either drop the upper rows or the lower rows --> T(n/2)
say we drop the lower rows, now we use O(n/2) time to find maximum in the upper column, and then choose to drop wither left or right.
Time complexity: T(n) = T(n/2) + O(n), where O(n) is to find the max col idx in a row,
using Master's Theorem: a = 1, b = 2, d = 1, d > logb(a), O(n^d) = O(n)
"""

class Solution:
    def findPeakII(self, A):
        upper, down = 1, len(A) - 2
        left, right = 1, len(A[0]) - 2

        while upper < down and left < right:
            height = down - upper + 1
            width = right - left + 1

            # if the width is larger, then we drop left part of right part
            # how do we decide to drop the left part of the right part?
            # compare the left_max, central_max and right_max
            # 为什么不能比较相邻的呢？因为可能回绕回来
            if width > height:  # Vertical split
                mid_j = left + (right - left) // 2

                # step 1: find the left_max, right_max and central_max
                left_max, central_max, right_max = 0, 0, 0
                max_i = -1
                for i in range(upper, down + 1):
                    if A[i][mid_j] > central_max:
                        max_i, max_j = i, mid_j
                        central_max = A[max_i][mid_j]
                    left_max = max(left_max, A[i][mid_j - 1])
                    right_max = max(right_max, A[i][mid_j + 1])

                # step 2: 二分
                if left_max > central_max and left_max > right_max:
                    right = mid_j
                elif right_max > central_max and right_max > left_max:
                    left = mid_j
                else:
                    return [max_i, max_j]

            else:  # Horizontal split.
                mid_i = upper + (down - upper) // 2

                upper_max, central_max, down_max = 0, 0, 0
                max_j = -1
                for j in range(left, right + 1):
                    if A[mid_i][j] > central_max:
                        max_i, max_j = mid_i, j
                        central_max = A[mid_i][j]
                    upper_max = max(upper_max, A[mid_i - 1][j])
                    down_max = max(down_max, A[mid_i + 1][j])

                if upper_max > central_max and upper_max > down_max:
                    down = mid_i
                elif down_max > central_max and down_max > upper_max:
                    upper = mid_i
                else:
                    return [max_i, max_j]

        return [-1, -1]  # Not found.


if __name__ == "__main__":
    test_matrix_1 = [[1, 2, 3, 6, 5],
                     [16, 41, 23, 22, 6],
                     [15, 17, 24, 21, 7],
                     [14, 18, 19, 20, 10],
                     [13, 14, 11, 10, 9]]

    test_matrix_2 = [[1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1],
                     [2, 17, 13, 6, 5, 17, 2],
                     [1, 15, 8, 10, 8, 15, 1],
                     [2, 14, 12, 11, 12, 14, 2],
                     [1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1]]

    solution_obj = Solution()
    peak_pos_1 = solution_obj.findPeakII(test_matrix_1)
    peak_pos_2 = solution_obj.findPeakII(test_matrix_2)
    print(peak_pos_1)
    print(peak_pos_2)





"""
Solution 2:
Time complexity: O(nlogn), because in every binary search, we need O(n) is to find the max col idx in a row
"""

class Solution:
    def findPeakII(self, grid):
        """
        :param grid:
        :return: the peak position in A
        """
        if not grid or not grid[0]:
            return [-1, -1]
        m, n = len(grid), len(grid[0])

        start, end = 1, m - 1
        while start + 1 < end:
            mid_row = start + (end - start) // 2
            max_col = self.findMax(grid, mid_row)
            if grid[mid_row][max_col] > grid[mid_row + 1][max_col] and grid[mid_row][max_col] > grid[mid_row - 1][max_col]:
                return [mid_row, max_col]
            elif grid[mid_row - 1][max_col] < grid[mid_row][max_col] <= grid[mid_row + 1][max_col]:
                start = mid_row
            else:
                end = mid_row

        return [start, max_col] if grid[start][max_col] > grid[end][max_col] else [end, max_col]

    @staticmethod
    def findMax(matrix, row):
        """
        :param matrix:
        :param row:
        :return: the col idx where matrix[row][col] is the largest in matrix[row]
        findMax()里面不能用binary search。因为我们要找row里面的**最大值**，而不是仅仅找到一个极大值而已，
        因为我们整个算法的目的是要保证每次都是往高爬的，如果选某一行的极大值的话，可能下一次又绕回到这一行了，
        具体可以参考九章算法强化班二分法55min.
        """
        col = 0
        for i in range(1, len(matrix[0]) - 1):
            if matrix[row][i] > matrix[row][col]:
                col = i

        return col


if __name__ == "__main__":
    test_matrix_1 = [[1, 2, 3, 6, 5],
                     [16, 41, 23, 22, 6],
                     [15, 17, 24, 21, 7],
                     [14, 18, 19, 20, 10],
                     [13, 14, 11, 10, 9]]

    test_matrix_2 = [[1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1],
                     [2, 17, 13, 6, 5, 17, 2],
                     [1, 15, 8, 10, 8, 15, 1],
                     [2, 14, 12, 11, 12, 14, 2],
                     [1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1]]

    solution_obj = Solution()
    peak_pos_1 = solution_obj.findPeakII(test_matrix_1)
    peak_pos_2 = solution_obj.findPeakII(test_matrix_2)
    print(peak_pos_1)
    print(peak_pos_2)


"""
下面把wrong answer也写一下
错误答案就错在run test_matrix_2的时候，findMax首先找打的不是15, 二分法找到的极大值10, 然后往11那一行走，
然后在11那一行继续用二分法找极大值14, 然后往15那一行走, 然后在15那一行继续二分法找极大值发现又找回10了，出不了循环。
而我们的正确答案用的是找最大值而不是极大值，这样就保证了每一次都是往高处走，所以不会出现又回到原来那一行的情况。
"""


class SolutionWrong:
    def findPeakII(self, grid):
        """
        :param grid:
        :return: the peak position in A
        """
        if not grid or not grid[0]:
            return [-1, -1]
        m, n = len(grid), len(grid[0])

        start, end = 1, m - 1
        while start + 1 < end:
            mid_row = start + (end - start) // 2
            max_col = self.findMax_usingBinarySearch(grid, mid_row)
            if grid[mid_row][max_col] > grid[mid_row + 1][max_col] and grid[mid_row][max_col] > grid[mid_row - 1][max_col]:
                return [mid_row, max_col]
            elif grid[mid_row - 1][max_col] < grid[mid_row][max_col] <= grid[mid_row + 1][max_col]:
                start = mid_row
            else:
                end = mid_row

        return [start, max_col] if grid[start][max_col] > grid[end][max_col] else [end, max_col]

    @staticmethod
    def findMax_usingBinarySearch(matrix, row):
        """
        :param matrix:
        :param row:
        :return:
        这里是一个错误的答案，用findMax_usingBinarySearch找极大值
        """
        start, end = 1, len(matrix[0]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[row][mid] > matrix[row][mid - 1] and matrix[row][mid] > matrix[row][mid + 1]:
                return mid
            elif matrix[row][mid - 1] < matrix[row][mid] <= matrix[row][mid + 1]:
                start = mid
            else:
                end = mid

        return start if matrix[row][start] > matrix[row][start] else end


if __name__ == "__main__":
    test_matrix_1 = [[1, 2, 3, 6, 5],
                     [16, 41, 23, 22, 6],
                     [15, 17, 24, 21, 7],
                     [14, 18, 19, 20, 10],
                     [13, 14, 11, 10, 9]]

    test_matrix_2 = [[1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1],
                     [2, 17, 13, 6, 5, 17, 2],
                     [1, 15, 8, 10, 8, 15, 1],
                     [2, 14, 12, 11, 12, 14, 2],
                     [1, 2, 1, 2, 1, 2, 1],
                     [1, 2, 1, 2, 1, 2, 1]]

    solution_obj_wrong = SolutionWrong()
    peak_pos_1_wrong = solution_obj_wrong.findPeakII(test_matrix_1)
    peak_pos_2_wrong = solution_obj_wrong.findPeakII(test_matrix_2)
    print(peak_pos_1_wrong)
    print(peak_pos_2_wrong)
