60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"



https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
https://leetcode.com/problems/permutation-sequence/discuss/22554/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)
O(N^2)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # step 1: calculate the factorial - 这样可以更快捷得到factorial
        factorial = [1 for _ in range(n+1)]
        for i in range(1, n+1):
            factorial[i] = i * factorial[i-1]

        # step 2: calculate the kth permutation using https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
        nums = [str(i) for i in range(1, n+1)]
        k -= 1
        res = ""
        for i in range(n, 0, -1):
            idx = k // factorial[i-1]
            res += nums[idx]
            del nums[idx]       # O(N)
            
            k = k % factorial[i-1]      # 这里没想出来！
            
        return res
