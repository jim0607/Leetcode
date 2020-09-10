"""
465. Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

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
time complexity is O(N*2^N) cuz we need to to balance curr_idx one by one, so O(N),
and each balance process, we need to put or not-put next_idx to balance curr_idx, so O(2^N)
"""
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def backtrack(curr_idx, curr_cnt):      # 我们backtrack的目标是是一个idx一个idx地去balance
            if curr_idx == len(lst) - 1:
                self.cnt = min(self.cnt, curr_cnt)
                return
            if lst[curr_idx] == 0:              # 如果当前curr_idx已经balanced了，那我们就去balance他的下一个idx
                backtrack(curr_idx + 1, curr_cnt)
            for next_idx in range(curr_idx + 1, len(lst)):  # 如果当前curr_idx没有balanced, 那我们就去后面找一个或几个idx去balance他
                if lst[curr_idx] * lst[next_idx] < 0:       # 题眼 - 只在一正一负的时候去balance curr_idx, 这样保证没有多余的操作
                    lst[next_idx] += lst[curr_idx]          # next_idx把钱交给curr_idx让curr_idx balance起来
                    backtrack(curr_idx + 1, curr_cnt + 1)   # 注意这里不要写成了backtrack(next_idx)哦，因为我们要一个idx一个idx去balance, 不能跳跃idx
                    lst[next_idx] -= lst[curr_idx]          # backrack
                    if lst[curr_idx] + lst[next_idx] == 0:  # 想想这个for loop是干什么的 - 在后面找一个或者几个idx去balance他
                        break     # 有可能在找的过程中lst[curr_idx]很负，但是lst[next_idx]不是很正，这时候就需要几个lst[next_idx]去balanced他
                                  # 但是如果lst[curr_idx]不是很负，一个lst[next_idx]就可以balanced他，那就不用继续在for loop里面找了
        
        # step 1: find all the balance information for each person
        mapping = collections.defaultdict(int)
        for u, v, money in transactions:
            mapping[u] += money
            mapping[v] -= money
        
        # step 2: we care only those person who own or owe money - put them in a list
        lst = []
        for key, val in mapping.items():
            if val != 0:
                lst.append(val)

        # step 3: backtrack to update the minimum transaction needed
        self.cnt = float("inf")     # minimum transaction needed
        backtrack(-1, 0)
        return self.cnt
