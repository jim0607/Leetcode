Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.



class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n & 1)  # & operator sets each bit to 1 if both bits are 1
            n = n >> 1      # this is how you iterate each bit in an integer
        return res

       
"""
Follow up question: Find the parity of a number. The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
"""
class Solution:
    def find_parity(self, n: int) -> int:
        res = 0
        while n > 0:
            res ^= (n & 1)  # ^ operator is very important, 相异为1, 相同为0
            n = n >> 1      # this is how you iterate each bit in an integer
        return res
