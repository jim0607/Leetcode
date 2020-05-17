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


  
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)  # child is another TrieNode
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        currNode = self.root
        for ch in word:
            currNode = currNode.child[ch]       # currNode往前遍历
            
        currNode.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.res = set()
        
        wordTrie = Trie()   # instantiate a Trie
        for word in words:
            wordTrie.insert(word)
            
        root = wordTrie.root
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] in root.child:
                    self.visited = set()
                    self.visited.add((i, j))
                    self.backtrack(i, j, root.child[self.board[i][j]], self.board[i][j])
                    
        return list(self.res)
    
    def backtrack(self, i, j, currNode, currPath):
        if currNode.isEnd:
            self.res.add(currPath)
            currNode.isEnd = False          # 注意千万不要return, 不然单词health找到之后就不再继续找单词healthy了，为了还能找到healty, 只能把currNode.isEnd设置为False

        for delta_x, delta_y in self.MOVES:
            next_x, next_y = i + delta_x, j + delta_y

            if next_x < 0 or next_x >= len(self.board) or next_y < 0 or next_y >= len(self.board[0]):
                continue
            if (next_x, next_y) in self.visited:
                continue
            if self.board[next_x][next_y] not in currNode.child:
                continue
                
            temp = currNode     # 记录一下，一会儿好在backtracking的时候回退回来
            currNode = currNode.child[self.board[next_x][next_y]]     # currNode往前遍历
            self.visited.add((next_x, next_y))
            self.backtrack(next_x, next_y, currNode, currPath + self.board[next_x][next_y])
            currNode = temp
            self.visited.remove((next_x, next_y))
