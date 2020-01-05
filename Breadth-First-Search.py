DFS: 不撞南墙不回头
BFS: 不需要递归，使用queue

BFS都是用queue，注意python实现的时候用list （可以用linked list实现，或者用circular list，环形数组实现）

主要分成三个部分的内容：
1. 二叉树上的BFS
2. 图上的BFS 
  * 拓扑排序: topological sorting
3. 棋盘上的BFS

什么时候该使用BFS:
1. 图的遍历Traversal in Graph （注意树是一种特殊形态的图）
  * level order traversal (层级遍历)
  * connected component (由点及面)
  * topological sorting (拓扑排序)
2. 最短路径(shortest path in simple graph)
  * 仅限简单图求最短路径（Dj...算法）
  * 即，图中每条边边长度都是一样的，且没有方向，即无向图
  
二叉树上的BFS：
  * Binary Tree Level order traversal (层级遍历)
  BFS解二叉树问题的模板：
  q = deque(）
  q.append([root])
  result = []
  while q:
    node = q.popleft()
    if node.left:
      q.append(node.left)
     if node.right:
      q.append(node.right)
    result.append(....)
  return result
  
  * Binary Tree Serialization (M+Y)
  序列化：将“内存”中结构化的数据变成“字符串”的过程
  序列化：object to string
  反序列化：string to object
  什么时候需要序列化：
  1. 将内存中的数据持久化存储：内存中重要的数据不能只呆在在内存里，这样断电就没有了，需要用一种方式写入硬盘，在需要的时候，能否再从硬盘中读出来在内存中重新创建
  2. 网络传输时：机器与机器之间交换数据的时候，不可能互相去读对方的内存，只能将数据变成字符流数据（即字符串）后通过网络传输过去，接收的一方再讲字符串解析后放在自己内存里。
  常用的一些序列化手段：
  * XML
  * JSON （就是一个hashmap）
  * Thrift (by Facebook)
  * ProtoBuf(by Google)
  
  
  
