556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1



class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)
        lens = len(nums)
        res = [int(num) for num in nums]
        
        # step 1: 从右至左找到第一个降序的
        found_decreasing = False
        for i in range(lens-2, -1, -1):
            if res[i+1] > res[i]:
                found_decreasing = True
                break
        if not found_decreasing:
            return -1
        
        idx = i
        # step 2: swap the nums[idx] with the num just larger then it
        diff = float("inf")
        idx_just_larger = 0
        for j in range(idx, lens):
            if res[j] > res[idx] and res[j] - res[idx] < diff:
                idx_just_larger = j
                
        # step 3: swap idx and idx_just_larger
        res[idx], res[idx_just_larger] = res[idx_just_larger], res[idx]
        
        # step 3: reverse the rest of the list
        i, j = idx + 1, lens - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
            
        res = int("".join(map(str, res))) 
        return res if res <= 2**31 - 1 else -1
