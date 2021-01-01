"""
465. Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. 
For example, Alice paid for Bill's lunch for $10. 
Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. 
Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), 
the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
"""




"""
用backtrack的方法我们一个idx一个idx去balance
backtrack结束条件: curr_balanced_idx == len(lst) - 1
constraints for next_candidate: next_balanced_idx = curr_balanced_idx + 1 
arguments pass into backtrack function: curr_idx, curr_cnt

time complexity is O(N*2^N) cuz we need to to balance curr_idx one by one, so O(N),
and each balance process, we need to put or not-put next_idx to balance curr_idx, so O(2^N)
"""
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def backtrack(curr_idx, curr_cnt):
            if curr_idx == len(lst) - 1:
                self.min_cnt = min(self.min_cnt, curr_cnt)
                return
            
            if lst[curr_idx] == 0:      # 如果当前curr_idx已经balanced了，那我们就去balance他的下一个idx
                backtrack(curr_idx + 1, curr_cnt)

            for idx in range(curr_idx + 1, len(lst)):     # 如果当前curr_idx没有balanced, 那我们就去后面找一个或几个idx去balance他
                if lst[idx] * lst[curr_idx] < 0:          # 题眼 - 只在一正一负的时候去balance curr_idx, 这样保证没有多余的操作
                    lst[idx] += lst[curr_idx]             # 把curr_idx里面的钱都扔给idx, 这样让lst[curr_idx] = 0
                    backtrack(curr_idx + 1, curr_cnt + 1) # 我们一个idx一个idx去balance, next_idx = curr_idx + 1
                    lst[idx] -= lst[curr_idx]             # backrack
        
        
        # step 1: create a lst of person who needs to get money (either positive or negative)
        mapping = defaultdict(int)  # person_id --> how much he/she needs to get
        for u, v, money in transactions:
            mapping[u] += money
            mapping[v] -= money
        lst = []
        for person_id, money in mapping.items():
            if money != 0:          # if a person doesn't own/owe money, don't put him/her in the lst
                lst.append(money)
                
        # step 2: do backtrack 模板
        self.min_cnt = sys.maxsize
        backtrack(-1, 0)
        return self.min_cnt
    
    
    
"""
优化一下： before the backtrack寻找一个idx满足 lst[idx] * lst[curr_idx] < 0的去cancel curr_idx, 
我们先看看有没有idx能够直接把curr_idx消成0的, 如果有，我们优先用这个idx - This is greedy algorithm
"""
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def backtrack(curr_idx, curr_cnt):
            if curr_idx == len(lst) - 1:
                self.min_cnt = min(self.min_cnt, curr_cnt)
                return
            
            if lst[curr_idx] == 0:      # 如果当前curr_idx已经balanced了，那我们就去balance他的下一个idx
                backtrack(curr_idx + 1, curr_cnt)
                
            # before the backtrack寻找一个idx满足 lst[idx] * lst[curr_idx] < 0的去cancel curr_idx, 
            # 我们先看看有没有idx能够直接把curr_idx消成0的, 如果有，我们优先用这个idx - This is greedy algorithm
            for idx in range(curr_idx + 1, len(lst)):
                if lst[idx] + lst[curr_idx] == 0:
                    lst[idx] += lst[curr_idx]
                    backtrack(curr_idx + 1, curr_cnt + 1)
                    lst[idx] -= lst[curr_idx]
                    return    # 注意这里return是因为只要找到一个idx能够直接把curr_idx消成0, 那就不用再继续往下找idx去cancel curr_idx了，因为他已经balance好了       

            for idx in range(curr_idx + 1, len(lst)):     # 如果当前curr_idx没有balanced, 那我们就去后面找一个或几个idx去balance他
                if lst[idx] * lst[curr_idx] < 0:          # 题眼 - 只在一正一负的时候去balance curr_idx, 这样保证没有多余的操作
                    lst[idx] += lst[curr_idx]             # 把curr_idx里面的钱都扔给idx, 这样让lst[curr_idx] = 0
                    backtrack(curr_idx + 1, curr_cnt + 1) # 我们一个idx一个idx去balance, next_idx = curr_idx + 1
                    lst[idx] -= lst[curr_idx]             # backrack
        
        
        # step 1: create a lst of person who needs to get money (either positive or negative)
        mapping = defaultdict(int)  # person_id --> how much he/she needs to get
        for u, v, money in transactions:
            mapping[u] += money
            mapping[v] -= money
        lst = []
        for person_id, money in mapping.items():
            if money != 0:          # if a person doesn't own/owe money, don't put him/her in the lst
                lst.append(money)
                
        # step 2: do backtrack 模板
        self.min_cnt = sys.maxsize
        backtrack(-1, 0)
        return self.min_cnt
