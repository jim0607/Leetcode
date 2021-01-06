"""
1383. Maximum Performance of a Team

There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent 
the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, 
since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 


Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). 
That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. 
That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
"""


"""
这题speed也可以变，efficiency也可以变，所以我们要想办法固定一个才能做计算，
将workers按照efficiency降序排序，这样我们只需要从第k个worker开始，
取他的efficiency去乘以(他之前所有workers选k个能组成的最大的speed)，
这个因为他的efficiency一定是这k个worker里面最小的。
可以保持一个k size的heap来存(他之前所有workers), 如果size>k就把min_speed的worker踢出去
"""
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        workers = [(speed[i], efficiency[i]) for i in range(len(speed))]
        workers.sort(key = lambda x: (-x[1], -x[0]))    # 将workers按照efficiency降序排序, 这样便利的时候就先取大的efficiency
        
        total_spd = 0
        max_perf = 0
        hq = []         # min heap 存我们想要的workers的speed
        
        # 遍历的过程中min_eff在不断减小，但是total_spd在不断增加，
        # 我们希望total_spd的增加能够弥补min_ef的减小
        for spd, eff in workers:
            heappush(hq, spd)
            total_spd += spd
            
            if len(hq) > k:
                total_spd -= heappop(hq)   # 不用担心踢出去的是现在这个，因为如果踢出去的正好是现在这个，那么上一个遍历已经考虑到了
                
            max_perf = max(max_perf, total_spd * eff)
            
        return max_perf % (10**9 + 7)
