"""
519. Random Flip Matrix

You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. 
Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. 
Also, write a function reset which sets all values back to 0. T
ry to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows and 0 <= col.id < n_cols
flip will not be called when the matrix has no 0 values left.
the total number of calls to flip and reset will not exceed 1000.
Example 1:

Input: 
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]
Example 2:

Input: 
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution's constructor has two arguments, n_rows and n_cols. 
flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""


    
"""
This is a sampling n elements without replacement problem. It is the same as the operation that random shuffe an array and then return the first n elements.
When we random pick an element in the array we can store its new position in a hash table instead of the array because n is extremely less than the total num. 
So we can accomplish this within O(1) time and O(k) space where k is the maxium call of flip.
"""
    
import random

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows= n_rows
        self.n_cols = n_cols
        self.start = 0
        self.end = self.n_rows * self.n_cols
        self.pos_dict = collections.defaultdict(int)
        

    def flip(self) -> List[int]:
        # generate index
        rand_idx = random.randrange(self.start, self.end)
        
        # check if we have already put something at this index
        # The get() method takes maximum of two parameters: 
        # key - key to be searched in the dictionary
        # value (optional) - Value to be returned if the key is not found. The default value is None.
        res = self.pos_dict.get(rand_idx, rand_idx)     
        
        # swap - put total at index that we generated
        self.pos_dict[rand_idx] = self.pos_dict.get(self.start, self.start)
        
        # decrease total number of values
        self.start += 1
        
        return [res // self.n_cols, res % self.n_cols]
    
    
    def reset(self) -> None:
        self.pos_dict = collections.defaultdict()
        self.start = 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
