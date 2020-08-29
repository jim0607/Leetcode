588. Design In-Memory File System

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

 

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem
 

Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.



"""
Trie solution: search/add/insert都是O(L)的时间复杂度，L是filePath的长度. 
像这种method里面函数很多的情况，不需要额外写一些helper funciton, 最好直接把Trie的实现在已经给定的class里面
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.content = ""


class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    def _insert(self, path, content):
        curr = self.root
        for name in path.split("/")[1:]:
            curr = curr.child[name]
        curr.content += content
            
    def _search(self, path):    # search for path and return node at the end of path
        curr = self.root
        for name in path.split("/")[1:]:
            if name not in curr.child:
                return curr
            curr = curr.child[name]
        return curr

    def ls(self, path: str) -> List[str]:
        node = self._search(path)
        if node.content:
            return [path.split("/")[-1]]        # 这里只输出一个
        else:
            return sorted(node.child.keys())    # lexicographic order

    def mkdir(self, path: str) -> None:
        self._insert(path, "")

    def addContentToFile(self, filePath: str, content: str) -> None:
        self._insert(filePath, content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self._search(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
