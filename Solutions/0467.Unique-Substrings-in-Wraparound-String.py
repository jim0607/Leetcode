"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", 
so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. 
In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
"""




"""
算法：我们看abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd, d，以d结尾的最长字符串是长度是4. 所以以d结尾有4个unique substring，
所以题目可以转换为分别求出以每个字符(a-z)为结束字符的最长连续字符串就行了，
我们用一个数组记录下 以每个字符(a-z)为结束字符的最长连续字符串，最后求出数组的所有数字之和就是我们要的结果啦.
扫描一边序列，利用动态规划记录到每个字符为止的最长子序列长度。时间复杂度O(n),空间复杂度O(1).
"""
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p: return 0
        if len(p) == 1: return 1
        
        all_lens = [0 for _ in range(26)]       # 记录到这个字符为止的最长子序列的长度
        all_lens[ord(p[0]) - ord("a")] = 1      # 初始化
        
        curr_lens = 1           # 记录到目前为止的最长子序列的长度
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i]) - ord(p[i-1]) == -25:
                curr_lens += 1
            else:
                curr_lens = 1
                
            # 更新dp数组
            all_lens[ord(p[i]) - ord("a")] = max(all_lens[ord(p[i]) - ord("a")], curr_lens)
            
        return sum(all_lens)
