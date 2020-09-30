"""
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


"""
O(N) solution: Rabin Karp / Rolling hash. calculate the hash_code for each L = 10 window. 
use a hash_code_set to record the calculated hash_code, if the newly calculated hahs_code is in the hash_code_set, then that means we have repeated sequance.
Naive rolling hash use ord(ch) - ord("A"), but this makes the number very large and easier to overflow thus more prone to collision.
Below is the naive rolling hash, which cannot pass the case when string is long.
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        HASH_SIZE = 2**31
        BASE = 31  

        power = 1
        for _ in range(L):
            power = power * BASE % HASH_SIZE
            
        hash_code = 0
        hash_code_set = set()
        res = set()
        for i, ch in enumerate(s):
            hash_code = (hash_code * BASE + ord(ch) - ord("A")) % HASH_SIZE
            if i < L - 1:
                continue
            if i >= L:
                hash_code = (hash_code - (ord(s[i-L]) - ord("A")) * power % HASH_SIZE) % HASH_SIZE
            
            if hash_code in hash_code_set:
                res.add(s[i-L+1: i+1])
            hash_code_set.add(hash_code)
        
        return list(res)
        
        
"""
since in DNA  sequence, we have only 4 chars - A C T G, instead of using ord(ch), we use a hashmap to assgin small
numbers to the 4 chars. this will largely avoid number overflow and hence avoid collision.
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
        L = 10
        HASH_SIZE = 2**31
        BASE = 31  

        power = 1
        for _ in range(L):
            power = power * BASE % HASH_SIZE
            
        hash_code = 0
        hash_code_set = set()
        res = set()
        for i, ch in enumerate(s):
            hash_code = (hash_code * BASE + mapping[ch]) % HASH_SIZE
            if i < L - 1:
                continue
            if i >= L:
                hash_code = (hash_code - mapping[s[i-L]] * power % HASH_SIZE) % HASH_SIZE
            
            if hash_code in hash_code_set:
                res.add(s[i-L+1: i+1])
            hash_code_set.add(hash_code)
        
        return list(res)
