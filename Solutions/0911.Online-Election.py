"""
911. Online Election

In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: 
TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
 
Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""


"""
Precomputed Answer + Binary Search.
Constructor: O(N). each query: O(logN)
"""
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        p_to_cnt = defaultdict(int)
        max_cnt = 0
        self.winners = []
        for p, t in zip(persons, times):
            p_to_cnt[p] += 1
            if p_to_cnt[p] >= max_cnt:
                self.winners.append((t, p))
                max_cnt = p_to_cnt[p]
            else:
                self.winners.append((t, self.winners[-1][1]))

    def q(self, t: int) -> int:
        if t >= self.winners[-1][0]:
            return self.winners[-1][1]
        
        start, end = 0, len(self.winners) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.winners[mid][0] >= t:
                end = mid
            else:
                start = mid
        if self.winners[end][0] <= t:
            return self.winners[end][1]
        else:
            return self.winners[start][1]



class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        
        # below 我们将每一个时刻的winner放到self.res中，这种提前计算好的思想非常重要！
        n = len(persons)
        p_to_cnt = collections.defaultdict(int)
        max_cnt, max_cnt_p = 0, 0
        self.res = []
        for i, time in enumerate(times):
            p = persons[i]
            p_to_cnt[p] += 1
            if p_to_cnt[p] >= max_cnt:  # 可以等于因为In the case of a tie, the most recent vote (among tied candidates) wins
                max_cnt = p_to_cnt[p]
                max_cnt_p = p
            self.res.append(max_cnt_p)

    def q(self, t: int) -> int:
        """
        Thanks to the pre-calculated res, now we can do binary search in each q
        """
        idx = bisect.bisect_right(self.times, t) - 1
        return self.res[idx]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
