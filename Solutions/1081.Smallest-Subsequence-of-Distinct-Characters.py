1081. Smallest Subsequence of Distinct Characters

Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occur = collections.defaultdict(int)
        for i, ch in enumerate(s):
            last_occur[ch] = i
            
        st = []
        included = set()
        for i, ch in enumerate(s):
            if ch not in included:
                while st and last_occur[st[-1]] > i and ord(st[-1]) > ord(ch):
                    included.remove(st.pop())
                st.append(ch)
                included.add(ch)
        
        return "".join(st)
