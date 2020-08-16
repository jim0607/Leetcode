1071. Greatest Common Divisor of Strings

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


"""
Let's firstly do it for integers.
"""
"""
The Euclidean algorithm for calculating the greatest common divisor (GCD) of two numbers is a
classic example of recursion. The central idea is that if y > x, the GCD of x and y is the GCD of x
and y − x. For example, GCD(156, 36) = GCD((156 − 36) = 120, 36). By extension, this implies that
the GCD of x and y is the GCD of x and y mod x, i.e., GCD(156, 36) = GCD((156 mod 36) = 12, 36) =
GCD(12, 36 mod 12 = 0) = 12.
"""
def GCD(x, y):
    while y != 0:   # here we use iterations, we can also use recursion
        x, y = y, x % y
    return x

print(GCD(156, 36))



"""
The greatest common divisor must be a prefix of each string, so we can try all prefixes.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1, s2 = str1, str2
        while s2:
            s1, s2 = s2, s1[:len(s1)%len(s2)]
        gcd = len(s1)
        
        if s1 * (len(str1) // gcd) == str1 and s1 * (len(str2) // gcd) == str2:
            return s1
        return ""
