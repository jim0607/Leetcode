"""
753. Cracking the Safe

There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
 
Note:

n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.
"""


"""
这道题说的是给了k个数字，值为0到k-1，可以组成n位密码。让我们找一个万能钥匙串，能破解任意的n位密码组合，
这里对于破解的定义为只要密码是钥匙串的子串就可以破解了，要求出最短的一个万能钥匙串。
来看一个例子，n=2，k=2，那么密码的组合有四种，
00，01，10，11
所以 00110 就是一种钥匙串，因为密码 00 (00110), 01 (00110), 10 (00110), 11 (00110), 分别都包括在钥匙串中。
可以发现，为了尽可能的使钥匙串变短，所以密码之间尽可能要相互重叠，
比如 00 和 01，就共享一个0，如果是3个数，012 和 120 共享两个数 "12"，
再进一步们可以发现，两个长度为n的密码最好能共享 n-1 个数字，这样累加出来的钥匙串肯定是最短的。

密码共有n位，每一个位可以有k种选择，总共不同的密码总数就有k的n次方个。
思路是先从n位都是0的密码开始，取出钥匙串的最后 n-1 个数字，然后在后面依次添加其他数字，
用一个 HashSet 来记录所有遍历过的密码，这样如果不在集合中，说明是一个新密码，
而生成这个新密码也只是多加了一个数字，能保证钥匙串最短，这是一种贪婪的解法，相当的巧妙。
就拿题目中的例子2来说明吧，n=2, k=2，最多有4个密码。开始时 res 初始化为 00，需要遍历4次。
第一次遍历时，先取最后一个数字0，此时先尝试再后面添加1，可组成新密码 01，不在 HashSet 中，将其加入 HashSet，
并且将这个1加到 res 后面，变为 001，然后断开内部 for 循环。
开始进行第2次遍历，取 res 中最后一个数字1，先尝试在后面添加1，可组成新密码 11，不在 HashSet 中，将其加入 HashSet，
并且将这个1加到 res 后面，变为 0011，然后断开内部 for 循环。
开始进行第3次遍历，取 res 中最后一个数字1，先尝试在后面添加1，可组成密码 11，已在 HashSet 中，跳过；
再尝试在后面添加0，可组成密码 10，不在 HashSet 中，将其加入 HashSet，并且将这个0加到 res 后面，变为 00110，然后断开内部 for 循环。
开始进行第4次遍历，取 res 中最后一个数字0，先尝试在后面添加1，可组成密码 01，已在 HashSet 中，跳过；
再尝试在后面添加0，可组成密码 00，已在 HashSet 中，跳过，循环结束。
这样最终的 res 为 00110 即为符合题意的万能钥匙.
"""
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        res = "0" * n
        covered = set()
        covered.add(res)
        for i in range(k**n):                       # 一共有k**n种可能的组合
            prefix = res[-n+1:] if n > 1 else ""    # 取res的最后n-1个数字(贪心)
            for j in range(k-1, -1, -1):            # 为什么要反向遍历呢？becuase we start from "00", the path is then blocked
                combination = prefix + str(j)       # 加上k中的一个新的数字来组新的combination
                if combination in covered:          # 如果这个combination已经cover到了，就不用更新res了
                    continue
                covered.add(combination)            # 更新cover和res
                res += str(j)
                break
        return res
""" Time complexity is O(k*k^n) """



"""
Same idea, implemented using recurssion.

dfs end condition: len(covered) == k ** n
constraints on next_candidates: next_password should choose the last k-1 ch from curr_comb, and then choose one ch from (0, k)
arguments pass into dfs: curr_comb
"""
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(curr_comb):
            if len(covered) == k ** n:    # if all passwords are covered
                self.res = curr_comb
                return
            
            for next_num in range(k - 1, -1, -1):    # 为什么要反向遍历呢？becuase we start from "00", the path is then blocked
                next_password = curr_comb[-n + 1:] + str(next_num)
                if next_password not in covered:
                    covered.add(next_password)
                    dfs(curr_comb + str(next_num))
                
                
        if n == 1:
            return "".join(str(i) for i in range(k))
        
        self.res = ""
        covered = set()
        covered.add("0" * n)
        dfs("0" * n)
        return self.res
            
            
"""
change res to a global variable
"""   
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        self.res = "0" * n
        covered = set()
        covered.add(self.res)
        self._dfs(n, k, covered)
        return self.res
        
    def _dfs(self, n, k, covered):
        if len(covered) == k**n:     # if all the combinations are covered
            return self.res
        
        prefix = self.res[-n+1:] if n > 1 else ""
        for j in range(k-1, -1, -1):
            combination = prefix + str(j)
            if combination in covered:
                continue
            covered.add(combination)
            self.res += str(j)
            self._dfs(n, k, covered)
