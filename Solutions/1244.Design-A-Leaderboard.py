"""
1244. Design A Leaderboard

Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. 
If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). 
It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.

Example 1:
Input: 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output: 
[null,null,null,null,null,null,73,null,null,null,141]

Explanation: 
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
"""



"""
use a dictionary for fast addscore and reset. use a heapq to find top K elements
"""
class Leaderboard:

    def __init__(self):
        self.mapping = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.mapping[playerId] += score

    def top(self, K: int) -> int:
        """
        we can wither use a heapq to find top K elements using O(NlogK),
        or use quick select to find top K elements using O(N)
        Let's use heapq here
        """
        hq = [-score for score in self.mapping.values()]
        heapq.heapify(hq)
        sums = 0
        for _ in range(K):
            sums += -heapq.heappop(hq)
        return sums

    def reset(self, playerId: int) -> None:
        self.mapping[playerId] = 0


"""
use sortedContainers, here we use SortedDict, which is implemented using red-black tree.
"""
