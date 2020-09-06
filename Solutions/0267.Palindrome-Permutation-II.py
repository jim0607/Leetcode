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

    
O(N*N!), N is for checking isPalin, N! is the number of solutions.  This solution TLE
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


    
"""
After examing 266, we can get the following solution:
say if we have a string "aabbcc", we only need to find all the permutations for "abc", then return all the permutations + permutation[::-1]
in this way the time complexity is O((N/2)!)
"""    


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:       
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(even_chars):
                res.append("".join(curr_comb.copy()))
                return
            for next_idx in range(len(even_chars)):
                if next_idx in visited:
                    continue
                if next_idx > 0 and even_chars[next_idx] == even_chars[next_idx-1] and next_idx - 1 not in visited:
                    continue            # 去重
                visited.add(next_idx)
                curr_comb.append(even_chars[next_idx])
                backtrack(next_idx, curr_comb)
                visited.remove(next_idx)
                curr_comb.pop()
        
        # step 1: pre-cessing: "aaabbbbcc" --> "abbc"
        res = []
        counter = collections.Counter(s)
        cnt = 0             # cnt of ch that appear only once
        even_chars = ""     # stores the chars that appear even times 
        only_once = ""      # store the char that appear only once
        for ch, freq in counter.items():
            if freq % 2 == 1:
                even_chars += ch * (freq // 2)      # "aaabb" --> "ab"
                only_once = ch
                cnt += 1
            else:
                even_chars += ch * (freq // 2)       # "aaaabb" --> "aab"
        if cnt > 1:
            return res
        
        # step 2: bachtrack for "abbc" and find all it's permutations
        even_chars = sorted(even_chars)     # 去重第一步 - sort
        visited = set()
        backtrack(0, [])
        
        # step 3: re-construct the pandlindrome using the generated permutations
        ans = []
        for comb in res:
            ans.append(comb + only_once + comb[::-1])
        return ans      












class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # step 1: put the characters that have seen two times in the char list
        charList = []
        charSet = set()
        for ch in s:
            if ch in charSet:
                charList.append(ch)
                charSet.remove(ch)
            else:
                charSet.add(ch)
                
        # now we have a charList that only holds char that appears two times, eg: "aaaabbc" now becomes "aab"
        # next we only need to do permutation for this charList
        # so the time complexity is O((n/2)!), which is quite an improve
                
        # if there are more than one char that appears odd times, then directly return []
        if len(charSet) > 1:
            return []
        
        # step 2: do a normal backtracking to find permutation of charList
        charList = sorted(charList)     # sort the list to avoid duplicates
        self.res = []
        self.visited = set()
        self.backtracking(charList, [])

        # step 3: when return the results, we just use the permuation generated in steps 2 + permuation[::-1]
        if len(charSet) == 0:
            return [permutation + permutation[::-1] for permutation in self.res]

        if len(charSet) == 1:
            midChar = charSet.pop()
            return [permutation + midChar + permutation[::-1] for permutation in self.res]
        
        
    def backtracking(self, charList, curr):
        if len(curr) == len(charList):
            self.res.append("".join(curr.copy()))   # always forgot has to be a deep copy
            return
        
        for i in range(len(charList)):
            if i in self.visited:
                continue
            if (i >= 1 and charList[i] == charList[i-1]) and (i-1) not in self.visited:    # avoid duplicates
                continue
            
            curr.append(charList[i])
            self.visited.add(i)
            self.backtracking(charList, curr)
            curr.pop()
            self.visited.remove(i)
