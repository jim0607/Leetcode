1316. Distinct Echo Substrings

Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".


class Solution:
    def distinctEchoSubstrings(self, s: str) -> int:
        n = len(s)
        self.HASH_SIZE = 2 ** 31
        hash_code = [0 for _ in range(n + 1)]   # hash_code[i] = the hash code for s[:i] 相当于prefix_hash_code
        power = [1 for _ in range(n + 1)]       # power[i] = the 31^i
        for i in range(1, n + 1):
            power[i] = power[i - 1] * 31 % self.HASH_SIZE
            hash_code[i] = (hash_code[i - 1] * 31 + ord(s[i - 1]) - ord("`")) % self.HASH_SIZE  # 不能用ord(s[i - 1]) - ord("a") 因为这样的话"aaaa"的hash code 就成了[0, 0, 0, 0]

        echo_codes = set()
        for i in range(n - 1):      # O(n^2)
            for j in range(i + 2, n + 1, 2):
                mid_idx = (i + j) // 2
                
                left_hash_code = self.calculate_hash_code(s, i, mid_idx, hash_code, power)
                right_hash_code = self.calculate_hash_code(s, mid_idx, j, hash_code, power)
                if left_hash_code == right_hash_code:
                    echo_codes.add(left_hash_code)
                    
        return len(echo_codes)
    
    def calculate_hash_code(self, s, i, j, hash_code, power):     # O(1)
        """
        calculate the hash code for s[i:j]
        """
        return (hash_code[j] - hash_code[i] * (31 ** (j - i)) % self.HASH_SIZE) % self.HASH_SIZE
