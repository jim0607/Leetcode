1231. Divide Chocolate

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]


"""
If I can get a sweetness of s, we can also get a sweetness less than s. 
So it's a OOXX problem. The difficult is to check whether or not can get the sweetness mid.
Use greedy to check can get - O(N).  Overall: O(NlogM), where N = len(sweetness), M = sum(sweetness)//(K+1)
"""
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        if K + 1 > len(sweetness):
            return 0
        if K == 0:
            return sum(sweetness)
        
        start, end = 0, sum(sweetness) // (K + 1)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._can_get(sweetness, mid, K):
                start = mid
            else:
                end = mid
        
        return end if self._can_get(sweetness, end, K) else start       # 注意是return end在前面，因为需要求的是能得到的最大值
    
    def _can_get(self, sweetness, sw, K):
        cnt = 0     # how many people can get at least sw sweetness
        chunk_sweet = 0
        for sweet in sweetness:
            chunk_sweet += sweet
            if chunk_sweet >= sw:
                cnt += 1
                chunk_sweet = 0
                
        return cnt >= K + 1
