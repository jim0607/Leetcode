"""
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


"""
维护一个charDict, 用来记录i->j中的char的频率，这题是sum at most s problem, 
写法是while loop里让前面的指针去追后面的指针; 更新j: charDict[s[j]+=1; 
更新i: charDict[s[i]] -= 1, if charDict[s[i]] == 0: del charDict[s[i]]
套用模板即可
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_lens = 0
        ch_to_cnt = collections.defaultdict(int)
        i = 0
        for j in range(len(s)):
            ch_to_cnt[s[j]] += 1        # 不管是哪种模板，都是先更新后面的指针
            
            while i <= j and len(ch_to_cnt) > k:
                ch_to_cnt[s[i]] -= 1
                if ch_to_cnt[s[i]] == 0:    # 注意要del掉cnt=0的ch
                    del ch_to_cnt[s[i]]
                i += 1
                
            if len(ch_to_cnt) <= k:
                max_lens = max(max_lens, j - i + 1)
                
        return max_lens
