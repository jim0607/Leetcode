190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, 
so return 3221225471 which its binary representation is 10111111111111111111111111111111.



class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        while n:
            res += (n & 1) << power     # & operator sets each bit to 1 if both bits are 1
            power -= 1
            n = n >> 1
        return res
        
      
"""
Follow up:
If this function is called many times, how would you optimize it?

Solution: Just cache the result for each number to each other.
By cache, I mean to use a look up table. So for example if you get the number 0001, 
you would reverse it to 1000 and then in the cache you would have 0001 -> 1000 and 1000 -> 0001. 
So next time you need the reverse of either 0001 or 1000 they are immediately available. 
This is good for when the same numbers and their reverse will be used frequently, but may not perform better when the numbers are randomized from 0 to 1<<32-1,
because if table is too big then look up time will become substantial.
"""
