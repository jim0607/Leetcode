"""解法一：暴力法，枚举所有子串，并逐一判断 O(N**3), O(1)"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 特判
        lens = len(s)
        if lens < 2:
            return s 
        # 枚举所有长度大于等于2的子串，然后判断哪些是回文子串，如果是回文串，那就比较这个回文串的长度是不是最长的
        maxLen = 1
        res = ''
        for i in range(lens-1):
            for j in range(i+1, lens):
                if self.isPalin(s[i:j+1]):
                    if j+1-i > maxLen:
                        maxLen = j+1-i 
                        res = s[i:j+1]
        return res 
    
    def isPalin(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
      
      
"""解法二：中心扩散法，center spread
暴力法采用双指针两边夹，验证是否是回文子串，时间复杂度比较高，除了枚举字符串的左右边界以外，比较容易想到的是枚举可能出现的回文子串的“中心位置”
从“中心位置”尝试尽可能扩散出去，得到一个回文串。
因此，中心扩散法的思路是：遍历每一个索引，以这个索引为中心，利用“回文串”中心对称的特点，往两边扩散，看最多能扩散多远。
枚举“中心位置”时间复杂度为 O(N)，从“中心位置”扩散得到“回文子串”的时间复杂度为 O(N)，因此时间复杂度可以降到 O(N^2)。
在这里要注意一个细节：回文串在长度为奇数和偶数的时候，“回文中心”的形式是不一样的。
奇数回文串的“中心”是一个具体的字符，例如：回文串 "aba" 的中心是字符 "b"；
偶数回文串的“中心”是位于中间的两个字符的“空隙”，例如：回文串串 "abba" 的中心是两个 "b" 中间的那个“空隙”。"""
class Solution:
    def longestPalindrome(self, s: str) -> str: 
        lens = len(s)
        if lens < 2:
            return s 
        
        maxLen = 1
        res = s[0]   # 初始化为s[0]的原因是如果完全找不到一个回子串至少要输出第一个元素
        for i in range(lens):
            palin_odd, lens_odd = self._central_spread(s, i, i)
            palin_even, lens_even = self._central_spread(s, i, i+1)
            
            (currMaxPalin, currMaxLen) = (palin_odd, lens_odd) if lens_odd > lens_even else (palin_even, lens_even)
            if currMaxLen > maxLen:
                maxLen = currMaxLen
                res = currMaxPalin
        return res
    # return the longest palin starting from left, right, and the correponding lenth
    def _central_spread(self, s, left, right):   
        lens = len(s)
        i, j = left, right
        while i >= 0 and j < lens and s[i]==s[j] :
            i -= 1
            j += 1
        return s[i+1:j], j-i-1
      
      
      
"""方法三：动态规划（推荐）
推荐理由：暴力解法太 naive，中心扩散不普适，Manacher 就更不普适了，是专门解这个问题的方法。而用动态规划我认为是最有用的，可以帮助你举一反三的方法。
解决这类 “最优子结构” 问题，可以考虑使用 “动态规划”：
1、定义 “状态”；
2、找到 “状态转移方程”。
记号说明： 下文中，使用记号 s[l, r] 表示原始字符串的一个子串，l、r 分别是区间的左右边界的索引值，使用左闭、右闭区间表示左右边界可以取到。举个例子，当 s = 'babad' 时，s[0, 1] = 'ba' ，s[2, 4] = 'bad'。
1、定义 “状态”，这里 “状态”数组是二维数组。
dp[l][r] 表示子串 s[l, r]（包括区间左右端点）是否构成回文串，是一个二维布尔型数组。即如果子串 s[l, r] 是回文串，那么 dp[l][r] = true。
2、找到 “状态转移方程”。
首先，我们很清楚一个事实：
1、当子串只包含 1 个字符，它一定是回文子串；
2、当子串包含 2 个以上字符的时候：如果 s[l, r] 是一个回文串，例如 “abccba”，那么这个回文串两边各往里面收缩一个字符（如果可以的话）的子串 s[l + 1, r - 1] 也一定是回文串，即：如果 dp[l][r] == true 成立，一定有 dp[l + 1][r - 1] = true 成立。
根据这一点，我们可以知道，给出一个子串 s[l, r] ，如果 s[l] != s[r]，那么这个子串就一定不是回文串。如果 s[l] == s[r] 成立，就接着判断 s[l + 1] 与 s[r - 1]，这很像中心扩散法的逆方法。
事实上，当 s[l] == s[r] 成立的时候，dp[l][r] 的值由 dp[l + 1][r - l] 决定，这一点也不难思考：当左右边界字符串相等的时候，整个字符串是否是回文就完全由“原字符串去掉左右边界”的子串是否回文决定。但是这里还需要再多考虑一点点：“原字符串去掉左右边界”的子串的边界情况。
1、当原字符串的元素个数为 3 个的时候，如果左右边界相等，那么去掉它们以后，只剩下 1 个字符，它一定是回文串，故原字符串也一定是回文串；也就是说当r - l <= 2 且 s[left]==[right] 时，那么从left到right肯定是回文串， meaning dp[left][right]=True
综上，如果一个字符串的左右边界相等，以下二者之一成立即可：
1、去掉左右边界以后的字符串不构成区间，即“ s[l + 1, r - 1] 至少包含两个元素”的反面，即 r - l <= 2；
2、去掉左右边界以后的字符串是回文串，具体说，它的回文性决定了原字符串的回文性。
于是整理成“状态转移方程” dp[l, r] = (s[l] == s[r] and (r - l <= 2 or dp[l + 1, r - 1]))
编码实现细节：因为要构成子串 l 一定小于等于 r ，我们只关心 “状态”数组“上三角”的那部分取值。理解上面的“状态转移方程”中的 (r - l <= 2 or dp[l + 1, r - 1]) 这部分是关键，因为 or 是短路运算，因此，如果收缩以后不构成区间，那么就没有必要看继续 dp[l + 1, r - 1] 的取值。
时间复杂度：O(N^{2}); 空间复杂度：O(N^{2})，二维 dp 问题，一个状态得用二维有序数对表示，因此空间复杂度是 O(N^{2})。"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        if lens <= 1:
            return s 
        
        maxLen = 1
        res = s[0]   # 初始化为s[0]的原因是如果完全找不到一个回子串至少要输出第一个元素
        dp = [[False]*lens for _ in range(lens)]
        for right in range(1, lens):
            for left in range(right):
                if s[left]==s[right] and (dp[left+1][right-1] or right-left <= 2):
                    dp[left][right] = True 
                    if right-left+1 > maxLen:
                        maxLen = right-left+1
                        res = s[left:right+1]
        return res
