648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

 

Example 1:

Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


"""
这题是用prefix build一个Trie, 而通过这个Trie来query输入word的prefix
"""

class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.prefix = "#"    # instead of store if it is end, we store the prefix
        
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, prefix):
        """
        insert a prefix string into the Trie, and update the self.prefix
        """
        curr = self.root
        for ch in prefix:
            curr = curr.child[ch]
        curr.prefix = prefix
            
    def find(self, word):
        """
        input is a word, return its corresponding prefix
        """
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return word
            curr = curr.child[ch]
            if curr.prefix != "#":      # meaning a prefix has been found for the word
                return curr.prefix
        return word


class Solution:
    def replaceWords(self, prefixs: List[str], sentence: str) -> str:
        # step 1: put all prefix into the trie
        trie = Trie()
        for prefix in prefixs:
            trie.insert(prefix)
            
        # step 2: find the prefix for each word in sentence
        res = []
        for word in sentence.split():
            res.append(trie.find(word))
            
        return " ".join(res)                    
