#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (47.47%)
# Likes:    2266
# Dislikes: 119
# Total Accepted:    155.7K
# Total Submissions: 327.3K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# Examples:
# 
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
# 
# 
#



class Solution:
    def decodeString(self, s: str) -> str:
        num_st = []         # store the number in s
        str_st = [""]       # store the string in s
        temp_num = 0
        i = 0
        while i < len(s):
            ch = s[i]
            
            if ch.isdigit():
                temp_num = int(ch)
                while i + 1 < len(s) and s[i+1].isdigit():      # 防止多个数字同时出现
                    temp_num = temp_num * 10 + int(s[i+1])
                    i += 1
            
            elif ch == "[":
                num_st.append(temp_num)
                temp_num = 0
                str_st.append("")
                
            elif ch.isalpha():
                str_st[-1] += ch   # 注意不能用strStack.append(ch)，因为我们想要行程一个整体才可以pop出来想要的。
                                   # eg:2[bc]，要让"bc"形成整体才可以一起pop出来
            elif ch == "]":
                num = num_st.pop()
                string = str_st.pop()
                str_st[-1] += num * string      # 这里不能用append，原因同上！
                
            i += 1
            
        return str_st[0]
    
    
    



class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s

        numStack = []      # store the number in s
        strStack = [""]      # store the string in s
        tempNum = 0
        for ch in s:
            if ch.isdigit():
                tempNum = tempNum * 10 + (ord(ch) - ord("0"))

            elif ch == "[":
                numStack.append(tempNum)
                tempNum = 0
                strStack.append("")     # 注意不能少，否则strStack[-1]会报错！
            
            elif ch.isalpha():
                strStack[-1] += ch      # 注意不能用strStack.append(ch)，因为我们想要行程一个整体才可以pop出来想要的。eg:2[bc]，要让"bc"形成整体才可以一起pop出来

            elif ch == "]":
                tempStr = strStack.pop()
                tempStr *= numStack.pop()
                strStack[-1] += tempStr     # 这里不能用append，原因同上！
            
        return ''.join(strStack)
   
# @lc code=end

