BFS的使用场景：
1. 简单图的最短路径（如骑士问题，word ladder问题）
2. 需要层序遍历

DFS的使用场景：
1. DFS 一般比BFS节省空间，因为BFS需要一个queue来存储至少一层的node。DFS的空间复杂度是递归的深度。
2. 组合搜索问题 combination （eg: subsets 问题）
3. DFS 的考点是考你会不会写递归

组合搜索问题模型：求出所有满足条件的组合
判断条件：组合中的元素是与顺序无关的
时间复杂度：与2^N有关，可能是N*2^N或者N^2*2^N等，总之是带个2^N的

subsets问题模板：https://www.youtube.com/watch?v=CUzm-buvH_8  DFS+Backtracking
O(N*2^N), O(N)
从m中选n个数组合 C(m, n)问题：
nums = [.....]
res = []
n = ....  # 很多时候n=len(nums)
for length in range(n + 1)：
  dfs(nums, length, 0, [], res)   # 这个循环是为了保证输出每一个length从0--n的conbinations
return res

func dfs(nums, length, startIndex, curr, res):
  if len(curr) == length:
    res.append(curr.copy()) # 注意是要append(curr.copy()) 不然只会输出空数组。https://docs.python.org/3/library/copy.html For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other.
    return
   
  for i in range(startIndex, len(nums)):
    curr.append(nums[i])
    dfs(nums, length, i + 1, curr, res)  # 注意这里是i+1
    curr.pop()  # 画递归图可以理解回溯法
    
    
递归三要素：
1. 递归的定义：这个递归take哪些参数，返回什么值，做了什么事
2. 递归的拆解，往往是先divide，后conquer
3. 递归的出口
  
 
