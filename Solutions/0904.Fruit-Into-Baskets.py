"""
904. Fruit Into Baskets

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""



"""
The problem is so poorly described, should be described as following:
"Start from any index, we can collect at most two types of fruits. What is the maximum lens"
eg: [3,3,3,1,2,1,1,2,3,3,4], we can choose [1,2,1,1,2] because there are only two types of fruit (1 and 2).
now that we sort it out, it is exactly the same as 159. Longest Substring with At Most Two Distinct Characters

longest substring with at most two distinct chars
"""
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        type_to_cnt = defaultdict(int)
        max_lens = 0
        i = 0
        for j in range(len(tree)):
            type_to_cnt[tree[j]] += 1
            
            while i <= j and len(type_to_cnt) > 2:
                type_to_cnt[tree[i]] -= 1
                if type_to_cnt[tree[i]] == 0:
                    del type_to_cnt[tree[i]]
                i += 1
                
            if len(type_to_cnt) <= 2:
                max_lens = max(max_lens, j - i + 1)
                
        return max_lens
