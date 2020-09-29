"""
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



"""
Let's firstly do it for integers.

The Euclidean algorithm for calculating the greatest common divisor (GCD) of two numbers is a
classic example of recursion. The central idea is that if y > x, the GCD of x and y is the GCD of x
and y − x. For example, GCD(156, 36) = GCD((156 − 36) = 120, 36). By extension, this implies that
the GCD of x and y is the GCD of x and y mod x, i.e., GCD(156, 36) = GCD((156 mod 36) = 12, 36) =
GCD(12, 36 mod 12 = 0) = 12.
"""
def GCD(x, y):
    while y != 0:   # iterative implementation
        x, y = y, x % y
    return x

def GCD(x, y):      # recursive implementation
    return x if y == 0 else GCD(y, x % y)

print(GCD(156, 36))





"""
The greatest common divisor must be a prefix of each string, so we use Euclidean algorithm to get the GCD of the two strings.
Recursive
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = self._get_gcd(str1, str2) 
        return gcd if gcd * (len(str1) // len(gcd)) == str1 and gcd * (len(str2) // len(gcd)) == str2 else ""
        
    def _get_gcd(self, s1, s2):
        return s1 if len(s2) == 0 else self._get_gcd(s2, s1[: len(s1) % len(s2)])
     
     
"""
Iterative
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
