"""
904. Fruit Into Baskets

In a row of trees, the i-th tree produces fruit with type tree[i].
"""



"""
The problem is so poorly described, should be described as following:
"Start from any index, we can collect at most two types of fruits. What is the maximum lens"
eg: [3,3,3,1,2,1,1,2,3,3,4], we can choose [1,2,1,1,2] because there are only two types of fruit (1 and 2).
now that we sort it out, it is exactly the same as 159. Longest Substring with At Most Two Distinct Characters
"""
"""
longest substring with at most two distinct chars
"""
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        type_to_cnt = collections.defaultdict(int)
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
