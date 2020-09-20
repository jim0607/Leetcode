"""
1552. Magnetic Force Between Two Balls

In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Example 1:

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
"""




"""
minimum of maximum / maximum of minimum 的问题
Thinking process for the helper function:
can we pick k positions to place the balls so that the minimum force is larger than mid.
can we pick k positions to place the balls so that the every force is larger than mid.
In a sorted arr, we want to place balls, each ball are at least mid distance to each other,
can we place more than k balls?
"""
class Solution:
    def maxDistance(self, positions: List[int], k: int) -> int:
        positions.sort()
        start, end = 1, positions[-1] - positions[0]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._can_place(positions, k, mid):
                start = mid
            else:
                end = mid
        return end if self._can_place(positions, k, end) else start
    
    def _can_place(self, positions, k, dist):
        """
        Return if we can place more than k balls so that each ball are at least dist to each other.
        Greedy: each time we find that a ball is needed, we place a ball.
        """
        cnt = 1
        prev_idx, curr_idx = 0, 1
        while curr_idx < len(positions):
            while curr_idx < len(positions) and positions[curr_idx] - positions[prev_idx] < dist:
                curr_idx += 1
            if curr_idx < len(positions):   # place a ball at curr_idx cuz it's larger than dist
                cnt += 1
            prev_idx = curr_idx
        return cnt >= k
