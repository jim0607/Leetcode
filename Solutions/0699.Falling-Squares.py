699. Falling Squares

On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0] and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.

 
Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].

Example 1:

Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:
After the first drop of positions[0] = [1, 2]: _aa _aa ------- The maximum height of any square is 2.

After the second drop of positions[1] = [2, 3]: __aaa __aaa __aaa _aa__ _aa__ -------------- The maximum height of any square is 5. The larger square stays on top of the smaller square despite where its center of gravity is, because squares are infinitely sticky on their bottom edge.

After the third drop of positions[1] = [6, 1]: __aaa __aaa __aaa _aa _aa___a -------------- The maximum height of any square is still 5. Thus, we return an answer of [2, 5, 5].

 

 
Example 2:

Input: [[100, 100], [200, 100]]
Output: [100, 100]
Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.


"""
solution 1: O(N^2)
Every time a new square falls down, we check the previous square to see if there is any square 
beneath the current falling square. If we found that we have squares i intersect with us,
which means my current square will go above to that square. Then we should update the max_h.
"""
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        res = []
        intervals = []      # store the intervals already fallen
        max_h = 0
        for left, lens in positions:
            left, right, curr_h = left, left + lens, lens
            
            # updating prev_max_h by checking all the previous fallen squares to see if 
            # there is previous fallen squares intersect with (or beneath) the curr falling square
            prev_max_h = 0      # record the max lens that will intersect with the falling ones
            for interval in intervals:
                if left >= interval[1] or right <= interval[0]:  # 如果interval与falling sqaure不相交
                    continue
                prev_max_h = max(prev_max_h, interval[2])
                
            max_h = max(max_h, prev_max_h + lens)   # update max_h after this square falls
            res.append(max_h)
            
            intervals.append([left, right, prev_max_h + lens])  # store the intervals already fallen
            
        return res
        
        
solution 2: segment tree O(NlogN) https://leetcode.com/problems/falling-squares/discuss/409304/Python-Diffenrent-Concise-Solutions
