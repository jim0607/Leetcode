421. Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.



"""
Python provides format(num, '') function to convert an Integer number to binary number as a String.
>>> format(3, '015b')         # converts integer 3 to binary with 15 digits
"000000000000011"
 
首先把所有的数的二进制存到 Trie 里面去，然后对于数组中的每个数 x，和 x 一起异或结果最大的 y 就是用 x 的二进制的反码在Trie 里面搜索，
尽可能的与 x 的反码匹配，这样当走到叶子节点时，叶子节点对应的数就是 y。然后遍历一遍数组，求出 max(x ^ y), solution 写的很差，但是图画的很好！
O(32N), where N is len(nums), 32 is the height of the trie using format(num, '032b') to convert to 32 bit
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.val = 0
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        """
        given a num, insert the bits of a num into the Trie
        """
        curr = self.root
        for bit in format(num, '032b'):
            curr = curr.child[bit]
        curr.val = num
            
    def search_max_XOR(self, num):
        """
        given a num, find the max_XOR it can generate with other nums in the Trie
        """
        curr = self.root
        for bit in format(num, '032b'):
            if bit == "1":
                curr = curr.child["0"] if "0" in curr.child else curr.child["1"]
            elif bit == "0":
                curr = curr.child["1"] if "1" in curr.child else curr.child["0"]
                    
        return curr.val ^ num
    
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_XOR = 0
        for num in nums:
            trie.insert(num)    # 注意要先把num insert进去，这样第一个进去的num在执行trie.search_max_XOR(num)的时候就会与自身异或, 否则会与0异或得到的值可能不对，eg: [2, 3]
            max_XOR = max(max_XOR, trie.search_max_XOR(num))
        return max_XOR
