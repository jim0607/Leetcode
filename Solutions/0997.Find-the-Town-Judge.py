997. Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Constraints:

1 <= N <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N



"""
Time complexity is O(E + N)
"""
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N if N <= 1 else -1
        
        beingTrusted = collections.defaultdict(int)
        trustOthers = collections.defaultdict(int)
        for lst in trust:     # O(E) is number of edges
            beingTrusted[lst[1]] += 1
            trustOthers[lst[0]] += 1
            
        cnt = 0
        res = -1
        for key, val in beingTrusted.items():   # O(N) is number of nodes
            if val == N - 1 and key not in trustOthers.keys():
                cnt += 1
                res = key

        return res if cnt == 1 else -1


Follow up:

Can There Be More Than One Town Judge?
In the problem description, we're told that iff there is a town judge, there'll only be one town judge.
It's likely that not all interviewers would tell you directly that there can only be one town judge. 
If you asked them whether or not there could be more than one town judge, they might ask you if there could be. And the answer is... 
it's impossible!
If there were two town judges, then they would have to trust each other, otherwise we'd have a town judge not trusted by everybody. 
But this doesn't work, because town judges aren't supposed to trust anybody. Therefore, we know there can be at most one town judge.


A Related Question
Secondly, for premium members, there is a similar question on Leetcode, called Find the Celebrity. 
You need to do the same thing—find a person who has an indegree of N - 1 and an outdegree of 0. 
However, the input format is a bit different.
It's well worth a look at. A seemingly small difference (the input format) completely changes what the optimal algorithm to solve it is.
Interestingly though, the optimal algorithm for that problem can also be used here. 
The only difference is that there, it has a cost of O(N)O(N), but here it has a cost of O(E)O(E). 
Try and figure out why once you've solved both problems. It's a really nice example of cost analysis with graphs.
