"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
"""



"""
swap[i] = min swaps with A[i] and B[i] swap
no_swap[i] = min swaps with A[i] and B[i] not swapped
"""
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        if len(A) <= 1:
            return 0
        swap = [float("inf") for _ in range(len(A))]
        no_swap = [float("inf") for _ in range(len(A))]
        swap[0] = 1
        no_swap[0] = 0
        for i in range(1, len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:     
                swap[i] = swap[i-1] + 1             # i-1那个位置swap过，需要swap过来
                no_swap[i] = no_swap[i-1]           # i-1那个位置没有swap过，不需要管
            if A[i] > B[i-1] and B[i] > A[i-1]:     
                swap[i] = min(swap[i], no_swap[i-1] + 1)  # i-1那个位置没有swap过，需要swap过来
                no_swap[i] = min(no_swap[i], swap[i-1])   # i-1那个位置swap过，不需要管
        return min(swap[-1], no_swap[-1])



"""
https://www.cnblogs.com/grandyang/p/9311385.html
和714.Best Time to Buy and Sell Stock with Transaction Fee 很像，都有交换和不交换两种情况
我们可以优化上面解法的空间复杂度，由于当前位置的值只跟前一个位置相关，所以我们并不需要保存整个数组，
用四个变量来分别表示当前位置和前一个位置的各两种状态，可以实现同样的效果，参见代码如下：
"""
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        lens = len(A)
        swap_prev = 1
        noSwap_prev = 0
        for i in range(1, lens):
            swap_curr, noSwap_curr = float("inf"), float("inf")
            if A[i] > A[i-1] and B[i] > B[i-1]:
                swap_curr = min(swap_curr, swap_prev + 1)
                noSwap_curr = min(noSwap_curr, noSwap_prev)
            if A[i] > B[i-1] and B[i] > A[i-1]:
                swap_curr = min(swap_curr, noSwap_prev+1)
                noSwap_curr = min(noSwap_curr, swap_prev)
            swap_prev, noSwap_prev = swap_curr, noSwap_curr
        return min(swap_curr, noSwap_curr)
