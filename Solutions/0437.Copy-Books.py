"""
437. Copy Books

Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the shortest time that the slowest copier spends.

Example 1:

Input: pages = [3, 2, 4], k = 2
Output: 5
Explanation: 
    First person spends 5 minutes to copy book 1 and book 2.
    Second person spends 4 minutes to copy book 3.
"""

    
"""
binary search: O(nlog(sum(pages)-max(pages))), n is the number of books
"""
class Solution:
    def copyBooks(self, pages, k):
        if not pages:
            return 0
            
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_possible(pages, mid, k):
                end = mid
            else:
                start = mid
        return start if self.is_possible(pages, start, k) else end
        
    def is_possible(self, pages, threshold, k):
        """
        return if k paople can finish in mid time.  Algorithm: greedy. 每次发现要超时了就加一个人。
        sweep the books and keep track of the curr_time. 
        when we find we cannot finish all pages in timeLimit, we add a new person and set the curr_time for the new person to be zero
        """
        people_needed = 1
        curr_time = 0
        for page in pages:
            if curr_time + page > threshold:
                people_needed += 1
                curr_time = 0
            curr_time += page
        return people_needed <= k





class Solution:
    def copyBooks(self, pages, k):
        if not pages: return 0
        start, end = max(pages), sum(pages) + 1
        while start + 1 < end:
            mid = start + (end - start ) // 2
            if self._can_finish(pages, k, mid):
                end = mid
            else:
                start = mid
        return start if self._can_finish(pages, k, start) else end
        
    def _can_finish(self, pages, k, mid):
        """
        return if k paople can finish in mid time.  Algorithm: greedy. 每次发现要超时了就加一个人。
        sweep the books and keep track of the curr_time. 
        when we find we cannot finish all pages in timeLimit, we add a new person and set the curr_time for the new person to be zero
        """
        i = 0
        while i < len(pages):
            curr_time = 0
            while i < len(pages) and curr_time + pages[i] <= mid:
                curr_time += pages[i]
                i += 1
            k -= 1      # 只有上一个人无法在mid时间内完成的情况下，我们才加一个人进来
        return k >= 0
    
  

    

"""需要找到一种分段方式，使得所有段的数字之和的最大值最小
f[k][i]=前k个(不包括k)抄写员最多需要多长时间抄完前i本书(不包括i)
f[k][j]=min(max(f[k-1][i], i~j所需时间)) for 0<i <j
初始条件：f[k][0]=0; f[0][0]=0; f[0][i] = inf for i > 0
O(N^2*K), O(N*K)"""
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        lens = len(pages)
        dp = [[float("inf")] * (lens + 1) for _ in range(k + 1)]
        
        for m in range(k + 1):
            dp[m][0] = 0
            for j in range(1, lens + 1):
                dp[0][j] = float("inf")
                
        for m in range(1, k + 1):
            for j in range(1, lens + 1):
                for i in range(j):
                    tempMax = max(dp[m - 1][i], sum(pages[i:j]))
                    dp[m][j] = min(dp[m][j], tempMax)
                    
        return dp[k][lens]
