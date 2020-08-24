757. Set Intersection Size At Least Two

An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2.

Example 1:
Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Example 2:
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.



"""
按结束为止排序，当两个结束位置相同时，起始位置大的排前面先处理，这也符合我们先处理小区间的原则
It is actually much simpler to understand, since once you sort intervals by end-point, 
you just left with 3 cases to consider:
1. Next interval does not overlap，这时候我们就需要从当前区间中取出两个数字加入集合S，取哪两个数呢？
为了尽可能少使用数字，我们取当前区间中的最大两个数字，因为我们区间位置不断变大，
所以取大的数字有更高的概率能和后面的区间有交集。
2. Intervals overlap 二者有一个数字的交集，那么这个交集数字一定是区间的起始位置，
那么我们需要从当前区间中再取一个数字加入集合S，根据上面的分析，我们取最大的那个数，即区间的结束位置
3. Next interval contains previous one, 二者有两个及两个以上数字的交集，那么不用做任何处理.
具体算法如下：用个数组v来表示集合S，先给区间排序，然后遍历每个区间，
case 3: 如果区间的起始位置小于等于数组的倒数第二个数字，说明此时已经有两个相同的数字了，直接跳过当前区间。
case 1: 否则如果区间的起始位置大于数组的最后一个位置，说明二者没有任何交集，
我们此时把区间的最小和倒数第二小的数字加入数组v中。
"""
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # need to sort increasingly by end time and decreasingly by start time.
        # why decreasingly by start time? run an example: [[16,18],[11,18],[18,20],[10,11]]
        # 我们总是优先处理小区间，如果先处理大空间的话会造成混乱
        intervals.sort(key = lambda x: (x[1], -x[0]))      
        v = []
        for start, end in intervals:
            if not v or v[-1] < start:  # case 1: 没有任何交集
                v.append(end - 1)       # 就需要加入两个数来形成长度至少为2的intersection
                v.append(end)           # greedily, v是一小段一小段不连续的长度为二的区间[1,2,  5,6]
                
            elif start <= v[-2]:        # case 3: 已经有两个相同的数字的交集了  
                continue                # 就不需要加入任何数字了，因为已经有至少为2的intersection了
                
            else:                       # case 2: 有一个数字的交集
                v.append(end)           # 就只需要加入一个数字来形成长度至少为2的intersection
                
        return len(v)
