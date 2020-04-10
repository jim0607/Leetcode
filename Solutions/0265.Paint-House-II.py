265. Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.



"""dp[i][j]=minimum cost to paint the ith house the be color j
O(N*K^2), O(N*K)"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n, k = len(costs), len(costs[0])
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(k):
                tempMin = float("inf")
                for m in range(j):
                    tempMin = min(tempMin, dp[i - 1][m])
                for m in range(j + 1, k):
                    tempMin = min(tempMin, dp[i - 1][m])
                    
                dp[i][j] = tempMin + costs[i][j]
        
        return min(dp[-1])
        
        
"""优化成O(N*K)，因为每次都需要求出最小值，如果我们记录最小值就可以减小计算量了"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n, k = len(costs), len(costs[0])
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0]
        
        for i in range(1, n):
            # find the position for the first and second minimum in dp[i - 1]
            min_1, min_2 = float("inf"), float("inf")
            j_1, j_2 = -1, -1
            for j in range(k):
                if dp[i - 1][j] <= min_1:
                    min_1, min_2 = dp[i - 1][j], min_1
                    j_1, j_2 = j, j_1
                elif min_1 < dp[i - 1][j] < min_2:
                    min_2 = dp[i - 1][j]
                    j_2 = j
                    
            for j in range(k):         
                if j != j_1:
                    dp[i][j] = dp[i - 1][j_1] + costs[i][j]
                else:
                    dp[i][j] = dp[i - 1][j_2] + costs[i][j]
        
        return min(dp[-1])
      
      
      
      
// Time: O(n*k), space: O(n*k)
class Solution {
    public int minCostII(int[][] costs) {
        if (costs.length == 0) return 0;
        
        int lens = costs.length, k = costs[0].length;
        int[][] dp = new int[lens][k];
        for (int i = 0; i < lens; i++) {
            if (i == 0) {
                dp[i] = costs[i];
            } else {
                // find the position for the 1st and 2nd minCost in the i-1 th row
                int firstMinCostPos = -1; int secondMinCostPos = -1;
                int firstMinCost = Integer.MAX_VALUE, secondMinCost = Integer.MAX_VALUE;
                for (int j = 0; j < k; j++) {
                    if (dp[i - 1][j] <= firstMinCost) {
                        secondMinCost = firstMinCost; firstMinCost = dp[i - 1][j];
                        secondMinCostPos = firstMinCostPos; firstMinCostPos = j;        
                    } else if (dp[i - 1][j] < secondMinCost) {
                        secondMinCost = dp[i - 1][j];
                        secondMinCostPos = j;
                    }
                }
                // apply dp algorithms to the i th row
                for (int j = 0; j < k; j++) {
                    if (j == firstMinCostPos) {
                        dp[i][j] = costs[i][j] + secondMinCost;
                    } else {
                        dp[i][j] = costs[i][j] + firstMinCost;
                    }
                }
            }
        }
        int minCost = Integer.MAX_VALUE;
        for (int cost : dp[lens - 1]) {
            minCost = Math.min(cost, minCost);
        }
        
        return minCost;
    }
}
