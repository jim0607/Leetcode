364. Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.



"""
do a dfs to find the depth first, then another dfs to do 339. Nested List Weight Sum I
"""
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.max_depth = 1
        self._find_depth(nestedList, 1)
        return self._calculate_sums(nestedList, self.max_depth)
        
    def _find_depth(self, nestedList, depth):
        for lst in nestedList:
            if lst.isInteger():
                self.max_depth = max(self.max_depth, depth)
            else:
                self._find_depth(lst.getList(), depth + 1)
    
    def _calculate_sums(self, nestedList, depth):
        sums = 0
        for lst in nestedList:
            if lst.isInteger():
                sums += lst.getInteger() * depth
            else:
                sums += self._calculate_sums(lst.getList(), depth - 1)
        return sums
