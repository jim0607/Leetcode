04/26/2020
Mock with Celia
1. 560. Subarray Sum Equals K
做出来了但是在 if tempSum - k in prefixSumDict: 这句话出现过一个bug
2. 269. Alien Dictionary
一个小bug: define a dictionary with values to be a list: edges = collections.defaultdict(list)
一个大bug!!! topological sorting在bfs过程中要减去inDegree的值，并且在inDegree减到0的时候加入到q中去。
            for char in edges[node]:
                inDegree[char] -= 1
                if inDegree[char] == 0:
                    q.append(char)
最后做出来了，没有提交成功是因为leetcode又添加了新的edge case
Follow up question: when doing bfs, we deal with one layer, then append the following layer and then deal with another layer.  
But there is no specific order within a layer.  What if I want to maintain an order within the layer?
Answer: instead of using a q, we use a heapq, then we can maintian an order each time we push a node into the the heapq.

问题：
1. 应该向面试官提问题，比如: Before implementing the algorithm, ask the intervier: is there an optimized solution you know that you want me 
to take, or we are ok if I implement this algorithm.
2. 写完code之后，应该主动写一个test case, 然后go over the test case with your code.
3. 感觉自己的表达真的很差，前期不知道怎么把自己的algorithm讲清楚，中途不知道怎么聊天，之后不知道怎么把每个block解释清楚。
4. Really should work on how to explain your algorithm!!!

Audience in LiBai's Mock
1. 695. Max Area of Island
用dfs解的，用到了global variable: max, cnt
2. 678. Valid Parenthesis String
这题没有看明白

04/27
1. 22. Generate parenthesis
2. peak in rotated array



05/03/2020
Mock with Celia
1. 415. Add strings
就是要注意carryBit和出了循环之后的判断
2. 215. Kth Largest Element in an Array
Solutions 1: Heapq: O(NlogK),  It should be noted that Heapify is O(N) time!!!
Solution 2: quick select
                        
05/03/2020
Audience
283. Move Zeroes
                        
05/04/2020
Audience
Kth closest to zero
how priority queue poll work? 
siftUp, siftDown, heapify
Solution 2: Quick select average O(N), worst case O(N^2)
Q: how to avoid O(N^2) time complexity
1. randomly choose a pivot, 可以把数分成每五个一组，然后在里面去取。
2. shuffle the list everytime choosing a pivot
技巧：
1. 问引导性问题, can we assume...., can we .....
2. 主动去run case, show you know debug
3. 先写一个seudo code, 然后问do you have any questions for me so far?

 - 面试的时候更关心bug free, 然后是time complexity. Space complexity不是很重要
 - 一定要保证bug free
 - 一定要快速的写很多的注释，把思路解释清楚，自己follow起来也很快一些。
