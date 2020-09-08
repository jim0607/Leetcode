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
"""
Time complexity: O(26NL^2), where N is the number of words in word_set, and L is avg length of words.
"""
class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = set(word_list)
        if end_word not in word_set:
            return 0
        
        q = collections.deque()
        visited = set()
        q.append(begin_word)
        visited.add(begin_word)
        
        steps = 0
        while len(q) > 0:       # O(N), where N is number of words in word_set
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_word = q.popleft()
                if curr_word == end_word:
                    return steps
                for next_word in self._get_next(word_set, curr_word):   # O(26L^2)
                    if next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
        return 0
        
    def _get_next(self, word_set, curr_word):           # O(26*L^2)
        res = []
        for i, ch in enumerate(curr_word):              # O(L) 
            for letter in "abcdefghijklmnopqrstuvwxyz": # O(26)
                if letter == ch:
                    continue
                next_word = curr_word[:i] + letter + curr_word[i+1:]  # string slicing is basically copy - O(L)
                if next_word in word_set:               # O(L) cuz we need check letter by letter
                    res.append(next_word)
        return res
                
    
"""
这是要了亲命了，Leetcode已经不接受 O(26NL^2) 了，我们想办法吧26去掉，因为L is less than 5 to 6 in real word.
方法是用一个构造一个dictionary, key is all possible combination of the word, value is the word, 这样就可以快速查询了。
Time complexity: O(NL^2), where N is the number of words in word_set, and L is avg length of words.
"""
class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = word_list
        if end_word not in word_set:
            return 0
        
        # step 1: 构造一个dictionary, key is all possible combination of the word, value is the word
        L = len(begin_word)
        all_combo_dict = collections.defaultdict(list)
        for word in word_set:           # constructing the all_combo_dict takes O(NL^2) overall
            for i in range(L):
                intermediate_word = word[:i] + "*" + word[i+1:]
                all_combo_dict[intermediate_word].append(word)
        
        q = collections.deque()
        visited = set()
        q.append(begin_word)
        visited.add(begin_word)
        
        steps = 0
        while len(q) > 0:       # O(N), where N is number of words in word_set
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_word = q.popleft()
                if curr_word == end_word:
                    return steps
                for next_word in self._get_all_combo(all_combo_dict, curr_word):   # O(L^2)
                    if next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
        return 0
        
    def _get_all_combo(self, all_combo_dict, curr_word):           # O(L^2)
        res = []
        for i in range(len(curr_word)):
            intermediate_word = curr_word[:i] + "*" + curr_word[i+1:]
            res += all_combo_dict[intermediate_word]
        return res



"""solution 2: double ended BFS
利用双端BFS大大提高速度，注意双端bfs传进去的参数包含q and visited, bfs返回值是updated q and visited. 
双端bfs是src/des每走一步判断一下if visited_src & visited_des: return step; 
在双端BFS的过程中判断if not q_src or not q_des: 则说明q_src或q_des里面的所有possible neighbor都不在wordList里面，也就是没有必要继续进行了; 
The idea behind bidirectional search is to run two simultaneous searches: 
one forward from the initial state and the other backward from the destination state — hoping that the two searches meet in the middle. 
The motivation is that b^(d/2) + b^(d/2) is much less than b^d. b is branch number, d is depth.

Time complexity: O(26NL^2), where N is the number of words in word_set, and L is avg length of words.
"""
class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = word_list
        if end_word not in word_set:
            return 0
        
        q_src, q_des = collections.deque(), collections.deque()
        visited_src, visited_des = set(), set()
        q_src.append(begin_word)
        q_des.append(end_word)
        visited_src.add(begin_word)
        visited_des.add(end_word)
        
        steps = 1
        while len(q_src) > 0 and len(q_des) > 0:  # 如果q_src为空了，说明从src开始的bfs不能再继续往下走了
            if visited_src & visited_des:   # set1 & set2 return the intersection of set1 and set2 - O(min(L1, L2))
                return steps                # where L1 is the length of set1
            
            q_src, visited_src = self._bfs(word_set, q_src, visited_src)
            steps += 1
            
            if visited_src & visited_des:
                return steps
            
            q_des, visited_des = self._bfs(word_set, q_des, visited_des)
            steps += 1
        
        return 0
        
    def _bfs(self, word_set, q, visited):    
        """
        注意双端bfs只走一步并更新q, visited. 因为只遍历一层, 所以没有while len(q) > 0的loop
        """
        lens = len(q)
        for _ in range(lens):
            curr_word = q.popleft()
            for next_word in self._get_next(word_set, curr_word):   # O(L^2)
                if next_word not in visited:
                    q.append(next_word)
                    visited.add(next_word)
        return q, visited       # 双端bfs return的是更新之后的q, visited
        
    def _get_next(self, word_set, curr_word):           # O(26*L^2)
        res = []
        for i, ch in enumerate(curr_word):              # O(L) 
            for letter in "abcdefghijklmnopqrstuvwxyz": # O(26)
                if letter == ch:
                    continue
                next_word = curr_word[:i] + letter + curr_word[i+1:]  # string slicing is basically copy - O(L)
                if next_word in word_set:               # O(L) cuz we need check letter by letter
                    res.append(next_word)
        return res
                
