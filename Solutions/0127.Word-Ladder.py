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
"""带层序遍历的BFS"""
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        if endWord not in wordList:
            return 0

        visited = set()
        steps = self.bfs(beginWord, endWord, wordList, visited)

        return steps

    # 直接套用带层序遍历的bfs的模板，都是一样的
    def bfs(self, beginWord, endWord, wordList, visited):
        q = collections.deque()
        q.append(beginWord)
        visited.add(beginWord)
        steps = 1
        while q:
            lens = len(q)
            steps += 1
            for _ in range(lens):
                currWord = q.popleft()
                # self.get_next_word 返回 a list of words that could be transformed from currWord in one step and also exist in wordList
                for nextWord in self.get_next_word(currWord, wordList):
                    if nextWord == endWord:
                        return steps
                    if nextWord not in visited:
                        q.append(nextWord)
                        visited.add(nextWord)
        
        return 0

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
    # 因为N很大， 想一个办法避免掉O(N)，可以将其做成一个hashmap
    # O(26*L+N) << O(L*N)
    def get_next_word(self, currWord, wordList):
        # convert List into set
        wordSet = set(wordList)                                 # O(N)

        possible_words = []
        for i in range(len(currWord)):                          # O(L)
            for ch in "poiuytrewqasdfghjklmnbvcxz":             # O(26)
                if ch != currWord[i]:
                    possible_word = currWord[:i] + ch + currWord[i + 1:]
                    if possible_word in wordSet:                # O(1)
                        possible_words.append(possible_word)
        
        return possible_words
    
# @lc code=end

