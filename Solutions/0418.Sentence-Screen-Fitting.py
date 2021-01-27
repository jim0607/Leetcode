"""
418. Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, 
find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
"""


"""
fit the sentence in line by line
"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        
        total_len = 0   # get the total_len we need to fit in the whole sentence
        for s in sentence:
            total_len += 1 + len(s)
        
        res = 0
        i = 0
        for _ in range(rows):
            remain = cols   # how many empty space we have in curr_row
            while remain > 0:
                if remain < len(sentence[i]):
                    break
                    
                remain -= len(sentence[i])
                if remain > 0:
                    remain -= 1
                
                i += 1
                if i == n:  # this is when we need to repeat in a row
                    i = 0
                    res += 1 + remain // total_len
                    remain %= total_len
                
        return res
