77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self._backtrack(n, k, 0, [], res)
        return res
    
    def _backtrack(self, n, k, idx, curr, res):
        if len(curr) == k:
            res.append(curr.copy())
            return
            
        for i in range(idx + 1, n + 1):
            curr.append(i)
            self._backtrack(n, k, i, curr, res)
            curr.pop()
