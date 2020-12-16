"""
763. Partition Labels

A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        step 1: use a hashmap to store the last time a ch appears. mapping[ch] = the last idx the ch appears
        step 2: construct has_to_reach[idx] = starting from idx, where we have to reach.
        step 3: jump game II
        """
        # step 1: use a hashmap to store the last time a ch appears. mapping[ch] = the last idx the ch appears
        mapping = collections.defaultdict(int)
        for idx, ch in enumerate(s):
            mapping[ch] = idx
            
        # step 2: construct has_to_reach[idx] = starting from idx, where we have to reach.
        has_to_reach = [0 for _ in range(len(s))]
        for idx, ch in enumerate(s):
            has_to_reach[idx] = mapping[ch]
            
        # step 3: jump game II
        res = []
        i = 0
        last_coverage = 0
        next_coverage = has_to_reach[0]
        start = 0
        while i < len(s):
            while i <= last_coverage:
                next_coverage = max(next_coverage, has_to_reach[i])
                i += 1

            if next_coverage == last_coverage:      # meaning if we stop here, no ch in current window will appear later
                res.append(next_coverage - start + 1)
                start = next_coverage + 1           # 更新下一段的start position
                if i < len(s): 
                    next_coverage = has_to_reach[i] # 更新next_coverage, last coverage保持不变就可以了
            else:
                last_coverage = next_coverage
            
        return res




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
