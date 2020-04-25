Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


"""f[i][j]=A前i个字符[0..i)和B前j个字符[0..j)的最小编辑距离
f[i][j]=min{1. f[i-1][j]+1 (f[i-1][j]表示A[0..i-1)就可以拼成B[0..j)了，所以A[0..i)要拼成B[0..j)需要删掉A[0..i)的最后一个字母); 2. f[i][j-1]+1 (B[0..j)需要删掉最后一个字母，即A[0..i)的后面需要增加一个字母); 3. f[i-1][j-1]+1 (A[0..i)的后面需要replace一个字母); 4. f[i-1][j-1] (if A[i-1]=B[j-1] 就不需要任何操作直接就是了)}"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = the min no. of operations to make word1 and word2 the same
        # if word1[i]=word2[j]: then dp[i][j]=dp[i-1][j-1]
        # else: 1. replace a char: dp[i][j] = dp[i-1][j-1]+ 1
        #       2. insert a char in word1: dp[i][j] = dp[i-1][j]+ 1
        #       3. insert a char in word2: dp[i][j] = dp[i][j-1]+ 1
        #       4. delete a char in word1: dp[i][j] = dp[i][j-1]+ 1   same as insert a char in word2
        #       5. delete a char in word2: dp[i][j] = dp[i-1][j]+ 1   same as insert a char in word1
        # dp[0][0] = 0, dp[0][i] = i; dp[i][0]=0
        # return dp[lens1][lens2]
        
        lens1, lens2 = len(word1), len(word2)
        if lens1 == 0:
            return lens2
        if lens2 == 0:
            return lens1
        
        dp = [[max(lens1, lens2)] * (lens2 + 1) for _ in range(lens1 + 1)]  # 注意这里的初始化没有用float("inf")因为会导致数组空间很大？
        for i in range(lens1):
            dp[i][0] = i
        for i in range(lens2):
            dp[0][i] = i
            
        for i in range(1, lens1 + 1):        # 注意点1: 因为有buffer layer, 所以范围是(1, lens1 + 1)
            for j in range(1, lens2 + 1):
                if word1[i - 1] == word2[j - 1]:    # 注意点2: 注意有了buffer layer之后，dp中的i对应的是text中的i-1,所以判断条件是when A[i-1]=B[j-1]
                    dp[i][j] = dp[i - 1][j - 1]    
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    
        return dp[lens1][lens2]
        
        
"""滚动数组空间优化"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lens1, lens2 = len(word1), len(word2)
        dp = [[float("inf")] * (lens2 + 1) for _ in range(2)]
        
        dp[0][0] = 0
        for j in range(1, lens2 + 1):
            dp[0][j] = j
            
        for i in range(1, lens1 + 1):
            dp[i % 2][0] = i
            for j in range(1, lens2 + 1):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1, dp[(i - 1) % 2][j - 1] + 1)
                if word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = min(dp[i % 2][j], dp[(i - 1) % 2][j - 1])
                    
        return dp[lens1 % 2][lens2]
