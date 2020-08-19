32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


"""
solution 1: stack.  use a stack to store the idx, maintain a start idx to record the start idx of a valid parentheses.
if ch == "(", push the idx into the stack;
if ch == ")", if the stack is empty, then start = i + 1; if not empty, then update max_lens as i - stack.pop() + 1
O(N), O(N)
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_lens = 0
        st = []
        start_idx = 0
        for i, ch in enumerate(s):
            if ch == "(":
                st.append(i)
            elif ch == ")":
                if len(st) == 0:
                    start_idx = i + 1
                else:
                    st.pop()
                    lens = i - st[-1] if len(st) != 0 else i - start_idx + 1
                    max_lens = max(max_lens, lens)
        return max_lens
    
""" run a test case ")()())", then we'll see why start idx is important """



"""
此题还有一种不用额外空间的解法，使用了两个变量 left 和 right，分别用来记录到当前位置时左括号和右括号的出现次数，
当遇到左括号时，left 自增1，右括号时 right 自增1。对于最长有效的括号的子串，一定是左括号等于右括号的情况，此时就可以更新结果 res 了，
一旦右括号数量超过左括号数量了，说明当前位置不能组成合法括号子串，left 和 right 重置为0。
但是对于这种情况 "(()" 时，在遍历结束时左右子括号数都不相等，此时没法更新结果 res，但其实正确答案是2，怎么处理这种情况呢？
答案是再反向遍历一遍，采取类似的机制，稍有不同的是此时若 left 大于 right 了，则重置0，这样就可以 cover 所有的情况了
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                right += 1
                
            if left == right:
                res = max(res, 2 * left)
            elif right > left:
                left, right = 0, 0
             
        # 完全相同的逻辑从右往左再扫一遍
        left, right = 0, 0
        for ch in s[::-1]:
            if ch == ")":
                right += 1
            else:
                left += 1
                
            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left, right = 0, 0
                
        return res
