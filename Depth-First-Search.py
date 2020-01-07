BFS的使用场景：
1. 简单图的最短路径问题（如骑士问题，word ladder问题）
2. 需要层序遍历

DFS的使用场景：
1. 打印/输出所有路径的问题一定是深度优先搜索。如果要求输出所有最短路径则需要DFS+BFS
2. 打印或输出所有组合/排列的问题：combination/permutation （eg: subsets/permutations 问题）
3. DFS 一般比BFS节省空间，因为BFS需要一个queue来存储至少一层的node。DFS的空间复杂度是递归的深度。DFS 的考点是考你会不会写递归

组合搜索问题模型：求出所有满足条件的组合
判断条件：组合中的元素是与顺序无关的
时间复杂度：与2^N有关，可能是N*2^N或者N^2*2^N等，总之是带个2^N的

Subsets问题模板：所有的combination问题都是这个模板，eg: combination sum, palindrome partition
def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)        
        return res
    
    # 递归的定义：从nums中的start位置开始，挑选一些数，放到curr中，然后存入res里面
    def dfs(self, nums: List[int], start: int, curr: List[int], res: List[List[int]]]):
        res.append(curr.copy())                 # has to be a deep copy
        # 这个for循环里curr一直在重复append和pop，[1, 2] -> [1] -> [1, 3] -> [1] -> [1, 4]......
        # 这就是为什么用back tracking了
        for i in range(start, len(nums)):              # 这里的for循环时间复杂度是N，所以总体时间复杂度是O(N*S)，S是solution的个数=2^N
            curr.append(nums[i])                # [1] -> [1, 2]
            self.dfs(nums, i + 1, curr, res)    # 从nums中的start位置开始，挑选一些数，放到curr（此时为[1,2]）中，然后存入res里面。这就相当于把所有的以[1, 2]开头的子集都找到，且放进res里面
            curr.pop()                          # [1, 2] -> [1]，然后在进入for循环，然后curr再append 2后面的数 3, curr 变成[1, 3]，然后......周而复始，直至for循环结束。



排列问题是顺序相关的，也就是说(1,3)和(3,1)是不一样的。时间复杂度与 N！相关。注意 N！比 2^N 还要大。
排列permutation问题模板：
与combination相比，少了startIndex这个参数，因为不需要care顺序了
时间复杂度为O(N*S)，用一个hashmap标记已经visited的元素，这样就不会让同一个元素被用到两次了。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        
        visited = {i: False for i in range(len(nums))}
        self.dfs(nums, [], res, visited)     # 与combination相比少了一个startIndex参数，加入visited用于防止重复访问

        return res

    def dfs(self, nums: List[int], curr: List[int], res: List[List[int]], visited):
        # 2. 递归的出口
        if len(curr) == len(nums):
            res.append(curr.copy())     # deep copy
            return

        for i in range(len(nums)):      # O(N)
            # 与combination相比多了这个if判断，这是因为在combination中有startIndex限制其职能从i+1后面找
            # 这里没有startIndex，每次都是从0开始找，可以找到自己，最后可能会输出[1,1,1]或[1,1,2]，显然不是[1,2,3]的permutation
            # 所以这个if是为了限制一个数只出现一次。
            if visited[i]:         # O(1), so overall O(N*S), S=solution=N!
                continue
            visited[i] = True       # append之后需要将visited[i]变为True
            curr.append(nums[i])
            self.dfs(nums, curr, res, visited)
            curr.pop()
            visited[i] = False     # pop出来之后将visited[i]再变回False


Search in Graph 的问题。
        
        
        
    
递归三要素：
1. 递归的定义：这个递归take哪些参数，返回什么值，做了什么事
2. 递归的拆解，往往是先divide，后conquer
3. 递归的出口
  
 
