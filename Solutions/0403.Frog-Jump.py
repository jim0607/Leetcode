"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
"""



"""
维护一个stonesDict的key is the stone in stones. value is the possible steps to reach the stone.
There could be multiple possible steps to reach the stone, so stonesDict[stone] = set(). 
状态转移方程为：1. 跳k-1到stone+k-1: stonesDict[stone + k - 1].add(k - 1); 2. 跳k到stone + k: stonesDict[stone + k].add(k); 
3. 跳k + 1到stone + k + 1:stonesDict[stone + k + 1].add(k + 1); Return the len(stonesDict[last stone])>0?
this is bottom up method O(N^2), O(N^2)
"""
"""
dp[i][k] = can the frog jump to the ith stone using k units?
dp[0][1] = True dp[0][other] = False
dp[j][k] = True if there is a dp[i][k,k+1,k-1] which nums[i] == k, k+1, k-1 is True
return dp[n-1][any] is True
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [defaultdict(lambda: False) for _ in range(n)]
        dp[0][0] = True
        for j in range(1, n):
            for i in range(j):
                k = stones[j] - stones[i]
                if dp[i][k] or dp[i][k+1] or (k > 0 and dp[i][k-1]):
                    dp[j][k] = True
        return any(val == True for val in dp[n-1].values())
    
    

"""
stone_to_steps = (stone --> possible steps taken to reach stone)
O(N)
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)    # convert to set for fast loop up
        
        stone_to_steps = defaultdict(set)
        stone_to_steps[stones[0]].add(0)
        for stone in stones:
            for k in stone_to_steps[stone]:     # 注意这个k不是任意取的
                if k + 1 + stone in stones_set:
                    stone_to_steps[k+1+stone].add(k+1)
                if k + stone in stones_set:
                    stone_to_steps[k+stone].add(k)
                if k - 1 > 0 and k - 1 + stone in stones_set:   # 如果这里用k>=1的话会报错: set changed size during interation, 因为change了自己的size
                    stone_to_steps[k-1+stone].add(k-1)
                    
        return len(stone_to_steps[stones[-1]]) > 0
    
    
    


class Solution {
    public boolean canCross(int[] stones) {
        HashMap<Integer, Set<Integer>> dpMap = new HashMap<>();  // dp[stone]为set，记录青蛙可以通过哪些步跳到stone
        for (int stone : stones) {
            dpMap.put(stone, new HashSet<Integer>());
        }
        
        dpMap.get(0).add(0);
        
        for (int stone : stones) {
            for (int k : dpMap.get(stone)) {
                if (k - 1 > 0 && dpMap.containsKey(stone + k - 1)) {
                    dpMap.get(stone + k - 1).add(k - 1);
                } if (dpMap.containsKey(stone + k)) {
                    dpMap.get(stone + k).add(k);
                } if (dpMap.containsKey(stone + k + 1)) {
                    dpMap.get(stone + k + 1).add(k + 1);
                }
            }
        }
        return dpMap.get(stones[stones.length - 1]).size() != 0;
    }
}



"""f[k][i]=能否用k步跳到位置i; the last jump is from j to i using k steps then j = dictStones[stones[i] - k]; f[k][i]=True if case 1: last jump was k-1步: f[k-1][i-dict[A[i-(k-1)]]] = True or case 2: last jump was k步: f[k][i-dict[A[i-k]]] = True or case 3: last jump was k+1步: f[k+1][i-dict[A[i-(k+1)]]] = True
This is top down method, somehow doesn't work"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return 0
        
        lens = len(stones)
        dictStones = {}
        for i, stone in enumerate(stones):
            dictStones[stone] = i
            
        dp = [[False] * lens for _ in range(lens)]
        
        for k in range(lens):
            for i in range(lens):
                if i == 0 and k == 0:
                    dp[k][i] = True
                    continue
                
                if stones[i] - k in dictStones:
                    j = dictStones[stones[i] - k]   # the last jump is from j to i using k steps
                    if dp[k - 1][j] or dp[k][j] or dp[k + 1][j]:
                        dp[k][i] = True
                    
        for k in range(1, lens):
            if dp[k][-1] == True:
                return True
            
        print(dp)
        
        return False
