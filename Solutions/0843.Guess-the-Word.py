"""
843. Guess the Word

This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
"""



# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
"""
Repeatedly choose a word to guess, and then eliminate all words that do not have the same number of matches as the guessed word. 
In this way, the wordlist is narrowed down each time we do a guess.
How to choose a word: solution 1: random guess; 2. choose the guess word wisely
"""
""" solution 1 """
import random

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        candidates = [word for word in wordlist]
        for i in range(10):
            guess_word = candidates[random.randrange(0, len(candidates))]     # choose word by random guess
            cnt = master.guess(guess_word)
            if cnt == 6:
                break
            
            # narrow down the wordlist by filtering words that only share cnt common chars with guess_word
            candidates = self._filter_words(candidates, guess_word, cnt)
            
    def _filter_words(self, candidates, guess_word, target_cnt):
        res = []
        for word in candidates:
            cnt = 0
            for i in range(len(word)):
                if word[i] == guess_word[i]:
                    cnt += 1
            if cnt == target_cnt:
                res.append(word)
        return res



# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

""" 
solution 2: choose the guess word wisely. 
Each time we guess, we choose the word that has the most common chars (overlaps) with other words in the candidates list.
This is just a hueristic estimation, hard to prove why it works. But indeed it works much better than random guess.
"""
import random

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        candidates = [word for word in wordlist]
        for i in range(10):
            guess_word = self._choose_word_by_most_overlap(candidates)    # choose word 
            cnt = master.guess(guess_word)
            if cnt == 6:
                break
            
            # narrow down the wordlist by filtering words that only share cnt common chars with guess_word
            candidates = self._filter_words(candidates, guess_word, cnt)
            
    def _filter_words(self, candidates, guess_word, target_cnt):
        res = []
        for word in candidates:
            cnt = 0
            for i in range(len(word)):
                if word[i] == guess_word[i]:
                    cnt += 1
            if cnt == target_cnt:
                res.append(word)
        return res
    
    def _choose_word_by_most_overlap(self, candidates):
        counts = collections.defaultdict(int)   # (ch, pos) --> cnt
        for word in candidates:
            for pos, ch in enumerate(word):
                counts[(ch, pos)] += 1
        
        most_overlap_cnt = 0
        most_overlap_word = candidates[0]
        for word in candidates:
            overlap_cnt = 0
            for pos, ch in enumerate(word):
                overlap_cnt += counts[(ch, pos)]
            if overlap_cnt > most_overlap_cnt:
                most_overlap_cnt = overlap_cnt
                most_overlap_word = word
        return most_overlap_word



"""
Note that the above solutions doesn't garantee that we can find the word in 10 guesses.
For solution 1, only about 80% percent chance that we can get the secret word in 10 guesses.
For solution 2: more than 99% precent chance it works.
"""
