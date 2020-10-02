"""
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


"""
这一题与659. Split Array into Consecutive Subsequences解法很类似，用以一个hashmap记录frequency.
由于必须固定长度为k, 所以我们每次都去连k个就可以了
"""
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        
        freq = collections.Counter(nums)

        for num in nums:
            if freq[num] == 0: continue

            for i in range(k):
                if freq[num + i] == 0:
                    return False
                freq[num + i] -= 1
            
        return True
