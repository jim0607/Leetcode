# [Dynamic Programming](Dynamic-Programming.py)
- [0322. Coin Change](Solutions/0322.Coin-Change.py) (!!M) <br>
最小值问题。状态: f[X]=最少用多少枚硬币拼出X; 转移方程：f[X] = min(f[X-2]+1, f[X-5]+1, f[X-7]+1)
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (!!M) <br>
存在性问题。状态: dp[j]=能不能跳到位置j; 转移方程：dp[j]=True if dp[i] and i+nums[i]>=j) (TLE)
- [0152. Maximum Product Subarray](Solutions/0152.Maximum-Product-Subarray.py) (M) <br>
最大值问题。用一个数组记录最大的正数maxDP[i]，另一个数组记录最小的负数minDP[i], maxDP[i] = max(nums[i], maxDP[i-1]*nums[i]) if nums[i]>0

### [坐标型DP](/Dynamic-Programming.py)
- [0062. Unique Paths](Solutions/0062.Unique-Paths.py) (!!M) <br>
状态: f[i][j]=有多少种方式从左上角走到(i, j); 转移方程：f[i][j] = f[i][j-1]+f[i-1][j]
- [0063. Unique Paths II](Solutions/0063.Unique-Paths-II.py) (M) <br> 
转移方程：f[i][j] = 0 if it is obstacle else f[i][j-1]+f[i-1][j])
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (M) <br> 
dp[i][j]=the minimum path sum to (i, j); dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j])
- [0120. Triangle](Solutions/0120.Triangle.py) (M) <br>
dp[i][j] = min(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1])
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M) <br>
dp[i][j]=以(i, j)为右下角的最大正方形的边长; dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j]=1 

### [序列型DP](/Dynamic-Programming.py)
- [0256. Paint House](Solutions/0256.Paint-House.py) (E) <br>
dp[i][j] means the minimum cost to paint house i to be color j; dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
- [0265. Paint House II](Solutions/0265.Paint-House-II.py) (E) <br> 
dp[i][j]=minimum cost to paint the ith house the be color j; dp[i][j] = tempMin + costs[i][j])
- [0198. House Robber](Solutions/0198.House-Robber.py) (E) <br>
f[i]=the max profit when reaching ith house; f[i] = max(rob ith = f[i-2]+nums[i], not rob ith = f[i-1]) <br>
空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]
- [0213. House Robber II](Solutions/0213.House-Robber-II.py) (E) <br>
房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：1. 房子1没偷：问题变成了对房子2:N做House robber I的问题; 2. 房子N没偷：问题变成了对房子1:N-1做House robber I的问题

### [Buy and sell stock DP问题](/Dynamic-Programming.py)
- [0121. Best Time to Buy and Sell Stock](Solutions/0121.Best-Time-to-Buy-and-Sell-Stock.py) (E) <br>
Only one transaction is allowed.  Maintain a minPrice and a maxProfit; maxProfit = max(maxProfit, price - minPrice)
- [0122. Best Time to Buy and Sell Stock II](Solutions/0122.Best-Time-to-Buy-and-Sell-Stock-II.py) (E) <br>
As many transaction as possible.  make a transaction every time price[i]>price[i-1]
- [0123. Best Time to Buy and Sell Stock III](Solutions/0123.Best-Time-to-Buy-and-Sell-Stock-III.py) (H) <br>
Only two transactions are allowed.  Maintain buy1=the minimum money you can own after the first buy, sell1=the maximum money you can earn after the first sell, also, buy2, sell2, and update them together in a for loop
- [0188. Best Time to Buy and Sell Stock IV](Solutions/0188.Best-Time-to-Buy-and-Sell-Stock-IV.py) (H) <br>
Only k transactions are allowed.   Maintain buy=[]*k, sell=[]*k, and update them together in a for loop
- [0309. Best Time to Buy and Sell Stock with Cooldown](Solutions/0309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py) (M) <br>
Has to rest for one day before buy another stock.  **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益 <br>
hold[i] = max(hold[i-1], unhold[**i-2**]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i])
- [0714. Best Time to Buy and Sell Stock with Transaction Fee](Solutions/0714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) (M) <br>
There is transaction fee when you sell. **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益 <br>
hold[i] = max(hold[i-1], unhold[i-1]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i] **- fee**)

###  [最长子序列问题](/Dynamic-Programming.py)
- [0674. Longest Continuous Increasing Subsequence](Solutions/0674.Longest-Continuous-Increasing-Subsequence.py) (E) <br>
dp[i] = 以i结尾(包括i)的最长连续子序列; dp[i] = dp[i-1] + 1 if nums[i]>nums[i-1]
- [0300. Longest Increasing Subsequence](Solutions/0300.Longest-Increasing-Subsequence.py) (!!M) <br>
不需要连续，所以不是dp[i] = dp[i-1] + 1，而是所有的j之前的i都有可能, 所以转移方程是 dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]); 还需要掌握dp + binary search (O(NlogN))
- [0673. Number of Longest Increasing Subsequence](Solutions/0673.Number-of-Longest-Increasing-Subsequence.py) (M) <br>
 dp=以i为结尾的最大的长度; cnt=以i为结尾的最大的长度的个数; cnt[j]+=cnt[i] if dp[j]=dp[i]+1
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.Longest-Arithmetic-Sequence.py) (M) <br>
dp[i][j]=以i结尾的等差数列且以j为公差的长度; dp = [collections.defaultdict(lambda: 1) for _ in range(lens)]
- [0873. Length of Longest Fibonacci Subsequence](Solutions/0873.Length-of-Longest-Fibonacci-Subsequence.py) (M) <br>
dp[i][j]=以i, j为最后两个数字的fib的长度; dp[j][index of (A[i]+A[j])]=dp[i][j]+1; index of (A[i]+A[j])是(A[i]+A[j])在A中的位置，为了快速找到index of (A[i]+A[j])，用一个dict存储索引即可
- [0354. Russian Doll Envelopes](Solutions/0354.Russian-Doll-Envelopes) (M) <br>
Similiar with 300. LIS; here we not only compare nums[j]>nums[i], but instead both the width and height; TLE, should learn how to do 300. LIS using DP+binary search (O(NlogN))
- [0334. Increasing Triplet Subsequence](Solutions/0334.Increasing-Triplet-Subsequence.py) (M) <br>
Similiar with 300. LIS; dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]); if dp[j]>=3 return True

### [区间型DP](/Dynamic-Programming.py)
- [0005. Longest Palindromic Substring](Solutions/0005.Longest-Palindromic-Substring.py) (!!M) <br>
Return the longest substr: dp[i][j]=from i to j (including j), is it a palindr? if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]): dp[i][j]=True; 注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i，所以i is from (j, 0)
- [0516. Longest Palindromic Subsequence](Solutions/0516.Longest-Palindromic-Subsequence.py) (!!M) <br>
Return the longest length: dp[i][j]=longest palindr from i to j; dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1]);注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i，所以i is from (j, 0)
- [0312. Burst Balloons](Solutions/0312.Burst-Balloons.py) (H) <br>
带memo的recursion比DP更好懂; left = self.memoSearch(nums, i, k, memo); right=self.memoSearch(nums, k, j, memo); maxCoins = max(maxCoins, left + right + nums[i]*nums[k]*nums[j])

###  [划分型DP](/Dynamic-Programming.py)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M) <br>
f[i]=number of decode ways until i; f[i]=f[i-1]+f[i-2] if int(s[i-1:i+1])<=26 else f[i-1]
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (M) <br>
f[i]=the least number of perfect square numbers which sum to i; f[j] = min(f[j-i^2]+1) for i^2<=j; Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5)
- [0132. Palindrome Partitioning II](Solutions/0132.Palindrome-Partitioning-II.py) (!!M) <br>
f[j]=the minimum number of total palindrome till the jth character (not including j); f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome： 划分型的dp的状态一般都not include j, 这样就有一个buffer layer可以用。

### [博弈型DP](/Dynamic-Programming.py)
- [0394. Coins in a Line](Solutions/0394.Coins-in-a-Line.py) (M) <br>
f[i]=面对i个石子，先手是必胜吗; f[i]=True if f[i-1] or f[i-2]都是False
- [0486. Predict the Winner](Solutions/0486.Predict-the-Winner.py) (M) <br>
f[i][j]=当石子还剩i到j时，先手最多能赢多少; f[i][j] = max(取左边A[i]-f[i+1][j], 取右边A[j]-f[i][j-1])

### [背包型DP](/Dynamic-Programming.py)
- [0092. Backpack](Solutions/0092.Backpack.py) (!!M Lintcode) <br>
f[i][m]=能否用前i个物品拼出重量m; f[i][m] = f[i-1][m] (表示前i-1个物品就可以拼出m) or f[i-1][m-A[i-1]] (表示前i-1个物品可以拼出m-A[i-1])
- [0563. Backpack-V](Solutions/0563.Backpack-V.py) (!!M Lintcode) <br>
f[i][m]=前i个物品能拼出重量m有多少种方式。f[i][m] = f[i-1][m] + f[i-1][m-A[i-1]]
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (!!M Lintcode) <br>
f[i]=how many ways to combine to number i; 背包问题一定要把总承重放到状态里！！ f[i]=f[i-A1]+f[i-A2]+f[i-A3].... <br>
- [0125. Backpack II](Solutions/0125.Backpack-II.py) (!!M Lintcode) <br>
这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。用子问题定义状态：即f[i][j]表示前i件物品拼出重量j可以获得的最大价值。
f[i][j]=max{f[i-1][j] (不放入),f[i-1][j-A[i]]+V[i] (放入)}; return f[lens-1][M]
- [0089. k Sum](Solutions/0089.k-Sum.py) (M Lintcode) <br>
f[i][j][s]表示有多少种方法可以在前i个数中选出j个，使得它们的和是s; 情况一:（A[n-1]不选入）：需要在前n-1个数中选K个数，使得它们的和是Target: f[i][j][s] += f[i-1][j][s]; 情况二（A[n-1]选入）：需要在前n-1个数中选K-1个数，使得它们的和是Target-A[n-1]: f[i][j][s] += f[i-1][j-1][s-A[i-1]]
- [0416. Partition Equal Subset Sum](Solutions/0416.Partition-Equal-Subset-Sum.py) (M) <br>
背包问题：将A中的物品放入容量为target的背包中，问是否存在？ f[i]=将前i个物品放入背包中，能否拼出t (背包问题重量一定要入状态); f[i][t]=True if 不放最后一个进背包: f[i-1][t]=True or 放最后一个进背包: f[i-1][t-A[i-1]]=True

### [位操作型DP](/Dynamic-Programming.py)
- [0338. Counting Bits](Solutions/0338.Counting-Bits.py) (M) <br>
状态f[i]=i的二进制中有多少个1; dp[i] = dp[i >> 1] + i % 2

### [双序列型DP](/Dynamic-Programming.py)
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (!!M) <br>
f[i][j]为A前i个字符A[0..i)和B前j个字符[0..j)的最长公共子串的长度，注意不包括i和j，前面有一层buffer layer非常重要，就像sputtering那样重要！ f[i][j]=max(f[i][j-1], f[i-1][j], f[i-1][j-1] when A[i-1]=B[j-1])
- [0097. Interleaving String](Solutions/0097.Interleaving-String.py) (!!H) <br>
f[i][j]=s3的前[0..i+j)个字符能否由s1前i个字符[0..i)和s2前j个字符[0..j)交错形成; f[i][j]=True when (s3[i+j-1]=s1[i-1] 且 f[i-1][j]=True 即s3的前[0..i+j-1)个字符能否由s1前i-1个字符[0..i-1)和s2前j个字符[0..j)交错形成) or (s3[i+j-1]=s2[j-1] and f[i][j-1]=True)
- [0072. Edit Distance](Solutions/0072.Edit-Distance.py) (!!H) <br>
f[i][j]=A前i个字符[0..i)和B前j个字符[0..j)的最小编辑距离; f[i][j]=min{1. f[i-1][j]+1 (f[i-1][j]表示A[0..i-1)就可以拼成B[0..j)了，所以A[0..i)要拼成B[0..j)需要删掉A[0..i)的最后一个字母); 2. f[i][j-1]+1 (B[0..j)需要删掉最后一个字母，即A[0..i)的后面需要增加一个字母); 3. f[i-1][j-1]+1 (A[0..i)的后面需要replace一个字母); 4. f[i-1][j-1] (if A[i-1]=B[j-1] 就不需要任何操作直接就是了)}
- [0115. Distinct Subsequences](Solutions/0115.Distinct-Subsequences.py) (H) <br>
f[i][j]=B前i个字符B[0..i)在A前j个字符A[0..j)中出现多少次; f[i][j] += f[i][j-1] if B[i-1]!=A[j-1] else += f[i-1][j-1] + f[i][j-1] 
- [0044. Wildcard Matching](Solutions/0044.Wildcard-Matching.py) (H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配； 画个图会很明了，详见九章算法动态规划双序列型DP。
情况一：B[j-1]不是"星": f[i][j] = f[i-1][j-1] if (B[j-1]="?" or A[i-1]=B[j-1])
情况二：B[j-1]是"星"：可以让"*"表示0个字符，那就让A[0..i)去和B[0..j-1)匹配： f[i][j] = f[i][j-1]；也可以让"星"表示字符，A[i-1]肯定是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j]
- [0010. Regular Expression Matching](Solutions/0010.Regular-Expression-Matching.py) (!!H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配; 情况一：B[j-1]不是"星": f[i][j] = f[i-1][j-1] if (B[j-1]="." or A[i-1]=B[j-1]); 情况二：B[j-1]是"星"：可以让"星"表示0个前面的字符，那就让A[0..i)去和B[0..j-2)匹配： f[i][j] = f[i][j-2]；也可以让"星"表示几个前面的字符，A[i-1]是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j] if (B[j-2]="." or B[j-2]=A[i-1])




### [Other DP Problems](https://juejin.im/post/5d556b7ef265da03aa2568d5)
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M)
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (M)
- [0718. Maximum Length of Repeated Subarray](Solutions/0718.Maximum-Length-of-Repeated-Subarray.py) (M)
- [1049. Last Stone Weight II](Solutions/1049.Last-Stone-Weight-II.py) (M)
- [1024. Video Stitching](Solutions/1024.Video-Stitching.py) (M)
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
- [0983. Minimum Cost For Tickets](Solutions/0983.Minimum-Cost-For-Tickets.py) (M)
- [0688. Knight Probability in Chessboard](Solutions/0688.Knight-Probability-in-Chessboard.py) (M)
- [0361. Bomb Enemy](Solutions/0361.Bomb-Enemy.py) (M)
- [0467. Unique Substrings in Wraparound String](Solutions/0467.Unique-Substrings-in-Wraparound-String.py) (M)
- [0898. Bitwise ORs of Subarrays](Solutions/0898.Bitwise-ORs-of-Subarrays.py) (M)
- [0343. Integer Break](Solutions/0343.Integer-Break.py) (M)
- [1223. Dice Roll Simulation](Solutions/1223.Dice-Roll-Simulation.py) (M)
- [1105. Filling Bookcase Shelves](Solutions/1105.Filling-Bookcase-Shelves.py) (M)
- [0464. Can I Win](Solutions/0464.Can-I-Win.py) (M)


# [Data Structure](/Data-Structure.py)
### [Stack and Queue](/Data-Structure.py)
- [0232. Implement Queue using Stacks](Solutions/0232.Implement-Queue-using-Stacks.py) (E) 
- [0225. Implement Stack using Queues](Solutions/0225.Implement-Stack-using-Queues.py) (E) 
- [0155. Min Stack](Solutions/0155.Min-Stack.py) (!!E) 
- [0716 (没搞懂！)] (E) 
- [0394. Decode String](Solutions/0394.Decode-String.py) (M) 
#### [Iterator](/Data-Structure.py)
- [0341. Flatten Nested List Iterator](Solutions/0341.Flatten-Nested-List-Iterator.py) (M) 
- [0251. Flatten 2D Vector](Solutions/0251.Flatten-2D-Vector.py) (M)
- [0281. Zigzag Iterator](Solutions/0281.Zigzag-Iterator.py) (M)
- [0284. Peeking Iterator](Solutions/0284.Peeking-Iterator.py) (M)
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (M)
#### [单调栈](/Data-Structure.py)
84. Largest Rectangle in Histogram  (H) (should understand later)


### [Hashmap/Dictionary](/Data-Structure.py)
- [0146. LRU Cache](Solutions/0146.LRU-Cache.py) (!!M)


### [Heap/Heapq](/Data-Structure.py)
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M)
- [0347. Top K Frequent Elements](Solutions/0347.Top-K-Frequent-Elements.py) (M)
- [0253. Meeting Rooms II](Solutions/00253.Meeting-Rooms-II.py) (!!M) (以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间)
- [0973. K Closest Points to Origin](Solutions/0973.K-Closest-Points-to-Origin.py) (M) （以squre来构建heap就可以了，heap中的元素是(square, point)）
- [0378. Kth Smallest Element in a Sorted Matrix](Solutions/0378.Kth-Smallest-Element-in-a-Sorted-Matrix.py) (M)
- [0264. Ugly Number II](Solutions/0264.Ugly-Number-II.py) (M)


# [Two Sum]()
- [0001. Two Sum](Solutions/0001.Two-Sum.py) (E) 
- [0167. Two Sum II - Input array is sorted](Solutions/0167.Two-Sum-II-Input-array-is-sorted.py) (E)
- [0170. Two Sum III - Data structure design](Solutions/0170.Two-Sum-III-Data-structure-design.py) (E)
- [0653. Two Sum IV - Input is a BST](Solutions/0653.Two-Sum-IV-Input-is-a-BST.py) (E)
- [1099. Two Sum Less Than K](Solutions/1099.Two-Sum-Less-Than-K.py) (E) 
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) (求和用反向双指针，求差用同向双指针)
- [0609. Two Sum - Less than or equal to target](Solutions/0609.Two-Sum-Less-than-or-equal-to-target.py) (E) 
- [0015. 3Sum](Solutions/0015.3Sum.py) (!!M) 
- [0016. 3Sum Closest](Solutions/0016.3Sum-Closest.py) (M) 
- [0259. 3Sum Smaller](Solutions/0259.3Sum-Smaller.py) (M) 
- [0018. 4Sum](Solutions/0018.4Sum.py) (M) 
- [0454. 4Sum II](Solutions/0454.4Sum-II.py) (M) 


# [Two Pointers](/Two-pointers.py)
### [反向双指针](/Two-pointers.py)
- [0977. Squares of a Sorted Array](Solutions/0977.Squares-of-a-Sorted-Array.py) (E) 
### Partition(/Two-pointers.py)
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode)
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E)
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) (三根指针partition成三个部分)
- [0561. Array Partition I](Solutions/0561.Array-Partition-I.py) (E) 

### [同向双指针](/Two-pointers.py)
- [0283. Move Zeroes](Solutions/0283.Move-Zeroes.py) (E) 
- [0026. Remove Duplicates from Sorted Array](Solutions/0026.Remove-Duplicates-from-Sorted-Array.py) (E) 
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) 

# [Sorted Array]() 
- [0088. Merge Sorted Array](Solutions/0088.Merge-Sorted-Array.py) (E) 
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M) (quick select) 
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) (Binary search) 

# [SubArray](/SubArray.py)
- [0053. Maximum Subarray](Solutions/0053.Maximum-Subarray.py) (！！E) (前缀和prefixSum)
- [0724. Find Pivot Index](Solutions/0724.Find-Pivot-Index.py) (E) (prefixSum)
- [0560. Subarray Sum Equals K](Solutions/0560.Subarray-Sum-Equals-K.py) (!!M) (prefixSum+hashmap)
- [0523. Continuous Subarray Sum](Solutions/0523.Continuous-Subarray-Sum.py) (M) (prefixSum+hashmap)
- [0974. Subarray Sums Divisible by K](Solutions/0974.Subarray-Sums-Divisible-by-K.py) (M) (prefixSum+hashmap)
- [0139. Subarray Sum Closest](Solutions/0139.Subarray-Sum-Closest.py) (Lintcode) (prefixSum+hashmap)

# [Linked List](/Linked-List)
- [0148. Sort List](Solutions/0148.Sort-List.py) (！！M)
- [0206. Reverse Linked List](Solutions/0206.Reverse-Linked-List.py) (！！E) (需要熟背理解)
- [0092. Reverse Linked List II](Solutions/0092.Reverse-Linked-List-II.py) (M)
- [0024. Swap Nodes in Pairs](Solutions/0024.Swap-Nodes-in-Pairs.py) (M)
- [0025. Reverse Nodes in k-Group](Solutions/0025.Reverse-Nodes-in-k-Group.py) (H)
- [0138. Copy List with Random Pointer](Solutions/0138.Copy-List-with-Random-Pointer.py) (M)
- [0141. Linked List Cycle](Solutions/0141.Linked-List-Cycle.py) (E)
- [0142. Linked List Cycle II](Solutions/0142.Linked-List-Cycle-II.py) (E)
- [0160. Intersection of Two Linked Lists](Solutions/0160.Intersection-of-Two-Linked-Lists.py) (E)
- [0021. Merge Two Sorted Lists](Solutions/0021.Merge-Two-Sorted-Lists.py) (E)
- [0002. Add Two Numbers](Solutions/0002.Add-Two-Numbers.py) (E)

# [Depth First Search](/Depth-First-Search.py)
### [Combination](/Depth-First-Search.py)
- [0078. Subsets](Solutions/0078.Subsets.py) (！！M)(DFS + Back tracking)
- [0090. Subsets II](Solutions/0090.Subsets-II.py) (！！M)(如果之前的那个2没被放进去，那么就不要放后面那个2，这样来去重)
- [0039. Combination Sum](Solutions/0039.Combination-Sum.py) (！M) (start是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次)
- [0518. Coin Change 2](Solutions/0518.Coin-Change-2.py) (！M) (与Combination Sum一模一样，只是题目不要求输出所有可能组合，只要求输出可能组合的数目，所以可以用DP解，用DFS+Backtracking超时)
- [0040. Combination Sum II](Solutions/0040.Combination-Sum-II.py) (！M) (避免重复输出的方法与Subsets II一样)
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (！M) (这个题更确切应该叫Permutatino Sum，TLE)
- [0131. Palindrome Partitioning](Solutions/0131.Palindrome-Partitioning.py) (！M) (递归的定义很重要)

### [Permutation](/Depth-First-Search.py)
- [0046. Permutations](Solutions/0046.Permutations.py) (！！M)
- [0047. Permutations II](Solutions/0047.Permutations-II.py) (！！M) (去重方法与Subsets是类似的)
- [0051. N-Queens](Solutions/0051.N-Queens.py) (！H) (核心是nums=[0,1,2,3]的去重排列问题，去重需要做三个visited的判断)
- [0052. NQueens II](Solutions/0052.N-Queens-II.py) (H) 

### [图上的搜索](/Depth-First-Search.py)（打印/输出所有满足条件的路径必用DFS）
- [0126. Word Ladder II](Solutions/0126.Word-Ladder-II.py) (！！H)（好神奇）

# [Breadth First Search](/Breadth-First-Search.py)
### [BFS in Trees](/Breadth-First-Search.py)
- [0102. Binary Tree Level Order Traversal](Solutions/0102.Binary-Tree-Level-Order-Traversal.py) (！！M)
- [0103. Binary Tree Zigzag Level Order Traversal](Solutions/0103.Binary-Tree-Zigzag-Level-Order-Traversal.py) (！M)
- [0107. Binary Tree Level Order Traversal II](Solutions/0107.Binary-Tree-Level-Order-Traversal-II.py) (！E)
- [0199. Binary Tree Right Side View](Solutions/0199.Binary-Tree-Right-Side-View.py) (！M)
- [0111. Minimum Depth of Binary Tree](Solutions/0111.Minimum-Depth-of-Binary-Tree.py) (E)
- [0297. Serialize and Deserialize Binary Tree](Solutions/0297.Serialize-and-Deserialize-Binary-Tree.py) (H)

### [BFS in Graphs](/Breadth-First-Search.py)
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (M)
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (M)
- [0127. Topological Sorting](Solutions/0127.Topological-Sorting.py) (！！LintCode M) (Topological Sorting)
- [0207. Course Schedule](Solutions/0207.Course-Schedule.py) (！！M) (opological Sort)
- [0210. Course Schedule II](Solutions/0210.Course-Schedule-II.py) (！！M) (Naked Topological Sort)
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (M)

### [BFS in Matrix](/Breadth-First-Search.py) (隐式图搜索问题!!!)
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (M)
- [0994. Rotting Oranges](Solutions/0994.Rotting-Oranges.py) (M) (需要层序遍历)
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (！！M) (需要层序遍历，利用对称解决LTE问题，也可以从两端同时开始BFS)
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (！！M) (层序遍历BFS，双端BFS看不太懂)
- [0317 Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (！！H) (选择1为起点做层序遍历的BFS)

# [Sort](/Sort.py) 
- [0912. Sort an Array](Solutions/0912.Sort-an-Array.py) (M) (quick sort vs. merge sort) 
- [0969. Pancake Sorting](Solutions/0969.Pancake-Sorting.py) (M) (two flips to move the max_num to the end of arr) 
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (M) (quick select)

### [Partition](/Sort.py) 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (Lintcode)
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E)
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) (三根指针partition成三个部分)


# [Binary Tree, Divide and Conquer](/Binary-Tree-Divide-and-Conquer.py) 
- [0144. Binary Tree Preorder Traversal](Solutions/0144.Binary-Tree-Preorder-Traversal.py) (M) (memorize the iterative version using stack)
- [0094. Binary Tree Inorder Traversal](Solutions/0094.Binary-Tree-Inorder-Traversal.py) (M) (memorize the iterative version using stack)
- [0104. Maximum Depth of Binary Tree](Solutions/0104.Maximum-Depth-of-Binary-Tree.py) (E) (Divide and Conquer vs Traverse)
- [0257. Binary Tree Paths](Solutions/0257.Binary-Tree-Paths.py) (E)
- [0596. Minimum Subtree](Solutions/0596.Minimum-Subtree.py) (LintCode) (Divide and Conquer + Traverse)
- [0597. Subtree with Maximum Average](Solutions/0597.Subtree-with-Maximum-Average.py) (LintCode) (Divide and Conquer + Traverse + resultType)
- [0110. Balanced Binary Tree](Solutions/0110.Balanced-Binary-Tree.py) (E) (resultType, used for return multipule values)
- [0235. Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py) (E)
- [0236. Lowest Common Ancestor of a Binary Tree](Solutions/0236.Lowest-Common-Ancestor-of-a-Binary-Tree.py) (M)
- [0700. Search in a Binary Search Tree](Solutions/0700.Search-in-a-Binary-Search-Tree.py) (E)
- [0938. Range Sum of BST](Solutions/0938.Range-Sum-of-BST.py) (E)
- [0098. Validate Binary Search Tree](Solutions/0098.Validate-Binary-Search-Tree.py) (M)
- [0426. Convert Binary Search Tree to Sorted Doubly Linked List](Solutions/0426.Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List.py) (M) (这种改变成linked list的题真是一头雾水呀)
- [0114. Flatten Binary Tree to Linked List](Solutions/0114.Flatten-Binary-Tree-to-Linked-List.py) (M)
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (M)
- [0285. Inorder Successor in BST](Solutions/0285.Inorder-Successor-in-BST.py) (M)
- [0701. Insert into a Binary Search Tree](Solutions/0701.Insert-into-a-Binary-Search-Tree.py) (M)
- [0450. Delete Node in a BST](Solutions/0450.Delete-Node-in-a-BST.py) (M)

# [Binary Search](/Binary-Search.py)
- [0704. Binary Search](Solutions/0704.Binary-Search.py) (E)
- [0702. Search in a Sorted Array of Unknown Size](Solutions/0702.Search-in-a-Sorted-Array-of-Unknown-Size.py) (M) (Find end point using "double method", same as dynamic array)
- [0069. Sqrt(x)](Solutions/0069.Sqrt(x).py) (E)
- [0034. Find First and Last Position of Element in Sorted Array](Solutions/0034.Find-First-and-Last-Position-of-Element-in-Sorted-Array.py) (M)
- [0035. Search Insert Position](Solutions/0035.Search-Insert-Position.py) (E)
- [0278. First Bad Version](Solutions/0278.First-Bad-Version.py) (E)
- [0153. Find Minimum in Rotated Sorted Array](Solutions/0153.Find-Minimum-in-Rotated-Sorted-Array.py) (M)
- [0154. Find Minimum in Rotated Sorted Array II](Solutions/0154.Find-Minimum-in-Rotated-Sorted-Array-II.py) (H)
- [0039. Recover Rotated Sorted Array](Solutions/0039.Recover-Rotated-Sorted-Array.py) (LintCode) (找到minPos, 然后三步反转法)
- [0033. Search in Rotated Sorted Array](Solutions/0033.Search-in-Rotated-Sorted-Array.py) (M)
- [0852. Peak Index in a Mountain Array](Solutions/0852.Peak-Index-in-a-Mountain-Array.py) (E)
- [0162. Find Peak Element](Solutions/0162.Find-Peak-Element.py) (M)
- [0875. Koko Eating Bananas](Solutions/0875.Koko-Eating-Bananas.py) (M) (Construct a OOOXXX problem to find the first X)
- [0074. Search a 2D Matrix](Solutions/0074.Search-a-2D-Matrix.py) (M) (Think the 2D array as a long 1D array cuz the rows and cols are sorted)
- [0240. Search a 2D Matrix II](Solutions/0240.Search-a-2D-Matrix-II.py) (M) (Start from bottom left, head to top right, each comparism rule out a colomn or a row)


## Rabin Karp Algorithm
- [0028. Implement strStr()](Solutions/0028.Implement-strStr().py) (E) (Rabin Karp Algorithm O(M+N), use Hashcode, ord(ch)-ord("a"))
