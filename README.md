## [Depth First Search](/Depth-First-Search.py)
- [0078. Subsets](Solutions/0078.Subsets.py) (！！M)(DFS + Back tracking)
- [0090. Subsets II](Solutions/0090.Subsets-II.py) (！！M)(如果之前的那个2没被放进去，那么就不要放后面那个2，这样会造成重复)
- [0039. Combination Sum](0039.Combination-Sum.py) (！M) (start是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次)
- [0040. Combination Sum II](0040.Combination-Sum-II.py) (！M) (避免重复输出的方法与Subsets II一样)
- [0131. Palindrome Partitioning](0131.Palindrome-Partitioning.py) (！M) (避免重复输出的方法与Subsets II一样)





## [Breadth First Search](/Breadth-First-Search.py)
### BFS in Trees
- [0102. Binary Tree Level Order Traversal](Solutions/0102.Binary-Tree-Level-Order-Traversal.py) (！！M)
- [0103. Binary Tree Zigzag Level Order Traversal](Solutions/0103.Binary-Tree-Zigzag-Level-Order-Traversal.py) (！M)
- [0107. Binary Tree Level Order Traversal II](Solutions/0107.Binary-Tree-Level-Order-Traversal-II.py) (！E)
- [0199. Binary Tree Right Side View](Solutions/0199.Binary-Tree-Right-Side-View.py) (！M)
- [0111. Minimum Depth of Binary Tree](Solutions/0111.Minimum-Depth-of-Binary-Tree.py) (E)
- [0297. Serialize and Deserialize Binary Tree](Solutions/0297.Serialize-and-Deserialize-Binary-Tree.py) (H)

### BFS in Graphs
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (M)
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (M)
- [0127. Topological Sorting](Solutions/0127.Topological-Sorting.py) (！！LintCode M) (Topological Sorting)
- [0207. Course Schedule](Solutions/0207.Course-Schedule.py) (！！M) (opological Sort)
- [0210. Course Schedule II](Solutions/0210.Course-Schedule-II.py) (！！M) (Naked Topological Sort)
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (M)

### BFS in Matrix !!
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (M)
- [0994. Rotting Oranges](Solutions/0994.Rotting-Oranges.py) (M) (需要层序遍历)
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (！！M) (需要层序遍历，利用对称解决LTE问题，也可以从两端同时开始BFS)
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (！！M) (层序遍历BFS，LTE，双端BFS看不太懂)
- [0317 Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (！！H) (选择1为起点做层序遍历的BFS)



## [Sort](/Sort.py) 
- [0912. Sort an Array](Solutions/0912.Sort-an-Array.py) (M) (quick sort vs. merge sort)



## [Binary Tree, Divide and Conquer](/Binary-Tree-Divide-and-Conquer.py) 
- [0144. Binary Tree Preorder Traversal](Solutions/0144.Binary-Tree-Preorder-Traversal.py) (M) (memorize the iterative version using stack)
- [0094. Binary Tree Inorder Traversal](Solutions/0094.Binary-Tree-Inorder-Traversal.py) (M) (memorize the iterative version using stack)
- [0104. Maximum Depth of Binary Tree](Solutions/0104.Maximum-Depth-of-Binary-Tree.py) (E) (Divide and Conquer vs Traverse)
- [0257. Binary Tree Paths](Solutions/0257.Binary-Tree-Paths.py) (E)
- [0596. Minimum Subtree](Solutions/0596.Minimum-Subtree.py) (LintCode) (Divide and Conquer + Traverse)
- [0597. Subtree with Maximum Average](Solutions/0597.Subtree-with-Maximum-Average.py) (LintCode) (Divide and Conquer + Traverse + resultType)
- [0110. Balanced Binary Tree](Solutions/0110.Balanced-Binary-Tree.py) (E) (resultType, used for return multipule values)
- [0235. Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py) (E)
- [0236. Lowest Common Ancestor of a Binary Tree](Solutions/0236.Lowest-Common-Ancestor-of-a-Binary-Tree.py) (M)
- [0700. Search in a Binary Search Tree](Solutions/0700.Search-in-a-Binary-Search-Tree.py) (E)
- [0938. Range Sum of BST](Solutions/0938.Range-Sum-of-BST.py) (E)
- [0098. Validate Binary Search Tree](Solutions/0098.Validate-Binary-Search-Tree.py) (M)
- [0426. Convert Binary Search Tree to Sorted Doubly Linked List](Solutions/0426.Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List.py) (M) (这种改变成linked list的题真是一头雾水呀)
- [0114. Flatten Binary Tree to Linked List](Solutions/0114.Flatten-Binary-Tree-to-Linked-List.py) (M)
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (M)
- [0285. Inorder Successor in BST](Solutions/0285.Inorder-Successor-in-BST.py) (M)
- [0701. Insert into a Binary Search Tree](Solutions/0701.Insert-into-a-Binary-Search-Tree.py) (M)
- [0450. Delete Node in a BST](Solutions/0450.Delete-Node-in-a-BST.py) (M)




## [Binary Search](/Binary-Search.py)
- [0704. Binary Search](Solutions/0704.Binary-Search.py) (E)
- [0702. Search in a Sorted Array of Unknown Size](Solutions/0702.Search-in-a-Sorted-Array-of-Unknown-Size.py) (M) (Find end point using "double method", same as dynamic array)
- [0069. Sqrt(x)](Solutions/0069.Sqrt(x).py) (E)
- [0034. Find First and Last Position of Element in Sorted Array](Solutions/0034.Find-First-and-Last-Position-of-Element-in-Sorted-Array.py) (M)
- [0035. Search Insert Position](Solutions/0035.Search-Insert-Position.py) (E)
- [0278. First Bad Version](Solutions/0278.First-Bad-Version.py) (E)
- [0153. Find Minimum in Rotated Sorted Array](Solutions/0153.Find-Minimum-in-Rotated-Sorted-Array.py) (M)
- [0154. Find Minimum in Rotated Sorted Array II](Solutions/0154.Find-Minimum-in-Rotated-Sorted-Array-II.py) (H)
- [0039. Recover Rotated Sorted Array](Solutions/0039.Recover-Rotated-Sorted-Array.py) (LintCode) (找到minPos, 然后三步反转法)
- [0033. Search in Rotated Sorted Array](Solutions/0033.Search-in-Rotated-Sorted-Array.py) (M)
- [0852. Peak Index in a Mountain Array](Solutions/0852.Peak-Index-in-a-Mountain-Array.py) (E)
- [0162. Find Peak Element](Solutions/0162.Find-Peak-Element.py) (M)
- [0875. Koko Eating Bananas](Solutions/0875.Koko-Eating-Bananas.py) (M) (Construct a OOOXXX problem to find the first X)
- [0074. Search a 2D Matrix](Solutions/0074.Search-a-2D-Matrix.py) (M) (Think the 2D array as a long 1D array cuz the rows and cols are sorted)
- [0240. Search a 2D Matrix II](Solutions/0240.Search-a-2D-Matrix-II.py) (M) (Start from bottom left, head to top right, each comparism rule out a colomn or a row)



## Dynamic Programming
### [Longest Subsequece Problems](/Longest-Subsequece-Problem.py)
- [0005. Longest Palindromic Substring](Solutions/0005.LongestPalindromicSubstring.py) (Center spread O(N^2); DP(N^2))
- [0516. Longest Palindromic Subsequence](Solutions/0516.LongestPalindromicSubsequence.py) (M)
- [0300. Longest Increasing Subsequence](Solutions/0300.LongestIncreasingSubsequence.py) (M)
- [0673. Number of Longest Increasing Subsequence.py](Solutions/0673.NumberofLongestIncreasingSubsequence.py) (M)
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.LongestArithmeticSequence.py) (M)
- [0873. Length of Longest Fibonacci Subsequence](Solutions/0873.LengthofLongestFibonacciSubsequence.py) (M)  
### [Classic DP Problems](https://juejin.im/post/5d556b7ef265da03aa2568d5)
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M)
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (M)
- [0718. Maximum Length of Repeated Subarray](Solutions/0718.Maximum-Length-of-Repeated-Subarray.py) (M)
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (M)
- [1049. Last Stone Weight II](Solutions/1049.Last-Stone-Weight-II.py) (M)
- [0322. Coin Change](Solutions/0322.Coin-Change.py) (M)
- [0714. Best Time to Buy and Sell Stock with Transaction Fee](Solutions/0714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) (M)
- [1024. Video Stitching](Solutions/1024.Video-Stitching.py) (M)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M)
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (M)
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M)
- [0486. Predict the Winner](Solutions/0486.Predict-the-Winner.py) (M)
- [0983. Minimum Cost For Tickets](Solutions/0983.Minimum-Cost-For-Tickets.py) (M)
- [0688. Knight Probability in Chessboard](Solutions/0688.Knight-Probability-in-Chessboard.py) (M)
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
- [0361. Bomb Enemy](Solutions/0361.Bomb-Enemy.py) (M)
- [0464. Can I Win](Solutions/0464.Can-I-Win.py) (M)
- [0467. Unique Substrings in Wraparound String](Solutions/0467.Unique-Substrings-in-Wraparound-String.py) (M)
- [0898. Bitwise ORs of Subarrays](Solutions/0898.Bitwise-ORs-of-Subarrays.py) (M)
- [0343. Integer Break](Solutions/0343.Integer-Break.py) (M)
- [1223. Dice Roll Simulation](Solutions/1223.Dice-Roll-Simulation.py) (M)
- [1105. Filling Bookcase Shelves](Solutions/1105.Filling-Bookcase-Shelves.py) (M)


## Rabin Karp Algorithm
- [0028. Implement strStr()](Solutions/0028.Implement-strStr().py) (E) (Rabin Karp Algorithm O(M+N), use Hashcode, ord(ch)-ord("a"))

