135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.





class Solution:
    def candy(self, ratings: List[int]) -> int:
        lens = len(ratings)
        candies = [1] * lens    # assign each child one candy
        
        # 从左往右扫，更新向上的child需要的candy
        for i in range(1, lens):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                
        # 从右往左扫，更新向下的child需要的candy
        for i in range(lens - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])  # 因为之前已经更新过i了，所以这里要比较一下
                
        return sum(candies)
