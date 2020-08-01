763. Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.


Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.



"""
put all the positions into a dictionary. Then find the max position of s[0] appears, 
for all the chars within this max position, search the max postion they appears, so on...
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ch_to_pos = collections.defaultdict(int)    # stores the max position of ch
        for i, ch in enumerate(s):
            ch_to_pos[ch] = max(ch_to_pos[ch], i)
        
        res = []
        i = 0
        while i < len(s):
            curr_max = ch_to_pos[s[i]]
            j = i
            while j <= curr_max:    # For all the chars within this max position, search the max postion they appears, 注意这里的curr_max是在变的
                curr_max = max(curr_max, ch_to_pos[s[j]])
                j += 1
            res.append(j - i)
            i = j
        
        return res
