1. Stack and Queue

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

Iterator/Generator的问题大部分都是用stack来做。



2. Hash/Dictionary
O(1) Insert / O(1) Find / O(1) Delete
hash function是针对任意一个key，算出其应该去到的地址。
O(1) find的原理是：比如来了一个key，需要查找这个key在不在hash中，这个时候hash map是把key代入到hash fuction中，然后算出这个key对应的地址，然后直接去这个地址去看，如果这个地址里面有key了，就说明key in hash map，如果没有就key not in hash map，所以O(1) find是因为hash function计算只需要O(1)的时间。
一个hash map的例子：MD5，其实就是取模：key % hash_table_size

hashing的冲突解决方法：
1. closed hashing: hash_table_size是固定的，采取取模的方式，如果出现冲突，比如8%7 = 1,将8放到地址1，下一个进来15%7 也是1，这个时候就把15放到紧接着的后面那个地址也就是2
2. opend hashing: 如果出现冲突，也坚决不去紧接着的后面那个地址，而是将15排在8的后面，两个数都占1那个地址。
  
如果hash_table_size不够大怎么办： re-hashing，若果存入的元素的个数大约hash_table_size的十分之一，那就要re-hashing了，不然冲突会很多。
146. LRU!!!



heap是通过二叉树实现的。



