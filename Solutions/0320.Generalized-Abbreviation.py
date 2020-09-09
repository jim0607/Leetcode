"""
320. Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""




"""
backtrack中传入的参数(curr_idx, curr_num, curr_word). 
backtrack结束条件: if curr_idx == len(word)-1. 
分两种情况: case 1: treat word[next_idx] as a letter; case 2: treat word[next_idx] as a number
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def backtrack(curr_idx, curr_num, curr_word):
            if curr_idx == len(word) - 1:
                res.append(curr_word)
                return
            
            # case 1: treat word[next_idx] as a letter
            backtrack(curr_idx + 1, 0, curr_word + word[curr_idx+1])
            
            # case 2: treat word[next_idx] as a number
            if curr_num == 0:
                backtrack(curr_idx + 1, curr_num + 1, curr_word + str(curr_num + 1))
            elif curr_num < 10:
                backtrack(curr_idx + 1, curr_num + 1, curr_word[:-1] + str(curr_num + 1))
            elif curr_num < 100:    # 如果curr_num大于10那么curr_word[:-1]就是错的，eg: "abc14"
                backtrack(curr_idx + 1, curr_num + 1, curr_word[:-2] + str(curr_num + 1))
                
        
        res = []
        backtrack(-1, 0, "")
        return res



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
