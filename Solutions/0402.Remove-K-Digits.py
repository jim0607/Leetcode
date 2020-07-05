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
维护一个递增栈，这样排在前面的就都是最小的了
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        
        st = []
        num += "0"  # 在最后补个0，如果k没用完的话可以用这个零把没用完的k用掉
        for ch in num:
            while k > 0 and st and int(st[-1]) > int(ch):
                st.pop()
                k -= 1
            st.append(ch)
            
        st.pop()
        i = 0
        while i < len(st) and st[i] == "0":
            i += 1
            
        return "0" if i == len(st) else "".join(st[i:])
