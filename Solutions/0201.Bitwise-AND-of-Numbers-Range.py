201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0


"""
[5, 7]里共有三个数字，分别写出它们的二进制为：
101　　110　　111
相与后的结果为100，仔细观察我们可以得出，最后的数是该数字范围内所有的数的左边共同的部分，
如果上面那个例子不太明显，我们再来看一个范围[26, 30]，它们的二进制如下：
11010　　11011　　11100　　11101　　11110
相与之后结果为11000
发现了规律后，我们只要写代码找到左边公共的部分即可
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   # shift是公共部分最右边的位置
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
