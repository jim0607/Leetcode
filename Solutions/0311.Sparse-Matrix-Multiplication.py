311. Sparse Matrix Multiplication

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |



"""
solution 1: brutal force: O(M*N) could be large for sparse large matrix
"""

"""
solution 2:
use a dictinoary to store the index and value of non-zero values
O(M+N + m*n), O(M+N), M is the number of elements in matrix A, m is the number of non-zero elements in A.
"""
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        dictA, dictB = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    dictA[(i, j)] = A[i][j]
                    
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    dictB[(i, j)] = B[i][j]
                   
        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for (rowA, colA), valA in dictA.items():
            for (rowB, colB), valB in dictB.items():
                if colA == rowB:        # 这里地方在面试的时候不一定写得出来，一定要多想想
                    res[rowA][colB] += valA * valB
                    
        return res
        
        
"""
solution 3: use a nested sequence to store the index value information. https://www.cs.cmu.edu/~scandal/cacm/node9.html
somehow the time complexity is better? don't know why.
"""

Follow up questions in a real interview:
面试官先问每个vector很大，不能在内存中存下怎么办，我说只需存下非零元素和他们的下标就行，然后问面试官是否可用预处理后的
这两个vector非零元素的index和value作为输入，面试官同意后写完O(M*N)的代码(输入未排序，只能一个个找)，MN分别是两个vector长度。

又问这两个输入如果是根据下标排序好的怎么办，是否可以同时利用两个输入都是排序好这一个特性，最后写出了O(M + N)的双指针方法，
每次移动pair里index0较小的指针，如果相等则进行计算，再移动两个指针。

又问如果一个向量比另一个长很多怎么办，我说可以遍历长度短的那一个，然后用二分搜索的方法在另一个vector中找index相同的那个元素，
相乘加入到结果中，这样的话复杂度就是O(M*logN)。

又问如果两个数组一样长，且一会sparse一会dense怎么办。他说你可以在two pointer的扫描中内置一个切换二分搜索的机制。
看差值我说过，设计个反馈我说过，他说不好。他期待的解答是，two pointers找到下个位置需要m次比较，而直接二分搜需要log(n)次比较。
那么在你用two pointers方法移动log(n)次以后，就可以果断切换成二分搜索模式了。

Binary search如果找到了一个元素index，那就用这次的index作为下次binary search的开始。可以节约掉之前的东西，不用search了。
然后问，如果找不到呢，如何优化。说如果找不到，也返回上次search结束的index，然后下次接着search。
就是上一次找到了，就用这个index继续找这次的；如果找不到，也有一个ending index，就用那个index当starting index。
比如[1, 89，100]，去找90；如果不存在，那么binary search的ending index应该是89，所以下次就从那个index开始。
如果找不到，会返回要插入的位置index + 1，index是要插入的位置，我写的就是返回要插入的index的。
但是不管返回89还是100的index都无所谓，反正只差一个，对performance没有明显影响的。
