745. Prefix and Suffix Search

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1



"""
pre-calculate the all the possible combination of prefix+"#"+suffix --> idx and store them in a dictionary.
so that each query only takes O(1).
This takes more space than the Trie solution, but much faster.
"""
class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_suf_fix_to_idx = collections.defaultdict(lambda: -1)
        
        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                prefix = word[:i]
                for j in range(len(word) + 1):
                    suffix = word[j:]
                    self.pre_suf_fix_to_idx[prefix + "#" + suffix] = idx

    def f(self, prefix: str, suffix: str) -> int:       # O(1) for query
        return self.pre_suf_fix_to_idx[prefix + "#" + suffix]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


"""
construct a pref-trie and a suff-trie. In the trie node, we should indlude the idx.
node.idx is a list consist of the idx of word in words
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.idx = []
        

class PrefTrie:
    
    def __init__(self, words):
        self.root = TrieNode()
        for i, word in enumerate(words):
            self._insert(i, word)
            
    def _insert(self, i, word):
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
            curr.idx.append(i) 
            
    def prefix(self, prefix):
        """
        find a list of the idx of words that have prefix as it's prefix
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.child:
                return []
            curr = curr.child[ch]
            
        return curr.idx
        
        
class SuffTrie:
    
    def __init__(self, words):
        self.root = TrieNode()
        for i, word in enumerate(words):
            self._insert(i, word)
            
    def _insert(self, i, word):
        curr = self.root
        for ch in word[::-1]:
            curr = curr.child[ch]
            curr.idx.append(i) 
        
    def suffix(self, suffix):
        """
        find a list of the idx of words that have suffix as it's suffix
        """
        curr = self.root
        for ch in suffix[::-1]:     # 注意处理suffix的时候的，碰到的word都需要reverse traversal
            if ch not in curr.child:
                return []
            curr = curr.child[ch]
            
        return curr.idx
                
               
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.pref_trie = PrefTrie(words)
        self.suff_trie = SuffTrie(words)

    def f(self, prefix: str, suffix: str) -> int:
        pre_idx = self.pref_trie.prefix(prefix) if prefix else [i for i in range(len(self.words))]
        suf_idx = self.suff_trie.suffix(suffix) if suffix else [i for i in range(len(self.words))]
        res = -1
        for i in pre_idx:
            for j in suf_idx:
                if i == j:
                    res = max(res, i)
        return res
    
""" 
The above solution is TLE
"""
