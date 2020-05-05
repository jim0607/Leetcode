Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
        
        
        
"""实际上这个问题和之前问题Leetcode 300：最长上升子序列（最详细的解法！！！）非常类似，我们可以使用动态规划来做。我们知道对于等差数列有三种情况
dp=a 2D array
dp[i]=以i结尾的等差数列
dp[i][j]=以i结尾的等差数列且以j为公差的长度"""
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        lens = len(A)
        # 构建一个二维字典，collections.defaultdict(int)的默认值是0，可以通过collections.defaultdict(lambda: 1)把默认值改成1
        dp = [collections.defaultdict(lambda: 1) for _ in range(lens)]   # 在每个位置上，以字典结构保存该位置元素与前面每个位置上元素的差值,这个差值就是字典的key，对应该差值的数列长度是字典的value。
        res = 1
        for i in range(lens-1):
            for j in range(i+1, lens):
                diff = A[j]-A[i]
                # 这里的二维字典dp[j][diff]表示以j作为键值1，键值1对应的value是一个嵌套的dict，这个嵌套的dict里面可能有很多key-val pair，这个嵌套的dict的key是diff，value是该j下标对应该差值diff的数列长度
                dp[j][diff] = dp[i][diff]+1
                res = max(dp[j][diff], res)
        return res
"""O(N^2), O(N^2)"""

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:        
        lens = len(A)
        if lens <= 2:
            return lens
        
        dp = [collections.defaultdict(lambda: 1) for _ in range(lens)]  # why this is incorrect: dp = [collections.defaultdict(lambda: 1)] * lens
        
        maxLens = 1
        for j in range(1, lens):
            for i in range(j):
                diff = A[j] - A[i]
                dp[j][diff] = max(dp[j][diff], dp[i][diff] + 1)   # 为什么这里不报错呢？如果dp[i][diff]不存在怎么办, 用defaultdict就不用担心了！
                    
            for val in dp[j].values():
                maxLens = max(maxLens, val)
                    
        return maxLens

"""暴力法：O(N^3), O(N)
思路：
等差数列 其实在 给定前2个数之后，就能求出整个等差数列(虽说是无限长的)。
既然如此，那就不断地 固定等差数列的 前2个数，去判断下1个理论值 是否在数组A[]中 且 在数组A[]中的下标 要 > 等差数列的最后1个实际值的下标(即理论值的 上1个值的下标)。
具体实现：
构建1个HashMap：数组A[]中的值作为key，值所对应的下标 去组成1个ArrayList 作为value。"""
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        lens = len(A)
        dictA = {}
        for i, num in enumerate(A):
            if num in dictA.keys():
                dictA[num].append(i)      # 注意这里可能会有不同的下标对应num值
            else:
                dictA[num] = [i]
        zeroCnt, res = 1, 2
        for i in range(lens-1):
            for j in range(i+1, lens):
                diff = A[j]-A[i]
                if diff == 0:
                    zeroCnt = max(len(dictA[A[i]]), zeroCnt)    # 数组中可能会有多个重复的数，如[2,2,2,3,4,4,4,4]，所以这里用max
                else:
                    temp = j
                    cnt = 2
                    for k in range(j+1, lens):
                        if A[k]-A[temp] == diff:
                            cnt += 1
                            temp = k
                    res = max(res, cnt)
        return max(res, zeroCnt)
