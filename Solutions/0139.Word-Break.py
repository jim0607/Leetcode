"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""



"""
dp[i]=can partition until ith char?, not including i
dp[j]=true if (for i < j, there is dp[i]=True and s[i:j]is in wordDict)
O(n^2)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)    # change to set so check if s[i:j] in word_set is faster
        dp = [False for _ in range(len(s) + 1)]  
        dp[0] = True
        for j in range(len(dp)):
            for i in range(j):    # 反向遍历 s[i:j] in wordSet 就更容易判断更快了！
                if dp[i] and s[i:j] in word_set:  # 这句话应该把dp[i]==True放到前面，因为dp[i]==True is low cost comparison
                    dp[j] = True
                    break
        return dp[-1]
      
      
      
      
"""
solution 2: dfs without memorization - O(2^N)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)    # find if word in the worddict in O(1)
        def dfs(curr_idx):
            if curr_idx == len(s) - 1:
                return True
            for next_idx in range(curr_idx + 1, len(s)):
                if s[curr_idx+1: next_idx+1] in word_set and dfs(next_idx):
                    return True
            return False
        return dfs(-1) 
      
      
      
"""
solution 3: dfs with memorization - O(N^2)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(curr_idx):
            if curr_idx == len(s) - 1:
                return True
            
            if curr_idx in memo:
                return memo[curr_idx]

            res = False
            for next_idx in range(curr_idx + 1, len(s)):
                if s[curr_idx + 1: next_idx + 1] in word_set and dfs(next_idx):
                    res = True
                    break
                        
            memo[curr_idx] = res
            return res
        
        
        word_set = set(wordDict)
        memo = collections.defaultdict(bool) 
        return dfs(-1) 
      

      
      
      
      
      
"""
bfs: next candidate is valid only if it is in the word_set - O(n^2)
"""
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_set= set()
        for word in word_dict:
            word_set.add(word)
            
        lens = len(s)
        q = collections.deque()
        visited = set()     # 必须用一个set记录已经visited的idx, 相当于dp solution中的那个break. 不然就会TLE
        for i in range(lens + 1):
            if s[:i] in word_set:
                q.append((s[:i], i))
                visited.add(i)
                
        while q:
            curr_word, curr_idx = q.popleft()   # 其实可以不用append curr_word, 后面根本用不到。
            if curr_idx == lens:
                return True
    
            for i in range(curr_idx + 1, lens + 1):
                next_word = s[curr_idx:i]
                if next_word in word_set and i not in visited:
                    q.append((next_word, i))
                    visited.add(i)
                    
        return False
      
      
"""
dfs: 只消把bfs中的q.popleft改成q.pop就变成了dfs了 - O(n^2)
"""
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_set= set()
        for word in word_dict:
            word_set.add(word)
            
        lens = len(s)
        q = collections.deque()
        visited = set()     # 必须用一个set记录已经visited的idx, 相当于dp solution中的那个break. 不然就会TLE
        for i in range(lens + 1):
            if s[:i] in word_set:
                q.append((s[:i], i))
                visited.add(i)
                
        while q:
            curr_word, curr_idx = q.pop()
            if curr_idx == lens:
                return True
    
            for i in range(curr_idx + 1, lens + 1):
                next_word = s[curr_idx:i]
                if next_word in word_set and i not in visited:
                    q.append((next_word, i))
                    visited.add(i)
                    
        return False

      
      
"""
dfs: recurssively = bottum up DP - O(n^2)
"""
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_set= set()
        for word in word_dict:
            word_set.add(word)
            
        lens = len(s)
        memo = collections.defaultdict()
            
        def dfs(curr_idx, curr_word):
            if curr_idx == lens:
                return True
            
            if curr_idx in memo:
                return memo[curr_idx]
            
            for i in range(curr_idx + 1, lens + 1):
                next_word = s[curr_idx:i]
                if next_word in word_set:
                    if dfs(i, next_word):
                        memo[curr_idx] = True
                        return True
                
            memo[curr_idx] = False
            return memo[curr_idx]
        
        return dfs(0, "")
      
      
"""
dfs: recurssively - 简化一点，不用传入curr_word
"""
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_set= set()
        for word in word_dict:
            word_set.add(word)
            
        lens = len(s)
        memo = collections.defaultdict()
            
        def dfs(curr_idx):
            if curr_idx == lens:
                return True
            
            if curr_idx in memo:
                return memo[curr_idx]
            
            for i in range(curr_idx + 1, lens + 1):
                next_word = s[curr_idx:i]
                if next_word in word_set:
                    if dfs(i):
                        memo[curr_idx] = True
                        return True
                
            memo[curr_idx] = False
            return memo[curr_idx]
        
        return dfs(0)
      
