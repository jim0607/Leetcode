You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

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
每次都选结束时间最大的，比如选了[0, 4], 那就选开始时间在[0, 4]的Interval中选结束时间最大的, 比如选到了[2, 9],
接着就在开始时间为[4, 9]的interval中选结束时间最大的，比如[7, 15]....这样依次下去。。。
直到找到一个结束时间大于T的 - 需要提前sort - O(nlogn)
"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key = lambda clip: (clip[0], clip[1]))
        
        if clips[0][0] > 0 or clips[-1][1] < T:
            return -1

        curr_start, curr_end, max_end = 0, 0, 0
        cnt = 0
        i = 0
        while i < len(clips):
            while i < len(clips) and curr_start <= clips[i][0] <= curr_end:
                max_end = max(max_end, clips[i][1])
                i += 1
                  
            if max_end == curr_end:
                return -1
            
            curr_start, curr_end = curr_end + 1, max_end
            cnt += 1
            
            if curr_end >= T:
                return cnt
            
        return -1

"""
[[0, 2], [1, 5], [1, 9], [4, 6], [5, 9], [8, 10]]
                           i                  j
   
   
curr_start = 10
curr_end =   10
"""




"""
solution 2: jump game - 无需sort - O(N).
先建立一个reacable list存放从当前idx出发能到达的地方，然后就是jump game II了，求最少几步从0跳到T.
Jump Game II greedy的思想非常重要。
"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # step 1: construct a reachable list to get prepared for jump game II
        # the index is each second of starting time, value is the largest end time can be reached at this second.
        reachable = [0 for _ in range(T)]
        for start, end in clips:
            if start >= T:
                continue
            reachable[start] = max(reachable[start], end)
            
        print(reachable)
        # step 2: now we can do jump game II to find min steps
        last_coverage = 0
        next_coverage = reachable[0]
        cnt = 0
        i = 0
        while i < T:
            while i < T and i <= last_coverage:     # 这里的下标i是start time, 所以自然而然是已经sort好了的
                next_coverage = max(next_coverage, reachable[i])
                i += 1
            
            if next_coverage == last_coverage:
                return -1
            
            last_coverage = next_coverage
            cnt += 1
            
            if last_coverage >= T:
                return cnt
            
        return -1





"""动态规划DP: O(T*N), O(T), 但是merge sort需要O(NlogN), O(N), 所以总的复杂度为O(T*N+NlogN), O(T+N)
这道题我看到了懵逼了一些时间。思考了良久发现这是一个跳蛙类型的动态规划。
动态规划的要点：
DP数组当中存储的状态i是：0-i时间段当中需要最小的视频数量。
DP数组当中的简要状态方程：dp[j]=min(dp[j], dp[clips[i][0]]+1) if j in clips[i]的区间"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        self.mergeSort2D(clips)
        if clips[0][0] > 0 or clips[-1][-1] < T:
            return -1
        dp = [float("inf")]*(T+1)
        dp[0] = 0
        for t in range(1, T+1):
            for i in range(len(clips)):
                if t > clips[i][0] and t <= clips[i][1]:  # 如果t在clips[i]的区间内的话，clips[i]可以贡献一波
                    dp[t] = min(dp[t], dp[clips[i][0]]+1)
        return -1 if dp[T] == float("inf") else dp[T]  
        
    # 经典的merge sort实现方法必须掌握,O(NlogN),O(N)
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        self.mergeSort(leftArr)
        self.mergeSort(rightArr)

        i, j, k = 0, 0, 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
                k += 1
            else:
                arr[k] = rightArr[j]
                j += 1
                k += 1

        if i == len(leftArr):
            arr[k:] = rightArr[j:]
        if j == len(rightArr):
            arr[k:] = leftArr[i:mid]

    # merge sort a 2D array by the order of the first element of each subarry
    def mergeSort2D(self, arr2D):
        if len(arr2D) <= 1:
            return 
        mid = len(arr2D)//2
        leftArr2D = arr2D[:mid]
        rightArr2D = arr2D[mid:]
        self.mergeSort2D(leftArr2D)
        self.mergeSort2D(rightArr2D)
        i, j, k = 0, 0, 0
        while i < len(leftArr2D) and j < len(rightArr2D):
            if leftArr2D[i][0] <= rightArr2D[j][0]:
                arr2D[k] = leftArr2D[i]
                i += 1
                k += 1
            else:
                arr2D[k] = rightArr2D[j]
                j += 1
                k += 1
        if i == len(leftArr2D):
            arr2D[k:] = rightArr2D[j:]
        if j == len(rightArr2D):
            arr2D[k:] = leftArr2D[i:mid]
            
            
"""解法二：贪心算法。这道题和算法书上的活动选择问题基本一致。O(NlogN+N), O(N)
利用贪心算法：在开始时间不大于t的视频中选择一个结束时间最大的那一个视频，其中t是上一个选择视频的结束时间。
算法：
对视频进行升序排列
选择一个从零开始的视频，它的结束时间是所有从零开始的视频中最大的，赋值给t
然后在其他视频中选择一个开始时间不超过t的视频，这个被选择的视频的结束时间也应该是最大的，赋值给t
重复，直到所有的视频都被遍历，或者t已经大于等于T"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        self.mergeSort2D(clips)
        print(clips)
        if clips[0][0] > 0 or clips[-1][-1] < T:
            return -1
        i, t, res = 0, 0, 0
        while i < len(clips) and t < T:
            temp_t = t
            while i < len(clips) and clips[i][0] <= temp_t:
                t = max(t, clips[i][1])
                i += 1
            res += 1
            print(i, t)
            if i < len(clips) and t < T and clips[i][0] > t:   # 因为数组排序了，clips[i][0] > t的话说明后面没有区间接的上了，如[[0,2],[7,10]]，这里的7就大于2。i < len(clips) and t < T 是必要的，因为可能i out of index, or t > T的情况下误输出-1
                return -1
        return res if t >= T else -1    # 注意这里不能用t==T，因为t可能大于T的。
