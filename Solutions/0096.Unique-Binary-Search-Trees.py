Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


"""卡塔兰数 Catalan Numbe 的一个例子
https://www.cnblogs.com/grandyang/p/4299608.html"""
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(n):
            C = C * (2 * (2 * i + 1) / (i + 2))
            
        return int(C)
