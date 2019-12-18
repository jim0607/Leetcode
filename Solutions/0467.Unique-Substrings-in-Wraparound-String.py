Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.


"""扫描一边序列，利用动态规划记录到每个字符为止的最长子序列长度。时间复杂度o(n),空间复杂度o(1)
算法：我们看abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd, d，那么我们可以发现bcd或者cd这些以d结尾的字符串的子字符串都包含在abcd中，那么我们知道以某个字符结束的最大字符串包含其他以该字符结束的字符串的所有子字符串，说起来很拗口，但是理解了我上面举的例子就行。"""
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        lensAll = [0] * 26 # 记录到这个字符为止的最长子序列的长度
        lensAll[ord(p[0])-ord("a")] = 1
        lens = 1 # cnt 记录到目前为止的最长子序列的长度
        for i in range(1, len(p)):
            if ord(p[i])-ord(p[i-1]) == 1 or ord(p[i])-ord(p[i-1]) == -25:
                lens += 1
            else:
                lens = 1
            lensAll[ord(p[i])-ord("a")] = max(lens, lensAll[ord(p[i])-ord("a")])
        return sum(lensAll)
