"""
1423. Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. 
The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
"""



"""
solution 1: find the minimum points you can get within window with fixed size: lens-k. 套用模板即可
"""
class Solution:
    def maxScore(self, card_points: List[int], k: int) -> int:
        total = sum(card_points)
        size = len(card_points) - k     # window size
        min_points = total      # min_points we can get within the window
        points = 0              # how many points we can get within the window
        for i in range(len(card_points)):
            points += card_points[i]
            
            if i >= size:
                points -= card_points[i - size]
            
            if i >= size - 1:
                min_points = min(min_points, points)
            
        return total - min_points










"""
solution 2: sliding window with fix size problem, the only difference is that some part of the window is 
at the beginning of the list and some are at the end.
"""
class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return sum(nums)
        
        curr_sum = sum(nums[-k:])   # the sum with window size k
        max_sum = curr_sum
        for i in range(1, k + 1):   # i 为左边的长度
            j = k - i            # j 为右边的长度
            curr_sum += nums[i - 1]
            curr_sum -= nums[len(nums) - j - 1]
            max_sum = max(max_sum, curr_sum)
        return max_sum
