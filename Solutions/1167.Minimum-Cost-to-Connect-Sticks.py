"""
1167. Minimum Cost to Connect Sticks

It killed me to understand this, I will try to explain it as best as I can.

The question IS NOT asking what the length of the stick will be at the end. It's asking to find the cost of assembling the final stick.

So before any work is done, we have 3 sticks, and 0 work completed:

0.) sticks: [2, 4, 3], work == 0

1.) in the first iteration, we combine the sticks of length 2 and 3, for a workload of 5:
sticks: [4, 5] (because 2 + 3), work == 5

2.) Next, we combine the sticks 4 and 5.
sticks: [9] (because 4 + 5) work == 9

Now, to compute the final result, sum up all of the WORK from ALL OF THE STEPS.

work 1 == 5
work 2 == 9

result = 9 + 5 == 14.
"""


"""
下面这个sort的解法不work原因是我们不能保证每次lens都是最小的，可能两个小的加起来得到了一个很大的。
eg: [4,5,6,7], 下面的解法是[4,5,6,7]-->[9,6,7]-->[15,7]-->[22]
正确的解法是[4,5,6,7]-->[9,6,7]-->[9,13]-->[22]
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        
        sticks.sort()
        
        cost = sticks[0] + sticks[1]
        lens = sticks[0] + sticks[1]
        for stick in sticks[2:]:
            cost += lens + stick
            lens += stick
        return cost
"""
"""
我们需要实时地保证选出两个数是最小的, heappop可以保证这一点，所以用heapq
"""
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        hq = []
        for stick in sticks:
            heappush(hq, stick)
            
        cost = 0
        while len(hq) > 1:
            stick_1, stick_2 = heappop(hq), heappop(hq)
            cost += stick_1 + stick_2
            heappush(hq, stick_1 + stick_2)
        return cost
