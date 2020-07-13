1166. Design File System

You are asked to design a file system which provides two functions:

createPath(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn't exist.
get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.



class TrieNode:
    
    def __init__(self, val):
        self.child = collections.defaultdict(TrieNode)
        self.val = val


class TrieNode:
    
    def __init__(self, val):
        self.child = collections.defaultdict(TrieNode)
        self.val = val


class FileSystem:

    def __init__(self):
        self.root = TrieNode(-1)

    def createPath(self, path: str, value: int) -> bool:
        curr = self.root
        path = path.split("/")[1:]
        for i, name in enumerate(path):   # O(L), L is lens of path
            if i == len(path) - 1:
                if name in curr.child:      # Returns False if the path already exists
                    return False
                curr.child[name] = TrieNode(value)  # create a new node for a new path
                return True
            
            if name not in curr.child:  
                return False
            
            curr = curr.child[name]

    def get(self, path: str) -> int:
        curr = self.root
        for name in path.split("/")[1:]:    # O(L), L is lens of path
            if name not in curr.child:
                return -1
            curr = curr.child[name]
        return curr.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
