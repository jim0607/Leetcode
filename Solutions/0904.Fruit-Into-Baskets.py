904. Fruit Into Baskets

In a row of trees, the i-th tree produces fruit with type tree[i].


"""
The problem is so poorly described, should be described as following:
"Start from any index, we can collect at most two types of fruits. What is the maximum lens"
eg: [3,3,3,1,2,1,1,2,3,3,4], we can choose [1,2,1,1,2] because there are only two types of fruit (1 and 2).
now that we sort it out, it is exactly the same as 159. Longest Substring with At Most Two Distinct Characters
"""
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        max_lens = 0
        j = 0
        freq = collections.defaultdict(int)
        for i in range(len(tree)):
            while j < len(tree) and len(freq) <= 2:
                if tree[j] not in freq and len(freq) == 2:
                    break
                freq[tree[j]] += 1
                j += 1
            
            if len(freq) <= 2:
                max_lens = max(max_lens, j - i)
                
            freq[tree[i]] -= 1
            if freq[tree[i]] == 0:
                del freq[tree[i]]
                
        return max_lens
