Given n unique postive integers, number k (1<=k<=n) and target.

Find all possible k integers where their sum is target.

Have you met this question in a real interview?  
Example
Example 1:

Input: [1,2,3,4], k = 2, target = 5
Output:  [[1,4],[2,3]]
Example 2:

Input: [1,3,4,6], k = 3, target = 8
Output:  [[1,3,4]]


"""要求输出所有组合，只能用dfs"""
class Solution:
    def kSumII(self, A, k, target):
        res = []
        if not A:
            return res
            
        A.sort()
        
        self.dfs(A, 0, [], target, k, res)
        
        return res
        
    def dfs(self, A, start, curr, target, k, res):
        if target < 0 or k < 0:
            return
        
        if target == 0 and k == 0:
            res.append(curr.copy())
            return
        
        for i in range(start, len(A)):
            if i >= 1 and A[i] == A[i - 1] and i != start:      # 去重
                continue
            
            curr.append(A[i])
            self.dfs(A, i + 1, curr, target - A[i], k - 1, res)
            curr.pop()
