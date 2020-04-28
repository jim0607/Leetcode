211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true



class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currNode = self.root
        for char in word:
            currNode = currNode.child[char]
            
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        currNode = self.root
        
        q = collections.deque()
        q.append((currNode, 0))    # Saving index in the queue
        while q:
            currNode, i = q.popleft()
            if i == len(word):
                if currNode.isEnd:    
                    return True
            
            # below we'll append layer by layer, that reminds us of 层序遍历bfs, 所以用q
            elif word[i] in currNode.child:
                q.append((currNode.child[word[i]], i + 1))  
            
            elif word[i] == ".":
                for char in currNode.child:
                    q.append((currNode.child[char], i + 1))
            
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
