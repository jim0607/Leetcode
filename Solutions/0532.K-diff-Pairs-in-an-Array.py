532. K-diff Pairs in an Array

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

"""注意不能先去重，因为可能有[3,3], k=0的情况
同向双指针法，如果碰到符合条件的，把j往前挪到不重复的元素去。
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < 2:
            return 0
        if k < 0:
            return 0
        
        nums.sort()
        
        i, j = 0, 0
        cnt = 0
        while i < len(nums) and j < len(nums):
            if nums[j] - nums[i] > k:
                i += 1
            elif nums[j] - nums[i] < k or i == j:
                j += 1
            elif nums[j] - nums[i] == k:
                i += 1
                j += 1
                cnt += 1
                # 去重：如果碰到符合条件的，把i和j往前挪到不重复的元素去。
                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
                while j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1
                    
        return cnt
        
        
"""hash map: use a hash map to store the frequency of num in nums
and use a set to store unique pairs
O(N), O(N)
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return 0
        
        dict_fq = {}
        for num in nums:
            if num not in dict_fq:
                dict_fq[num] = 1
            else:
                dict_fq[num] += 1
        
        lens = len(nums)
        pairs = set()           # set 会自动过滤掉重复的paris
        for num in dict_fq.keys():
            if k == 0:
                if dict_fq[num] > 1:
                    pairs.add((num, num))
            else:
                num_2 = num + k
                if num_2 in dict_fq.keys():
                    pairs.add((num, num_2))
                    
        return len(pairs)
