92. Backpack

Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

You can not divide any item into small pieces.
 
Example
Example 1:
	Input:  [3,4,8,5], backpack size=10
	Output:  9



"""dp[i][m]表示前i个石头(不包括i)能否承重m
dp[i][m] = True if dp[i-1][m] for dp[i-1][m-A[i-1]]"""
"""
dp[i][m]=can make up m with the 1st i num?
dp[i][m]=d[i-1][m] or dp[i-1][m-A[i]]
dp[i][0]=True
"""
class Solution:
    def backPack(self, size, nums):
        lens = len(nums)
        if lens == 0:
            return 0
            
        dp = [[False for _ in range(size + 1)] for _ in range(lens + 1)]    # 注意点1：这里要定义lens+1，这样就可以做一个buffer layer出来了
        for i in range(lens + 1):
            dp[i][0] = True
            
        for i in range(1, lens + 1):    # 注意点2；这里循环i在外面，m在里面，千万别搞反了！！！！！！！！！！
            for m in range(1, size + 1):
                dp[i][m] = dp[i - 1][m]
                
                if m >= nums[i - 1]:    # 注意点3：由于buffer layer的存在，这里用nums[i-1]
                    dp[i][m] = dp[i][m] or dp[i - 1][m - nums[i - 1]]
                    
        for m in range(size, -1, -1):
            if dp[lens][m]:
                return m
        
        
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



"""
以下算法不对因为我们不能一个物品取两次
"""
class Solution:
    def backPack(self, m, nums):
        lens = len(nums)
        if lens == 0:
            return 0
            
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        
        for k in range(m + 1):
            for num in nums:
                if k >= num and dp[k - num]:
                    dp[k] = True
                    break
                
        for k in range(m, -1, -1):
            if dp[k]:
                return k
