"""
1147. Longest Chunked Palindrome Decomposition

Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

Each a_i is a non-empty string;
Their concatenation a_1 + a_2 + ... + a_k is equal to text;
For all 1 <= i <= k,  a_i = a_{k+1 - i}.
 

Example 1:

Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
Example 2:

Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
Example 3:

Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
Example 4:

Input: text = "aaa"
Output: 3
Explanation: We can split the string on "(a)(a)(a)".
"""


"""
greedy algorithm: 双指针left and right, 一个从前往后遍历得到left_s，另一个从后往前遍历right_s，
if left_s == right_s: res += 1;
O(NL), N is lens of s, L is the average lens of equal string.
"""
class Solution:
    def longestDecomposition(self, s: str) -> int:
        left_str, right_str = "", ""
        res = 0
        for left_ch, right_ch in zip(s, s[::-1]):   # O(N)
            left_str = left_str + left_ch
            right_str = right_ch + right_str        # 注意这里是right_ch + right_str不能调换位置
            
            if left_str == right_str:               # O(L), 这里可能可以用rolling hash优化吧
                res += 1
                left_str, right_str = "", ""
                
        return res

       
       
"""
Improve: instead of comparing left_s == right_s, we compare left_hash_code == right_hash_code.
"""
class Solution:
    def longestDecomposition(self, s: str) -> int:
        res = 0
        SIZE = 2**31
        BASE = 31
        left_hash, right_hash = 0, 0
        power = 0       # power for right_hash
        for i, (left_ch, right_ch) in enumerate(zip(s, s[::-1])):           # O(N)
            left_hash = (left_hash * BASE + ord(left_ch) - ord("a")) % SIZE
            right_hash = (right_hash + (ord(right_ch) - ord("a")) * BASE**power) % SIZE
            power += 1

            if left_hash == right_hash:     # this takes O(1)
                res += 1
                left_hash, right_hash = 0, 0
                power = 0
                
        return res
