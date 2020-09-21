453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, 
where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]




"""
需要换一个角度来看问题，其实给 n-1 个数字加1，效果等同于给那个未被选中的数字减1，
比如数组 [1，2，3]，给除去最大值的其他数字加1，变为 [2，3，3]，等价于最大的数减一变为 [1，2，2]，
那么问题也可能转化为，将所有数字都减小到最小值，只要先找到最小值，然后累加每个数跟最小值之间的差值即可
"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        return sum(num - min_num for num in nums)
