1100. Find K-Length Substrings With No Repeated Characters

Given a string S, return the number of substrings of length K with no repeated characters.

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.



"""
Brutal force / sliding window with fixed length: O(26N)
"""
"""
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        freq = collections.defaultdict(int)
        for ch in S[:K]:
            freq[ch] += 1
            
        res = 0
        if len(freq) == K and max(val for val in freq.values()) == 1:
            res += 1 
        
        for i in range(K, len(S)):
            freq[S[i]] += 1
                
            freq[S[i-K]] -= 1
            if freq[S[i-K]] == 0:
                del freq[S[i-K]]
                
            if len(freq) == K and max(val for val in freq.values()) == 1:
                res += 1
                
        return res
        
        
"""
Sliding window O(N): find the substring longer than K that has no repeating chars.
This algorithm works as following:
eg: "abcdcfg" k = 3. 首先i = 0, j 往前走找longer than K的substring，找到了"abcd"，
这时候我们res += 1计入以"a"开头的长度大于K的substring，然后i往前挪一步，这时候得到的是"bcd"，
这时候我们res += 1计入以"b"开头的长度大于K的substring，然后i往前挪一步，这时候得到的是"cd"，
"cd"不满足大于K, 所以我们不做res+=1, i往前挪一步，这时候得到的是"d", 接下来由于S[j] not in included,
我们把S[j]依次加入，变成了"dcfg", 然后重复上面res+1 as i moves foward.
"""
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        included = set()
        j = 0
        res = 0
        for i in range(len(S)):
            while j < len(S) and S[j] not in included:
                included.add(S[j])
                j += 1
            
            if j - i >= K:  # 如果
                res += 1
                
            included.remove(S[i])
            
        return res
