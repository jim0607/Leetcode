"""
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
"""


"""
backtrack for search
"""
class TrieNode:
    
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:       # O(L) where L is lens of word
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:        # worst case O(26^M), where M is how many wildcard in word
        def backtrack(curr_node, curr_idx):
            if curr_idx == len(word) - 1:
                if curr_node.is_end:
                    return True
                return False
            
            if word[curr_idx + 1] != ".":
                if word[curr_idx + 1] in curr_node.child:
                    if backtrack(curr_node.child[word[curr_idx + 1]], curr_idx + 1):
                        return True
            else:
                for next_ch in "abcdefghijklmnopqrstuvwxyz":    # worst case O(26^M), where M is how many wildcard in word
                    if next_ch in curr_node.child:      # but since there is pruning here, the time complexity is better than O(26^M)
                        if backtrack(curr_node.child[next_ch], curr_idx + 1):
                            return True
            
            return False
        
        
        return backtrack(self.root, -1)




"""
bfs for search
"""
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


"""
solution 2: hashset
"""
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_set = set()

    def addWord(self, word: str) -> None:
        self.word_set.add(word)

    def search(self, word: str) -> bool:
        def backtrack(curr_idx, curr_comb):     # backtrack to find all combinations
            if curr_idx == len(word) - 1:
                if curr_comb in self.word_set:
                    return True
                return False
            
            if word[curr_idx+1] != ".":
                if backtrack(curr_idx + 1, curr_comb + word[curr_idx+1]):
                    return True
            else:
                for next_ch in "abcdefghijklmnopqrstuvwxyz":        # solid O(26^M), where M is how many wildcard in word
                    if backtrack(curr_idx + 1, curr_comb + next_ch):
                        return True
                
            return False
        
        
        return backtrack(-1, "")
