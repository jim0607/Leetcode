212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


  
"""
Solution 1: we put the board into a trie. Then we loop over the words list to check if the word is in the trie.
This solution is hard to implement and it's also very costy, especially when board is huge and len(words) is small.
Solution 2: we put the words into a trie. Then we loop over the board, whenever we found a letter==word[0], we trigger a backtrak.
Backtrack 的结束条件是if curr_node.is_end.
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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)      # instantiate a Trie
        root = trie.root
        
        res = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                if ch in root.child:    # trigger a dfs whenever we find a char in root.child
                    visited = set()
                    visited.add((i, j))
                    self._backtrack(board, i, j, visited, root.child[ch], ch, res)
        return list(set(res))
    
    # 其实下面就是dfs的模板
    def _backtrack(self, board, i, j, visited, curr_node, curr_word, res):
        if curr_node.is_end:
            res.append(curr_word)   # 注意千万不要return, 不然单词health找到之后就不再继续找单词healthy了，
            curr_node.is_end = False    # 为了还能找到healty, 只能把currNode.isEnd设置为False
        
        for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_i, next_j = i + delta_i, j + delta_j
            if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]):
                if (next_i, next_j) not in visited:
                    ch = board[next_i][next_j]
                    if ch in curr_node.child:       # 注意这里要check if ch is in curr_node.child
                        visited.add((next_i, next_j))
                        self._backtrack(board, next_i, next_j, visited, curr_node.child[ch], curr_word + ch, res)
                        visited.remove((next_i, next_j))
