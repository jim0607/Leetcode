"""
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
"""



"""
dp[i]=dictionary{key: last num of the fib; val: the lens of the fib ended with ith}
dp[j][nums[i]]=d[i][nums[j]-nums[i]]+1
"""
class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens <= 2:
            return lens
            
        dp = [collections.defaultdict(lambda: 1) for _ in range(lens)]
            
        maxLens = 2
        for j in range(1, lens):
            for i in range(j):
                dp[j][nums[i]] = dp[i][nums[j] - nums[i]] + 1
                
            for val in dp[j].values():
                maxLens = max(maxLens, val)
                
        return maxLens if maxLens > 2 else 0
 
 
 
"""想法很简单，就是每次从A中找前两个数，然后查看后续符合斐波那契的数在A中有没有。复杂度O(n^2 * logn) 空间复杂度O(1)"""
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        lens = len(A)
        maxCnt = 2
        for i in range(lens-1):
            for j in range(i+1, lens):
                sums = A[i]+A[j]
                cnt = 2
                tempI, tempJ = A[i], A[j]
                temp = j
                while self.binarySearch(A[temp:], sums) >= 0:   # 由于数组是严格递增的，所以这里可以用二分法
                    cnt += 1
                    tempI, tempJ, temp = tempJ, sums, self.binarySearch(A[temp:], sums)
                    sums = tempI + tempJ
                maxCnt = max(maxCnt, cnt)
        return 0 if maxCnt < 3 else maxCnt
        
    def binarySearch(self, A: List[int], target: int) -> int:
        left, right = 0, len(A)-1
        while left <= right:
            mid = left+(right-left)//2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
