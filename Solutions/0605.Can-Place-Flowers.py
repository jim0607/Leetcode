"""
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, 
return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


"""
把arr进行预处理：把arr的头部和尾部各加上0
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i, bed in enumerate(flowerbed):
            if bed == 0:
                if i >= 2 and flowerbed[i-1] == 0 and flowerbed[i-2] == 0:
                    flowerbed[i-1] = 1
                    n -= 1

            if n <= 0:
                return True
            
        return False
    
    
    
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 and n <= 1 else False
        
        cnt = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            cnt += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            cnt += 1
            flowerbed[-1] = 1
        
        i = 1
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0:
                j = i
                while j < len(flowerbed) - 1 and flowerbed[j] == 0:
                    j += 1
                cnt += (j - i - 1) // 2
                i = j
            i += 1
        return n <= cnt
