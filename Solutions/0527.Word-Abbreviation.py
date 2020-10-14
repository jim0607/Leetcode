"""
527. Word Abbreviation

Given an array of n distinct non-empty strings, 
you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, 
which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, 
a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. 
In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
"""



"""
step 1: 建立一个abbrev函数：从idx开始，对 word 做abbreviation. 
step 2: 建立一个abbr2word保存 abbr-->word.
step 3: 遍历建立好了的abbr2word。 for abbr, word_lst in abbr2word.items(), 
如果len(word_lst)==1, 那说明这个abbr是unique的，直接res.append(abbr); 
如果len(word_lst)>1, 那说明这个abbr不是unique的，我们需要去寻找每一个word的unique prefix,
所以对这个word_lst就一个Trie, Trie中写一个find_idx函数 to where the prefix for word is unique (cur_node.cnt == 1)
Time Complexity: O(C) where C is the number of characters across all words in the given array.
Space Complexity: O(C).
"""
class TrieNode:
    
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.cnt = 0
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Insert a word into Trie
        """
        curr_node = self.root
        curr_node.cnt += 1
        for ch in word:
            curr_node = curr_node.child[ch]
            curr_node.cnt += 1
    
    def find(self, word):
        """
        Find the idx where the prefix for word is unique (cnt == 1)
        """
        curr_node = self.root
        for i, ch in enumerate(word):
            if curr_node.cnt == 1:
                return i
            curr_node = curr_node.child[ch]


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        abbr2word = defaultdict(list)
        for word in words:
            abbr2word[self._abbrev(word, 1)].append(word)
            
        res = []
        for abbr, word_lst in abbr2word.items():
            if len(word_lst) == 1:
                res.append(abbr)
            else:
                trie = Trie()
                for word in word_lst:
                    trie.insert(word)
                for word in word_lst:
                    abbr_idx = trie.find(word)   # 从idx开始，对 word 做abbreviation
                    res.append(self._abbrev(word, abbr_idx))
        return res
        
        
    def _abbrev(self, word, idx):
        """
        从idx开始，对 word 做abbreviation
        """
        if len(word) - idx < 3:
            return word
        else:
            return word[:idx] + str(len(word) - idx - 1) + word[-1]
            
            
            
            
"""
由于题目要求输出必须保持原有顺序，所以我们可以做一点小小的修改，
abbr2word dictionary 保存 abbr --> index of word in words.
"""
class TrieNode:
    
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.cnt = 0        # how many words used this node
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Insert a word into Trie
        """
        curr_node = self.root
        curr_node.cnt += 1
        for ch in word:
            curr_node = curr_node.child[ch]
            curr_node.cnt += 1
    
    def find_idx(self, word):
        """
        Find the idx where the prefix for word is unique (cnt == 1)
        """
        curr_node = self.root
        for i, ch in enumerate(word):
            if curr_node.cnt == 1:
                return i
            curr_node = curr_node.child[ch]


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        abbr2word = defaultdict(list)   
        for i, word in enumerate(words):
            abbr2word[self._abbrev(word, 1)].append(i)  # value is the index in words
            
        res = ["" for _ in range(len(words))]
        for abbr, word_lst in abbr2word.items():
            if len(word_lst) == 1:
                res[word_lst[0]] = abbr
            else:
                trie = Trie()
                for word_idx in word_lst:
                    trie.insert(words[word_idx])
                for word_idx in word_lst:
                    abbr_idx = trie.find_idx(words[word_idx])  # 从abbr_idx开始，对 word 做abbreviation
                    res[word_idx] = self._abbrev(words[word_idx], abbr_idx)
        return res
        
        
    def _abbrev(self, word, idx):
        """
        从idx开始，对 word 做abbreviation
        """
        if len(word) - idx < 3:
            return word
        else:
            return word[:idx] + str(len(word) - idx - 1) + word[-1]
