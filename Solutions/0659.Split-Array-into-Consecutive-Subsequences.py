659. Split Array into Consecutive Subsequences

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

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
这道题我们遍历nums的时候只要当前的num被前面的顺子需要，就把num连上去，顺子连得越长越好，这就是greedy所在，
使用两个 HashMap，第一个 HashMap 用来建立某个数字和其出现次数之间的映射 freq，
第二个用来建立某个数字被前面顺子所需要的次数之间的映射 need。
对于第二个 HashMap，举个例子来说，就是假如有个连牌，比如对于数字1，此时检测数字2和3是否存在，
若存在的话，表明有连牌 [1,2,3] 存在，由于后面可以加上4，组成更长的连牌，
所以不管此时牌里有没有4，都可以建立 4->1 的映射，表明此时需要一个4。
"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        need = collections.defaultdict(int)
        for num in nums:
            if freq[num] == 0: continue
                
            # need[num] > 0说明num被前面的顺子所需要，也就是可以和前面组顺子
            if need[num] > 0:       
                need[num] -= 1      # 只要被前面的顺子需要，我就连上去，顺子连得越长越好，这就是greedy所在
                need[num + 1] += 1
                
            # need[num] > 0说明不被前面的顺子所需要，也就是不能和前面组顺子
            # 那就只能往后面找顺子，去找num+1, num+2存不存在数组中
            elif need[num] == 0:    
                if freq[num + 1] > 0 and freq[num + 2] > 0:
                    freq[num + 1] -= 1
                    freq[num + 2] -= 1
                    need[num + 3] += 1
                else:
                    return False    
            
            freq[num] -= 1      # 别忘了freq自减一
            
        return True
