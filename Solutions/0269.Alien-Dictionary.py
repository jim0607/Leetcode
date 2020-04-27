There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.


"""理解题目关键在于理解words are sorted lexicographically的意思。举个例子: ["wrt","wrf"]这个例子中，"wrt"排在"wrf"前面，
这是因为在外星文中"t"排在"f"的前面。想想我们地球文中"abc"排在"abd"前面是因为"c"排在"d"前面，或者说ord("c") < ord("d")。
在外星文中，他们认为ord("t") < ord("f")。
理解了这个，我们进行比较的时候只需要比较word[i]与word[i+1]即可得到inDegree的关系以及neighbors的关系了。
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        inDegrees = collections.defaultdict(int)
        for word in words:          # initialize inDegrees for all chars to 0
            for ch in word:
                inDegrees[ch] = 0

        neighbors = collections.defaultdict(list)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]     # since dictionary given in lex. order, just need to compare one string to next
            for j in range(min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]
                if parent != child:
                    neighbors[parent].append(child)
                    inDegrees[child] += 1
                    break          # we can only learn from one char difference at a time, so break
        
        q = collections.deque()
        res = []
        for node, inDegree in inDegrees.items():
            if inDegree == 0:
                q.append(node)
                res.append(node)
            
        while q:
            currNode = q.popleft()
            for neighbor in neighbors[currNode]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    q.append(neighbor)
                    res.append(neighbor)
                    
        return "".join(res) if len(res) == len(neighbors) else ""  # 注意len(res) 的比较对象是inDegrees，因为前面初始化了inDegrees[所有的 ch] = 0

 
# leetcode变坏了，现在成功提交需要加一个self.abc_ab_Check(prevWord, currWord):
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        lens = len(words)
        if lens == 0:
            return ""
        
        inDegree = collections.defaultdict()
        for word in words:
            for char in word:
                inDegree[char] = 0
                
        edges = collections.defaultdict(list)
        
        # find Indegree and edges
        for i in range(1, lens):
            prevWord, currWord = words[i - 1], words[i]
            if self.abc_ab_Check(prevWord, currWord):
                return ""
            for j in range(min(len(prevWord), len(currWord))):
                if prevWord[j] != currWord[j]:              
                    inDegree[currWord[j]] += 1
                    edges[prevWord[j]].append(currWord[j])
                    break
                    
        print(edges)
        print(inDegree)
        
        q = collections.deque()
        # put all the indegree=0 into the q
        flag = False
        for char in inDegree.keys():
            if inDegree[char] == 0:
                q.append(char)            
           
        res = []
        while q:
            node = q.popleft()  # pop the node out
            res.append(node)

            for char in edges[node]:
                inDegree[char] -= 1
                if inDegree[char] == 0:
                    q.append(char)
        
        return "".join(res) if len(res) == len(edges) else ""
    
    def abc_ab_Check(self, prevWord, currWord):
        """
        return bool for abc, ab case
        """
        if len(prevWord) > len(currWord):
            for i in range(len(currWord)):
                if currWord[i] != prevWord[i]:
                    return False
            return True
        
        return False
