"""
1499. Max Value of Equation

Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, 
where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. 
It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. 
Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 
Constraints:

2 <= points.length <= 10^5
points[i].length == 2
-10^8 <= points[i][0], points[i][1] <= 10^8
0 <= k <= 2 * 10^8
points[i][0] < points[j][0] for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.
"""



"""
solution 1: heapq - O(nlogn).
In this problem, we are asked to find yi - xi + yj + xj as j is looping over points and i be the prev seen point.
we just need to maintain the max yi - xi that we previously met. We can use a heapq for quick access the max(yi - xi) we've met.
Should be noted that we need to make sure xj - xi <= k.
"""
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        hq = []     # store (-(yi - xi), xi)
        max_res = -sys.maxsize
        for xj, yj in points:
            while len(hq) > 0 and xj - hq[0][1] > k:   # need to make sure xj - xi <= k
                heappop(hq)
            
            if len(hq) > 0:
                max_res = max(max_res, xj + yj - hq[0][0])
            
            heappush(hq, (xj - yj, xj))     
            
        return max_res
        
        
        
"""
Solution 2: maintain previous min/max problem: monodeque - O(N).
similar with 239. Sliding Window Maximum;

In this problem, we are asked to find yi - xi + yj + xj as j is looping over points and i be the prev seen point.
we just need to maintain the max yi - xi that we previously met.

If there is no window size limitation, to find previous largest/smallest number, monotonous stack is always what we need. 
Should be noted that we need to make sure xj - xi <= k. So in this problem, the window size is set to k, 
we can use monotonous queue to find largest/smallest element in a fixed size sliding window.

注意如果题目需要我们在window里更新最大值或最小值，我们往往需要maintian一个mono increasing or mono decreasing deque. 
在mono deque中会有两个while loop，第一个while loop从左端pop作为sliding window去限定window size, 
第二个while loop从右端pop作为monostack去maintain 最大值/最小值.
"""
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()        # store (yi - xi, xi)
        max_res = -sys.maxsize
        for xj, yj in points:
            while len(dq) > 0 and xj - dq[0][1] > k:    # 第一个while loop从左端pop作为sliding window去限定window size
                dq.popleft()
                
            if len(dq) > 0:
                max_res = max(max_res, xj + yj + dq[0][0])
                
            while len(dq) > 0 and dq[-1][0] <= yj - xj: # 第二个while loop从右端pop作为monostack去maintain 最大值
                dq.pop()
            
            dq.append((yj - xj, xj))     
            
        return max_res
