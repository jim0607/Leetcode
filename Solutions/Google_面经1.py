"""
第二题给一个int array， select elements使得sum最大，条件是选择的数字之间abs gap不能等于1，
比如[1，2，2，3，3, 100]最后的选择[1，3，3] return 7，不能选2是因为它和1或者3的abs diff是1。

solution 1: Backtrack - O(2^N) in worst case.
backtrack结束条件: curr_idx = len(nums) - 1
constraints on next_candidate: next_idx in range(curr_idx + 1, len(nums)), nums[next_idx] != last_num + 1
arguments pass into backtrack function: curr_idx, last_num, curr_sum
"""
import sys

class SelectNumber:
    def select_number(self, nums) -> int:
        def backtrack(curr_idx, last_num, curr_sum):
            if curr_idx == len(nums) - 1:
                self.max_sum = max(self.max_sum, curr_sum)
                return

            for next_idx in range(curr_idx + 1, len(nums)):
                if nums[next_idx] == last_num + 1:
                    continue
                backtrack(next_idx, nums[next_idx], curr_sum + nums[next_idx])


        nums.sort()
        self.max_sum = -sys.maxsize
        backtrack(-1, sys.maxsize, 0)
        return self.max_sum



"""
solution 2: recursion + memorization - O(N^2)
"""
class SelectNumber:
    def select_number(self, nums) -> int:
        def backtrack(curr_idx, last_num):
            if curr_idx == len(nums) - 1:
                return 0

            if (curr_idx, last_num) in memo:
                return memo[(curr_idx, last_num)]

            res = -sys.maxsize
            for next_idx in range(curr_idx + 1, len(nums)):
                if nums[next_idx] == last_num + 1:
                    continue
                res = max(res, nums[next_idx] + backtrack(next_idx, nums[next_idx]))

            memo[(curr_idx, last_num)] = res
            return res


        nums.sort()
        memo = defaultdict(int)     # (curr_idx, curr_last_num) --> from (curr_idx, curr_last_num), what is the max_sum we can get
        return backtrack(-1, sys.maxsize)  # returns from (curr_idx, curr_last_num), what is the max_sum we can get
