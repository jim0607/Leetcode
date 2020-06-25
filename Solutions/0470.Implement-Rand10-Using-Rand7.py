470. Implement Rand10() Using Rand7()

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().


Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]


"""
This solution is based upon Rejection Sampling. 
The main idea is when you generate a number in the desired range, output that number immediately. 
If the number is out of the desired range, reject it and re-sample again. 
As each number in the desired range has the same probability of being chosen, a uniform distribution is produced.

Obviously, we have to run rand7() function at least twice, as there are not enough numbers in the range of 1 to 10. 
By running rand7() twice, we can get integers from 1 to 49 uniformly. Why? 可以想想成一个2D table, 先生成一个row, 在生成一个col

rejection sampling: O(1), might call random multipule times
"""
class Solution:
    def rand10(self):
        row, col, idx = 0, 0, 0
        while True:
            row = rand7()
            col = rand7()
            idx = 7 * (row - 1) + col - 1       # 注意col-1和row-1是必须的，不然就不是在[1, 48]的均匀分布

            # 得到的idx是[1, 48]内uniform分布的数
            if idx < 40:
                return idx % 10 + 1       # +1是为了变成[1, 10]
