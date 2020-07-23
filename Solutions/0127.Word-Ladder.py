#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (26.81%)
# Likes:    2206
# Dislikes: 964
# Total Accepted:    340.9K
# Total Submissions: 1.3M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
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
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
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
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        visited = set()
        steps = self.bfs(beginWord, endWord, wordList, visited)
        
        return steps
    
    def bfs(self, beginWord, endWord, wordList, visited):
        q = collections.deque()
        q.append(beginWord)
        visited.add(beginWord)
        
        steps = 1
        while q:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                currWord = q.popleft()
                neighborWords = self.getNeighborWords(currWord, wordList)
                
                for neighborWord in neighborWords:
                    if neighborWord == endWord:
                        return steps
                    if neighborWord not in visited:
                        q.append(neighborWord)
                        visited.add(neighborWord)
        
        return 0
    
    def getNeighborWords(self, currWord, wordList):
        wordSet = set(wordList)
        neighborWords = set()
        
        for i in range(len(currWord)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch != currWord[i]:
                    neighborWord = currWord[:i] + ch + currWord[i + 1:]     # 用ch替换currWord中的第i个元素
                    if neighborWord in wordSet:             # 变成set之后，这个语句就成了O(1)了，所以这个函数的整体为O(26*L) where L=len(currWord)
                        neighborWords.add(neighborWord)
                        
        return neighborWords
    
    # """    
#     # O(N*L), 本题中N很大，L比较小不会超过6，所以主要的时间复杂度花在了N身上
#     def get_next_word(self, currWord, wordList):
#         res = []
#         for word in wordList:               # O(N), N is the number of word in wordList
#             cnt = 0
#             for i in range(len(word)):      # O(L), L is the legth of the word
#                 if word[i] != currWord[i]:
#                     cnt += 1
#             if cnt == 1:
#                 res.append(word)

#         return res
# """



"""solution 2: double ended BFS"""
"""
"The idea behind bidirectional search is to run two simultaneous searches—one forward from
the initial state and the other backward from the goal—hoping that the two searches meet in
the middle. The motivation is that b^(d/2) + b^(d/2) is much less than b^d. b is branch factor, d is depth."

----- section 3.4.6 in Artificial Intelligence - A modern approach by Stuart Russel and Peter Norvig
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        q_src, q_des = collections.deque(), collections.deque()
        visited_src, visited_des = set(), set()
        q_src.append(beginWord)
        visited_src.add(beginWord)
        q_des.append(endWord)
        visited_des.add(endWord)
        
        steps = 0
        while q_src and q_des:              # 这里是为了判断如果q_src为空了，说明所有的q_src里面的possible beighbor都不在wordList里面，也就是说not possible to trasform from beginWord to endWord
            if visited_src & visited_des:   # 找到了可以从src也可以从des到达的节点了
                return steps
            
            q_src, visited_src = self.bfs(wordList, q_src, visited_src)
            steps += 1
            
            if visited_src & visited_des:
                return steps
            
            q_des, visited_des = self.bfs(wordList, q_des, visited_des)
            steps += 1
            
        return 0
        
    def bfs(self, wordList, q, visited):
        """
        双端bfs中每个bfs只走一步，走完一步之后比较visited_src & visited_des
        """
        lens = len(q)
        for _ in range(lens):
            currWord = q.popleft()
            for nextWord in self.neighbors(wordList, currWord):
                if nextWord not in visited:
                    q.append(nextWord)
                    visited.add(nextWord)

        return q, visited
    
    
    def neighbors(self, wordList, currWord):
        """
        return all the neighbors of currWord that exist in wordList
        """
        wordSet = set()
        for word in wordList:
            wordSet.add(word)
            
        neighborSet = set()
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(currWord)):
            for ch in letters:
                if ch != currWord[i]:
                    tempWord = currWord[:i] + ch + currWord[i + 1:]
                    if tempWord in wordSet:
                        neighborSet.add(tempWord)
                        
        return neighborSet
