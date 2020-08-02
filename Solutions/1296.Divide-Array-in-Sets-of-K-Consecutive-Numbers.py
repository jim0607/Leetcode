1296. Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.



"""
这一题与659. Split Array into Consecutive Subsequences解法很类似，需要的是两个hashmap
一个记录freq, 一个记录how many need, 只是我们update need的方式有一点变化，如果已经拼出了长度为k的substring,
那就不去update need[num+1]了
"""
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        
        freq = collections.Counter(nums)
        need = collections.defaultdict(int)

        curr_lens = 0       # curr_lens 记录当前拼出的长度
        for num in nums:
            if freq[num] == 0: continue
                
            if need[num] > 0:
                need[num] += 1
                curr_lens += 1
                if curr_lens < k:        # need num+1 only if lens is less than k
                    need[num + 1] += 1
                else:                    # if we found one k lens substring, reset cur_lens
                    curr_lens = 0
            
            elif need[num] == 0:
                for i in range(1, k):
                    if freq[num + i] == 0:
                        return False
                    freq[num + i] -= 1
                curr_lens = 0             # if we found one k lens substring, reset cur_lens
                
                # need[num + k] += 1      # need num+1 only if lens is less than k
            
            freq[num] -= 1
            
        return True
