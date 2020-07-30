164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

"""
solution 1: sort the list and then compare adjacent num
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i] - nums[i-1])
        return max_diff
        
        
        
"""
遇到这类问题肯定先想到的是要给数组排序，但是题目要求是要线性的时间和空间，那么只能用桶排序Bucket Sort 。
If we set the bucket size clever(relatively small), 
we can ensure that the max gap cannot be in same bucket.
Largest gap can not be smaller than (max-min)/lens + 1, so if we make the buckets smaller than this number, 
any gaps within the same bucket is not the amount we are looking for, 
so we are safe to look only for the inter-bucket gaps.
首先要确定每个桶的容量size，即为 (max-min)/lens + 1，
然后再确定桶的个数，即为 (max-min)/size + 1
Bucket sort的本质是让idx含信息，把信息压缩到idx里，变相用空间换时间了。
In order to use bucket sort:
step 1: 确定把什么放进bucket里做idx, 什么做idx对应的val, 这一题是把num-min当做idx来放入bucket中, idx对应的val是a list of num having distance less than size;
step 2: 确定bucket size, 这一题是 (max-min)/lens + 1 as our bucket size;
step 3: O(N) 遍历, 这样一来similar distance的ch就天然的放在同一个bucket了, 就内部比较了，只需要比较inter-bucket.
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        
        mx = max(nums)
        mn = min(nums)
        lens = len(nums)
        size = (mx - mn) // lens + 1
        buckets_number = (mx - mn) // size + 1       # how many buckets are there
        # buckets = [[] for _ in range(buckets_number)]  # 可要可不要，主要是存每个bucket里的最大值和最小值
        buckets_max = [float("-inf") for _ in range(buckets_number)]      # keep track of max_num in each bucket
        buckets_min = [float("inf") for _ in range(buckets_number)]
        for num in nums:   
            idx = (num - mn) // size
            # buckets[idx].append(num)  # put nums into the bucket
            buckets_max[idx] = max(buckets_max[idx], num)   # update the max and min number in the bucket
            buckets_min[idx] = min(buckets_min[idx], num)

        # next, check the inter-bucket for the max_diff
        max_diff = 0
        prev_max = float("-inf")
        for i in range(len(buckets_max)):
            if buckets_max[i] == float("-inf") and buckets_min[i] == float("inf"):    # empty bucket
                continue
            if prev_max == float("-inf"):
                prev_max = buckets_max[i]
                continue
            max_diff = max(max_diff, buckets_min[i] - prev_max)
            prev_max = buckets_max[i]
        return max_diff
