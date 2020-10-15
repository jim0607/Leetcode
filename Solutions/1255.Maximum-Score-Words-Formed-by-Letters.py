"""
1255. Maximum Score Words Formed by Letters

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. 
Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], 
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], 
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], 
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.
 
Constraints:

1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
"""



"""
find all subsets, similar with 78. Subsets.
O(26*2^n), n = len(words)
"""
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def backtrack(curr_idx, curr_score):
            """
            Subsets的问题不需要visited, 因为我们把curr_idx传入函数signature
            """
            self.max_score = max(self.max_score, curr_score)
            
            for next_idx in range(curr_idx + 1, len(words)):
                next_word = words[next_idx]                    
                w_cnter = Counter(next_word)
                if any(w_cnter[ch] > ch_cnter[ch] for ch in w_cnter):
                    continue        # 如果现有的letters无法组成这个word, 那就不能继续

                for ch in w_cnter:         # 从letters中减去word
                    ch_cnter[ch] -= w_cnter[ch]
                backtrack(next_idx, curr_score + word_score[next_word])
                for ch in w_cnter:         # 在letters中加入word: backtrack
                    ch_cnter[ch] += w_cnter[ch]

                    
        ch_cnter = Counter(letters)      
        word_score = defaultdict(int)   # word --> score of the word
        for word in set(words):     
            for ch in word:
                word_score[word] += score[ord(ch) - ord("a")]

        self.max_score = 0
        backtrack(-1, 0)
        return self.max_score
