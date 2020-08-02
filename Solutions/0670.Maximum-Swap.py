670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.


"""
solution 1: sort and compare - O(nlogn)
"""
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        arr = [ch for ch in s]
        sorted_arr = sorted(arr, key = lambda x: -ord(x))
        print(arr, sorted_arr)
        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                temp = arr[i]
                
                # step 1: # 找到arr中靠后的那个需要替换的idx
                idx = 0
                for j in range(len(arr)-1, -1, -1):  # 找到靠后的那个需要替换的idx
                    if arr[j] == sorted_arr[i]:
                        idx = j
                        break
                    
                # step 2: swap 操作
                arr[i] = sorted_arr[i]     
                arr[idx] = temp
                return int("".join(arr))
                
        return num
        

"""
solution 2: one pass from backward - O(N)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(ch) for ch in str(num)]
        max_idx = len(nums) - 1     # the idx for the max number
        need_swap_idx_small = 0     # the idx that needs to be swapped
        need_swap_idx_large = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[max_idx]:
                max_idx = i
            elif nums[i] < nums[max_idx]:
                need_swap_idx_small = i     # 如果碰到一个小的，应该与后面已经遍历过的max_idx交换
                need_swap_idx_large = max_idx
        
        nums[need_swap_idx_small], nums[need_swap_idx_large] = nums[need_swap_idx_large], nums[need_swap_idx_small]
        
        return "".join([str(x) for x in nums])
        
