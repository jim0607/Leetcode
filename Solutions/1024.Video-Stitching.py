"""
You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  
We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation: 
We can't cover [0,5] with only [0,1] and [0,2].
Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation: 
We can take clips [0,4], [4,7], and [6,9].
Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation: 
Notice you can have extra video after the event ends.
"""



"""
每次都选结束时间最大的，比如选了[0, 4], 那就选开始时间在[0, 4]的Interval中选结束时间最大的, 比如选到了[2, 9],
接着就在开始时间为[4, 9]的interval中选结束时间最大的，比如[7, 15]....这样依次下去。。。
直到找到一个结束时间大于T的 - 需要提前sort - O(nlogn)
"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key = lambda x: (x[0], x[1]))
    
        # 下面就是套用jump game II的模板
        curr_coverage = 0
        i = 0
        steps = 0
        while i < len(clips):
            next_coverage = curr_coverage
            while i < len(clips) and clips[i][0] <= curr_coverage:
                next_coverage = max(next_coverage, clips[i][1])
                i += 1
            
            steps += 1
            if next_coverage >= T:
                return steps
            if curr_coverage == next_coverage:
                return -1
            
            i = curr_coverage + 1
            curr_coverage = next_coverage
        
        return -1




"""
solution 2: jump game - 无需sort - O(N).
先建立一个reacable list. reachable[idx]=start from idx, where can we reach.  然后就是jump game II了，求最少几步从0跳到T.
Jump Game II greedy的思想非常重要。
"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        reachable = [0 for _ in range(T)]
        for start, end in clips:
            if start < T:
                reachable[start] = max(reachable[start], end)
                
        # step 2: now we can do jump game II to find min steps
        last_coverage = 0
        next_coverage = reachable[0]
        steps = 0
        i = 0
        while i < T:
            while i <= last_coverage:     # 这里的下标i是start time, 所以自然而然是已经sort好了的
                next_coverage = max(next_coverage, reachable[i])
                i += 1
            
            if next_coverage == last_coverage:
                return -1
            last_coverage = next_coverage
        
            steps += 1
            if next_coverage >= T:
                return steps
