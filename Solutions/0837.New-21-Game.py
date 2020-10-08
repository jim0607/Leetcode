"""
837. New 21 Game

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  
During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  
Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  
What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
"""


"""
    The probability to get point K point is
    p(K) = p(K-1) / W + p(K-2) / W + p(K-3) / W + ... p(K-W) / W
         = (p(K-1) + p(K-2) + ... + p(K-W)) / W
    
    let wsum = p(K-1) + p(K-2) + ... + p(K-W)
        p(K) = wsum / W
    
    dp is storing p(i) for i in [0 ... N]
    - We need to maintain the window by
      adding the new p(i), 
      and getting rid of the old p(i-w)
    - check i >= W because we would not have negative points before drawing a card
      For example, we can never get a point of 5 if we drew a card with a value of 6
    - check i < K because we cannot continue the game after reaching K
      For example, if K = 21 and W = 10, the eventual point is between 21 and 30
      To get a point of 27, we can have:
      - a 20 point with a 7
      - a 19 point with a 8
      - a 18 point with a 9
      - a 17 point with a 10
      - but cannot have 21 with a 6 or 22 with a 5 because the game already ends
"""
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        if K == 1:
            return N / W if N / W <= 1 else 1
        if N >= K + W:
            return 1.0
        
        dp = [0 for _ in range(N + 1)]
        dp[0] = 1.0
        w_sum = 1.0
        for n in range(1, N + 1):
            dp[n] = w_sum / W
            if n < K:       # we can only add dp[n] to w_sum when n < k
                w_sum += dp[n]
            if n >= W:      # we maintain a window W, cuz only w_sum in window W can cnt
                w_sum -= dp[n-W]
        
        return sum(dp[K:])
