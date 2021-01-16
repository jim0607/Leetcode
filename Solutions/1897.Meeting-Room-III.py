"""
1897. Meeting Room III
you have a list intervals of current meetings, and some meeting rooms with start and end timestamp.When a stream of new meeting ask coming in, 
check if it can be scheduled.A meeting room can only hold one meeting at a time. Each inquiry is independent.

Example 1:
Input:
Intervals:[[1,2],[4,5],[8,10]], rooms = 1, ask: [[2,3],[3,4]]
Output: [true,true]
Explanation:
For the ask of [2,3], we can arrange a meeting room room0.
The following is the meeting list of room0:
[[1,2], [2,3], [4,5], [8,10]]
For the ask of [3,4], we can arrange a meeting room room0.
The following is the meeting list of room0:
[[1,2], [3,4], [4,5], [8,10]]
Example 2:
Input:
[[1,2],[4,5],[8,10]]
1
[[4,5],[5,6]]
Output:
[false,true]
Notice
Ensure that Intervals can be arranged in rooms meeting rooms
Ensure that the end time of any meeting is not greater than 50000
|Intervals|<=50000
|ask|<=50000
rooms<=20
"""


"""
sweep line + pre calculation solution: O(1) for queery. O(M + N) overall, M = len(intervals), N = len(ask)
给定一个区间组成的数组A，每个区间代表一个会议的开始和结束时间。
一共有room个会议室。再给定若干个询问，问(a , b)这个会议是否可以加入。

思路是pre-calculation: 开一个数组M，对于会议(a, b)，我们让M[a]加1，然后让M[b]减1。A遍历完之后，M[x]代表的是x这个时刻有多少个会议同时在进行。
如果M[x] < rooms，那么说明这个时刻是可以插入新会议的，否则说明不能.
我们可以用一个数组P来标记每个时刻是否需要新会议室（也就是如果来了新会议，是否需要新的会议室），如果不需要，则标记为0，否则标记为1，
那么：P[x] = 0 if M[x] < rooms, else 1.
给定新的会议(a, b)问题就转化为，问[a, a+1, . . . , b−1]这些位置上的P是否都是0，
也就是问以P[a−1]为结尾的前缀和是否等于以P[b-1]结尾的前缀和。所以只需要再缓存一下P的前缀和就行了
"""
class Solution:
    def meetingRoomIII(self, intervals, rooms, queries):
        max_end = max(max(end for _, end in intervals), max(end for _, end in queries))
        
        # cnter[x]代表的是x这个时刻有多少个会议同时在进行，算法: 只记录上升沿和下降沿
        cnter = [0 for _ in range(max_end + 1)]
        for start, end in intervals:
            cnter[start] += 1   # 只记录上升沿和下降沿
            cnter[end] -= 1
            
        # need[x]表示x时刻是否需要新会议室（也就是如果来了新会议，是否需要新的会议室）
        need = [0 for _ in range(max_end + 1)]
        need_cnt = 0
        for i in range(max_end + 1):
            need_cnt += cnter[i]
            if need_cnt >= rooms:
                need[i] = 1
                
        # 构造前缀和presums
        presums = [0 for _ in range(max_end + 2)]
        for i in range(max_end + 1):
            presums[i+1] = presums[i] + need[i]
            
        # 给定新的会议(a, b)问题就转化为，问[a, a+1, . . . , b−1]这些位置上的need是否都是0
        res = []
        for start, end in queries:
            if presums[end] == presums[start]:   # [a, a+1, . . . , b−1]这些位置上的need是否都是0
                res.append(True)
            else:
                res.append(False)
        return res


"""
naive sweep line solutoin: O(N) for query, O(MN) overall. 
"""
class Solution:
    def meetingRoomIII(self, intervals, rooms, ask):
        def can_book(start, end):             # O(N)
            start_idx = bisect.bisect_left(starts, start)
            end_idx = bisect.bisect_left(ends, end)
            starts.insert(start_idx, start)
            ends.insert(end_idx, end)
            
            i, j = 0, 0
            rooms_needed = 0
            can_book = True
            while i < len(starts) and j < len(ends):
                if starts[i] < ends[j]:
                    rooms_needed += 1
                    i += 1
                else:
                    rooms_needed -= 1
                    j += 1
                if rooms_needed > rooms:
                    can_book = False
                    
            starts.remove(start)
            ends.remove(end)
            
            return can_book
        
        
        starts = [start for start, end in intervals]
        ends = [end for start, end in intervals]
        
        starts.sort()
        ends.sort()
        
        res = []
        for start, end in ask:
            res.append(can_book(start, end))
        return res
