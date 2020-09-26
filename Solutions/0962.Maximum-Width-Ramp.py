"""
962. Maximum Width Ramp

Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
"""



"""
solution 1: sort the list - O(nlogn)
step 1: sort the list based on values.
step 2: now as we traverse over the sorted list, the curr_num is surely larger than any previous number,
so if we keep a min_idx to record the minimum idx we have seen, then we can update the max_lens.
"""
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        nums = [(num, idx) for idx, num in enumerate(A)]
        nums.sort(key = lambda x: x[0])
        
        # next is similar with 121. best time to buy and sell stock
        min_idx = float("inf")      # keep the minimum idx we have seen
        max_lens = float("-inf")    
        for num, idx in nums:
            max_lens = max(max_lens, idx - min_idx)
            min_idx = min(min_idx, idx)
        return max_lens if max_lens > 0 else 0
        
        
     
"""
solution 2: This is "Last Greater Element" problem. monostack - O(n)
Step 1: put valid candidates into stack: loop from left to the right, if there's a value greater than a value to the left, 
it doesn't make sense to use it. So we create a stack in descending order. 
这里跟sort很像，但是我们是把unordered的num直接不要，而不是把它放到该有的地方。
Step 2: now go backwards on A, and compare the values to the stack to see the max_lens we can have.
"""
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # step 1: put valid candidates into stack to maintain a momo decreasing st
        st = []
        for i, num in enumerate(A):
            if len(st) == 0 or num < st[-1][0]:
                st.append((num, i))
        
        # step 2: go backwards on A, compare values and update res as we go
        max_lens = 0
        for i in range(len(A) - 1, -1, -1):
            while len(st) > 0 and A[i] >= st[-1][0]:
                max_lens = max(max_lens, i - st.pop()[1])    # 这里可以pop是因为st[-1]用过一次就不会再用了，因为i在不断减小，
        return max_lens                                      # 如果下次再用，得到的lens只可能比现在的lens更小
