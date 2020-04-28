208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.



# Before implement a trie, we should firstly define a trieNode class.  
# This is similar with tree, before implement a tree, we should firstly define a treeNode class
# a treeNode class has 3 properties: treeNode.left, treeNode.right, treeNode.val
# a trieNode class has 2 preperties: trieNode.child, trieNode.isEnd
class TrieNode:     
    def __init__(self):
        """
        A TrieNode has two properties:
        1. child, which represents the children of the TrieNode, all the children are stored in a dictionary
        2. isEnd, which represents whether or not the TrieNode is the end of a word
        """
        
        self.child = collections.defaultdict(TrieNode)    # use a defaultdict, key is char, value is trieNode
        self.isEnd = False                                # return True if it is the end of the Trie


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()       # at the beginning, we should create a dummy root as a new trieNode 

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for char in word:           # O(m), where m is the word length
            currNode = currNode.child[char]   # 把char 放入 curr.child dictionary 中作为 key, 然后 curr 往下遍历
            
        currNode.isEnd = True        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for char in word:             # O(m), where m is the word length
            if char not in currNode.child:
                return False
            currNode = currNode.child[char]
            
        return currNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for char in prefix:     # O(m), where m is the prefix length
            if char not in currNode.child:
                return False
            currNode = currNode.child[char]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
