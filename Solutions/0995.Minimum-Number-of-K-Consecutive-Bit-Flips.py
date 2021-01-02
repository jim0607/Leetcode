995. Minimum Number of K Consecutive Bit Flips

In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

 

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]

 
"""
solution 1: modify the input nums by changing the 0 one by one - O(nk)
"""
class Solution:
    def minKBitFlips(self, nums: List[int], K: int) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            if nums[i] == 0:
                if i + K > len(nums):  # 如果位置i需要一次翻转，但是空间又不够，就表示不可能了
                    return -1
                for k in range(K):
                    nums[i+k] = 1 - nums[i+k]
                res += 1
                
            i += 1
        
        return res

"""
solution 2: do not change the input nums, just use a q to record if ith num has been changed - O(n)
Leetcode China题解：首先我们可以知道，对于每个位置而言，只有初始状态和总共被反转了多少次决定了自己最终的状态。
另一方面，我们知道每一个长度为K的区间，最多只会被反转一次，因为两次反转后对最终结果没有影响。
基于此，我们从前往后遍历数组，如果遇到一个0，我们将当前位置开始的长度为k区间的区间反转。
如果遇到0时，剩下的区间长度不足K说明我们没有办法完成反转。
但是如果我们每次反转当前区间时，将区间内每个数都取反，时间复杂度是O(n*k)的，这样是不够快的。
我们需要优化一下，我们再考虑每个位置上的元素，他有没有被反转过只会被前面K - 1个元素是否被反转过所影响，
所以我们只需要知道前面k - 1个元素总共反转了多少次(更进一步的说我们只需要知道反转了奇数次还是偶数次)。
我们使用一个队列保存i前面k - 1个位置有多少元素被反转了，即i被反转了多少次，
如果队列长度为奇数，说明被i被翻转了奇数次，如果为偶数，说明i被翻转了偶数次。
如果i需要翻转就将i加入队列，更新答案。如果i需要翻转但是已经到了队尾不足K个长度了，那就return -1.
时间复杂度：每个元素最多被进入队列和出队列一次，所以总的时间复杂度为O(n)的。
"""
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        q = deque()     # q 记录区间[i-k, i]内被反转了的idx
        res = 0
        for i, num in enumerate(A):
            while q and q[0] + K <= i:   # 把里i很远的idx都pop出来，保持窗口小于等于K
                q.popleft()
            
            # 此时len(q)就是位置i已经被翻转的次数，如果为奇数表示i已经从0翻到1或者从1翻到0了
            # 如果被翻了奇数次且num==1那说明现在变成0了，需要一次翻转
            if (len(q) % 2 == 1 and num == 1) or (len(q) % 2 == 0 and num == 0):
                if i + K > len(A):      # 如果位置i需要一次翻转，但是空间又不够，就表示不可能了
                    return -1 
                q.append(i)
                res += 1
                
        return res
