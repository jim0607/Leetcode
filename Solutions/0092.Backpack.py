92. Backpack

Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

You can not divide any item into small pieces.
 
Example
Example 1:
	Input:  [3,4,8,5], backpack size=10
	Output:  9



"""空间优化
dp[i][m]至于dp[i-1][...]有关，所以可以采用滚动数组的方法优化空间"""
class Solution:
    def backPack(self, M, A):
        lens = len(A)
        dp = [[False] * (M + 1) for _ in range(lens + 1)]
        
        for i in range(lens + 1):
            
            dp[i][0] = True
            
            if i == 0:
                for m in range(1, M + 1):
                    dp[i][m] = False
                    
                continue
            
            for m in range(1, M + 1):
                if m >= A[i - 1]:
                    dp[i][m] = dp[i - 1][m] or dp[i - 1][m - A[i-1]]
                else:
                    dp[i][m] = dp[i - 1][m]
                    
        for m in range(M, -1, -1):
            if dp[lens][m]:
                return m
                
        return 0
        
        
        
        
"""空间优化
dp[i][m]至于dp[i-1][...]有关，所以可以采用滚动数组的方法优化空间"""
class Solution:
    def backPack(self, M, A):
        lens = len(A)
        dp = [[False] * (M + 1) for _ in range(2)]
        
        for i in range(lens + 1):
            
            dp[i % 2][0] = True
            
            if i == 0:
                for m in range(1, M + 1):
                    dp[i][m] = False
                    
                continue
            
            for m in range(1, M + 1):
                if m >= A[i - 1]:
                    dp[i % 2][m] = dp[(i - 1) % 2][m] or dp[(i - 1) % 2][m - A[i-1]]
                else:
                    dp[i % 2][m] = dp[(i - 1) % 2][m]
                    
        for m in range(M, -1, -1):
            if dp[lens % 2][m]:
                return m
                
        return 0
