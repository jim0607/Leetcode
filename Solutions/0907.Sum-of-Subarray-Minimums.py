907. Sum of Subarray Minimums

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


"""
就拿题目中的例子 [3,1,2,4,3] 来分析，开始遍历到3的时候，其本身就是一个子数组，最小值也是其本身，累加到结果 res 中，此时 res=3，
然后看下个数1，是小于3的，此时新产生了两个子数组 [1] 和 [3,1]，且最小值都是1，此时在结果中就累加了 2，此时 res=5。
接下来的数字是2，大于之前的1，此时会新产生三个子数组，其本身单独会产生一个子数组 [2]，可以先把这个2累加到结果 res 中，
然后就是 [1,2] 和 [3,1,2]，可以发现新产生的这两个子数组的最小值还是1，跟之前计算数字1的时候一样，可以直接将以1结尾的子数组最小值之和加起来，
那么以2结尾的子数组最小值之和就是 2+2=4，此时 res=9。对于最后一个数字4，其单独产生一个子数组 [4]，
还会再产生三个子数组 [3,1,2,4], [1,2,4], [2,4]，直接加上以2结尾的子数组最小值之和，总共就是 4+4=8，最终 res=17。
接下来来了3，会产生5个新数组，本身[3]是单独一个，累加到res中，res=20, 然后是子数组[4,3],[2,4,3],[1,2,4,3],[3,1,2,4,3], 
由于4比3大, 所以我们首先pop出4，res += 3, 然后发现2比3小，这时候就把以2结尾计算的结果加给res就可以了res+=4, 所以最终res=27
"""
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        st = []     # store idx
        res = 0
        A = [0] + A + [0]
        for i, num in enumerate(A):
            while st and A[st[-1]] > num:
                top_idx = st.pop()
                res += A[top_idx] * (i - top_idx) * (top_idx - st[-1])      # 这里需要好好想想
            
            st.append(i)
            
        return res % (10 ** 9 + 7)
