986. Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)


Example 1:


Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]



"""
这题是找两个Interval的overlaps, 和merge interval有点像，we update res as res.append([max_start, min_end]).
然后两个sweep line的指针，谁的end比较小，谁先往前挪一步
"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            max_start = max(A[i][0], B[j][0])
            min_end = min(A[i][1], B[j][1])
            if max_start <= min_end:
                res.append([max_start, min_end])
            
            if A[i][1] < B[j][1]:   # 主要是这里没想出来，两个sweep line的指针，谁的end比较小，谁先往前挪一步
                i += 1
            else:
                j += 1
                
        return res
