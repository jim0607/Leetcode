350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


"""
Approach 1: hashmap to store the frequency of each num.
O(m+n), O(m+n)
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = collections.defaultdict(int)
        freq2 = collections.defaultdict(int)
        for num in nums1:
            freq1[num] += 1
        for num in nums2:
            freq2[num] += 1
            
        res = []
        for num in freq1:
            if num in freq2:
                res += [num] * min(freq1[num], freq2[num])
        return res
        
        
"""
Facebook follow ups:
follow up 1: What if the given array is already sorted? How would you optimize your algorithm?
"""
"""
Approach 2 - O(m+n), O(1)
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        lens1, lens2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < lens1 and j < lens2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1      # 本题不用去重
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
        
        
        
"""
Follow up 2: What if nums1's size is small compared to nums2's size? Which algorithm is better?
"""
"""
1. If lens1 is relatively small and nums2 is not sorted, we can choose Approach 1 and use a hashmap for nums1, which takes small space;
2. If lens1 is relatively small and nums2 is sorted, we can choose Approach 2.
2. if lens1 is very small, say lens1 == 2, and nums2 is sorted, then we can use binary search,
in binary search, target is the num in nums1, we try to find if it exist in nums2.
Let's say nums1 is K size. Then binary search will take O(K log N).
If K this is small enough, O(KlogN) < O(M+N). Otherwise, we have to use the previous Approach 2 method.
"""

"""
Follow up 3: What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
"""
Step 1: Choose Appoach 1, use a Map to store nums1.
Step 2: Divide nums2 into n chunks of 1/n size.
Step 3: Bring 1 chunk at a time of nums2 into memory and see if it intersects with our Map. 
        If the intersection we're generating gets too big to fit in memory, we can save our partial solution to disk and continue with our algorithm.
        
Also, Map-Reduce is a good answer too.
"""

"""
Follow up 4: What if neither nums1 or nums2 can fully fit in memory?
"""
"""
Step 1: Use external sort to sort nums1
Step 2: Use external sort to sort nums2 (this step can theoretically be done in parallel to the above step)
Step 3: Use the 2-pointer approach (approach 2) above to generate our solution:
        - Divide nums1 into chunks that can fit in memory without consuming over ~10% of it
        - Divide nums2 into chunks that can fit in memory without consuming over ~10% of it
        - The resulting ~80% can be used for our generated intersection
        - Bring in 1 chunk of nums1 and 1 chunk of nums2 into memory together
        - If the intersection we're generating gets too big to fit in memory, we can save our partial solution to disk and continue with our algorithm
"""
"""
External sorting is a class of sorting algorithms that can handle massive amounts of data. 
External sorting is required when the data being sorted do not fit into the main memory of a computing device (usually RAM) 
and instead they must reside in the slower external memory, usually a hard disk drive. 
Thus, external sorting algorithms are external memory algorithms and thus applicable in the external memory model of computation.

External sorting algorithms generally fall into two types, 
distribution sorting, which resembles quicksort, 
and external merge sort, which resembles merge sort. 
In the sorting phase, chunks of data small enough to fit in main memory are read, sorted, and written out to a temporary file. 
In the merge phase, the sorted subfiles are combined into a single larger file.
"""
