"""
1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(curr_idx, curr_comb):
            self.maxlens = max(self.maxlens, len(curr_comb))
            
            for next_idx in range(curr_idx + 1, len(arr)):  # 一个string只能取一次，所以从curr_idx+1开始
                next_comb = curr_comb + arr[next_idx]
                if is_unique(next_comb):
                    backtrack(next_idx, next_comb)  
                    
        
        def is_unique(s):
            cnter = Counter(s)
            for cnt in cnter.values():
                if cnt > 1:
                    return False
            return True

                
        self.maxlens = 0
        backtrack(-1, "")
        return self.maxlens
    

    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(curr_idx, curr_comb):
            res.append("".join(curr_comb.copy()))
            for next_idx in range(curr_idx + 1, len(lst)):      # 一个string只能取一次，所以从curr_idx+1开始
                if next_idx > 0 and lst[next_idx] == lst[next_idx-1] and next_idx - 1 != curr_idx:
                    continue
                if has_same_char(lst[next_idx], curr_comb):
                    continue
                curr_comb.append(lst[next_idx])
                backtrack(next_idx, curr_comb)
                curr_comb.pop()
                
        def has_same_char(s, comb):
            set_s = set([ch for ch in s])
            for string in comb:
                for ch in string:
                    if ch in set_s:
                        return True
            return False        
        
        
        # step 1: remove the invalid strings in arr
        lst = []
        for s in arr:
            if len(s) == len(set([ch for ch in s])):
                 lst.append(s)
        lst = sorted(lst)   # 去重第一步
                    
        # step 2: backtrack to find all combinations
        res = []
        backtrack(-1, [])
        return max(len(comb) for comb in res) 
    
    
    
    
    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # step 1: remove the invalid strings in arr
        lst = []
        for s in arr:
            if len(s) == len(set([ch for ch in s])):    # a string is invalid if it contains duplicates
                lst.append(s)
        
        # step 2: backtrack to find the combinations
        lst.sort()      # 去重第一步
        res = [""]
        visited = set()
        self._backtrack(lst, -1, [], res, visited)
        return max(len(s) for s in res)     # 其实也没有必要输出所有的res, 只需要用一个global viraiable max_lens去_backtrack 函数中打擂台即可

    def _backtrack(self, lst, curr_idx, curr_path, res, visited):
        res.append("".join(curr_path.copy()))   # 注意这里是subset问题，不需要idx == lens的判断 
        
        for next_idx in range(curr_idx + 1, len(lst)):
            if (next_idx > 0 and lst[next_idx] == lst[next_idx-1]) and lst[next_idx] not in visited:
                continue
            if not self._is_valid(lst[next_idx], curr_path):
                continue
            visited.add(lst[next_idx])
            curr_path.append(lst[next_idx])
            self._backtrack(lst, next_idx, curr_path, res, visited)
            visited.remove(lst[next_idx])
            curr_path.pop()
    
    def _is_valid(self, s, lst):    # helper 函数判断next_idx是不是valid
        for string in lst:
            for ch in string:
                for c in s:
                    if ch == c:
                        return False
        return True
