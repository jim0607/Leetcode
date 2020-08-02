857. Minimum Cost to Hire K Workers

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 
Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 



"""
Suppose we have a team of two workers (w1, q1), (w2, q2). 
What we need to pay is max(w1, q1*w2/q2) + max(w2, q2*w1/q1). And w1 = q1*w1/q1, w2 = q2*w2/q2. 
So the cost is q1*max(w1/q1,w2/q2) + q2*max(w1/q1,w2/q2) = max(w1/q1,w2/q2) * (q1+q2).
So generally, a team cost is ∑wi = w/q * ∑qi where w/q is the maximum wage/quality ratio in that team.
分析到这，我们发现与1383. Maximum Performance of a Team是类似的。
我们将workers按照wage/quality ratio 升序排列，这样curr worker的wage/quality就是前K个中最大的，
我们curr worker 前面的quality存在一个max_heap中，heap的size保持为k，如果size>k就把最大的quiality踢出去。
"""
from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [(wage[i]/quality[i], quality[i]) for i in range(len(quality))]
        workers.sort(key = lambda x: (x[0], x[1]))
        
        max_quality = []
        min_payment = float("inf")
        total_qlt = 0
        for ratio, qlt in workers:
            heappush(max_quality, -qlt)
            total_qlt += qlt
            if len(max_quality) > k:
                total_qlt -= -heappop(max_quality)
            if len(max_quality) == k:
                min_payment = min(min_payment, total_qlt * ratio)
            
        return min_payment
