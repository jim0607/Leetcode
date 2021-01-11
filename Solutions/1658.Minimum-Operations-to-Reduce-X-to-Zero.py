"""
1658. Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x. 
In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 
Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""


"""
这题是从两端找 the fewest number added to x. 
换个角度就是找 the longest subarry that sum up to sum(nums) - x.
由于nums are all positive, sliding window即可 - O(N)
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        sums = 0
        max_len = -1
        j = 0
        for i, num in enumerate(nums):
            while j < len(nums) and sums < target:
                sums += nums[j]
                j += 1

            if sums == target:
                max_len = max(max_len, j - i)
                
            sums -= num
            
        return len(nums) - max_len if max_len != -1 else -1

"""
Follow up: what if there are negative numbers in nums?
then sliding window won't work, we have to do backtrack, or memorization
or we can do bfs
"""

"""
backtrack结束条件: left_idx > right_idx (return False), or curr_x == 0 (return True)
constraint on next_candidates: can only come from left_end or right_end, and cannot exceed curr_x
arguments pass into backtrack function: left_idx, right_idx, curr_x, curr_opt
O(2^N)
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        def backtrack(left_idx, right_idx, curr_x, curr_opt):
            if curr_x == 0:
                self.min_opt = min(self.min_opt, curr_opt)
                return
            
            if left_idx > right_idx:
                return
            
            if nums[left_idx] <= curr_x:
                backtrack(left_idx + 1, right_idx, curr_x - nums[left_idx], curr_opt + 1)
            if nums[right_idx] <= curr_x:
                backtrack(left_idx, right_idx - 1, curr_x - nums[right_idx], curr_opt + 1)
                
        
        self.min_opt = sys.maxsize
        backtrack(0, len(nums) - 1, x, 0)
        return self.min_opt if self.min_opt != sys.maxsize else -1
        
        
"""
memorization - O(X*N^2)
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        def backtrack(left_idx, right_idx, curr_x):
            if curr_x == 0:
                return 0
            
            if left_idx > right_idx:
                return sys.maxsize
            
            if (left_idx, right_idx, curr_x) in memo:
                return memo[(left_idx, right_idx, curr_x)]
            
            res = sys.maxsize
            if nums[left_idx] <= curr_x:
                res = min(res, 1 + backtrack(left_idx + 1, right_idx, curr_x - nums[left_idx]))
            if nums[right_idx] <= curr_x:
                res = min(res, 1 + backtrack(left_idx, right_idx - 1, curr_x - nums[right_idx]))
                
            memo[(left_idx, right_idx, curr_x)] = res
            return res
                
        
        memo = defaultdict(int)     # (left_idx, right_idx, curr_x) --> from (left_idx, right_idx, curr_x), the min_opt to reduce curr_x to 0
        res = backtrack(0, len(nums) - 1, x)    # returns from (left_idx, right_idx, curr_x), the min_opt to reduce curr_x to 0
        return res if res != sys.maxsize else -1
