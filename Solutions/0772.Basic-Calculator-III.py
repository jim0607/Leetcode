772. Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12


"""
这道题是基本计算器系列的第三道，前两道分别为 Basic Calculator 和 Basic Calculator II，
区别是，第一道只有加减法跟括号，第二道只有加减乘除法，而这第三道既有加减乘除法又有括号运算。
但是好就好在我们可以将括号里的内容当作一个整体调用递归函数来处理。而其他部分，就跟第二道一模一样了。
"""
class Solution:
    def calculate(self, s: str) -> int:
        prev_sign = "+"
        num_st = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ord(s[i]) - ord("0")
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = 10 * num + ord(s[i + 1]) - ord("0")
                    i += 1
                
                # whenever we get a num, we calculate with prev_sign and append it to num_st
                # which is exactly the same as Basic Calculator II
                if prev_sign == "+":
                    num_st.append(num)
                elif prev_sign == "-":
                    num_st.append(-num)
                elif prev_sign == "*":
                    num_st.append(num_st.pop() * num)
                elif prev_sign == "/":
                    num_st.append(int(num_st.pop() / num))
                    
            elif s[i] in ["+", "-", "*", "/"]:
                prev_sign = s[i]
                
            # all the above code are exactly the same as Basic Calculator II, which has not parenthses
            # below we deal with the case of parenthses using recursion.
            # we first find the open-close parentheses pair, and do recursion to find the num in the open-close parentheses pair
            elif s[i] == "(":
                j = self._close_parentheses(s, i)   # find the position of ")"
                num = self.calculate(s[i + 1: j])
                
                # whenever we get a num, we calculate with prev_sign and append it to num_st
                if prev_sign == "+":
                    num_st.append(num)
                elif prev_sign == "-":
                    num_st.append(-num)
                elif prev_sign == "*":
                    num_st.append(num_st.pop() * num)
                elif prev_sign == "/":
                    num_st.append(int(num_st.pop() / num))
                    
                i = j       # move i to the colse parentheses position
                
            i += 1
            
        return sum(num_st)
    
    def _close_parentheses(self, s, open_pos):
        """
        find the corresponding close parenthses 这个算法也很有意思！
        """
        cnt = 0
        i = open_pos
        while i < len(s):
            if s[i] == "(":
                cnt += 1
            elif s[i] == ")":
                cnt -= 1
                
            if cnt == 0:
                return i
            
            i += 1
