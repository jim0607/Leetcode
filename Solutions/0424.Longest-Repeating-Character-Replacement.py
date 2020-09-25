"""
424. Longest Repeating Character Replacement

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
"""



"""
Given a string convert it to a string with all same characters with minimal changes. 
The answer is (length of the entire substring) - (number of times of the maximum occurring character in the string).
Given this, this problem is to find the max_lens of substring so that 
(length of substring - number of times of the maximum occurring character in the substring) is at most K.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_to_cnt = collections.defaultdict(int)
        max_lens = 0
        max_occur = 0       # number of times of the maximum occurring character in the string
        i = 0
        for j in range(len(s)):
            ch_to_cnt[s[j]] += 1
            max_occur = max(max_occur, ch_to_cnt[s[j]])
            
            while i <= j and j - i + 1 - max_occur > k:   # window的长度是j - i + 1, window长度减去max_occur就是需要replace的次数
                ch_to_cnt[s[i]] -= 1
                i += 1
                
            if j - i + 1 - max_occur <= k:
                max_lens = max(max_lens, j - i + 1)
                
        return max_lens
    
"""
需要注意的是，当滑动窗口的左边界向右移动了后，窗口内的相同字母的最大个数貌似可能会改变啊，为啥这里不用更新 max_occur 呢？
这是个好问题，原因是此题让求的是长度为 j - i + 1 的字符串，窗口长度j - i + 1要保证满足j - i + 1 - max_occur <= k，
假设窗口在滑动的过程中 max_occur 变小了，为了满足j - i + 1 - max_occur <= k的条件，j - i + 1 只可能变更小，
所以减小 max_occur 并不会使结果 res 变大，所以我们才不去更新 max_occur 
"""
