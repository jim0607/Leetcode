DFS: 不撞南墙不回头
BFS: 不需要递归，使用queue
*** 能用BFS解决的问题，一定不要用DFS去做，因为DFS需要递归，递归的深度可能会很深的。
*** 图上的问题一般都是BFS解决。

BFS都是用queue，注意python实现的时候用list （可以用linked list实现，或者用circular list，环形数组实现）

主要分成三个部分的内容：
1. 二叉树上的BFS
2. 图上的BFS 
  * 拓扑排序: topological sorting （非常重要，必考）
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
  q.append(root)
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
            
            
图上的BFS：与二叉树上BFS最大的区别就在于图上的BFS是存在环的，如果不处理的话会一直循环下去，所以比树的BFS多了一个hashmap和一条判断语句
用hashmap存储访问过的节点，然后判断这个节点是否访问过，如果访问过就不再重复访问。
图的实现方法是使用hashmap，key是int表示节点, value是set(int)表示该节点所连接的相邻节点。
图上的BFS是由点及面，从一个点开始找到所有的点。
            
topological sorting 拓扑排序 （针对有向图）
* indegree 入度：表示依赖于几个点
* 拓扑排序是一个一个按顺序你把节点删掉，按什么样的顺序呢？就是保证先删掉的节点不会影响到后删掉的节点。
*** 
所有的topological sort 都是两步：
1. 从数字关系求出每个节点的inDegrees（就是找节点与相邻节点的依赖关系） 
   和 每个节点的neighbors （edges = collections.defaultdict(list)), key是node, val是装有这个node的neighbor的list
2. 然后 BFS
***
Topological sort 必考，其实也非常模板化，一定要记住。



图中的BFS假设有N个点，M条边，M < N^2, 图上的BFS的时间复杂度是O(M)
矩阵有N行M列，N*M个点，N*M*2 条边（每个点上下左右4条边，每条边被2个点共享），因此矩阵中BFS时间复杂度 = O(N * M)

矩阵中的图的问题一般是棋盘问题。
坐标变换数组：deltaX, deltaY
一般需要一个 inBound 函数用于判断下一步是否出界了
一般需要两个for循环去扫描棋盘数组的每个位置，然后选择从某些个位置出发开始BFS，在BFS的时候记录visited=set()，所以bfs函数往往是def bfs(grid, i, j, visited)


















  
