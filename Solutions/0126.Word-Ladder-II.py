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
# @lc code=start
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

"""二刷: made a slight change to help it faster: break in bfs if neighbor == beginWord"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        
        distance = collections.defaultdict()
        self.bfs(endWord, beginWord, wordList, distance)
        
        print(distance)
        
        res = []
        self.dfs(endWord, wordList, beginWord, [beginWord], distance, res)
        
        return res
    
    def bfs(self, endWord, beginWord, wordList, distance):
        q = collections.deque()
        q.append(endWord)
        distance[endWord] = 0
        
        dist = 0
        while q:
            dist += 1
            lens = len(q)
            for _ in range(lens):
                currWord = q.popleft()
                neighbors = self.getNeighbors(wordList, currWord)
                for neighbor in neighbors:
                    if neighbor not in distance:
                        q.append(neighbor)
                        distance[neighbor] = dist + 1
                        
                        if neighbor == beginWord:       # I thought I made it a little faster here, but somehow didn't, but good thinking man.
                            break
    
    def dfs(self, endWord, wordList, currWord, currWords, distance, res):
        if currWord == endWord:
            res.append(currWords.copy())        # !!! has to be a deep copy
            return
        
        neighbors = self.getNeighbors(wordList, currWord)
        for neighbor in neighbors:
            if currWord in distance and neighbor in distance:
                if distance[neighbor] >= distance[currWord]:
                    continue

                currWords.append(neighbor)
                self.dfs(endWord, wordList, neighbor, currWords, distance, res)
                currWords.pop()
            
    def getNeighbors(self, wordList, currWord):
        wordSet = set(wordList)
        res = []
        
        for i in range(len(currWord)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch != currWord[i]:
                    possibleWord = currWord[:i] + ch + currWord[i + 1:]
                    if possibleWord in wordSet:
                        res.append(possibleWord)
                    
        return res
