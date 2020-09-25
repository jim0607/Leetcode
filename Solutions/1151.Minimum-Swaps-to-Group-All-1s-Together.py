"""
1151. Minimum Swaps to Group All 1's Together

Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.


Example 1:

Input: [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
Example 3:

Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
"""




"""
window size is how many 1s are there in data, our goal to reaplace all 0s in the window to 1s,
find the window that has the least 0s, so that we can do minimum replacement
"""
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = sum(data)           # k is the window size, which equals how many 1s are there in data
        min_cnt = len(data)     # record the min_cnt of 0s in the window
        zero_cnt = 0            # record cnt of 0s in the window
        for i in range(len(data)):
            zero_cnt += 1 if data[i] == 0 else 0
            
            if i >= k:
                zero_cnt -= 1 if data[i-k] == 0 else 0
            
            if i >= k - 1:      # 返回结果必须保证window size大于等于k
                min_cnt = min(min_cnt, zero_cnt)
            
        return min_cnt
