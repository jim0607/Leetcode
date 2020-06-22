677. Map Sum Pairs

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5


"""
In TrieNode, define a self.sums 代表所有的子node所代表的string的val的和。
在class MapSum中用一个dictionary记录之前出现的key-val pair, 如果key出现过，就通过delta=val-self.dict[key]来update node.sums的值。
"""

class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.sums = 0       # sums 代表所有的子node所代表的string的val的和
        

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.dict = collections.defaultdict(int)    # key is string, val is val corresponding to the string

    def insert(self, key: str, val: int) -> None:
        delta = val - self.dict[key]    # if key already exsit, we update the val using delta
        self.dict[key] = val
        curr = self.root
        curr.sums += delta
        for ch in key:      # O(k) where k is the length of the key
            curr = curr.child[ch]
            curr.sums += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:   # O(k) where k is the length of the prefix
            if ch not in curr.child:
                return 0
            curr = curr.child[ch]
        return curr.sums
