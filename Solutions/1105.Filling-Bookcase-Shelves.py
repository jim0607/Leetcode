"""
We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

We want to place these books in order onto bookcase shelves that have total width shelf_width.

We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
"""


"""
dp[i]: the min height to place the first i-1 books.
For dp[i+1], either place book i on a new shelve dp[i] = dp[i-1] + height[i-1],
or grab previous books together with book i and move to next level together: 
dp[i] = min(dp[j-1] + max(height[j-1] .. height[0])), where sum(width[j-1] + ... + sum(width[i]) <= shelve_width
"""
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float("inf") for _ in range(n + 1)]   # the min height to place the first i-1 books
        dp[0] = 0
        
        for i in range(1, n + 1):
            # step 1: 开一层新的把books[i-1]放上
            dp[i] = dp[i-1] + books[i-1][1]     
            
            # step 2: 看看之前一层的书能不能挪到这一层来
            curr_width = books[i-1][0]
            curr_height = books[i-1][1]
            for j in range(i-1, 0, -1):
                if curr_width + books[j-1][0] > shelf_width:
                    break
                curr_width += books[j-1][0]
                curr_height = max(curr_height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + curr_height)
        
        return dp[n]
