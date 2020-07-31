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
find the substring with lens=k and minimum 0s in it.
"""
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        lens = len(data)
        total_cnt = 0       # find the total_cnt of 1s, which is used as window size
        for i, num in enumerate(data):
            if num == 1:
                total_cnt += 1
        
        cnt_zero = 0
        for i in range(total_cnt):
            if data[i] == 0:
                cnt_zero += 1
                
        min_cnt = cnt_zero
        for i in range(total_cnt, lens):
            if data[i] == 0:
                cnt_zero += 1
            if data[i-total_cnt] == 0:
                cnt_zero -= 1
            min_cnt = min(min_cnt, cnt_zero)
            
        return min_cnt
