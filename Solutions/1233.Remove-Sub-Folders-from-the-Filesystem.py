"""
1233. Remove Sub-Folders from the Filesystem

Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. 
For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 

Constraints:

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'
folder[i] always starts with character '/'
Each folder name is unique.
"""


"""
define has_prefix function in the Trie class, which returns whether or not there is already a string in the Trie that is the prefix of the word. 
step 1: sort the strings by lens. step 2: loop over all the words and check the has_prefix(word).
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):     # here input is a list of chars
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
        curr.is_end = True
        
    def has_prefix(self, word):    # we defind a has_prefix function to return whether or not
        curr = self.root           # there is already a string in the Trie that is the prefix of the word
        for ch in word:
            curr = curr.child[ch]
            if curr.is_end:        # if curr.is_end, then there is already a string in the Trie that is a prefix of the word
                return True
        return False

       
class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort(key = lambda x: len(x))        # we sort the folders by lens
        
        trie = Trie()
        
        res = []
        for folder in folders:
            words = folder.split("/")
            if not trie.start_with(words):  # if doesn't have prefix in the trie, then it is a stand-alone word
                res.append(folder)          # should append this stand-alone word into res
                trie.insert(words)          # and also insert it into the trie cuz it might be the prefix of some words later on
        
        return res
        





"""
solution 2
find the folder names with common prefix using a Trie, 
we only keep the shortest folder name among all the words that share the same prefix.
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        self.folder = ""
        

class Trie:
    
    def __init__(self, folder):
        self.root = TrieNode()
        for name in folder:
            name = name.split("/")[1:]      # str.split(sep) returns a list
            self._insert(name)
            
    def _insert(self, name):
        curr = self.root
        for s in name:
            temp = curr.folder
            if s not in curr.child:
                curr = curr.child[s]
                curr.folder = temp + "/" + s
            else:
                curr = curr.child[s]
                
            if curr.is_end:
                break

        curr.is_end = True

        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda name: len(name))

        trie = Trie(folder)     # after constructing the trie, we've got a short verion trie, meaning all the uneccessary long names were not includedin the trie.
        root = trie.root        # so next, we only need to do dfs to out put all the names in the trie

        res = []
        self._dfs(root, res)
        return res
    
    def _dfs(self, curr, res):
        if curr.is_end:
            res.append(curr.folder)
            return
        
        for next in curr.child.values():
            self._dfs(next, res)
