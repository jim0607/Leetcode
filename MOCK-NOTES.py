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
