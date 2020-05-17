## 三刷：不做新题了，就这250题！目标是刷熟练！模板总结出来天天拿出来背诵！
## 每日10题：05/01 - 05/25
#### Review: 
05/04 - 0337; 05/05 - 0334; 05/06 - 0416; 05/08 - 0010; 05/10 - 0713; 05/11 - 0394; 05/12 - 654; 05/13 - 621; 05/14 - 200; 05/15 - 212


# [Dynamic Programming](Dynamic-Programming.py)
### [Recursion with memoization](/Dynamic-Programming.py)
139. word break; 312. Burst Balloons
使用记忆数组 memo 的递归写法，和使用 dp 数组的迭代写法，乃解题的两大神器，凡事能用 dp 解的题，一般也有用记忆数组的递归解法，好似一对形影不离的好基友～何时用带memo的recursion? 如果用dp的转移方程很复杂，那就用带memo的recursion, 一定要会默写！


### [坐标型DP](/Dynamic-Programming.py)
- [0062. Unique Paths](Solutions/0062.Unique-Paths.py) (!!M) <br>
状态: f[i][j]=有多少种方式从左上角走到(i, j); 转移方程：f[i][j] = f[i][j-1]+f[i-1][j]
- [0063. Unique Paths II](Solutions/0063.Unique-Paths-II.py) (M) <br> 
转移方程：f[i][j] = 0 if it is obstacle else f[i][j-1]+f[i-1][j])
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (M) <br> 
dp[i][j]=the minimum path sum to (i, j); dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j])
- [0120. Triangle](Solutions/0120.Triangle.py) (M) <br>
dp[i][j] = min(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1]), rolling array to reduce space to O(N)
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M) <br>
dp[i][j]=以(i, j)为右下角的最大正方形的边长; dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j]=1 
- [0403. Frog Jump](Solutions/0403.Frog-Jump.py) (M) <br>
维护一个stonesDict的key is the stone in stones. value is the possible steps to reach the stone.
There could be multiple possible steps to reach the stone, so stonesDict[stone] = set(). 
状态转移方程为：1. 跳k-1到stone+k-1: stonesDict[stone + k - 1].add(k - 1); 2. 跳k到stone + k: stonesDict[stone + k].add(k); 3. 跳k + 1到stone + k + 1:stonesDict[stone + k + 1].add(k + 1); Return stonesDict[last stone] is not empty; this is bottom up method O(N^2), O(N^2)
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (!!H) <br>
存在性问题。状态: dp[j]=能不能跳到位置j; 转移方程：dp[j]=True if dp[i] and nums[i]>=j-i) (TLE 注意只要有一个dp[i]是的dp[j]=True了就可以break了). DP解法: O(N^2).  Greedy 解法: O(N) Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index (currPosition + nums[currPosition] >= GoodIndex). If we can reach a GOOD index, then our position is itself GOOD. Iteration continues until the beginning of the array.  Return if the first position is a GOOD index.

### [序列型DP](/Dynamic-Programming.py)
- [0256. Paint House](Solutions/0256.Paint-House.py) (E) <br>
dp[i][j] means the minimum cost to paint house i to be color j; dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
- [0265. Paint House II](Solutions/0265.Paint-House-II.py) (H) <br> 
dp[i][j]=minimum cost to paint the ith house the be color j; dp[i][j] = dp(minIThe(i-1)thRow) + costs[i][j]. In order to find dp(minIThe(i-1)thRow fast), we can find the position for the 1st and 2nd min in the i-1 th row first, then in the ith row calcuation, if j=1stMinposition, then dp[i][j]=2nd_min + costs[i][j], else dp[i][j]=1st_min + costs[i][j]
- [0198. House Robber](Solutions/0198.House-Robber.py) (E) <br>
f[i]=the max profit when reaching ith house; f[i] = max(rob ith = f[i-2]+nums[i], not rob ith = f[i-1]) <br>
空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]
- [0213. House Robber II](Solutions/0213.House-Robber-II.py) (M) <br>
房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：1. 房子1没偷：问题变成了对房子2:N做House robber I的问题; 2. 房子N没偷：问题变成了对房子1:N-1做House robber I的问题
- [0337. House Robber III](Solutions/0337.House-Robber-III.py) (M) <br>
树状的house.递归： def with_without_rob(self, root): return a tuple, the 1st element in the tuple is the max profift with_rob_root， the 2nd element in the tuple is the max profit without_rob_root. 递归公式：with_rob_root = root.val + without_rob_left + without_rob_right; without_rob_root = max(with_rob_left, without_rob_left) + max(with_rob_right, without_rob_right)

### [Buy and sell stock DP问题](/Dynamic-Programming.py)
- [0121. Best Time to Buy and Sell Stock](Solutions/0121.Best-Time-to-Buy-and-Sell-Stock.py) (E) <br>
Only one transaction is allowed.  Maintain a minPrice and a maxProfit; maxProfit = max(maxProfit, price - minPrice)
- [0122. Best Time to Buy and Sell Stock II](Solutions/0122.Best-Time-to-Buy-and-Sell-Stock-II.py) (E) <br>
As many transaction as possible.  make a transaction every time price[i]>price[i-1]
- [0123. Best Time to Buy and Sell Stock III](Solutions/0123.Best-Time-to-Buy-and-Sell-Stock-III.py) (H) <br>
Only two transactions are allowed.  Maintain buy1=the minimum money you can **owe** after the first buy, sell1=the maximum money you **earn** after the first sell, also, buy2, sell2, and update them together in a for loop, 算法只是把121中的算法重复两次而已.
- [0188. Best Time to Buy and Sell Stock IV](Solutions/0188.Best-Time-to-Buy-and-Sell-Stock-IV.py) (H) <br>
Only k transactions are allowed.   Maintain buy=[]*k, sell=[]*k, and update them together in a for loop. buy[i] = min(buy[i], price - sell[i - 1]), buy[i] = the minimum money you can own after the ith purchase; sell[i] = max(sell[i], price - buy[i]), sell[i] = the maximum money you can earn after the ith purchase.  Solve the memory overflow problem: if k>prices.length/2, then it is the same as 122.
- [0309. Best Time to Buy and Sell Stock with Cooldown](Solutions/0309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py) (M) <br>
Has to rest for one day before buy another stock.  **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益, return unhold[-1] <br> 
hold[i] = max(hold[i-1], unhold[**i-2**]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i]) 学会画state machine
- [0714. Best Time to Buy and Sell Stock with Transaction Fee](Solutions/0714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) (M) <br>
There is transaction fee when you sell. **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益 <br>
hold[i] = max(hold[i-1], unhold[i-1]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i] **- fee**)

###  [最长子序列问题](/Dynamic-Programming.py) (dp[i]都是定义为以i结尾的最长....)
- [0674. Longest Continuous Increasing Subsequence](Solutions/0674.Longest-Continuous-Increasing-Subsequence.py) (E) <br>
dp[i] = 以i结尾(包括i)的最长连续子序列; dp[i] = dp[i-1] + 1 if nums[i]>nums[i-1]
- [0300. Longest Increasing Subsequence](Solutions/0300.Longest-Increasing-Subsequence.py) (!!M) <br> --- 1048 --- 
不需要连续，所以不是dp[i] = dp[i-1] + 1，而是所有的j之前的i都有可能, 所以转移方程是 dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]) <br>
dp + binary search (O(NlogN))的算法也很重要！dp[i] = the maintianed array with i as the possible increadsing numbers, dp should be an orderd array: if nums[i] > the last item in dp, then append nums[i] to dp, if < the first item in dp, then replacethe first item with nums[i], if is in between, then将sorted arr中最接近num的数用num取代, by using binary search.
- [0673. Number of Longest Increasing Subsequence](Solutions/0673.Number-of-Longest-Increasing-Subsequence.py) (M) <br>
 dp=以i为结尾的最大的长度; cnt=以i为结尾的最大的长度的个数; 在nums[j]>nums[i]的情况下：cnt[j]+=cnt[i] if dp[j]=dp[i]+1
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.Longest-Arithmetic-Sequence.py) (M) <br>
dp[i] = {key:diff, val:lens of arithmetic sequence ended with i and diff as 公差}; dp[j][nums[j]-nums[i]] = dp[i][nums[j] - nums[i]] + 1
- [0873. Length of Longest Fibonacci Subsequence](Solutions/0873.Length-of-Longest-Fibonacci-Subsequence.py) (M) <br>
dp[i]=dictionary{key: last num of the fib; val: the lens of the fib ended with ith}, dp[j][nums[i]]=d[i][nums[j]-nums[i]]+1
- [0354. Russian Doll Envelopes](Solutions/0354.Russian-Doll-Envelopes.py) (H) <br>
Similiar with 300. LIS; sort the list first envelopes.sort(key = lambda x: (x[0], x[1])), here we not only compare nums[j]>nums[i], but instead both the width and height; TLE, should 300. LIS using DP+binary search (O(NlogN))??
- [0334. Increasing Triplet Subsequence](Solutions/0334.Increasing-Triplet-Subsequence.py) (M) <br>
Similiar with 300. LIS; dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]); if dp[j]>=3 return True；  how to solve it in O(N), O(1); min_1, min_2 and are the most min and the second min in the arr, if min_1 and min_2 are renewed twice already and there is a num>min_2 later, then return True.

### [区间型DP](/Dynamic-Programming.py) 自然而然将状态定义为f[i][j]表示面对子区间[i, j]时的最佳性质
- [0005. Longest Palindromic Substring](Solutions/0005.Longest-Palindromic-Substring.py) (!!M) <br>
题目问substring, substring就需要是连续的，题目要求Return the longest substr: dp[i][j]=from i to j (including j), is it a palindr? if s[i]==s[j]: dp[i][j] = dp[i+1][j-1]; 注意初始化对角线和相邻的，因为计算dp[i][j]需要用到dp[i+1][j-1]，所以要先算i+1, 再算i，所以i 是倒序遍历
solution 2: 从中间c往两边遍历i--, j++，遍历两次：一次是i=c, j=c开始遍历， 一次是i=c, j=c+1开始遍历。
- [0516. Longest Palindromic Subsequence](Solutions/0516.Longest-Palindromic-Subsequence.py) (!!M) <br>
题目问subsequence, subsequence不需要连续，题目要求Return the longest length: dp[i][j]=longest palindr from i to j; dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1]);注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i，所以i is from (j, 0)
- [0312. Burst Balloons](Solutions/0312.Burst-Balloons.py) (!!H) <br>
带memo的recursion比DP更好懂; left = self.memoSearch(nums, i, k, memo); right=self.memoSearch(nums, k, j, memo); maxCoins = max(maxCoins, left + right + nums[i] * nums[k] * nums[j]). 
也可以用dp: https://qoogle.top/leetcode-312-burst-balloons/ <br>
Lintcode 476. Stone Game <br>
1011
410. Split Array Largest Sum
1444
###  [划分型DP](/Dynamic-Programming.py) (状态往往定义为前j个的某种特性，不包括j！！！！，这个思想很重要，相当于给前面做了一层buffer layer)
- [0139. Word Break](Solutions/0139.Word-Break.py) (!!M) <br>
dp[i]=can partition until ith char?, not including i; dp[j]=true if (for i < j, there is dp[i]=True and s[i:j]is in wordDict)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M) <br>
f[i]=number of decode ways until i (not including i); f[i]=f[i-1]+f[i-2] if int(s[i-2:i])<=26 else f[i-1]
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (M) <br>
f[j]=the least number of perfect square numbers which sum to i; f[j] = min(f[j-i^2]+1) for i^2<=j; Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5); solution 2 mathematics: Four-square theorem states that every natural number can be represented as the sum of at most four integer squares.
- [0132. Palindrome Partitioning II](Solutions/0132.Palindrome-Partitioning-II.py) (!!H) <br>
子数组或者子字符串且求极值的题，基本就是 DP 没差了. f[j]=the minimum number of total palindrome till the jth character (not including j); f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome. O(N^3), 划分型的dp的状态一般都not include j, 这样就有一个buffer layer可以用。Solution 2: 优化为O(N^2), 用一个isPalin[i][j]记录s[i:j]是否是palindrome, 更新isPalin[i][j]的方法与leetcode 5 相同，这样就不用每次都用双指针去判断s[i:j]是不是palindrome. 输出所有的可能的partition成palindrome的组合问题只能dfs+backtracking了- 131. Palindrome Partitioning


### [博弈型DP](/Dynamic-Programming.py)
- [0394. Coins in a Line](Solutions/0394.Coins-in-a-Line.py) (M Lintcode) <br>
Solution1 dp: f[i]=面对i个石子，先手是必胜吗; f[i]=True if f[i-1] or f[i-2] 有一个是False <br>
Solution 2: 至于prev, curr有关，所以可以空间优化成O(1)了; Solution 3 数学: 只要是3的倍数就一定输 return n % 3 != 0
- [0486. Predict the Winner](Solutions/0486.Predict-the-Winner.py) (M) <br>
f[i][j]=当石子还剩i到j时，先手最多能赢多少; f[i][j] = max(取左边A[i]-f[i+1][j], 取右边A[j]-f[i][j-1]), 注意f[i][j]与f[i+1][j]相关，所以i要从后往前遍历.

### [背包型DP](/Dynamic-Programming.py)
- [0322. Coin Change](Solutions/0322.Coin-Change.py) (!!M) <br>
背包问题，重量一定要入状态。状态: f[X]=最少用多少枚硬币拼出X; 转移方程：f[X] = min(f[X-1]+1, f[X-2]+1, f[X-5]+1, f[X])
- [0092. Backpack](Solutions/0092.Backpack.py) (!!M Lintcode) <br>
f[i][m]=能否用前i个物品拼出重量m; f[i][m] = f[i-1][m] (放不入，表示前i-1个物品就可以拼出m) or f[i-1][m-A[i-1]] (放入，表示前i-1个物品可以拼出m-A[i-1]); # 注意点1：这里要定义lens+1，这样就可以做一个buffer layer出来了; # 注意点2；这里循环i在外面，m在里面，千万别搞反了！！# 注意点3：由于buffer layer的存在，这里用nums[i-1]与m相比较
- [0563. Backpack-V](Solutions/0563.Backpack-V.py) (!!M Lintcode) <br>
一个num不能取多次，所以与322. coin change 不同。所以必须用二维数组，f[i][m]=前i个物品能拼出重量m有多少种方式。f[i][m] = 不放入 f[i-1][m] + 放入 f[i-1][m-A[i-1]] if m > nums[i] else =f[i-1][m]
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (!!M) <br> 
一个num能取多次，所以与322. coin change 相同。所以可以用一维数组，f[i]=how many ways to combine to number i; 背包问题一定要把总承重放到状态里！！ f[i]=f[i-A1]+f[i-A2]+f[i-A3].... <br>
- [0125. Backpack II](Solutions/0125.Backpack-II.py) (!!M Lintcode) <br>
这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。用子问题定义状态：即f[i][j]表示前i件物品拼出重量j可以获得的最大价值。
f[i][j]=max{f[i-1][j] (不放入),f[i-1][j-A[i]]+V[i] (放入)}; return f[lens-1][M]
- [0089. k Sum](Solutions/0089.k-Sum.py) (M Lintcode) <br>
f[i][j][s]表示有多少种方法可以在前i个数中选出j个，使得它们的和是s; 情况一:（A[i-1]不选入）：需要在前n-1个数中选K个数，使得它们的和是Target: f[i][j][s] += f[i-1][j][s]; 情况二（A[i-1]选入）：需要在前i-1个数中选j-1个数，使得它们的和是Target-A[i-1]: f[i][j][s] += f[i-1][j-1][s-A[i-1]]
- [0416. Partition Equal Subset Sum](Solutions/0416.Partition-Equal-Subset-Sum.py) (M) <br>
背包问题：将A中的物品放入容量为target的背包中，问是否存在？一个num不能取多次，所以与322. coin change 不同。所以必须用二维数组。与0092一模一样。 f[i][t]=将前i个物品放入背包中，能否拼出t (背包问题重量一定要入状态); f[i][t]=True if 不放最后一个进背包: f[i-1][t]=True or 放最后一个进背包: f[i-1][t-A[i-1]]=True

### [位操作型DP](/Dynamic-Programming.py)
- [0338. Counting Bits](Solutions/0338.Counting-Bits.py) (M) <br>
状态dp[i]=i的二进制中有多少个1; dp[i] = dp[i >> 1] + i % 2

### [双序列型DP!!](/Dynamic-Programming.py) 
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (!!M) <br>
f[i][j]为A前i个字符A[0..i)和B前j个字符[0..j)的最长公共子串的长度，注意不包括i和j，前面有一层buffer layer非常重要，就像sputtering那样重要！ f[i][j]=f[i-1][j-1] + 1 when A[i-1]=B[j-1], else f[i][j]=max(f[i-1][j], f[i][j-1])) # 注意有了buffer layer之后，dp中的i对应的是text中的i-1,所以判断条件是when A[i-1]=B[j-1]
- [583. Delete Operation for Two Strings](Solutions/0583.Delete-Operation-for-Two-Strings.py) (M) <br>
f[i][j] = the min number of steps needed to make word1[:i] and word[:j] the same; f[i][j]=f[i-1][j-1] when A[i-1]=B[j-1], else f[i][j]=min(f[i-1][j], f[i][j-1])) + 1
- [0072. Edit Distance/Levenshtein distance](Solutions/0072.Edit-Distance.py) (!!H) <br>
f[i][j]=A前i个字符[0..i)和B前j个字符[0..j)的最小编辑距离; f[i][j]=min{1. f[i-1][j]+1 (f[i-1][j]表示A[0..i-1)就可以拼成B[0..j)了，所以A[0..i)要拼成B[0..j)需要删掉A[0..i)的最后一个字母); 2. f[i][j-1]+1 (B[0..j)需要删掉最后一个字母，即A[0..i)的后面需要增加一个字母); 3. f[i-1][j-1]+1 (A[0..i)的后面需要replace一个字母); 4. f[i-1][j-1] (if A[i-1]=B[j-1] 就不需要任何操作直接就是了)}
- [0097. Interleaving String](Solutions/0097.Interleaving-String.py) (!!H) <br>
f[i][j]=s3的前[0..i+j)个字符能否由s1前i个字符[0..i)和s2前j个字符[0..j)交错形成; f[i][j]=True when (s3[i+j-1]=s1[i-1] 且 f[i-1][j]=True 即s3的前[0..i+j-1)个字符能否由s1前i-1个字符[0..i-1)和s2前j个字符[0..j)交错形成) or (s3[i+j-1]=s2[j-1] and f[i][j-1]=True)
- [0115. Distinct Subsequences](Solutions/0115.Distinct-Subsequences.py) (H) <br>
dp[i][j] = the number of discinct subeseq until ith char in s and jth char in t; if s[i]!=t[j], dp[i][j] = dp[i - 1][j]  eg: rab, ra; else: rabb, rab, dp[i][j] = dp[i-1][j] + dp[i-1][j-1], 品，细品！ 
- [0044. Wildcard Matching](Solutions/0044.Wildcard-Matching.py) (H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配； 画个图会很明了，详见九章算法动态规划双序列型DP。
情况一：B[j-1]不是"星": if (B[j-1]="?" or A[i-1]=B[j-1]): f[i][j] = f[i-1][j-1]  <br>
情况二：B[j-1]是"星"：可以让"星"表示0个字符，那就让A[0..i)去和B[0..j-1)匹配： f[i][j] = f[i][j-1]；也可以让"星"表示字符，A[i-1]肯定是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j]
- [0010. Regular Expression Matching](Solutions/0010.Regular-Expression-Matching.py) (!!H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配; 情况一：B[j-1]不是"星": f[i][j] = f[i-1][j-1] if (B[j-1]="." or A[i-1]=B[j-1]); 情况二：B[j-1]是"星"：可以让"星"表示0个前面的字符，那就让A[0..i)去和B[0..j-2)匹配： f[i][j] = f[i][j-2]；也可以让"星"表示几个前面的字符，A[i-1]是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j] if (B[j-2]="." or B[j-2]=A[i-1])


# [Sliding Window (同向双指针)](/Sliding-window.py)
- [0209. Minimum Size Subarray Sum](Solutions/0209.Minimum-Size-Subarray-Sum.py) (!!M) <br>
维护一个sums, 用来记录i->j中数的和，套模板时满足的条件是sums < target; 更新j: sums += nums[j]; 更新i: sums -= nums[j]
Can we solve in O(NlogN)? Yes, we can traverse the the list, say at i, we search the fisrt j that satisfy sum(nums[i:]>=s), so it is a OOXX probelm, which could be solved using binary search.
- [0003. Longest Substring Without Repeating Characters](Solutions/0003.Longest-Substring-Without-Repeating-Characters.py) (!!M) <br>
维护一个included=set(), 用来记录i->j中include的char，套模板时满足的条件是s[j] not in included; 更新j: included.add(s[j]); 更新i: included.remove(s[i])
- [0076. Minimum Window Substring](Solutions/0076.Minimum-Window-Substring.py) (H) <br>
维护一个sourceFreqDict, 用来记录i->j中的char的频率，套用模板时满足的条件是sourceFreqDict all included in targetFreqDict; 更新j: sourceDict[s[j]] += 1, 更新i: sourceDict[s[i]] -= 1.  time complexity is O(MN).
It seems there is an O(M+N) solution, same idea of using slideing window, I should understand it later. 山景城一姐有video
- [0340. Longest Substring with At Most K Distinct Characters](Solutions/0340.Longest-Substringwith-At-Most-K-Distinct-Characters.py) (H) <br>
维护一个charDict, 用来记录i->j中的char的频率，套模板时满足的条件是len(charDict) <= k; 更新j: charDict[s[j]+=1; 更新i: charDict[s[i]] -= 1, if charDict[s[i]] == 0: del charDict[s[i]]
- [0713. Subarray Product Less Than K](Solutions/0713.Subarray-Product-Less-Than-K.py) (M) <br>
Note that the numbers are positive, so the prefixProd will be an increasing arr. 维护一个sums, 用来记录i->j中数的produce. 

-------567. Permutation in String----------



# [Data Structure](/Data-Structure.py)
### [Stack and Queue](/Data-Structure.py)
- [0232. Implement Queue using Stacks](Solutions/0232.Implement-Queue-using-Stacks.py) (E) <br>
use two stack, 要学会写raise IndexError("queue is empty") 的语句
- [0225. Implement Stack using Queues](Solutions/0225.Implement-Stack-using-Queues.py) (E) <br>
use two deques; 要学会抛出error: in pop function, if the stack is empty then raise IndexError("stack is empty");
也可以用一个list实现，每次push进去的时候，把元素插入到最前面即可，与两个queue相比，时间复杂度也还是O(N)
- [0155. Min Stack](Solutions/0155.Min-Stack.py) (!!E) <br>
use two stacks, a stack is to store all items, a minStack to store min items. If a num is less than minStack[-1] then we should append to minStack.
- [0716. Max Stack](Solutions/0716.Max-Stack.py) (E) <br>
Solutino 1: just use one list. Since we have to implement popMax method, we have to find the maxItem pos in the stack, it takes O(N).  Solution 2: by using double linked list and tree map, we can realize O(logN) for push, pop and popMax
- [0346. Moving Average from Data Stream](Solutions/0346.Moving-Average-from-Data-Stream.cs) (E) <br>
In C#, Queue class is by default a deque, with two methods: 1. enqueue, meaning push to the back of the queue; 2. dequeue, meaning pop from the front of the queue. They are all O(1).
- [0933. Number of Recent Calls](Solutions/0933.Number-of-Recent-Calls.py) (E) <br>
In C#, Count is a method that gets the number of elements contained in the Queue.
- [0394. Decode String](Solutions/0394.Decode-String.py) (!!M) <br>

### [Iterator](/Data-Structure.py)
- [0341. Flatten Nested List Iterator](Solutions/0341.Flatten-Nested-List-Iterator.py) (!!M) <br>
注意这类问题的主程序一般都写在hasNext里面！if topItem.isInteger(): return True; else: if it is a nestedList, 就展开: self.stack = self.stack[:-1] + topItem.getList()[::-1]
- [0251. Flatten 2D Vector](Solutions/0251.Flatten-2D-Vector.py) (M) <br>
- [0281. Zigzag Iterator](Solutions/0281.Zigzag-Iterator.py) (M) <br>
use two pointers and a flag. What if you are given k 1d vectors? How well can your code be extended to such cases? Solution: We append all the list into one deque. Every time we call next(), we pop a list first, then pop the first num from the list, and then re-add it to the end to deque so that we can call it again after k next calls.
- [0284. Peeking Iterator](Solutions/0284.Peeking-Iterator.py) (!M) saving peeked value
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (!!M) <br>
用stack实现binary search tree的in order traversal的方法类似

### [Monotonic stack](/Data-Structure.py) （递增栈，就是栈中只存放递增序列）
- [0084. Largest Rectangle in Histogram](Solutions/0084.Largest-Rectangle-in-Histogram.py) (!!H) <br>
非单调栈算法：从左向右遍历数组，然后每遍历到一个高度h，向左边找第一个比自己小的的高度在位置i，向右边找第一个比自己小的的高度在位置j，
那此时的面积就是h*(j-i). 这个算法需要向左向右找第一个比自己小的元素，这类问题就要想到用monostack. 通过maintain a monostack,可以很快找到第一个比i小的元素，就是栈中排在i前面的元素，我们需要做的只是向右找了，所以我们向右遍历，每当遇到大于栈顶的值时，直接入栈保持递增stack，如果遇到小于栈顶的值，这时候说明找到了第一个比i（栈顶）小的元素，这时候我们回头且慢莫慌，栈内各个元素依次出栈并回头计算一下面积。
- [0085. Maximal Rectangle](Solutions/0085.Maximal-Rectangle.py) (!!H) <br>
step 1: construct a heights list for each row; step 2: calculate the largestRectangularHistogram of each height using the same method in 84; Should think about dynamic programming solution also.
- [0654. Maximum Binary Tree](Solutions/0654.Maximum-Binary-Tree.py) (M) <br>
solution 1: simple recursionsolution 2: monostack 通过观察发现规律，对于每个node的父亲节点 = min(左边第一个比它大的，右边第一个比它大的), 维护一个降序数组，可以实现对这个min的快速查找, # O(N), O(N)


### [Deque](/Data-Structure.py) 
- [0239. Sliding Window Maximum](Solutions/0239.Sliding-Window-Maximum.py) (H) <br>
heapq的方法是O(NK); deque O(N): Iterate over the array. At each step: I. Clean the deque: 1. Keep only the indexes of elements from the current sliding window; 2. Remove indexes of all elements smaller than the current one, since they will not be the maximum ones. eg: [1,2,7,3,5,4], k = 3, because of 7, 1 and 2 will never be in res; II. Append the current element to the deque. Append deque[0] to the output.


### [Hashmap/Dictionary](/Data-Structure.py) 
- [0146. LRU Cache](Solutions/0146.LRU-Cache.py) (!!M youtubed) <br>
use a double linked list and a dictionary; Double linkedlist: newest node append to tail, eldest node remove from head, so that the operation is O(1); Hashmap: key is key, value is the corresponding double linkedlist node

### [Heap/Heapq](/Data-Structure.py) 
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M) <br>
time: O(NlogK), N 来自于for循环，logK来自于heap的长度是K，heap 的push 和pop都是logK; heapq适合做第K大，第K小，前K大，前K小问题
- [0347. Top K Frequent Elements](Solutions/0347.Top-K-Frequent-Elements.py) (M) <br>
需要一个freqDict来记录每个数出现的freq， heapq, heapq中放入的是(freq, key)对; 按照freq来做heapq，这样就保证了可以筛选出most freqent k item
- [0253. Meeting Rooms II](Solutions/0253.Meeting-Rooms-II.py) (!!M) <br>
solution 1: 扫描线；solution 2: 以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间
- [0973. K Closest Points to Origin](Solutions/0973.K-Closest-Points-to-Origin.py) (M) <br>
（以squre来构建heap就可以了，heap中的元素是(square, point)）
- [0378. Kth Smallest Element in a Sorted Matrix](Solutions/0378.Kth-Smallest-Element-in-a-Sorted-Matrix.py) (!!M) <br>
利用sorted matrix的性质，从左上角第一个元素开始，添加进heap，然后heap当然自动排序了，然后pop出最小的，然后把最小的那个数的右边和下边的元素分别入heap，这样可以保证每次pop出来的都是最小的。1. use a heap to store (num, row, col); 2. use a set to check if row + 1, col + 1 visited already before push into the heap; Solution 2: binary search 了解一下。<br>
- [0465 Kth Smallest Sum in Two Sorted Arrays](Solutions/0465.Kth-Smallest-Sum-in-Two-Sorted-Arrays.py) (M Lintcode) <br>
将两个list各挑一个数出来的加和做成一个2D Array, 由于两个list都是sorted, 那么这个2D array就是与378同样sorted array了。
- [0023. Merge k Sorted Lists](Solutions/0023.Merge-k-Sorted-Lists.py) (!!M) <br>
maintain一个heapq，初始化将每个list的head放入，# overwrite the compare function, so that we can directly put ListNode into heapq: ListNode.__lt__ = lambda x, y: (x.val < y.val)然后每次pop出一个最小的，再把最小的那个的.next push进heapq, O(NlogK); Solution 2: divide and conquer, O(NlogK).
- [0621. Task Scheduler](Solutions/0621.Task-Scheduler.py) (!!M) <br>
I have to be concerned about tasks with higher frequencies. This makes it a perfect candidate for a Priority Queue, or a Max-Heap. 维护一个最大堆 by using negative freq
- [0264. Ugly Number II](Solutions/0264.Ugly-Number-II.py) (M) <br>
维护一个heapq，让它记录从小到大的ugly number, 每次pop出一个currMin，然后生成三个数2* currMin, 3*currMin, 5*currMin, 如果not in seen, 就push进heapq
- [0407. Trapping Rain Water II](Solutions/0407.Trapping-Rain-Water-II.py) (!!H) <br>
Similar with 1D trapping rain water. Step 1: store all the outliners of the matrix in heapq.  Maintain a visited set to mark all the visited locations. Step 2: starting from the min height position, do BFS the 4 possible moves. If found a height < the min Height, then we can store water, else we cannot store water and we should update this leaking point by putting the new height into the heapq
- [0295. Find Median from Data Stream](Solutions/0295.Find-Median-from-Data-Stream.py) (!!H) <br>
定义两个heap: self.leftHq as a maxheap to store the nums that are smaller than median; and self.rightHq as a minheap store the nums that are larger then median.  每次新增一个数num的时候，先根据比 maxheap 中最后一个数大还是小丢到对应的 heap 里。丢完以后，再处理左右两边的平衡性:如果左边太少了，就从右边拿出一个最小的丢到左边。如果右边太少了，从左边拿出一个最大的丢到右边。How to answer following questions.
- [0480. Sliding Window Median](Solutions/0480.Sliding-Window-Median.py) (H) <br>
similar with 295, we need to maintain two heaps, leftHq and rightHq. To slide one step is actually to do two things: 1. add a number, which is exactly the same as that in 295. 2. remove a number; 全是难题，看不进去https://leetcode.com/problems/sliding-window-median/discuss/412047/Two-heaps-%2B-sliding-window-approach-O(-n-*-k-)-runtime-O(k)-space


### [Union-Find](Union-Find-and-Trie.py)
- [0589. Connecting Graph](Solutions/0589.connecting-graph.java) (!!M Lintcode) <br>
将a和b connect: 只需要将a和b的father connect就好；query a和b有没有连接:其实就是判断a和b在不在同一个集合里面，只需要判断find(a) == find(b)
- [0590 Connecting Graph II](Solutions/0590.Connecting-Graph-II.java) (!!M Lintcode) <br>
需要query 点a所在集合的元素个数，所以需要一个list size, 用来记录每个father节点所在集合的点的个数，在union i 和 j 的时候: father[i] = j, sz[j] += sz[i];
- [0591. Connecting Graph III](Solutions/0591.Connecting-Graph-III.py) (!!M Lintcode) <br>
需要query 整个图中有多少个集合，所以需要一个counter, 用来记录图中集合的个数，初始化为n, 在union i 和 j 的时候: father[i] = j, counter--;
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (!!M, youtubed) <br>
Soluiton 1: Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search. <br>
SOlution 2: Union Find: think the grid as a graph, find how may isolated components in the graph, we traversal the whole gird, whenever find a 1, we connect all the 4 adjacent 1s. 方法同lintcode 591.
- [0305. Number of Islands II](Solutions/0305.Number-of-Islands-II.py) (!!H) <br>
Union-Find 算法是解决动态连通性（Dynamic Conectivity）问题的一种算法. 这里的island可以看做是一个图. 每放置一个1, 就将其与其上下左右四个点的1连接起来。O(m×n+L), follow up question?
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (!!M) <br>
Solution 2: Union find: O(N); Solution 1: BFS O(N)判断图是不是一棵树（不一定非要是二叉树）需要满足两点:1. 首先点的数目一定比边的数目多一个; 2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目, 如果小于则说明有的节点被访问不到，如果大于说明有环，则不是树
- [0128. Longest Consecutive Sequence](Solutions/0128.Longest-Consecutive-Sequence.py) (!!H) <br>
Solution 1: Greedy O(N) 使用一个集合HashSet存入所有的数字，然后遍历数组中的每个数字，如果其在集合中存在，那么将其移除，然后分别用两个变量pre和next算出其前一个数跟后一个数，然后在集合中循环查找，如果pre在集合中，那么将pre移除集合，然后pre再自减1，直至pre不在集合之中，对next采用同样的方法，
那么next-pre-1就是当前数字的最长连续序列，更新res即可; Solution 2: Union find: O(N),


### [Trie](Union-Find-and-Trie.py)
- [0208. Implement Trie (Prefix Tree)](Solutions/0208.Implement-Trie-(Prefix-Tree).py) (!!M) <br>
Firstly we need to define a TrieNode class, a TrieNode class hs two properties: 1. self.child = collections.defaultdict(TrieNode)  # use a defaultdict, key is char, value is TrieNode corresponding to the char.  2. self.isEnd = False   # return True if reached the end of the Trie.  Then implement 3 methods: insert(word), search(word), startWith(prefix); 注意currNode往下遍历时currNode = currNode.child[char]
- [0211. Add and Search Word - Data structure design](Solutions/0211.Add-and-Search-Word-Data-structure-design.py) (!!M) <br>
addWord mehtod is the same as 208 insert method. But search mehtod is a little different than search method in 208, cuz "." is a wildcard that can represent any char. So we use a queue to store (currNode, idx), then append layer by layer.
- [0212. Word Search II](Solutions/0212.Word-Search-II.py) (!!M) <br>
The capability of finding matching prefix is where the data structure called Trie would shine, comparing the hashset data structure. Not only can Trie tell the membership of a word, but also it can instantly find the words that share a given prefix. 打印所有路径所以用Trie + Backtracking DFS. 非常经典的题呀！


# [Breadth First Search](/Breadth-First-Search.py)
### [BFS in Trees](/Breadth-First-Search.py) (总结：Tree中需要一层一层输出的都用BFS)
- [0102. Binary Tree Level Order Traversal](Solutions/0102.Binary-Tree-Level-Order-Traversal.py) (!!M, youtubed) <br>
BFS的铁律就是用queue, 在while q: 循环里做两件事 1. 处理这一层。那就需要把这一层的node逐个pop出，然后append到res里，有时候需要用for循环for _ in range(len(q))来遍历这一层所有的node; 2. append下一层进q。BFS is O(N) since each node is processed exactly once
- [0103. Binary Tree Zigzag Level Order Traversal](Solutions/0103.Binary-Tree-Zigzag-Level-Order-Traversal.py) (M) <br>
same as 102, 在res.append(level)的时候间隔性选择res.append(level) or res.append(level[::-1])
- [0107. Binary Tree Level Order Traversal II](Solutions/0107.Binary-Tree-Level-Order-Traversal-II.py) (E) <br>
same as 102，只是题目要求从下至上输出，只需要return res[::-1]即可
- [0199. Binary Tree Right Side View](Solutions/0199.Binary-Tree-Right-Side-View.py) (M) <br>
same as 102，只需要res.append(level[-1])即可
- [0111. Minimum Depth of Binary Tree](Solutions/0111.Minimum-Depth-of-Binary-Tree.py) (E) <br>
solution 1: recursion; soluiton 2: BFS; for _ in range(lens): if not node.left and not node.right: return depth
- [0297. Serialize and Deserialize Binary Tree](Solutions/0297.Serialize-and-Deserialize-Binary-Tree.py) (!!H) <br>
should practice more times!

### [BFS in Graphs](/Breadth-First-Search.py)
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (!!M) <br>
判断图是不是一棵树（不一定非要是二叉树）需要满足两点:1. 首先点的数目一定比边的数目多一个; 2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目, 如果小于则说明有的节点被访问不到，如果大于说明有环，则不是树
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (M) <br>
Step 1：找到所有的original_nodes，存到一个set里面，用BFS实现; Step 2: 复制所有原有的node，存到mapping中，这样就建立了一个new_node和original_node的一一映射; Step 3: 复制所有original_node对应的neighbors 到 new_node里面
- [0127. Topological Sorting](Solutions/0127.Topological-Sorting.py) (!!LintCode) <br>
有向图的问题，可以检测有向图是否有环！必考，其实也非常模板化，一定要记住。Three steps: 1. 从数字关系求出每个节点的inDegrees（就是找节点与相邻节点的依赖关系） (inDegrees = collections.defaultdict(int))，key是node, val是这个node的indegree值; 2. 和每个节点的neighbors （neighbors = collections.defaultdict(list)), key是node, val是装有这个node的neighbor的list; 3. 然后 BFS，背诵模板就可以了。
- [0207. Course Schedule](Solutions/0207.Course-Schedule.py) (!!M) <br>
套用模板分三步：1. collect the inDegree of each node; 2. collect the neighbors information; 3. topological sort - BFS
- [0210. Course Schedule II](Solutions/0210.Course-Schedule-II.py) (!!M) <br>
套用模板 return res if len(res) == numCourses else []
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (!!M) <br>
这个题目要做三个判断：1. 判断seqs的拓扑排序是否存在，只需判断len(res) 是否等于len(neighbors) or len(inDegrees), 如果小于说明有孤立节点，如果大于说明有环，两者都不存在拓扑排序; 2. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素, 即每一层只有一个选择: if len(q)>1: return False; 3. 最后判断这个唯一的拓扑排序res是否等于org
- [0269. Alien Dictionary](Solutions/0269.Alien-Dictionary.py) (!!H) <br>
只需要比较word[i]与word[i+1]中每个char，即可得到inDegree的关系以及neighbors的关系



### [BFS in Matrix](/Breadth-First-Search.py) (隐式图搜索问题!!!)
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (!!M, youtubed) <br>
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
Solution 2: dynamic connection problem, Union Find
- [0994. Rotting Oranges](Solutions/0994.Rotting-Oranges.py) (M) <br>
Step 1. append the rotten ones to the first level, Step 2: bfs to turn the adjacent fresh ones into rotten ones. 在class solution(): 后面定义全局变量 EMPTY = 0; FRESH = 1; MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
- [286. Walls and Gates](Solutions/0286.Walls-and-Gates.py) (M) <br>
Step 1: append all the gates into the queue; Step 2: change all the "INF" to a value that equals the layer number
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (!!M) <br>
solution 1: 利用对称性质: x,y=abs(x),abs(y); q.append(neighbor) only if (-2 <= next_x <= x + 2 and -2 <= next_y <= y + 2); 1816 ms<br>
solution 2!!!: 从source和destination两端同时进行bfs!!!! if visited_src & visited_des: return cnt_src + cnt_des; 452 ms<br>
solution 3: recurrsion with memorization: cache[(x, y)] = min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1; 60 ms<br>
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (!!M) <br>
定义一个wordSet = set(wordList)来降低时间寻找下一个neighborWord的复杂度到O(26L); 利用双端BFS大大提高速度，在双端BFS的过程中判断if not q_src or not q_des: 则说明q_src或q_des里面的所有possible neighbor都不在wordList里面，也就是没有必要继续进行了; The idea behind bidirectional search is to run two simultaneous searches: one forward from the initial state and the other backward from the destination state — hoping that the two searches meet in the middle. The motivation is that b^(d/2) + b^(d/2) is much less than b^d. b is branch number, d is depth.
- [1162. As Far from Land as Possible](Solutions/1162.As-Far-from-Land-as-Possible.py) (M) <br>
bfs: the maximum distance is steps needed to change all WATER to be LAND; solution 2: DP same as 542. 01 matrix
- [0542. 01 Matrix](Solutions/0542.01-Matrix.py) (M) <br>
bfs: the maximum distance is steps needed to change all WATER to be LAND; solution 2: DP same as 542. 01 matrix
- [0317. Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (!!H) <br>
Use reachable_cnt[i][j] to record how many times a 0 grid has been reached and use dist[][] to record the sum of distance from all 1 grids to this 0 grid. Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS. in the bfs, we do level bfs and update the reachable_cnt matrix and dist matrix. reach bfs, all position are visited, so O(M*N*k) where k is how many building are there or how many bfs are triggered. Finnaly return the min of dist[i][j] if reachable_cnt[i][j] = total number of buildings. Strong Prune: if if starting from building (i, j), can reach all other building? if not, that means at least one building is isolated and can not be reached, then return -1, in each BFS we use reachableBuildings to count how many 1s we reached. If reachableBuldings != totalBuildings - 1 then we know not all 1s are connected are we can return -1 immediately, which greatly improved speed.




# [Binary Tree, Divide and Conquer](/Binary-Tree-Divide-and-Conquer.py) <br> 
- [0144. Binary Tree Preorder Traversal](Solutions/0144.Binary-Tree-Preorder-Traversal.py) (M) memorize the iterative version using stack
- [0094. Binary Tree Inorder Traversal](Solutions/0094.Binary-Tree-Inorder-Traversal.py) (M) memorize the iterative version using stack
- [0104. Maximum Depth of Binary Tree](Solutions/0104.Maximum-Depth-of-Binary-Tree.py) (E) <br>
rootDepth = max(leftDepth, rightDepth) + 1
- [0257. Binary Tree Paths](Solutions/0257.Binary-Tree-Paths.py) (!!E) <br>
for leftPath in leftPaths: rootPaths.append(str(root.val) + "->" + leftPath); 注意递归出口 if not root.left and not root.right: 注意这里往往需要判断之后根节点没有左右节点的特殊的情况，养成好习惯，尤其是本题，没有这个判断无法输出正确结果
- [0112. Path Sum](Solutions/0112.Path-Sum.py) (E) <br>
Similar with 257, find all the paths and put all the pathSums in a set. 
- [0113. Path Sum II](Solutions/0113.Path-Sum-II.py) (!!M) <br> 
Solution 1: 碰到打印所有路径的问题，第一反应就是带backtracking the dfs
Solution 2: similar with 257 and 112, we just find all the possible paths.
- [0437. Path Sum III](Solutions/0437.Path-Sum-III.py) (M) <br>
不需要从根节点出发，所以 leftCnt_withoutRoot = self.pathSum(root.left, sum); leftCnt_withRoot = self.pathSum(root.left, sum - root.val), why doesnot work?
- [0596. Minimum Subtree](Solutions/0596.Minimum-Subtree.py) (LintCode) <br>
Divide and Conquer的方法输出以root为根的subTree的subSum，然后每次与minSum打擂台进行比较，注意python中定义全局变量可以用self.minSum = float("inf"), self.minNode = None，在主函数中定义这两个变量就可以了
- [0597. Subtree with Maximum Average](Solutions/0597.Subtree-with-Maximum-Average.py) (LintCode) 同上 Divide and Conquer
- [0124. Binary Tree Maximum Path Sum](Solutions/0124.Binary-Tree-Maximum-Path-Sum.py) (H) <br>
题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter. 方法是定义一个self.maxSum在helper函数中去打擂台。helper 函数return the maxPathSum for tree ended with root: return max(left of root, right of root) + root.val; 打擂台: self.maxSum = max(self.maxSum, leftmax + rightMax + root.val)
- [0110. Balanced Binary Tree](Solutions/0110.Balanced-Binary-Tree.py) (E) <br>
helper function return (if the tree is balanced, maxDepth); rootIsBalan = leftIsBalan and rightIsBalan and abs(leftMaxDepth - rightMaxDepth) <= 1
- [0543. Diameter of Binary Tree](Solutions/0543.Diameter-of-Binary-Tree.py) (E) <br>
helper function 是 104. Maximum Depth of Binary Tree, 在helper function 中用 self.maxDmtr 去打擂台, self.maxDmtr = max(self.maxDmtr, leftDepth + rightDepth)
- [0235. Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py) (E) <br>
因为是BST, 所以if p.val < root.val < q.val or q.val < root.val < p.val or p.val == root.val or q.val == root.val: return root; Otherwise 要么去左边找要么去右边找。
- [0236. Lowest Common Ancestor of a Binary Tree](Solutions/0236.Lowest-Common-Ancestor-of-a-Binary-Tree.py) (!!M) <br>
- [0700. Search in a Binary Search Tree](Solutions/0700.Search-in-a-Binary-Search-Tree.py) (E) <br>
- [0938. Range Sum of BST](Solutions/0938.Range-Sum-of-BST.py) (E) <br>
- [0226. Invert Binary Tree](Solutions/0226.Invert-Binary-Tree.py) (E) <br>
STEP 1. divide 先局部有序; STEP 2. conquer 再整体有序
- [0617. Merge Two Binary Trees](Solutions/0617.Merge-Two-Binary-Trees.py) (E) <br>
- [0108. Convert Sorted Array to Binary Search Tree](Solutions/0108.Convert-Sorted-Array-to-Binary-Search-Tree.py) (!!E) <br>
we can always choose the left middle number as root, or always choose right middle number as root, or sometimes left sometimes right as root. That is why the answer is not unique
- [0098. Validate Binary Search Tree](Solutions/0098.Validate-Binary-Search-Tree.py) (M) <br>
注意判断条件不仅仅是left.val<root.val<right.val而是max of left < root < min of right; helper函数返回以root为根的树(是不是BST，max and min value in the tree); if (isLeftBST and isRightBST and maxLeft < root.val < minRight): return True
- [0426. Convert Binary Search Tree to Sorted Doubly Linked List](Solutions/0426.Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List.py) (!!M)  <br>
solution 1: 定义两个全局变量self.head, self.curr，进行in order traversal的过程中不断更新curr的位置并hook up nodes
- [0114. Flatten Binary Tree to Linked List](Solutions/0114.Flatten-Binary-Tree-to-Linked-List.py) (M) <br>
divide and conquer: root.right = leftHead; root.left = None; 找到tail并让tail.right = rightHead
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (!!M) <br>
use a stack with controlled recursion, some part of the algorithm is similar with the in order traversal of a tree using a stack; define a getLeftMost function, each time we call next function, we pop the smallestNode from stack and run getLeftMost function for the smallestNode.right if smallestNode.right exist.  this algorithm has space complexity of O(h)
- [0285. Inorder Successor in BST](Solutions/0285.Inorder-Successor-in-BST.py) (!!M) <br>
Divide and conquer: if p.val < root.val: return left if left else root; else: return right
- [0701. Insert into a Binary Search Tree](Solutions/0701.Insert-into-a-Binary-Search-Tree.py) (M) <br>
if val > root.val则更新root.right: root.right = self.insertIntoBST(root.right, val); else: root.left = self.insertIntoBST(root.left, val); return root.  这题的recursion exist should be: if not rot: return TreeNode(val). 另外, Time complexity: O(H), where H is a tree height. That results in O(logN) in the average case. So it takes O(logN) to insert an element into a BST.
- [0450. Delete Node in a BST](Solutions/0450.Delete-Node-in-a-BST.py) (H) <br>
Case 1: if node is a leaf, simply delete it Case 2: If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then delete the successor in the right subtree root.right = deleteNode(root.right, root.val). Case 3: If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val). define a function to find successor: find the successor of the root by taking one step right and always left, cuz the successor is the node just larger than the root. define a function to find predecessor: find the predecessor of the root by taking one step left and then always right.
- [1214. Two Sum BSTs](Solutions/1214.Two-Sum-BSTs.py) (M) <br>
Iteratively do an inorder traversal for root1, and store the val in a hashSet; then itteratively do an inorder traversal for root2, and at the same time check if a target-val is in the hashSet. time complexity: O(M + N). 算法跟two sum是一样的，如果闭着眼睛能写要会iterative in-order traversal的哈！
- [1038. Binary Search Tree to Greater Sum Tree](Solutions/1038.Binary-Search-Tree-to-Greater-Sum-Tree.py) (M) <br>
do a in order traversal (reversed version: go all the way to the right) to keep track the addValues
- [0095. Unique Binary Search Trees II](Solutions/0095.Unique-Binary-Search-Trees-II.py) (!!M) <br>
helper(start, end): return the trees from start to end.  Finally return helper(1, n). Time complexity: The main computations are to construct all possible trees with a given root, that is actually Catalan number Gn (超纲).
- [0096. Unique Binary Search Trees](Solutions/0096.Unique-Binary-Search-Trees.py) (M) <br>
same as 95, return len(helper(1, n)).
- [0241. Different Ways to Add Parentheses](Solutions/0241.Different-Ways-to-Add-Parentheses.py) (M) <br>
similar with 95, in helper function, return all the different results to add parentheses for input, for i in range(len(input): divide into leftResults and rightResults. Optimization: use a memo dictionary in the helper function to memorize the input that has already been calculated.






# [Depth First Search / Backgracking](/Depth-First-Search.py)
### [Combination](/Depth-First-Search.py)
- [0078. Subsets](Solutions/0078.Subsets.py) (!!M) <br>
C(m, n)：m个里面找出n个的组合问题; 模板的DFS + back tracking求combination问题 O(NS), S是solution的个数，这里S=2^N; 注意两点：1.res.append(curr.copy()); has to be a deep copy; 2. self.dfs(nums, i + 1, curr, res) 要从i+1开始cuz不能回头找会重复
其实可以不用把res传进去，定义一个全局变量self.res即可，可以简化dfs传入的参数。
- [0090. Subsets II](Solutions/0090.Subsets-II.py) (!!M)<br>
如果输入存在重复元素，[1, 2, 2]的遍历中，我们只取前面的那个2，对于后面的那个2，如果不是挨着前面那个2选的，也就是说i != startIndex，那么就不要放后面那个2，这样会造成重复出现[1,第一个2],[1,第二个2], 注意可以挨着第一个2来选第二个2是可以的，因为允许出现[1,2,2]作为答案。所以contraint是: if (i >= 1 and nums[i] == nums[i-1]) and i != startIndex: continue
- [0039. Combination Sum](Solutions/0039.Combination-Sum.py) (M) <br>
模板：find_solution: if target == 0； Is_not_valid：if nums[i] > targetstart是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
- [0040. Combination Sum II](Solutions/0040.Combination-Sum-II.py) (M) <br>
输入中存在重复元素，避免重复输出的方法与Subsets II一样; 模板 find_solution: if target == 0; is_not_valid: if (nums[i] > target) or (i >= 1 and nums[i] == nums[i-1]) and i != startIdx
- [0518. Coin Change 2](Solutions/0518.Coin-Change-2.py) (M) <br>
与Combination Sum一模一样，只是题目不要求输出所有可能组合，只要求输出可能组合的数目，所以可以用DP解。不理解DP解的for循环顺序。有时间请教高人，怎么理解这个DP的顺序。
- [0216. Combination Sum III](Solutions/0216.Combination-Sum-III.py) (M)<br>
self.dfs(nums, k - 1, n - nums[i], i + 1, curr)   # 不能出现重复数字，所以从i+1开始
- [0090. k Sum II](Solutions/0090.k-Sum-II.py) (M Lintcode) <br>
exactly the same as 216.
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (M)<br>
self.dfs(nums, target - nums[i], 0, curr, res)  # 顺序不重要（(1, 3)和(3, 1)都可以，所以让i从0开始; solution 2: dp. 
- [0131. Palindrome Partitioning](Solutions/0131.Palindrome-Partitioning.py) (!!!M) <br>
递归的定义：从s中的start位置开始，挑一些位置切割，判断从start到i的部分是否为回文，如果是就放入curr中，如果i到了string末尾了则说明此事curr是一种组合方式，放入res中 <br>
- [0332. Reconstruct Itinerary](Solutions/0332.Reconstruct-Itinerary.py) (!!M) <br>
有向图的遍历问题，LeetCode关于有向图的题只有两道Course Schedule和Course Schedule II，而那两道是关于有向图的顶点的遍历的，而本题是关于有向图的边的遍历。每张机票都是有向图的一条边，我们需要找出一条经过所有边的路径，那么DFS不是我们的不二选择. 这题选择interative way to do backtracking更简单。


### [Permutation](/Depth-First-Search.py)
- [0046. Permutations](Solutions/0046.Permutations.py) (!!M)<br>
与combination相比少了一个startIndex参数，加入visited用于防止重复出现; append之后需要将visited[i]变为True; pop出来之后将visited[i]再变回False
- [0052. N Queens II](Solutions/0052.N-Queens-II.py) (!!H) <br>
排列问题：先打印出数组[0, 1, 2, 3....n]中所有的可能排列：[[0,1,2,3], [1,3,0,2].....]，其中的每一个子数组表示一种可能的方法，子数组中的数字表示在哪个数字的地方放一个Queen，数字对应的下标位置是放那个Queen的行，数字的值是放那个Queen的列。由于Queen可以很冲直撞，所以列是不能相同的，所以需要去重，用visited标记就可以。又由于Queen还可以斜着走，所以横纵坐标的和与差不能相同，也需要用visited标记。用三个字典visited_col, visited_sum, visited_diff分别存储列号，横纵坐标之和，横纵坐标之差有没有被用过
- [0051. N Queens](Solutions/0051.N-Queens.py) (H)<br>
- [0047. Permutations II](Solutions/0047.Permutations-II.py) (M) <br>
模板: is_not_valid: if i in self.visited: continue; if (i > 0 and nums[i] == nums[i-1]) and (i-1) not in self.visited: continue
- [0031. Next Permutation](Solutions/0031.Next-Permutation.py) (M) <br>
step 1: sweeping from right to left, find the first decreasing element; Step 2: sweep from right to left, find the first element larger just than nums[i], then swap nums[i] and nums[j], then swap all the items starting from i+1
- [0267. Palindrome Permutation II](Solutions/0267.Palindrome-Permutation-II.py) (!!M)  <br>
step 1: put the characters that have seen two times in the char list; now we have a charList that only holds char that appears even times, eg: "aaaabbc" now becomes "aab", Step 2: we only need to do permutation for this charList, so the time complexity is O((n/2)!), which is quite an improve. Step 3: when return the results, we just use the permuation generated in steps 2 + permuation[::-1]
- [0060. Permutation Sequence](Solutions/0060.Permutation-Sequence.py) (M)  <br>
It really is all about pattern finding; https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)


### [树上的DFS](/Depth-First-Search.py) <br>
- [0113. Path Sum II](Solutions/0113.Path-Sum-II.py) (!!M) <br> 
Solution 1: 碰到打印所有路径的问题，第一反应就是带backtracking the dfs
Solution 2: similar with 257 and 112, we just find all the possible paths.
- [0298. Binary Tree Longest Consecutive Sequence](Solutions/0298.Binary-Tree-Longest-Consecutive-Sequence.py) (!!M) <br> 
Solution 1: 带backtracking the dfs
solution 2: backtracking dfs 的 interative 的写法 by using a stack
Solution 3: 不需要打印所有的路径，所以可以用普通的二叉树的divide and conquer方法：helper function return the Longest Consecutive Sequence **started with** root node, 全局变量res进到helper function中去打擂台
- [0549. Binary Tree Longest Consecutive Sequence II](Solutions/0549.Binary-Tree-Longest-Consecutive-Sequence-II.py) (M) <br> 
Solution 1: divide and conquer方法：helper function return the increasing and decreasing Longest Consecutive Sequence **started with** root node, 全局变量res进到helper function中去打擂台: self.res = max(self.res, root_increasing + root_decreasing - 1)



### [图上的搜索](/Depth-First-Search.py) <br>
- [0079. Word Search](Solutions/0079.Word-Search.py) (!!M) <br>
经典的backtrack题，whenever we find a char == word[0], we trigger a backtracking dfs. in dfs template, find solution:  currIdx == len(word); is_not_valid:  if new_x < 0 or new_x >= len(self.board) or new_y < 0 or new_y >= len(self.board[0]): continue; if (new_x, new_y) in self.visited: continue; if self.board[new_x][new_y] != word[currIdx]: continue; 需要一个visited set来标记已经走过的路径避免走重复的路径。
- [0212. Word Search II](Solutions/0212.Word-Search-II.py) (!!H) <br>
要求打印所有路径所以：Trie + Backtracking DFS. in dfs template, find_solution:  if currNode.isEnd; is_not_valid: if next_x < 0 or next_x >= len(self.board) or next_y < 0 or next_y >= len(self.board[0]): continue; if (next_x, next_y) in self.visited: continue; if self.board[next_x][next_y] not in currNode.child: continue.
- [0126. Word Ladder II](Solutions/0126.Word-Ladder-II.py) (!!H) 打印/输出所有满足条件的路径必用DFS
Step 1. 从end到start做BFS，记录每一个节点到end节点的距离，存入hashmap中 eg: distance["dog"] = 2 <br>
Step 2. 从start到end做DFS，每走一步都必须确保end的distance越来越近(if self.distance[nextWord] >= self.distance[currWord]: continue)。最后将路径都存入到res里
695. Max Area of Island
301. Remove Invalid Parentheses
489. Robot Room Cleaner
Sudoku Solver
980. Unique Paths III
3. 二维数组下的DFS搜索（八皇后、黄金矿工、数独）
93 复原IP地址
996 正方形数组的数目
1239 串联字符串的最大长度











# [Binary Search](/Binary-Search.py)
- [0704. Binary Search](Solutions/0704.Binary-Search.py) (!!E) <br>
九章模板: 1. while start + 1 < end; 2. mid = start + (end - start) // 2; 3. 循环内只写两个分支； 4. 往左逼find the first X; 5. 往右逼find the last X
- [0702. Search in a Sorted Array of Unknown Size](Solutions/0702.Search-in-a-Sorted-Array-of-Unknown-Size.py) (M) <br>
Find end point using "double method", same as dynamic array
- [0069. Sqrt(x)](Solutions/0069.Sqrt(x).py) (E) <br>
两种方法：1. Binary Search; 2. Newton's Method. x<sub>k+1</sub> = (x<sub>k</sub> + x/x<sub>k</sub>) / 2; O(logN) since the set converges quadratically
- [0034. Find First and Last Position of Element in Sorted Array](Solutions/0034.Find-First-and-Last-Position-of-Element-in-Sorted-Array.py) (!!M) <br>
用两次二分分别找first pos of target and last pos of target. 想找first position of target，要保证两点：1. while循环里的判断要往左逼，也就是if nums[mid] **>=** target: end = mid； 2. 就把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉，因为start肯定是小于end的。<br>
Follow up: In a sorted array [1,3,4.......], search the elements that are in a certain range eg:[10, 100]. solution: 用两次二分分别找first position of 10 and last position of 100.  Then the elements between the two positions should be in range [10, 100].
- [0035. Search Insert Position](Solutions/0035.Search-Insert-Position.py) (E) <br>
This is to implement bisect.bisect_left(nums, target), which returns the position of inserting target in order to keep nums sorted
- [0278. First Bad Version](Solutions/0278.First-Bad-Version.py) (E)
- [0153. Find Minimum in Rotated Sorted Array](Solutions/0153.Find-Minimum-in-Rotated-Sorted-Array.py) (!!M) <br>
解法一：nums[mid]可以与nums[0]比较；解法二：也可以与nums[-1]比较；解法三：也可以与nums[end]比较
- [0154. Find Minimum in Rotated Sorted Array II](Solutions/0154.Find-Minimum-in-Rotated-Sorted-Array-II.py) (H) <br>
与153类似，只是array里可能有duplicates，采用153的解法三，唯一不同的是：nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半，因为eg: nums=[2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2........], 由于不知道mid是1前面的2还是1后面的2，所以无法确定是drop前面还是drop后面，只能保险地把end往前挪一位，所以154这题in extreme case, 时间复杂度是O(N)
- [0039. Recover Rotated Sorted Array](Solutions/0039.Recover-Rotated-Sorted-Array.py) (M LintCode) <br>
154 相同方法binary search找到minPos, 然后三步反转法recover
- [0033. Search in Rotated Sorted Array](Solutions/0033.Search-in-Rotated-Sorted-Array.py) (M) 画个图分几个区间讨论就可以了！
- [0852. Peak Index in a Mountain Array](Solutions/0852.Peak-Index-in-a-Mountain-Array.py) (E)<br>
- [0162. Find Peak Element](Solutions/0162.Find-Peak-Element.py) (M) <br>
OOXX问题，找到第一个出现的X，X是the first position of 递减的序列
- [0390. Find Peak Element II](Solutions/0390.Find-Peak-Element-II.java) (H Lintocde) <br>
先二分找到中间某一行的最大值位置(i, j)，然后这个最大值的地方向上(i, j-1)和向下(i, j+1)分别比一下，如果(i, j)最大，那恭喜找到了peak, 如果向上更大，那就往上爬到(i,j-1), 此时i行及其以下的行都可以丢掉了，然后在j-1那一列查找最大值的位置(ii, j-1), 这时候在(ii, j-1)这个位置向左(ii-1, j-1)向右(ii+1, j-1)分别比一下，如果发现(ii, j-1)最大，那么恭喜找到peak了，如果发现(ii-1, j-1)更大，那就继续往(ii-1, j-1)爬一步，可以直接丢掉j-1列及其右边的部分了。这样的时间复杂度是T(N)=O(N 在第i行查找最大值)+T(N/2), 所以时间复杂度T(N) = O(N)+O(N/2)+O(N/4)+....+O(2)+O(1) = O(N)+O(N/2)+O(N/4)+....+O(2)+O(1)+O(1)-O(1) = O(2N)-O(1) = O(N).
- [0875. Koko Eating Bananas](Solutions/0875.Koko-Eating-Bananas.py) (M) <br>
If Koko can finish eating all the bananas (within H hours) with an eating speed of K, she can finish with a larger speed too. So it is a OOOXXX problem trying to find the first X. end is set to be max(piles). Every time find if it posible to eat all the bananas with speed mid. if yes, then drop the right part, if no, then drop the left."""
- [0183. Wood Cut](Solutions/0183.Wood-Cut.py) (!!H Lintcode) <br>
If we can cut into pieces with lens, then we can also cut into prices with len - 1, So this is a OOOXXX problem, to find the last O. <br>
lintcode 437 copy books!!
- [0074. Search a 2D Matrix](Solutions/0074.Search-a-2D-Matrix.py) (M) <br>
Think it as a long 1D array with MxN element, then we can use binary search; row = mid // n, col = mid % n; O(log(MN)), O(1)
- [0240. Search a 2D Matrix II](Solutions/0240.Search-a-2D-Matrix-II.py) (M) <br>
start from left bottom, head up to right top, each comparism rule out a row (i-1=1) or rule out a col (j+=1)
- [0050. Pow(x, n)](Solutions/0050.Pow(x,n).py) (M) <br>
if mod == 0: res * = x^div; else: res * = x^div * x
- [0029. Divide Two Integers](Solutions/0029.Divide-Two-Integers.py) (M) <br>
eg: 10//3, 每次通过右移3 << 1的方法将3乘以2,这种算法是O(N), 每次都右移几次3 << x, 相当于3x2x2x2...,直到3x2x2x2...>10, 然后取余数继续这个算法
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) <br>
target是随着i的移动而变化的binary search





# [Sort](/Sort.py) check Celia's template for partition, 九章模板。
- [0912. Sort an Array](Solutions/0912.Sort-an-Array.py) (!!M Youtubed) <br>
quick sort: 用partition function先整体有序，返回pivotPos，然后再pivotPos两边分边局部有序
merge sort: 用mid分成左右两部分，leftArr和righArr分别记录局部的有序数组，然后merge到arr数组
- [0179. Largest Number](Solutions/0179.Largest-Number.py) (M) <br>
quick sort, self-define comparing two strings by: if s1 + s2 <= s2 + s1: return True else False
- [0969. Pancake Sorting](Solutions/0969.Pancake-Sorting.py) (M) <br>
for i in range(lens-1, -1, -1 ): Find maxIndex -> flip max to top -> flip max to bottom of the whole arr -> repeat
<br> 147. Insertion sort a linked list <br>
- [0280. Wiggle Sort](Solutions/0280.Wiggle-Sort.py) (M) <br>
O(N): 从左到右扫一遍，不满足条件的交换就好了。定义一个变量prevShouldLessThanCurr, in the for loop, prevShouldLessThanCurr = not prevShouldLessThanCurr every step, and based on prevShouldLessThanCurr is true or not, we swap nums[i-1] with nums[i] or not.


### [Partition and quick select](/Sort.py) 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode) 
好多细节!!要背熟理解partition这个函数. partition这个函数的作用是O(N)找到某个数k在一个无序数组中所在的位置，并按照这个数k将该数组分为左右两部分。
399. Nuts & Bolts Problem (Lintcode)
用bolt作为nuts的pivot进行partition, 用nut作为bolts的pivot进行partition
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M Youtubed)  <br>
solution 1: quick select O(N) in average!!!!; solution 2: heap O(NlogK): heapq.heappush(numsHeap, num); heapq.heappop(numsHeap)
<br> 一个follow up: find the median in a un-sorted array.  solution: this is to find the Kth largest in an array, where K=len(arr)//2
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E) <br>
solution 1: 同向双指针； solution 2: 反向双指针同上题
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
STEP 1: 反向双指针（或同向双指针）对[-1,-2,4,,5,-3,6]进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]; STEP 2: 再正负正负安插
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) <br>
同向双指针: move '2's to the right first, then move '1's to the middle

### [Sorted Array](/Sort.py) 
- [0056. Merge Intervals](Solutions/0056.Merge-Intervals.py) (M) <br>
sort the intervals first, res = []; for interval in intervals: if the interval start time is larger than the largest end time in res, then the interval cannot be merged, then res.append(interval), else then res[-1][1] = max(res[-1][1], interval[1])
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) <br>
target是随着i的移动而变化的binary search






# [Linked List](/Linked-List)
- [0021. Merge Two Sorted Lists](Solutions/0021.Merge-Two-Sorted-Lists.py) (E) <br>
如果需要return一个新的headNode，一般定义一个dummyNode = ListNode(0), curr = dummyNode; 最后return dymmyNode.next
- [0148. Sort List](Solutions/0148.Sort-List.py) (!!M) <br>
step1: divide: 先找到mid, 然后在mid处cut成左右half, 再分别sort left and right; step 2: merge, 同21
- [0206. Reverse Linked List](Solutions/0206.Reverse-Linked-List.py) (!!E) 需要熟背理解
- [0092. Reverse Linked List II](Solutions/0092.Reverse-Linked-List-II.py) (M) <br>
reverse node from m to n: step 1: find node_m and node_m_minus; find node_n and node_n_plus; step 2. reverse the nodes from m to n; 3. hook up node_m_minus with node_n, node_m with node_n_plus
- [0024. Swap Nodes in Pairs](Solutions/0024.Swap-Nodes-in-Pairs.py) (M) <br>
想要reverse n1->n2->n3->n4->n5->n6 in pairs: step 1: 在n1前面添加一个dummy n0, 然后在while curr循环里每次都调用reverse函数，reverse函数做的事情是操作四个节点n0->n1->n2->n3, 将其变成n0->n2->n1->n3, 然后return n1，注意每次都是return想要swap的两个节点的前一个节点！step 2: curr = return的n1，然后继续循环
- [0025. Reverse Nodes in k-Group](Solutions/0025.Reverse-Nodes-in-k-Group.py) (!!H) <br>
similar with 24, 在reverse函数中要做的事情是reverse n0->n1->n2------>nk->n_k+1 to be n0->nk------>n2->n1->n_k+1 and return n1; 也是分两步: 首先翻转n1->n2------>nk, 然后hook up n0 with n_k, n1 with n_k+1
- [0138. Copy List with Random Pointer](Solutions/0138.Copy-List-with-Random-Pointer.py) (!!M) <br>
step 1: create new node and interleave new node into original node; step 2: link the random pointer for the new nodes; step 3: seperate the interleaved old nodes and new nodes
- [0141. Linked List Cycle](Solutions/0141.Linked-List-Cycle.py) (E) <br>
在做环形list的题目时, while slow != fast是很常用的句型
- [0142. Linked List Cycle II](Solutions/0142.Linked-List-Cycle-II.py) (!!M) <br>
step 1: 快慢指针找到相遇的点; step 2: 重新定义两根指针p1, p2分别从head和上面相遇的点出发，然后p1,p2相遇的地方就是环的入口
- [0287. Find the Duplicate Number](Solutions/0287.Find-the-Duplicate-Number.py) (M) <br>
把这个数组的每一个数num看成这样一个linked list node: num的下标代表.val, num的值代表.next指向下一个node。那么如果存在重复的num，那就表示有两个不同node都指向了同一个公共，也就是成环的地点。这么想这个题目就和142一样了，具体实现过程中对p取一个nums[p]，就相当于取一个p.next
- [0160. Intersection of Two Linked Lists](Solutions/0160.Intersection-of-Two-Linked-Lists.py) (E) <br>
两个指针currA, currB; if not currA: currA = headB; if not currB: currB = headA
- [0002. Add Two Numbers](Solutions/0002.Add-Two-Numbers.py) (!!M) <br>
本题的考点是关于如何新建一个linked list, 要用someNode.next = ListNode(someVal), 而不是简单的修改value; 还考察了是否细心, 最后很容易漏掉carryBit != 0的判断"
<br> 23. Merge k Sorted Lists: heapq to find the minimum of the k lists. O(NlogK) https://www.youtube.com/watch?v=Uz4fTr34270 <br>




# [SubArray](/SubArray.py)
- [0053. Maximum Subarray](Solutions/0053.Maximum-Subarray.py) (!!E) <br>
Maintian a prefixSum and minPrefixSum, so that maxSubSum = max(maxSubSum, prefixSum - minPrefixSum)
- [0724. Find Pivot Index](Solutions/0724.Find-Pivot-Index.py) (E) <br>
leftSum = prefixSum[i] # prefixSum[i]是不包括nums[i]的; ightSum = prefixSum[-1] - prefixSum[i] - nums[i] 
- [0560. Subarray Sum Equals K](Solutions/0560.Subarray-Sum-Equals-K.py) (!!M) <br>
新建一个prefixSumDict = {0: 1}, key是prefixSum, val是how many times the prefixSum appears; if prefixSum - k in prefixSumDict: 等价于if prefixSum[j+1]-prefixSum[i] == k
- [0053. Maximum Subarray](Solutions/1074.Number-of-Submatrices-That-Sum-to-Target.py) (H) <br>
用前缀和优化, 令 matrix[i][0] = matrix[i][0] + matrix[i][1] + ... + matrix[i][j], 这样matrix的行里保存的就是上面所有列的和了
然后枚举左右边界left and right, 确定左右边界left and right 之后，接下来就相当于在一列内(指的是right那一列), 求一个数组连续子串和为0的问题了
O(M* N* N)
- [0523. Continuous Subarray Sum](Solutions/0523.Continuous-Subarray-Sum.py) (M) <br>
prefixSumMap = {0: -1} # key: prefixSum[j], val: j/position, initial position should be -1; prefixSum += num; prefixSum = prefixSum % k 因为题目要求要能被subArray Sum 要能被k整除
- [0974. Subarray Sums Divisible by K](Solutions/0974.Subarray-Sums-Divisible-by-K.py) (M) <br>
prefixSumDict = {0: 1} # key is the prefixSum, val is how many times the prefixSum appears; prefixSum += num; prefixSum %= K
- [0139. Subarray Sum Closest](Solutions/0139.Subarray-Sum-Closest.py) (Lintcode) <br>
题目要求NlogN, 那就是疯狂暗示要sort, prefixSumList = [(0, -1)] # (0, 1) are prefixSum and index; 对prefixSum来进行sort，这样最小的subArrSum (或者prefixSums[j+1][0] - prefixSums[i][0])就一定来自于相邻的两个prefisxSums了
- [0152. Maximum Product Subarray](Solutions/0152.Maximum-Product-Subarray.py) (M) <br>
最大值问题。用一个数组记录最大的正数maxDP[i]，另一个数组记录最小的负数minDP[i], maxDP[i]表示以i为结尾的subarray的最product. 分nums[i]的正负,更新maxDP[i]和minDP[i]。maxDP[i] = max(nums[i], maxDP[i-1]* nums[i]) if nums[i]>0






# [Two Pointers](/Two-pointers.py)
### [反向双指针](/Two-pointers.py)
- [0977. Squares of a Sorted Array](Solutions/0977.Squares-of-a-Sorted-Array.py) (E) <br>
three pointers: i starts from beginning of A; j starts from the end of A; k starts from end of res 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode) <br>
note 1: temp = nums[i], 出循环后需要nums[i] = temp回来; note 2: 先判断j, j-=1出来后nums[i]=nums[j] 
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E) <br>
solution 1: 同上31的方法做partition; solution 2: 同向双指针: anchor and curr, swap A[anchor] and A[curr] when A[curr] is even
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
STEP 1: 反向双指针进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]; STEP 2: 再来进行正负正负正负安插
- [0561. Array Partition I](Solutions/0561.Array-Partition-I.py) (E) <br>
sort the arr first, then the maximum sum of pairs is the sum of every other num
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) <br>
solution 1: typical partition problem, step 1: 先把0放到最前面; step 2: 再把2放到最后
solution 2: 同向双指针的方法也应该理解掌握！
- [0238. Product of Array Except Self](Solutions/0238.Product-of-Array-Except-Self.py) (M) <br>
定义两个数组分别记录product before ith num: fwd[i]=fwd[i-1] * nums[i-1] and product after ith num: bwd[i]=bwd[i+1] * nums[i+1], then res[i]=fwd[i] * bwd[i]
- [0011. Container With Most Water](Solutions/0011.Container-With-Most-Water.py) (!!M) <br>
if height[i] > height[j]: j -= 1  # meaning that 右边的栅栏更低，所以把右边指针移动一下，希望能用长度去compromise宽度，即寄希望于min(height[i], height[j])会变大，来compromise掉(j - i)的变小. 为什么不移左边指针呢？因为移动左边的话，min(height[i], height[j])不会变大，但是(j - i)一定变小，所以面积一定变小.


### [同向双指针](/Two-pointers.py)
- [0019. Remove Nth Node From End of List](Solutions/0019.Remove-Nth-Node-From-End-of-List.py) <br>
fast 比 slow 先出发 n 步即可
- [0088. Merge Sorted Array](Solutions/0088.Merge-Sorted-Array.py) <br>
modify nums1 in-place, use i, j, k = m - 1, n - 1, m + n -1; 把最大的数放到nums1的后面
- [0283. Move Zeroes](Solutions/0283.Move-Zeroes.py) <br>
anchor keeps all the non-zero numbers, while curr runs forward; whenever curr equals a non-zero number, switch it to anchor.  Solution 2: partition using the method in 31, but not accepted cuz partition changes the original order of non-zero numbers
- [0026. Remove Duplicates from Sorted Array](Solutions/0026.Remove-Duplicates-from-Sorted-Array.py) (!!E) 典型的同向双指针
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) <br>
同向双指针法，如果碰到符合条件的，把j往前挪到不重复的元素去。dfs解subset问题里的去重是怎么做的：前面的3用到了，后面的3就跳过就可以了。
- [0042. Trapping Rain Water](Solutions/0042.Trapping-Rain-Water.py) (!!H) <br>
首先找到最高highestBar的位置。然后从左边往最高的位置扫，同时maintain一个指针记录leftHighest的高度，如果扫到的地方i小于这个leftHighest的高度，
则说明i这个地方可以蓄水，可蓄水量为leftHighest的高度减去i的高度；如果扫到的地方i大于这个leftHighest的高度，则说明i这个地方不可以蓄水，所以这时候要更新leftHighest为i的高度。同理对右边做同样的操作



# [Two Sum]()
- [0001. Two Sum](Solutions/0001.Two-Sum.py) (E) hashMap
- [0167. Two Sum II - Input array is sorted](Solutions/0167.Two-Sum-II-Input-array-is-sorted.py) (E) 反向双指针
- [0170. Two Sum III - Data structure design](Solutions/0170.Two-Sum-III-Data-structure-design.py) (E) hashMap
- [0653. Two Sum IV - Input is a BST](Solutions/0653.Two-Sum-IV-Input-is-a-BST.py) (E) <br>
In order traversal into an array and then use two pointer method
- [1099. Two Sum Less Than K](Solutions/1099.Two-Sum-Less-Than-K.py) (E) 
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) (求和用反向双指针，求差用同向双指针)
- [0609. Two Sum - Less than or equal to target](Solutions/0609.Two-Sum-Less-than-or-equal-to-target.py) (E) <br>
if nums[i] + nums[j] <= target: cnt += j - i		# 注意这里是 cnt += j - i 表示nums[i] 加上 i 到 j之间的任何数，一定也是小于等于target的
- [0015. 3Sum](Solutions/0015.3Sum.py) (!!M) <br>
背模板，注意点一：对i去重；left, right=i+1, lens-1 # 注意点二：left和right的初始值；注意点三：对left和right去重
- [0016. 3Sum Closest](Solutions/0016.3Sum-Closest.py) (M) <br>
- [0259. 3Sum Smaller](Solutions/0259.3Sum-Smaller.py) (M) <br>
优化：if nums[i] * 3 >= target: break；其解法类似609
- [0018. 4Sum](Solutions/0018.4Sum.py) (M) <br>
solution 1: O(N^3): 3Sum模板双指针法。注意这里给j去重不能从j>=1开始，因为要至少让j先取上第一个值i+1之后才能与前一个数比较！不然[0,0,0,0], 0就通不过了；solution 2: O(N^2): hashmap. for循环a, b,保存a+b的值进hashmap, 再for循环c, d, 判断c+d是否在hashmap中
- [0454. 4Sum II](Solutions/0454.4Sum-II.py) (M) <br>
有四个数组，不好用双指针，所以就使用hashmap，用一个hashmap 保存a + b
- [0089. k Sum](Solutions/0089.k-Sum.py) (H Lintcode) <br>
采用动态规划，用dp[i][j][t]表示前i个数里选j个和为t的方案数。dp[i][j][t] = 选A[i-1]: dp[i-1][j-1][t-A[i-1]] + 不选 A[i-1]: dp[i-1][j][t]; initialize: dp[i][0][0] = 1; return dp[lens][k][target]




# [Sweep-Line](/Sweep-Line.py) <br>
- [0391. Number of Airplanes in the Sky](Solutions/0391.Number-of-Airplanes-in-the-Sky.py) (M Lintcode) <br>
扫描线做法：碰到interval的start，也就是起飞一架飞机，当前天上的飞机数++。碰到interval的end，也就是降落一架飞机，当前天上的飞机数--。
Step 1: 我们分别把所有的start和所有的end放进两个数组，并排序。Step 2: 然后从第一个start开始统计，碰到start较小就加一，碰到end较小就减一。并且同时维护一个最大飞机数的max。
- [0253. Meeting Rooms II](Solutions/0253.Meeting-Rooms-II.py) (!!M) <br>
solution 1: 扫描线；minimum meeting rooms required could be understood us maximum meeting rooms in use
Then this problem is exaclty the same as the lintcode 0391. Number of Airplanes in the Sky <br> solution 2: 以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间
<br>
218. The Skyline Problem


# [Greedy](/) <br>
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (!!M) <br>
存在性问题。状态: dp[j]=能不能跳到位置j; 转移方程：dp[j]=True if dp[i] and nums[i]>=j-i) (TLE 注意只要有一个dp[i]是的dp[j]=True了就可以break了). DP解法: O(N^2).  Greedy 解法: O(N) Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index (currPosition + nums[currPosition] >= leftmostGoodIndex). 
If we can reach a GOOD index, then our position is itself GOOD. Iteration continues until the beginning of the array. 
If first position is a GOOD index then we can reach the last index from the first position.







# [Other High Freq](/)
- [0415. Add Strings](Solutions/0415.Add-Strings.py) (!!E) <br>
similar with leetcode 2.  while i >= 0 and j >= 0:  循环之后，还要check while i >= 0: ;  while i >= 0: ; 最后还要check if carryBit > 0:







### [Other DP Problems](https://juejin.im/post/5d556b7ef265da03aa2568d5)
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M)
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


# Other Algorithms
### [Rabin Karp / Rolling Hash]()
- [0028. Implement strStr()](Solutions/0028.Implement-strStr().py) (E) (Rabin Karp Algorithm O(M+N), use Hashcode, ord(ch)-ord("a"))
1062. Logest repeating substring

Tarjan's algorithm: 1192. Critical Connections in a Network


### At last, let's take a look at the famous Algorithm book.
### 看Abby google doc的归类，还有liweiwei Github的归类，根据归类再适当刷一些新题。
### https://blog.csdn.net/fuxuemingzhu/article/details/101900729 很好的分类总结
