630. Course Schedule III

There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.



""" Course Schedule 三部曲，前两部都是topological sort, 这一部是heapq贪心处理intervals """
"""
首先给课程排个序，按照结束时间的顺序来排序，我们维护一个当前的时间，对于每一个遍历到的课程，将该课程持续时间放入优先数组中,
并选择参加这个课程：更新结束时间，然后我们判断更新后的结束时间是否大于该课程的结束时间，如果大于，说明这门课程无法被如期完成，
此时我们要选择一门课gvie up掉，那么问题是我们该gvie up掉哪门课呢？
注意我们并不是直接gvie up掉这门课，而是选择gvie up掉用时最长的一门课，这也make sense，
因为我们的目标是尽可能的多上课，既然非要去gvie up掉一门课，那肯定是去掉耗时最长的课，
这样省下来的时间说不定能多上几门课呢
"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: (x[1], x[0]))
        
        hq = []     # max heap for duration
        curr_time = 0
        for duration, end_time in courses:
            heappush(hq, -duration)         # 以duration来维护一个最大堆，这么做可行是因为hq中的intervals是没有overlapping的
            curr_time += duration           # 更新参加这个course之后的结束时间
            if curr_time > end_time:        # this means that curr course cannot be taken in time
                curr_time -= -heappop(hq)   # so we need to give up one class, which course should we give up?
                                            # the one that can make curr_time as small as possible: the one with largest duration
        return len(hq)
