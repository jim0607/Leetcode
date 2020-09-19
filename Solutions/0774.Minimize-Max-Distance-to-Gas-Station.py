774. Minimize Max Distance to Gas Station

On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000



"""
If we can do it at D, then we can do it at larger than D. This is a OOXX problem to find the minimum D.
The difficult part is to find if is_valid to place K stations so that every adjacent station has distance smaller than D - using greedy.
"""
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        start, end = 1e-6, stations[-1] - stations[0]       # 注意start, end可以是小数
        while start + 1e-6 < end:
            mid = start + (end - start) / 2     # 注意是小数，不要用整除号
            if self._is_valid(stations, mid, K):
                end = mid
            else:
                start = mid
                
        return start if self._is_valid(stations, start, K) else end
    
    def _is_valid(self, stations, D, K):
        """
        Return if we can add K gas stations to make every adjacent gas station have distance no larger than D.
        Algorithm: whenever we find a distance larger then D, we add a gas statation. 
        """
        cnt = 0     # how many stations we need to add
        for i in range(1, len(stations)):
            if stations[i] - stations[i-1] > D:
                cnt += (stations[i] - stations[i-1]) // D       # 注意这里cnt是一个整数 但是D是一个小数，所以不要用(stations[i] - stations[i-1] - 1) // D
                
        return cnt <= K
