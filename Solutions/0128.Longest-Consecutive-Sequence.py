128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.



"""
使用一个集合HashSet存入所有的数字，然后遍历数组中的每个数字，如果其在集合中存在，那么将其移除，然后分别用两个变量pre和next算出其前一个数跟后一个数，
然后在集合中循环查找，如果pre在集合中，那么将pre移除集合，然后pre再自减1，直至pre不在集合之中，对next采用同样的方法，
那么next-pre-1就是当前数字的最长连续序列，更新res即可。
这里再说下，为啥当检测某数字在集合中存在当时候，都要移除数字。这是为了避免大量的重复计算，就拿题目中的例子来说吧，
我们在遍历到4的时候，会向下遍历3，2，1，如果都不移除数字的话，遍历到1的时候，还会遍历2，3，4。同样，遍历到3的时候，向上遍历4，向下遍历2，1，等等等。
如果数组中有大量的连续数字的话，那么就有大量的重复计算，十分的不高效，所以我们要从HashSet中移除数字.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_cnt = 0
        for num in nums:
            if num in numset:
                numset.remove(num)
                cnt = 1
                
                prev = num - 1
                while prev in numset:
                    numset.remove(prev)
                    cnt += 1
                    prev -= 1
                
                next = num + 1
                while next in numset:
                    numset.remove(next)
                    cnt += 1
                    next += 1
                    
                max_cnt = max(max_cnt, cnt)
                
        return max_cnt

    
"""
Follow up question: what if we can add a number into the nums list, 
and each time we add a number, we need to query the longest consecutive seqence?
Answer: we need to realize dynamic connection.  We can choose UnionFind.
需要query 点a所在集合的元素个数，所以需要用一个dictionary self.size 用来记录每个father节点所在集合的点的个数，
在union i 和 j 的时候: father[i] = j, sz[j] += sz[i].  
算法是我们遍历nums, 对于每一个num, 我们connect num and num-  1, also connect num and num + 1
"""

class UnionFind:
    
    def __init__(self, nums):
        self.father = collections.defaultdict(int)
        self.size = collections.defaultdict(int)
        
        for num in nums:
            self.add(num)
            
    def add(self, x):
        self.father[x] = x
        self.size[x] = 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]  # 更新root_b的size


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        uf = UnionFind(nums)
        for num in nums:
            if num - 1 in uf.father:        # 注意这里要判断一下是不是在uf.father里面
                uf.union(num, num - 1)
            if num + 1 in uf.father:
                uf.union(num, num + 1)
                
        return max(sz for _, sz in uf.size.items())
