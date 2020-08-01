1029. Two City Scheduling

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000



class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 排序标准：去city A比去city B多用多少钱
        # 这样一来去排在前面的就是去city A能省下最多钱的人
        # 让前N个人都去A就能省下最多的钱
        costs.sort(key = lambda x: (x[0] - x[1]))   
        N = len(costs) // 2
        total_cost = 0
        for i, [cost_A, cost_B] in enumerate(costs):
            total_cost = total_cost + cost_A if i < N else total_cost + cost_B
        return total_cost
