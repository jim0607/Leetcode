Stack/Queue 其实是上层数据结构，我们用的时候叫他stack/queeu，他们通过的是底层的数据结构实现的，地岑的数据结构不外乎几种：
连续的数组list，不连续的数组Linked-list，以及另一种不连续的数据结构tree

Queue: 
push, pop, top 都是O(1)的时间复杂度
q = collections.deque()
q.append()
q.popleft()
BFS的主要数据结构
非递归实现二叉树的level-order的数据结构

Stack:
push, pop, top 都是O(1)的时间复杂度
push: stack.append()
pop: stack.pop()
非递归实现DFS的主要数据结构
非递归实现二叉树的pre,in,post-order的数据结构




heap是通过二叉树实现的。
