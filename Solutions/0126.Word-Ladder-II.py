#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (19.89%)
# Likes:    1373
# Dislikes: 220
# Total Accepted:    153.1K
# Total Submissions: 765.1K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#
"""
本题要求最短路径，所以一定要用到BFS
又要求输出满足最短这个条件的所有路径，所以一定要用到DFS
本题是带层序遍历的BFS + 带backtracking的DFS
算法：如果需要从start位置出发做DFS，想要走最短路径去end位置，我们每一步都不能往远离end位置的节点走，因为如果往远离end位置的节点走的话就不会是最短路径了，
所以每一步都要往离end更近的节点走，那么问题来了，start位置开始有好几个节点可以走，怎样判断选哪一个节点走会往end更进一步呢？那就需要直到这些节点离end的距离，
求每个节点离某个end位置的距离问题，就需要用到带层序遍历的BFS，用一个hashmap记录每一个节点离end的距离
所以总结起来程序的顺序是：
1. 从end到start做BFS，记录每一个节点到end节点的距离，存入hashmap中 eg: distance["dog"] = 2
2. 从start到end做DFS，每走一步都必须确保end的distance越来越近。最后将路径都存入到res里
"""

class Solution:
    def findLadders(self, beginword: str, endword: str, wordlist: list[str]) -> List[List[str]]:
        def backtrack(curr_node, curr_comb):
            if curr_node == endword:
                res.append(curr_comb.copy())
                return
        
            for next_node in get_nextwords(curr_node):
                if next_node not in distance or distance[next_node] >= distance[curr_node]:
                    continue
                curr_comb.append(next_node)
                backtrack(next_node, curr_comb)
                curr_comb.pop()
        
        
        def bfs():              # O(N), where N is number of words in word_set
            q = deque()
            visited = set()
            q.append(endword)
            visited.add(endword)
            dist = -1
            while len(q) > 0:
                dist += 1
                lens = len(q)
                for _ in range(lens):
                    curr_node = q.popleft()
                    distance[curr_node] = dist
                    if curr_node == beginword:      # don't need to keep going anymore
                        return
                    for next_node in get_nextwords(curr_node):
                        if next_node not in visited:
                            q.append(next_node)
                            visited.add(next_node)        
        
        
        def get_nextwords(word):                # O(L^2)
            res = []
            for i, ch in enumerate(word):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter != ch:
                        candidate = word[:i] + letter + word[i+1:]
                        if candidate in wordset:
                            res.append(candidate)
            return res      

        
        wordset = set(wordlist)  
        wordset.add(beginword)
        if endword not in wordset:
            return []
        
        distance = defaultdict(int)         # node --> distance of this node to end node
        bfs()                               # update distance dictionary in bfs
        
        res = []
        backtrack(beginword, [beginword])   # backtrack to find the path
        return res



















class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        word_set = set(word_list)
        word_set.add(begin_word)
        if end_word not in word_set:
            return []
        
        # step 1: 构造一个dictionary, key is all possible combination of the word, value is the word
        # this makes it much much fater cuz finding next_word only takes O(L^2) now
        L = len(begin_word)
        all_combo_dict = collections.defaultdict(list)
        for word in word_set:           # constructing the all_combo_dict takes O(NL^2) overall
            for i in range(L):
                intermediate_word = word[:i] + "*" + word[i+1:]
                all_combo_dict[intermediate_word].append(word)

        # step 2: bfs to find the distance of each node to the end_word
        distance = collections.defaultdict(int)
        self._bfs(end_word, begin_word, all_combo_dict, distance)
        
        # step 3: backtrack to get the shortest path
        res = []
        visited = set()
        self._backtrack(begin_word, end_word, all_combo_dict, distance, visited, [begin_word], res)
        return res
    
    def _backtrack(self, curr_word, end_word, all_combo_dict, distance, visited, curr_res, res):
        if curr_word == end_word:
            res.append(curr_res.copy())
            return
        for next_word in self._get_all_combo(all_combo_dict, curr_word):   # O(L^2)
            if next_word in visited:
                continue
            if distance[next_word] >= distance[curr_word]:
                continue
            visited.add(next_word)
            curr_res.append(next_word)
            self._backtrack(next_word, end_word, all_combo_dict, distance, visited, curr_res, res)
            curr_res.pop()
            visited.remove(next_word)        
        
    def _bfs(self, end_word, begin_word, all_combo_dict, distance) -> int:
        q = collections.deque()
        visited = set()
        q.append(end_word)
        visited.add(end_word)
        steps = -1
        while len(q) > 0:       # O(N), where N is number of words in word_set
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_word = q.popleft()
                distance[curr_word] = steps
                if curr_word == begin_word:
                    return
                for next_word in self._get_all_combo(all_combo_dict, curr_word):   # O(L^2)
                    if next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)

    def _get_all_combo(self, all_combo_dict, curr_word):           # O(L^2)
        res = []
        for i in range(len(curr_word)):
            intermediate_word = curr_word[:i] + "*" + curr_word[i+1:]
            res += all_combo_dict[intermediate_word]
        return res











class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList:
            return []
        if endWord not in wordList:
            return []

        # beginWord is not in the wordList according to the problem discribtion
        wordList.append(beginWord)
        
        distance = collections.defaultdict()        # 相当于visited = set()，还有一个作用是存储每个节点到end节点的距离
        self.bfs(endWord, wordList, distance)

        res = []
        self.dfs(endWord, wordList, beginWord, [beginWord], distance, res)

        return res

    # 求出每一个节点离end节点的距离，存入到distance中
    def bfs(self, endWord, wordList, distance):
        q = collections.deque()
        q.append(endWord)
        distance[endWord] = 0       # 一对孪生兄弟

        # 带层序遍历的BFS
        while q:
            lens = len(q)
            currWord = q.popleft()
            for nextWord in self.get_next_words(currWord, wordList):
                if nextWord not in distance.keys():     # 相当于if nextWord not in visited
                    distance[nextWord] = distance[currWord] + 1
                    q.append(nextWord)

    # 找出所有从start出发的路径，该路径满足每一步都往end更近的方向走，直到end
    def dfs(self, endWord, wordList, currWord, currWords, distance, res):
        if currWord == endWord:
            res.append(currWords.copy())    # deep copy
            return
        
        for nextWord in self.get_next_words(currWord, wordList):    # 相当于for neighbor in neighbors:
            if distance[nextWord] >= distance[currWord]:        # 不往远离end的方向走
                continue

            currWords.append(nextWord)
            self.dfs(endWord, wordList, nextWord, currWords, distance, res)
            currWords.pop()

    # 用O(26*L)的时间复杂度实现
    def get_next_words(self, currWord, wordList):
        wordSet = set(wordList)

        possible_words = []
        for i in range(len(currWord)):
            for ch in "poiuytrewqasdfghjklmnbvcxz":
                if ch != currWord[i]:
                    possible_word = currWord[:i] + ch + currWord[i+1:]
                    if possible_word in wordSet:
                        possible_words.append(possible_word)

        return possible_words

# @lc code=end

"""三刷: made a slight change to help it faster"""
"""
step 1: from endWord to startWord, do a bfs and store all the distance to endWord information in bfs
step 2: start from startWord, we do dfs, each tiem, we only travel to the word with distance closer to endWord
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        self.wordList = wordList
        
        self.distance = collections.defaultdict(int)
        self.distance[endWord] = 0
        
        self.bfs(beginWord, endWord)
        
        if beginWord not in self.distance:      # if beginWord not in the dictionary, then we cannot reach beginWord from endWord
            return []
        
        self.res = []
        self.backtrack(endWord, beginWord, [beginWord])
        
        return self.res
        
    def bfs(self, beginWord, endWord):
        q = collections.deque()
        visited = set()
        q.append(endWord)
        visited.add(endWord)
        
        dist = 0
        while q:
            dist += 1
            lens = len(q)
            
            for _ in range(lens):
                currWord = q.popleft()
                
                for nextWord in self.nextWords(currWord):
                    if nextWord in visited:
                        continue
                    
                    q.append(nextWord)
                    visited.add(nextWord)
                    self.distance[nextWord] = dist
                    
                    if nextWord == beginWord:   # pruning: return if nextWord == beginWord
                        return
    
    
    def backtrack(self, endWord, currWord, currWords):
        if currWord == endWord:
            self.res.append(currWords.copy())
            
        for nextWord in self.nextWords(currWord):
            if self.distance[nextWord] >= self.distance[currWord]:
                continue
            
            currWords.append(nextWord)
            self.backtrack(endWord, nextWord, currWords)
            currWords.pop()
            
    
    def nextWords(self, word):
        wordSet = set(self.wordList)
        
        possibleWords = set()
        for i in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter != word[i]:
                    possibleWord = word[:i] + letter + word[i+1:]
                    if possibleWord in wordSet:
                        possibleWords.add(possibleWord)
                        
        return possibleWords
