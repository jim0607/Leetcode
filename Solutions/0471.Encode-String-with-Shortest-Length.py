"""
471. Encode String with Shortest Length

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
 
Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
 
Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
 
Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 
Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
 
Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
"""



"""
dp[i][j] is the encode of substring including index i to index j.
dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j], potential_candidate) in terms of length.
potential_candidate = "k[repeating_pattern]", 
where pattern is the repeating string in substring s[i:j+1] and k is the number of repeating times.

initializaton: dp[i][j] = s[i:j+1] originally
return dp[0][n-1]
O(N^3)
"""
class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [["" for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                substr = s[i:j+1]
                dp[i][j] = substr       # initialization
                if j - i >= 4:          # 如果长度小于5的话就没有必要进行压缩了
                    for k in range(i, j):
                        if len(dp[i][k] + dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
                    
                    # Next: find the posible compression for s. eg: "aabcdaabcd" --> "2[aabcd]"
                    # algorithm: step 1: double the string "aabcdaabcdaabcdaabcd";
                    # step 2: start from idx 1, get the idx for the first s in the doubled string, in this eg: idx = 5.
                    double_s = substr + substr
                    repeat_idx = double_s.index(substr, 1)      # start from idx 1, find the position of substr in double_s
                    repeat_time = len(substr) // repeat_idx
                    candidate = str(repeat_time) + "[" + dp[i][i+repeat_idx-1] + "]"  # 注意这里repeated pattern是dp[i:i+repeat_idx-1]
                    if len(candidate) < len(dp[i][j]):
                        dp[i][j] = candidate
                        
        return dp[0][n-1]
        
        
"""
如果substr是重复的，是不是就不需要再看len(dp[i][k] + dp[k+1][j]) < len(dp[i][j])了。
例如substr是abcabcabcabcabc, 最终肯定是5[abc]，不需要再看3[abc]+abcabc或者abcabc+3[abc]。
对于一个本身就重复的字符串，最小的长度肯定是n[REPEATED]，不会是某个left+right。
所以应该把k的那个循环放在t和replace那部分代码的后面。这样的确提高了一些运算效率的
"""
class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [["" for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                substr = s[i:j+1]
                dp[i][j] = substr       # initialization
                if j - i >= 4:          # 如果长度小于5的话就没有必要进行压缩了
                    
                    # Next: find the posible compression for s. eg: "aabcdaabcd" --> "2[aabcd]"
                    # algorithm: step 1: double the string "aabcdaabcdaabcdaabcd";
                    # step 2: start from idx 1, get the idx for the first s in the doubled string, in this eg: idx = 5.
                    double_s = substr + substr
                    repeat_idx = double_s.index(substr, 1)      # start from idx 1, find the position of substr in double_s
                    repeat_time = len(substr) // repeat_idx
                    candidate = str(repeat_time) + "[" + dp[i][i+repeat_idx-1] + "]"  # 注意这里repeated pattern是dp[i:i+repeat_idx-1]
                    if len(candidate) < len(dp[i][j]):
                        dp[i][j] = candidate
                        continue        # 可以直接continue掉后面的for k in range(i, j)循环，从而提高效率
                        
                    for k in range(i, j):
                        if len(dp[i][k] + dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
                        
        return dp[0][n-1]
