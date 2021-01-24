"""
720. Longest Word in Dictionary

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. 
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
"""


"""
首先insert所有的word进Trie, 然后再将words list按照长度反向sort, 
最后遍历words, 如果发现有一个word can_be_built, then return the word.
需要在Trie class里面写一个can_be_built(word)函数
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        
    
class Trie:
    
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self._insert(word)
            
    def _insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
        curr.is_end = True
            
    def can_be_built(self, word):
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
            if not curr.is_end:
                return False
        return True
    

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie(words)
        words.sort(key = lambda x:(-len(x), x))     # sort这样我们第一个can_be_built的数就是想return的了
        for word in words:
            if trie.can_be_built(word):
                return word
        return ""




"""
Trie + bfs: 首先insert所有的word进Trie, 然后再从root出发对所有的nodes进行bfs, 只要next_node.is_end=True就可以append到q中；
O(∑wi) to insert all words into Trie where wi is the lens of ith word, same for search longest word.
"""
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        return trie.find_longest_word()     # 注意这里调用函数要带(), 不然会报错
        
        
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        self.word = ""
        
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        insert a word into the Trie
        """
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
        curr.is_end = True
        curr.word = word
        
    def find_longest_word(self):
        """
        use bfs to find the longest word
        """
        curr = self.root
        res = ""
        q = collections.deque()
        q.append(curr)
        while q:
            curr = q.popleft()
            for next in curr.child.values():     # 注意curr.child的key是character, value才是TrieNode
                if next.is_end:
                    q.append(next)
                    if len(next.word) > len(res) or next.word < res:  # return the longest word with the smallest lexicographical order
                        res = next.word
        return res
