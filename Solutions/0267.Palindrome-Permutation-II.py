266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charFreq = collections.defaultdict(int)
        for char in s:
            charFreq[char] += 1
            
        cnt = 0
        for char, freq in charFreq.items():
            if freq % 2 == 1:
                cnt += 1
            
            if cnt > 1:
                return False
        
        return True


    
267. Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []

    
O(N*N!)
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if not self.canPermutePalindrome(s):
            return False
        
        s = sorted(s)    # 去重需要先sort, string 不能用s.sorted()来sort
        
        res = []
        visited = {i: False for i in range(len(s))}
        self.dfs(s, [], res, visited)
        
        return res
    
    def dfs(self, s, curr, res, visited):
        if len(curr) == len(s) and self.isPalin("".join(curr)):
            res.append("".join(curr.copy()))
            return
        
        for i in range(len(s)):
            if visited[i] or (i >= 1 and s[i] == s[i -1] and not visited[i - 1]):   # 注意需要去重
                continue
            
            curr.append(s[i])
            visited[i] = True
            self.dfs(s, curr, res, visited)
            curr.pop()
            visited[i] = False
            
    def isPalin(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True
    
    
    def canPermutePalindrome(self, s: str) -> bool:
        charFreq = collections.defaultdict(int)
        for char in s:
            charFreq[char] += 1
            
        cnt = 0
        for char, freq in charFreq.items():
            if freq % 2 == 1:
                cnt += 1
            
            if cnt > 1:
                return False
        
        return True
