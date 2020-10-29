"""
1047. Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""


"""
use a st to store 左边等待消掉的chars. loop the string s, if s[i] == st[-1], then pop. else append.
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for ch in s:
            if len(st) == 0:
                st.append(ch)
            else:
                if ch == st[-1]:
                    st.pop()
                else:
                    st.append(ch)
        return "".join(st)
