碰到二叉树的问题，就想想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么!!

递归三要素：eg: 257.Binary Tree Paths
1. 递归的定义（这个递归函数要干一件什么事情）
2. 递归的拆解：对于Binary Tree一般就是处理 根、左、右 三步就可以了，用divide and conquer的思想
3. 递归的出口（结束条件，一般最后写）

实现递归有两种方法：Traverse; Divide and Conquer
Traverse vs Divide Conquer:
  • They are both Recursion Algorithm
  • Result in parameter(所以往往要用到global variable作为结果那个我们关心的parameter) vs Result in return value
  • Top down vs Bottom up
  
  Divide and conquer/merge用的最多，也更简洁易懂。
  1. divide and conquer is also called bottom up resursion。divide的过程是往下走一步，conquer的过程其实是往上走一步
  2. divide and conquer的返回值就是我们想要的结果
  3. 有时返回值不止一个的，我们需要将result打包起来，如110. Balanced Binary Tree， 1. 递归的定义：返回以root为根的二叉树（是不是balanced, 高度）
  4. 重点是conquer部分，找到拆成左子树之后左右的性质对root这个根节点是什么关系即可！！
  
  最好Traversal 和 divide and conquer的方法都写一遍进行比较理解。
  BST的问题用traverse中序遍历的方法会比较简洁一些，因为BST的中序遍历得到的是一个递增（非递减）的数组。
  
  必“背”程序：
• 非递归版本的 Pre Order (144), In Order (98)！！
merge sort 是最有名的divide and conquer！

几乎所有的二叉树的时间复杂度都是O(N)！！N是节点个数。
空间复杂度是O(h), h是递归的深度，如果是平衡二叉树h=logN, 如果不是平衡二叉树，则最坏情况是h=N。

BST排序或重构的问题一般使用in Order Traverse的方法，将node一次放入arr中自然形成sortedArr
BST中的查找、删除某个节点问题往往可以使用divide and conquer的方法，每次将要查找的val与root比较，如果大于就去右边查找，小于就去左边查找。
One of the huge BST advantages is a search for arbitrary element in O(logN) time in the average case. eg: 701. insert int oa binary tree
