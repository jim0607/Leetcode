556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1



"""
124354 -> 124453 -> 1244 35
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 通过取余数的方法将n转换成bits存到数组中
        bits = []
        while n > 0:
            bits.append(n % 10)
            n //= 10
        bits = bits[::-1]
        
        # step 1: 从右至左找第一个降序的idx
        idx = -1
        for i in range(len(bits)-1, 0, -1):
            if bits[i] > bits[i-1]:
                idx = i - 1
                break
        if idx == -1:
            return -1
                
        # step 2: 找到右边just larger than bits[idx]的数的idx
        idx_gt = idx + 1
        for i in range(idx + 1, len(bits)):
            if bits[i] > bits[idx]:
                idx_gt = i      # 由于右边是递增的，所以可以这样直接更新
        
        # step 3: swap the idx with the idx_gt
        bits[idx], bits[idx_gt] = bits[idx_gt], bits[idx]
        
        # step 4: 再将idx之后的数升序排列
        # bits = bits[:idx+1] + sorted(bits[idx+1:])
        # 由于idx之后的数是递增的，所以只需要交换即可
        i, j = idx + 1, len(bits) - 1
        while i < j:
            bits[i], bits[j] = bits[j], bits[i]
            i += 1
            j -= 1
        
        # step 5: 将bits还原成数字
        res = 0
        for bit in bits:
            res = 10 * res + bit
        return res if res <= 2**31 - 1 else -1
