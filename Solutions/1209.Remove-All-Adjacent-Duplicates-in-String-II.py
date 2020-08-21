1209. Remove All Adjacent Duplicates in String II

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"



"""
use a st to store 左边等待消掉的k-1 个chars. loop the string s.
if s[i] == st最上面k-1个char, then pop all k-1 个 char. 
To make it more efficient, use a pair to store the value and the count of each character.
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for ch in s:
            if len(st) == 0:
                st.append((ch, 1))
            else:
                if ch == st[-1][0]:
                    if st[-1][1] == k - 1:
                        st.pop()
                    else:
                        top = st.pop()
                        st.append((top[0], top[1] +1))
                else:
                    st.append((ch, 1))
                    
        return "".join(ch * cnt for ch, cnt in st)
