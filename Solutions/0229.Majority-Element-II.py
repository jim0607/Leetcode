"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 
Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
"""

"""
O(N), O(N)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnter = Counter(nums)
        
        res= []
        for num, cnt in cnter.items():
            if cnt > len(nums) // 3:
                res.append(num)
        return res

"""
O(N), O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # step 1: find the two most freq num in nums
        cnt1, cnt2 = 0, 0
        cand1, cand2 = sys.maxsize, sys.maxsize
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            else:
                if cnt1 == 0:
                    cand1 = num
                    cnt1 = 1
                elif cnt2 == 0:
                    cand2 = num
                    cnt2 = 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1
                    
        # step 2: check the if two most freq num larger n//3
        res = []
        if nums.count(cand1) > len(nums) // 3:
            res.append(cand1)
        if nums.count(cand2) > len(nums) // 3:
            res.append(cand2)
        return res
