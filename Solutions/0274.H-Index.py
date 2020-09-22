"""
274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""



"""
bucket sort: - O(N) garanteed.
step 1: 把citation num被引次数放入bucket中作为idx, 而idx上对应的值是cnt of how many papers were cited this much time.
step 2: bucket size 是 len(citations);
step 3: O(N) 遍历把相应的(被引次数, how many paper被引了那么多次) pair 放到相应的(idx, val)上, 这样一来high idx上就天然放着high 被引次数了, 就不需要sort了
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0 for _ in range(n + 1)]    # 也可以将bucket size定义为 max(citations) + 1, 但是h-idx的上限是n
        
        for citation in citations:
            if citation >= n:
                bucket[n] += 1
            else:
                bucket[citation] += 1

        paper = 0           # paper代表符合条件的paper总数
        for i in range(n, -1, -1):      # 注意i代表的是被引次数
            paper += bucket[i]
            if i <= paper:
                return i
            
        return 0

      
# 也可以将bucket size定义为 max(citations) + 1    
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        bucket = [0 for _ in range(max(citations) + 1)]
        for citation in citations:
            bucket[citation] += 1
        
        cnt = 0     # record how many papers were cited as we traversal the bucket reversely
        for cited_times in range(len(bucket) - 1, -1, -1):
            cnt += bucket[cited_times]
            if cited_times <= cnt:
                return cited_times
