"""
68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""



"""
use curr_line = [] to record curr words in curr_line; use curr_width = 0 to record curr total number of chars in curr_line.
Iterate the word in words, if too many words to fit in one line, we first justify that line and update res, 
then start over the curr_line = [] and curr_width = 0 for the next line.
Lastly, we deal with the last line seperately.
"""
class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        curr_line = []
        curr_width = 0
        res = []
        
        for word in words:
            if len(word) + curr_width + len(curr_line) > max_width:     # len(curr_line)代表有多少空格
                curr_line = self._justify_line(curr_width, curr_line, max_width)
                res.append("".join(curr_line))
                curr_line = []
                curr_width = 0
                
            curr_line.append(word)
            curr_width += len(word)
            
        # now deal with last line
        last_line = " ".join(curr_line)     
        last_line += " " * (max_width - len(last_line))
        res.append(last_line)
        
        return res
    
    def _justify_line(self, width, line, max_width):
        nspaces = len(line) - 1 
        if nspaces == 0:    # deal with special case seperately to avoid error for i % nspaces division by zero
            line.append(" " * (max_width - width))
        else:
            for i in range(max_width - width):
                line[i % nspaces] += " "        # 在每一个word后面加一个空格, 加一轮空格之后如果没用完再回头加一轮
        return line
