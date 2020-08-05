Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]



"""
build a content_to_dir dictionary where key is content in txt file, 
val is a list of dir holding the content eg: ["root/a/1.txt"]
"""
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_dir = collections.defaultdict(list)
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            for s in path[1:]:
                file_name = s[:s.index(".txt") + 4]
                content = s[s.index(".txt") + 5:-1]
                directory = folder + "/" + file_name
                content_to_dir[content].append(directory)
                
        res = []
        for directory in content_to_dir.values():
            if len(directory) > 1:
                res.append(directory)
        return res
        
        
        
"""
Follow-ups:

1. Imagine you are given a real file system, how will you search files? DFS or BFS?
BFS vs. DFS in real file system:
BFS: BFS explores neigbours first. This means that files which are located close to each other are also accessed one after another. 
This is great for space locality and that's why BFS is expected to be faster. Also, BFS is easier to parellelize.
The memory of BFS is determined by the width of search. The memory of DFS is decided by the depth. Generally on average BFS takes more memory.
Dfs, if you run DFS in a real file system, you may get a read lock on the a node X then that lock will be active for longer time if there are a lot of nodes under X 
which is usually the case in real file system.
As a conculution: In general, BFS will use more memory then DFS. 
However BFS can take advantage of the locality of files in inside directories, and therefore will probably be faster.


2. If the file content is very large (GB level), how will you modify your solution?
In a real life solution we will not hash the entire file content, since it's not practical. 
Instead we will firstly map all the files according to size. Files with different sizes are guaranteed to be different. 
We will then hash a small part of the files with equal sizes (using MD5 for example). 
Only if the md5 is the same, we will finally then compare the files byte by byte.


3. If you can only read the file by 1kb each time, how will you modify your solution?
This won't change the solution. We can create the hash from the 1kb chunks, and then read the entire file if a full byte by byte comparison is required.


4. What is the time complexity of your modified solution? What is the most time consuming part and memory consuming part of it? How to optimize?
Time complexity is O(n^2 * k) since in worse case we might need to compare every file to all others. k is the file size
The worst case is when there are lots of collisions.
So hash collision part is the most time-consuming and memory consuming because we need to compare byte by byte if there is a colision.


5. How to make sure the duplicated files you find are not false positive?
Firstly, what is flase positive? False positive is something like you think you find the right file, but you the files are not exactly the same,
this happens especialy when a hash colision happens, where the hash funciton thinks they are the same, but they are not.
Similar with question 2, or very large files we should do the following comparisons in this order:
Firstly, compare sizes, if not equal, then files are different and stop here!
Then, hash them with a fast algorithm e.g. MD5 or use SHA256 (no collisions found yet), if not equal then stop here!
Finally, compare byte by byte to avoid false positives due to collisions.
        
         
        
