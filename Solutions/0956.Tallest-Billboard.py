"""
956. Tallest Billboard

You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports, one on each side.  Each steel support must be an equal height.

You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.

Example 1:

Input: [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.
"""




"""
The problem can be stated as:
Given a list of numbers, multiply each number with 1 or 0 or -1, make the sum of all numbers to 0. 
Find a combination which has the largest sum of all positive numbers.

We can consider the sum as the key and positive number sum as the value.
We initally have dp[0] = 0
Let's run through a example, [1,2,3]
First we have {0:0}.
After 1, we have {0: 0, 1: 1, -1: 0}
After 2, we have {0:0, 2:2, -2:0, 1:1, 3:3,-1:1, -1:0,1:2,-3:0}
we will drop 1:1 and -1:0 since they have smaller value with the same key[1]and [-1]. 
That left us with {0:0, 2:2, -2:0, 3:3,-1:1,1:2,-3:0}
Number 3 is doing pretty much the same. we will update -3:0 to be 0:3
Then we will get the final result with dp[0], and our final answer will be 3.
Time complexity is O(min(3^N, 5000)), where N is number of rods.
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # (the sum --> the sum of corresponding positive numbers)
        dp = collections.defaultdict(int)
        dp[0] = 0
        for lens in rods:
            curr = collections.defaultdict(int)
            for sum, pos_sum in dp.items():
                curr[sum + lens] = max(curr[sum + lens], pos_sum + lens)    # case 1: 加lens
                curr[sum] = max(curr[sum], pos_sum)                         # case 2: 不加lens
                curr[sum - lens] = max(curr[sum - lens], pos_sum)           # case 3: 减lens - 这一这里只记positive sum
            dp = curr
        return dp[0]
