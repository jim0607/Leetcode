425. Word Squares

Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).


"""
这题的核心方法是backtrack: 一个单词一个单词往上加，每次加一个单词都必须保证其prefix是之前所加单词的对应列组成的，
比如我们想加在第五行加单词，那这个单词必须满足prefix是前4行的第四列组成的。
知道了这个我们可以尝试套着模板来backtrack了.
Time complexity: It is tricky to calculate the exact number of operations in the backtracking algorithm. 
We know that the trace of the backtrack would form a n-ary tree. 
Therefore, the upper bound of the operations would be the total number of nodes in a full-blossom n-ary tree.
In our case, at any node of the trace, at maximum it could have 26 branches (i.e. 26 alphabet letters). 
Therefore, the maximum number of nodes in a 26-ary tree would be approximately 26^L.
O(K26^L*L), where K is the len(words), L is len(words[0]).
"""
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        N = len(words[0])

        for word in words:
            self._backtrack(words, N, 1, [word], res)       # try every word as start word in the word_square
        
        return res
    
    def _backtrack(self, words, N, curr_row, curr_square, res):
        if curr_row == N:
            res.append(curr_square.copy())
            return
        
        for next_word in self._valid_candidates(words, curr_row, curr_square):
            curr_square.append(next_word)
            self._backtrack(words, N, curr_row + 1, curr_square, res)
            curr_square.pop()
            
    def _valid_candidates(self, words, curr_row, curr_square):  
        prefix = "".join(word[curr_row] for word in curr_square)    # 我们想加在第五行加单词，那这个单词必须满足prefix是前4行的第四列组成的
        for word in words:
            if word.startswith(prefix):     # this takes O(L) where L is the lens of the word, we can use a hash map to store the (prefix, word) pairs in advance. 
                yield word
                
                
                
                
"""
use a hashtable to store the (prefix, word) pairs in advance, so that when we search for next_word with a specific prefix, it will be O(1) 
- O(K26^L), O(KL)
"""
"""
hashmap + backtrack - O(N*26^L)
"""
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def backtrack(curr_sq):
            if len(curr_sq) == n:
                res.append(curr_sq.copy())
                return
            should_start_with = _should_start_with(curr_sq)
            for next_word in start_with[should_start_with]:     # 我们想加在第五行加单词，
                curr_sq.append(next_word)       # 那这个单词必须满足prefix是前4行的第四列组成的
                backtrack(curr_sq)
                curr_sq.pop()
                    
                    
        def _should_start_with(word_lst):
            ans = ""
            idx = len(word_lst)
            for word in word_lst:
                ans += word[idx]
            return ans
        
        
        # step 1: build a hashmap
        start_with = collections.defaultdict(list)
        n = len(words[0])
        for word in words:
            for i in range(n):
                start_with[word[:i]].append(word)
                
        # step 2: try backtrack for each word as the start word
        res = []
        for word in words:
            backtrack([word])
        return res
                
                
"""
Brutal force takes O(K) time to query the word with a certain prefix, and it takes O(1) space.
Hashmap realized O(1) time to query the word with a certain prefix, but it takes way more space: O(KL).
Trie data structure provides a compact and yet still fast way to retrieve words with a given prefix.
It takes O(L) time to query the word, where L is the lens of the word, which is much faster than the Brutal force,
especially in real world, there could be millions of words in a book, but the lens of each words are within 20.
It takes O(KL) space in worst case, but in real world, it is much less than that, cuz lots of words share the same prefix.
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        

class Trie:
    
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:          # build the Trie in the constructor
            self._insert(word)
        
    def _insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
            
        curr.is_end = True
    
    def find_word(self, prefix):
        res = []    # return a list of words prefixed with prefix
        curr = self.root
        for ch in prefix:
            curr = curr.child[ch]
            
        self._backtrack(curr, prefix, res)      # use backtack to find the word that starts with prefix, 常用方法，需掌握！！
        
        return res
        
    def _backtrack(self, curr, curr_word, res):    
        if curr.is_end:
            res.append(curr_word)
            
        for ch in curr.child:
            self._backtrack(curr.child[ch], curr_word + ch, res)
    
    
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        N = len(words[0])
        
        trie = Trie(words)

        for word in words:
            self._backtrack(trie, N, 1, [word], res)       # try every word as start word in the word_square
        
        return res
    
    def _backtrack(self, trie, N, curr_row, curr_square, res):
        if curr_row == N:
            res.append(curr_square.copy())
            return
        
        prefix = "".join(word[curr_row] for word in curr_square)    # 我们想加在第五行加单词，那这个单词必须满足prefix是前4行的第四列组成的
        for next_word in trie.find_word(prefix):
            curr_square.append(next_word)
            self._backtrack(trie, N, curr_row + 1, curr_square, res)
            curr_square.pop()
