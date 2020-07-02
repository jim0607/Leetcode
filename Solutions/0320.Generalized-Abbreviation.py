320. Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


"""
curr_idx: the idx at word; 
curr_cnt: the cnt at of number BEFORE curr_idx;
curr_path: the path BEFORE curr_idx;
分两个case做backtrack: case 1: treat word[next_idx] as a number; # case 2: treat word[next_idx] as a ch, then 我们需要结算curr_cnt了
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        lens = len(word)
        res = []
        
        def backtrack(curr_idx, curr_cnt, curr_path):
            if curr_idx == lens:
                res.append(curr_path if curr_cnt == 0 else curr_path + str(curr_cnt))
                return
            
            # case 1: treat word[next_idx] as a number
            backtrack(curr_idx + 1, curr_cnt + 1, curr_path)                    
            # case 2: treat word[next_idx] as a ch, then 我们需要结算curr_cnt了
            backtrack(curr_idx + 1, 0, curr_path + ("" if curr_cnt == 0 else str(curr_cnt)) + word[curr_idx])   
            
        backtrack(0, 0, "")
                      
        return res
