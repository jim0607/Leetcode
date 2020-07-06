275. H-Index II

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?


"""
The list is sorted, 疯狂暗示二分呀有木有！
find the first idx where citations[idx] >= N - idx, OOOXXX problem
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1
        if citations[-1] == 0:
            return 0
        
        N = len(citations)
        start, end = 0, N - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if citations[mid] >= N - mid:
                end = mid
            else:
                start = mid
            
        return N - start if citations[start] >= N - start else N - end
