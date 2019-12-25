碰到二叉树的问题，就想想整棵树在该问题上的结果和左右儿子在该问题上的结果之间的联系是什么!!

递归三要素：eg: 257.Binary Tree Paths
1. 递归的定义（这个递归函数要干一件什么事情）
2. 递归的拆解：对于Binary Tree一般就是处理 根、左、右 三步就可以了，用divide and conquer的思想
3. 递归的出口（结束条件，一般最后写）

实现递归有两种方法：Traverse; Divide and Conquer
Traverse vs Divide Conquer:
  • They are both Recursion Algorithm
  • Result in parameter vs Result in return value
  • Top down vs Bottom up
