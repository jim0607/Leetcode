"""
248. Strobogrammatic Number III

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.
"""



"""
想想如果 low = 99, high = 1000, 那所有的valid nums都是由三个数字组成的。
这就变成了 247. Strobogrammatic Number II 中 n = 3 的情况，只是这题不需要输出组合，只需要求多少种可能组合
可能的组合数其实就是247. Strobogrammatic Number II的数间复杂度: O(5^(n//2))
所以我们只需要算组合个数就行，不需要做 backtrack
"""
