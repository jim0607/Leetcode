"""
402. Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


"""
维护一个递增栈，这样排在前面的就都是最小的了
"""
"""
maintain an increasing st. we iterate the num,
if num < st[-1], then keep popping.
"""
class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        st = []
        for i, num in enumerate(nums):           
            while len(st) > 0 and st[-1] > num:
                if k == 0:
                    break
                st.pop()
                k -= 1
            st.append(num)

        while len(st) > 0 and k > 0:    # 如果k有多的，那就删后面的
            st.pop()
            k -= 1

        # deal with "0"开头的数字
        i = 0
        while i < len(st) and st[i] == "0":  # deal with "0"开头的数字
            i += 1

        return "0" if i == len(st) else "".join(st[i:])
    
    
class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if k >= len(nums):
            return "0"
        
        st = []
        n = len(nums)
        for i, num in enumerate(nums):
            while len(st) > 0 and st[-1] > num and (len(st) - 1 + n - i) >= n - k:
                st.pop()
            st.append(num)

        if len(st) > n - k:
            st = st[:n-k]
        
        i = 0
        while i < len(st):
            if st[i] != "0":
                break
            i += 1
        return "0" if len(st[i:]) == 0 else "".join(st[i:])
