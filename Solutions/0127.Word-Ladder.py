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
        if not wordList:
            return 
        
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
