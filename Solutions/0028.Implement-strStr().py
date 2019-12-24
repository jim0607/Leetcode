Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


# 回溯法 O(M*N)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lens1, lens2 = len(haystack), len(needle)
        if lens2 == 0:
            return 0
        i, j, anchor = 0, 0, 0
        while i < lens1 and j < lens2:
            anchor = i
            while i < lens1 and j < lens2 and haystack[i] == needle[j]: # 养成每次都判断i, j不超过长度的好习惯
                i += 1
                j += 1
            if j == lens2:
                return anchor
            i = anchor + 1
            j = 0
        return -1
        
        
# 方法二：Rabin Karp Algorithm O(M+N)
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

            if hashStr < 0:
                hashStr = hashStr + modulus
            # 这里虽然直接判断hashStr == hashNeedle程序通过了，但是要注意hashStr == hashNeedle不一定意味着haystack[i-lens2:i]与Needle相等，面试时再加一句haystack[i-lens2:i]==Needle的判断语句。
            if hashStr == hashNeedle:
                return i - lens2 + 1
        return -1
        
        
# KMP算法，超纲，不会在面试中出现的。
