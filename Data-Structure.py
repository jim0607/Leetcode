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


2. Deque ⁄dek⁄ double-ended queue is a combination of stack and queue
deque mehtods: all O(1)
append: append from right end of the deque
appendleft: append from left end of the deque
pop: pop from the right end
popleft: pop from the left end
当做普通queue来用: append + popleft
当做普通stack来用: append + pop





3. Hash/Dictionary
常见面试问题：what is hash map?
Hash table or a Hashmap is a type of data structure that maps keys to its value pairs
how to implement a hash map?
using a hash function, for examples, we want to put an int 8 in hash map. First step is take mode 8%7 = 1, then choose to store 8 at address 1.
when trying to find if an int say 8 is in the hashmap, first step is take mode 8%7 = 1, then compare the integer stored in adrress 1 to see if it is 8.  By using a funciton, we can realize O(1) find operation.
O(1) Insert / O(1) Find / O(1) Delete
hash function是针对任意一个key，算出其应该去到的地址。
O(1) find的原理是：比如来了一个key，需要查找这个key在不在hash中，这个时候hash map是把key代入到hash fuction中，然后算出这个key对应的地址，然后直接去这个地址去看，如果这个地址里面有key了，就说明key in hash map，如果没有就key not in hash map，所以O(1) find是因为hash function计算只需要O(1)的时间。
一个hash map的例子：MD5，其实就是取模：key % hash_table_size

hashing的冲突解决方法：
1. Seperate chaining: hash_table_size是固定的，采取取模的方式，如果出现冲突，比如8%7 = 1,将8放到地址1，下一个进来15%7 也是1，这个时候就把15放到紧接着的后面那个地址也就是2
2. Opend addressing / Linear probing: 如果出现冲突，也坚决不去紧接着的后面那个地址，而是将15排在8的后面，两个数都占1那个地址。
  
如果hash_table_size不够大怎么办： re-hashing，若果存入的元素的个数大约hash_table_size的十分之一，那就要re-hashing了，不然冲突会很多。
In practicle: shrink the size when less than 1/8 were full, double the size when 1/2 were full
****146. LRU!!!




4. heap and heapq
https://docs.python.org/2/library/heapq.html
  
heap是通过二叉树实现的，该二叉树的特性：
1. 结构特性：优先从上至下排列，同一层优先从左至右排列。
2. 数值特性：min heap：父节点总是小于等于儿子的。max heap: father >= child
支持操作：O(log N) Add / O(log N) Remove or pop / O(1) Min or Max
Max Heap vs Min Heap

Priority Queue or heap queue 使用heap实现的。
一般都是使用heap queue而不是heap来解决实际题目，解决哪些实际题目呢？
一般是查找最大值最小值的题目，因为可以在O(1)时间内找到最大值最小值，但是heap queue的delete任意一个值是O(N)

或者可以使用Tree map来解决问题，Tree map使用BBST （balanced binary search tree）实现的，所有操作全是O(logN)。

****heapq非常重要****
heapq模块是python的一个标准库，在heapq中，使用的是最小堆。正因为堆的这种特殊结构，使得通过heapq模块，可以快速获取一个列表的前N个最大(小)值，即Top N。
python维护了一个堆，使用的存储结构是列表，通过heapq模块来管理、操作这个堆。heapq提供了插入、删除元素的方法，并且保证在插入或删除元素时，所有节点自动调整，保证堆的结构，同时尽量高效，复杂度为O(logN)，在大数据时，效率高于直接暴力sort排序。

********heapq适合做第K大，第K小，前K大，前K小问题，总之就是需要多次取最大或最小数的问题。原因是这类问题往往需要多次pop出最小值，而heap的pop操作是O(1)

********如果题目需要不断更新最大值/最小值，就要想能不能用heap

******heapq的用法：*******

import heapq

list = [1,5,3,2,8,5]
# heapify实际上是从后向前 从第一个非叶子结点开始做percolateup/percolatedown
heapq.heapify(list)           # heapq.heapify(list) 往往用于创建堆, 将list 转换成堆，原地，线性时间O(N)。
or define a hq = [], and push in one by one
heapq[0]                      # O(1) 只访问最小的元素而不弹出它。
heapq.heappush(hq, item)    # O(logN) 将 item 的值加入 heap 中。
heapq.heappop(hq)           # O(logN) 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。


Python中的 heapq 是一个 list [], 所以删除一个元素只能当做list来删除 hq.remove(item), 时间复杂度是O(N)
如果想要实现O(logN)的删除时间复杂度需要用 dictionary/set 来实现heapq, 这时候的数据结构叫做Ordereddict
