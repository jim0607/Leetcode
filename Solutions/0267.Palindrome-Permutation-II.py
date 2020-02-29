Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
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
