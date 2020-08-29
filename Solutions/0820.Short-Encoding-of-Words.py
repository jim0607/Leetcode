820. Short Encoding of Words

Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].


    
    
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
    
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def is_suffix(self, word):  # return True if word is a suffix of the Trie
        curr = self.root
        for ch in word[::-1]:   # 注意要search in the reverse order
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return True
    
    def insert(self, word):
        curr = self.root
        for ch in word[::-1]:    # 注意要insert in the reverse order才能与上面的is_suffix对应
            curr = curr.child[ch]
            

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x: -len(x))     # 注意要sort in the reversed order
                                                #这样才能search for suffix
        trie = Trie()
        
        res = []
        for word in words:
            if not trie.is_suffix(word):
                trie.insert(word)
                res.append(word + "#")
                
        return sum(len(word) for word in res)
    
    
    
    
    


"""
另一种写法
"""
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.lens = 0
        
class Trie:
    
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:          # this takes O(∑wi) where wi is the length of words[i].
            self._insert(word)
            
    def _insert(self, word):
        curr = self.root
        cnt = 0
        for ch in word[::-1]:       # 处理suffix只需要反向遍历就可以了
            curr = curr.child[ch]
            cnt += 1
        curr.lens = cnt
            

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie(words)
        root = trie.root
        
        self.res = 0
        self._dfs(root)
        
        return self.res
        
    def _dfs(self, curr):
        if not curr.child:
            self.res += curr.lens + 1
        
        for ch in curr.child:
            next = curr.child[ch]
            self._dfs(next)
