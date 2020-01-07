BFS的使用场景：
1. 简单图的最短路径（如骑士问题，word ladder问题）
2. 需要层序遍历

DFS的使用场景：
1. DFS 一般比BFS节省空间，因为BFS需要一个queue来存储至少一层的node。DFS的空间复杂度是递归的深度。
2. 打印或输出所有组合的问题：combination （eg: subsets 问题）
3. DFS 的考点是考你会不会写递归

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
        for i in range(start, len(nums)):
            curr.append(nums[i])                # [1] -> [1, 2]
            self.dfs(nums, i + 1, curr, res)    # 从nums中的start位置开始，挑选一些数，放到curr（此时为[1,2]）中，然后存入res里面。这就相当于把所有的以[1, 2]开头的子集都找到，且放进res里面
            curr.pop()                          # [1, 2] -> [1]，然后在进入for循环，然后curr再append 2后面的数 3, curr 变成[1, 3]，然后......周而复始，直至for循环结束。



排列问题是顺序相关的，也就是
排列permutation问题模板：
与combination相比，少了startIndex这个参数，因为不需要care顺序了



        
    
递归三要素：
1. 递归的定义：这个递归take哪些参数，返回什么值，做了什么事
2. 递归的拆解，往往是先divide，后conquer
3. 递归的出口
  
 
