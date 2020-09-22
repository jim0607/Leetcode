"""
220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


"""
Solution 3: buckets method  O(N)
bucket sort利用的是分块的思想
The main idea is splitting elements in nums into different buckets in terms of the value of t (for each element, divide by (t+1) for integer division). 
保持bucket的大小为t这样只要有两个数被分配到了同一个bucket, 那么就可以return True了
If the result is True, which means one of the following 3 cases hold:
1. Two elements in the same bucket
2. One in the previous bucket
3. One in the next bucket
If the case 2 or 3 holds, you need to check if their difference <= t.
And there can be at most k buckets at any time. If i (counter in code) >= k, delete the (i-k)-th one.
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        
        bucket = collections.defaultdict(int) # key is bucket_id where nums[i] should be put in, val is nums[i]
        for i in range(len(nums)):     
            bucket_id = nums[i]//(t+1)  # 取除数在python里-4//3=-2, 所以不用像java solution那样还要考虑负数的情况, 除以t+1是为了防止t=0的情况
            if bucket_id in bucket: # meaning that there is already a number that is in there
                return True
            if bucket_id + 1 in bucket and abs(bucket[bucket_id+1] - nums[i]) <= t:
                return True
            if bucket_id - 1 in bucket and abs(bucket[bucket_id-1] - nums[i]) <= t:
                return True
            
            bucket[bucket_id] = nums[i]     # 把bucket_id加进去
            
            # 这一步是为了保证所有装在bucket dictionary里面的数的idx与下一个进来的i不会超过k的距离，如果有超过的就del出bucket dict
            if i >= k:
                bucket_id_to_delete = nums[i-k]//(t+1)    # 离i距离大于k的数字都用不到了，因为题目要求距离必须小于k
                del bucket[bucket_id_to_delete]     # 可以delete掉的前提是一个bucket_id里面只有一个数，因为如果存在两个数的话早就return True了
            
        return False   
        
"""
自己想了下例子还是明白了，任何数落在t+1的自己bucket 里他们的difference abs一定小于等于t 例如说t=3 bucket 1里的数就是 4,5,6,7 
你看里面任何一个数相减的abs都是小于等于3的。 然后再看邻居 bucket 0 里有的数在这个例子里是 0,1,2,3 
那么这里面其中有些数和bucket 1里的有些数相减的 abs会小于等于t 
同样的解释可以用于bucket2. bucket 3里的数为 12，13，14，15.这里的任何一个数和bucket1 里的任意数相减都不会小于等于 t (12-7=5). 
为什么+1 因为避免t=0. 
"""
    
    

""" 
Brute Force Solution
Brute force solution is use two loops and test both the conditions. The inner loop starts from i+1 to i+k. Because of that, we no longer need to test one of the conditions since that is taken care of automatically.
Time complexity : O(n * k).
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(0, len(nums)):
            for j in range(i+1, i+k+1):
                if j < len(nums):
                    if abs(nums[i]-nums[j]) <= t:
                        return True
        return False


"""
Solution 2: balanced BST: O(nlogk)
Binary Search Tree Solution.  In solution 1, for nums[i], we need to compare with every nums[j] that are within (i+1, i+k+1).
In fact we just need to compare nums[i] with the number that is just larger than it and the number that is just smaller than it.
How can we effeciently find the number that is just larger/smaller than it? Use a balanced BST.
Maintain a BST of previous k elements. This is the invariant for this problem!
When you get element x, we want to find an element y in the BST such that (y-x)<=t or (x-y)<=t
How do we find (y-x)<=t ? Solution: Find the smallest value in the BST greater than or equal to x i.e. ceiling of x. Then test that value for the above condition.If the smallest value greater than x doesnt meet the criterion, then no other value y greater than x will meet the condition. One may consider the smallest element y that is greater or equal to x as the successor of x in the BST, as in: "What is the next greater value of x?"
How do we find (x-y)<=t? Find the greatest element y in the BST which is smaller than or equal to x. Again if this y doesnt meet the condition, no other y in the BST will meet the condition. We consider the greatest element y that is smaller or equal to x as the predecessor of x in the BST, as in: "What is the previous smaller value of x?
Visualize or imagine this as x and its two closest neighbors.
After trying the above tests, if they fail, then put x in set
If the size of the set is larger than k, remove the oldest item - this maintains the invariant.
Time complexity : O(n * log (min(n,k))). Space complexity: O(min(n,k))

In Java, it is called TreeMap, but in Python, there is no such data structure to use.
We have to implement a balanced BST in Python. The implementation is below:
https://leetcode.com/problems/contains-duplicate-iii/discuss/174416/Python-balanced-BST-solution
"""

