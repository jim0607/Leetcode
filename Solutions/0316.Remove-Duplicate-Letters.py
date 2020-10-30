"""
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""


"""
we use a stack to store the solution we have built as we iterate over the string.
We delete a ch if two conditions are meet:
1. the ch can occur later on
2. the ch is greater than the curr ch;
Need to use a dictionary to pre-record the last pos a ch appears.  
Also need a included set to mark the chars that are already in the st.
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = collections.defaultdict(int)   # store the pos where ch last occured
        for i, ch in enumerate(s):
            last_occur[ch] = i

        st = []
        included = set()
        for i, ch in enumerate(s):
            if ch not in included:      # if ch is in included, we just skip
                while st and ord(st[-1]) > ord(ch) and last_occur[st[-1]] > i:
                    included.remove(st.pop())
                st.append(ch)
                included.add(ch)
                
        return "".join(st)
