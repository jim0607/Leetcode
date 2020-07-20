Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


        
        
# Rabin Karp Algorithm O(M+N)

"""
Rolling hash 的核心就是用一个hash function把一个长度为m的string hash成一个整数，这样就可以避免O(m)的时间复杂度去比较两个string是否相等，
而是去比较两个string的hash code 只用O(1)的就可以比较了。
eg: string = "abcdef"  pattern = "cde"
step 1: 首先我们计算hash code of pattern:
hash code for "cde" is: ( (ord("c")-ord("a"))*31^2 + (ord("d")-ord("a"))*31^1 + (ord("e")-ord("a"))*31^0 ) % BASE
实际计算过程中为了防止hash code太大overflow，我们每算一下就取个模：
( (ord("c")-ord("a"))*31^2 ) % BASE + ( (ord("d")-ord("a"))*31^1 ) % BASE + ( (ord("e")-ord("a"))*31^0 ) % BASE ) % BASE
step 2: 然后我们计算hash code in source
首先计算hash code for "abc", compare the hash code of "abc" with target_code
then calculate the hash code for "abcd", then calculate the hash code for "bcd", and then compare with target_code
go on and on until the hash code equals.
"""


class Solution:
    def strStr(self, source: str, target: str) -> int:
        n, m = len(source), len(target)
        if m == 0:
            return 0
        if n == 0:
            return -1

        HASH_SIZE = 2 ** 31

        # step 1: calculate the hash code of the target
        target_code = 0
        for ch in target:
            target_code = (target_code * 31 + (ord(ch) - ord("a"))) % HASH_SIZE

        # step 2: calculate the hash code in source
        source_code = 0
        power = 1
        for _ in range(m):
            power = (power * 31) % HASH_SIZE
        for i, ch in enumerate(source):
            source_code = (source_code * 31 + (ord(ch) - ord("a"))) % HASH_SIZE
            if i < m - 1:
                continue
            if i >= m:
                source_code = (source_code - (ord(source[i - m]) - ord("a")) * power % HASH_SIZE) % HASH_SIZE  # in python, we don't need to worry aobut get mod for negative vals because python already taken care of that: (-3) % 4 = 1, the mod always return a positive val
            if source_code == target_code:
                if source[i - m + 1:i + 1] == target:
                    return i - m + 1

        return -1



# 26 是很常用的hash表里做进制转换的常数
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lens1, lens2 = len(haystack), len(needle)
        if lens2 == 0:
            return 0
        if lens2 > lens1:
            return -1
        
        # base value for thr rolling hash function
        base = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**31  # 注意这里的modulus不能取的太小，不然会产生不同的数得到同样的mod的情况
        
        # compute the hash of needle
        hashNeedle = 0
        for ch in needle:
            hashNeedle = (hashNeedle * base + (ord(ch) - ord("a"))) % modulus  # 这里每计算一个字符串就去一次mod，这样可以防止overflow

        # compare the hash of strings in haystack with hashNeedle
        # Firstly calculte the first lens2 ch
        hashStr = 0
        for i in range(lens2):
            hashStr = (hashStr * base + (ord(haystack[i]) - ord("a"))) % modulus  # 千万不要写成了hashStr += ....
        if hashStr == hashNeedle:
            return 0
        # eg: abcde, cde, abc has been calculated, we can get bcd based on abc without having to iretate lens2 again. and this is why this algorithm is O(M+N)
        # compute power for abtract a, power = 26^(lens2-1), 不直接使用power = 26^(lens2-1)而用循环取模是为了防止溢出
        power = 1
        for i in range(lens2):
            power = (power * base) % modulus
        for i in range(lens2, lens1):  # i points to the last ch of the comparing string
            # 已知abc, compute abcd fist
            hashStr = (hashStr * base + (ord(haystack[i]) - ord("a"))) % modulus
            # then compute abcd-a
            hashStr = hashStr - (ord(haystack[i-lens2]) - ord("a")) * power % modulus  # 有时候hashStr < (ord(haystack[i-lens2]) - ord("a")) * power % modulus, 这时候hashStr会变成负值，不过没关系，如果变成负值，再加上nodulus就可以了。

            # in python, we don't need to worry aobut get mod for negative vals because python already taken care of that: (-3) % 4 = 1, the mod always return a positive val
            if hashStr < 0:     # 如果用java的话这一句是必要的，如果用python的话就没必要担心了
                hashStr = hashStr + modulus
            # 这里虽然直接判断hashStr == hashNeedle程序通过了，但是要注意hashStr == hashNeedle不一定意味着haystack[i-lens2:i]与Needle相等，面试时再加一句haystack[i-lens2:i]==Needle的判断语句。
            if hashStr == hashNeedle:
                return i - lens2 + 1
        return -1
        
        
        
"""
A good application of this strStr() problem is that it can be used as an API for solving the problem of check if T2 is subtree of T1 ,both are very large trees.
572. Subtree of Another Tree
https://leetcode.com/discuss/interview-question/738978/Amazon-Onsite-or-check-if-T2-is-subtree-of-T1-both-are-very-large-trees
https://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
"""
    
        
# KMP算法，超纲，不会在面试中出现的。



# 回溯法 O(M*N)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lens_1, lens_2 = len(haystack), len(needle)
        if lens_2 == 0:
            return 0
        if lens_1 == 0:
            return -1
        if needle not in haystack:
            return -1
        
        i, j = 0, 0
        while i < lens_1 and j < lens_2:
            temp_i = i
            while i < lens_1 and j < lens_2 and haystack[i] == needle[j]:   # 养成每次都判断i, j不超过长度的好习惯
                i += 1
                j += 1
            if j == lens_2:
                return temp_i
            i = temp_i + 1
            j = 0
            
        return -1
