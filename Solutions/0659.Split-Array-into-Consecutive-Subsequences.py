"""
659. Split Array into Consecutive Subsequences

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences 
such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False
"""


"""
这道题我们遍历nums的时候只要当前的num被前面的顺子需要，就把num连上去，顺子连得越长越好，这就是greedy所在，
使用两个 HashMap，第一个 HashMap 用来建立某个数字和其出现次数之间的映射 freq，
第二个用来建立某个数字被前面顺子所需要的次数之间的映射 need。
对于第二个 HashMap，举个例子来说，就是假如有个连牌，比如对于数字1，此时检测数字2和3是否存在，
若存在的话，表明有连牌 [1,2,3] 存在，由于后面可以加上4，组成更长的连牌，
所以不管此时牌里有没有4，都可以建立 4->1 的映射，表明此时需要一个4。

The logic is to just apply a greedy approach and try to find a group of 3 consecutive numbers first and then
for other numbers try to check if existing groups can be used or it is neccessary to create a new group.
"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnter = Counter(nums)
        can_append = defaultdict(int)
        for num in nums:
            if cnter[num] == 0:
                continue

            # can_append[num] > 0 说明num可以append到前面已经存在的顺子中，那就不需要开一个新顺子了
            # greedy: 只要能append到前面已经存在的顺子中，就append上去
            if can_append[num] > 0:
                cnter[num] -= 1         # 用num append到前面的顺子中
                can_append[num] -= 1        # 只要被前面的顺子需要，我就连上去
                can_append[num + 1] += 1
                
            # can_append[num] == 0 说明不能append到前面的顺子中，那只能新开一个新顺子
            # 那就只能往后面找顺子，去找num+1, num+2存不存在数组中
            else:
                for i in range(3):
                    if cnter[num + i] == 0:
                        return False
                    cnter[num + i] -= 1
                can_append[num + 3] += 1  # can_append[num + 3] += 1只是表示num + 3可以append到一个新顺子上去，num + 3不一定需要存在于nums中
                
        return True                
