"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.construct(S) == self.construct(T)
    
    def construct(self, s):
        backspace_cnt = 0
        res = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "#":
                backspace_cnt += 1
            else:
                if backspace_cnt > 0:
                    backspace_cnt -= 1
                else:
                    res += s[i]
        return res[::-1]
    


"""
naively, we can use stacks to find out the final string of S and T, and compare them. But that takes O(N) space.
The problem is asking for O(1) space.
由于题目"#"可以删掉前面的ch, We can use a pointer traverse from right to left, and use a counter to count how many # we got so far.
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_cnt = 0
        t_cnt = 0
        i, j = len(s) - 1, len(t) - 1
        while True:         # 注意不要写成while i >= 0 and j >= 0 了
            # step 1: find the first 裸露在外面的ch of s and t
            while i >= 0:
                if s[i] == "#":
                    s_cnt += 1
                    i -= 1
                else:
                    if s_cnt > 0:
                        s_cnt -= 1
                        i -= 1
                    else:
                        break
            while j >= 0:
                if t[j] == "#":
                    t_cnt += 1
                    j -= 1
                else:
                    if t_cnt > 0:
                        t_cnt -= 1
                        j -= 1
                    else:
                        break
            
            # step 2: 比较裸露在外面的ch of s and t
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False
            else:
                i -= 1
                j -= 1
                
                    
                    
"""                 
Google follow up: 加一个按键是类似caps lock，即按了之后所有的字母小写变大写，再按一下大写变小写。
思路：分别定义caps cnt，先扫一遍看多少个caps lock，比较s1.charAt(i) == s2.charAt(j) && caps1 == caps2
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        lens1, lens2 = len(S), len(T)
        idx1, idx2 = lens1 - 1, lens2 - 1
        cnt1, cnt2 = 0, 0
        cap1, cap2 = 0, 0
        
        # step 1: find how many caps are there in total for S and for T
        for ch in S:
            if ch == "*":
                cap1 += 1
        for ch in T:
            if ch == "*":
                cap2 += 1
        
        # step 2: traverse from right to left and 比较s1.charAt(i) == s2.charAt(j) && caps1 == caps2
        while True:
            while idx1 >= 0:
                if S[idx1] == "#":
                    cnt1 += 1
                    idx1 -= 1
                elif S[idx1] == "*":
                    cap1 -= 1    # the "*" in front of idx1 should be one less now
                    idx1 -= 1
                else:
                    if cnt1 > 0:
                        idx1 -= 1
                        cnt1 -= 1
                    else:
                        break
            while idx2 >= 0:
                if T[idx2] == "#":
                    cnt2 += 1
                    idx2 -= 1
                elif T[idx2] == "*":
                    cap1 -= 1
                    idx1 -= 1
                else:
                    if cnt2 > 0:
                        idx2 -= 1
                        cnt2 -= 1
                    else:
                        break
                        
            if idx1 < 0 and idx2 < 0:
                return True
            if idx1 < 0 or idx2 < 0:
                return False
            if idx1 >= 0 and idx2 >= 0:
                if S[idx1] != T[idx2] or cap1 % 2 != cap2 % 2:
                    return False
                else:
                    idx1 -= 1
                    idx2 -= 1
