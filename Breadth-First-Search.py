BFS的使用场景：
1. 简单图的最短路径问题（如骑士问题，word ladder问题）
2. 需要层序遍历

DFS: 不撞南墙不回头
BFS: 不需要递归，使用queue
*** 能用BFS解决的问题，一定不要用DFS去做，因为DFS需要递归，递归的深度可能会很深的。
*** 图上的问题一般都是BFS解决。

BFS都是用queue，注意python实现的时候用list （可以用linked list实现，或者用circular list，环形数组实现）

****！！！！
bfs只需谨记一条铁律，那就是在while q: 里面只做两件事：
1. 处理这一层。那就需要把这一层的node逐个pop出，然后append到res里，有时候需要用for循环for _ in range(len(q))来遍历这一层所有的node
2. append下一层。那就需要遍历下一层所有的node，有时候需要用for循环for neighbor in neighbors[currNode]。
   这里的neighbors是一个存储边的对应关系的hashmap，有的题目需要提前找出来。
   另外为了处理带环的图，有时需要在append下一层的某个节点时候判断是不是已经visited，这就需要提前定义好一个set来存储已经visited的节点，visited.add和q.append永远是一对孪生兄弟。
****！！！！

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
  * 对于最短路径问题，有时候题目是隐式的BFS，比如word ladder，给你的是一个字符串，然后可通过一些变换，得到另外一些字符串，
    我们可以认为一个字符串就是一个节点，通过这个节点可以连接到另外的一些节点。
  
二叉树上的BFS：
  * Binary Tree Level order traversal (层级遍历)
  BFS解二叉树问题的模板：
res = []
q = deque()
q.append(root)
while q:
    level = []
    lens = len(q)  # important
    # 用一个for循环来处理每一层
    for _ in range(lens):
        # 在这一层要做两件事情：1. 将该层的所有的node.val依次放入level中
        node = q.popleft()
        level.append(node.val)
        # 2. 将该层所有的node的左右子节点依次入队列
        if node.left:  # 注意这里判断是为了不把None放到队列里去，这样res出来的结果就没有None了。
            q.append(node.left)
        if node.right:
            q.append(node.right)
    res.append(level)
return res
  
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
有向图的问题，用topological sorting, 可以检测有向图是否有环！
如果是无向图，那就用Union Find!
拓扑排序其实就是一步一步剥皮的过程！！
* indegree 入度：表示依赖于几个点
* 拓扑排序是一个一个按顺序你把节点删掉，按什么样的顺序呢？就是保证先删掉的节点不会影响到后删掉的节点。
*** 
所有的topological sort 都是两步：
1. 从数字关系求出每个节点的inDegrees（就是找节点与相邻节点的依赖关系） (inDegrees = collections.defaultdict())，key是node, val是这个node的indegree
   和 每个节点的neighbors （edges = collections.defaultdict(list)), key是node, val是装有这个node的neighbor的list
2. 然后 BFS，背诵模板就可以了。
***
Topological sort 必考，其实也非常模板化，一定要记住。
模板如下：
        # 1. 用一个hashmap来存储每个节点的相邻节点
        edges = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
     
        # 2. 用一个hashmap来存储每个节点的indgree的值
        inDegree = {}
        inDegree = self.get_inDegree(numCourses, prerequisites)

        # BFS 模板
        q = collections.deque()
        # 初始化q，先把q里面装入那些indegree=0的node
        for n, cnt in inDegree.items():
            if cnt == 0:
                q.append(n)
        cntCourses = 0
        while q:
            currNode = q.popleft()
            cntCourses += 1
            for neighbor in edges[currNode]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:     # 只把入度为0的node放到q里面，这样如果有环的话就不会进q了，所以最后判断如果cntCourses < numCourses, 那就说明有环。
                    q.append(neighbor)

        return cntCourses == numCourses


如果DFS+topological sorting的话，必须保证图没有环。
   
   

图中的BFS假设有N个点，M条边，M < N^2, 图上的BFS的时间复杂度是O(M)
矩阵有N行M列，N*M个点，N*M*2 条边（每个点上下左右4条边，每条边被2个点共享），因此矩阵中BFS时间复杂度 = O(N * M)

矩阵中的图的问题一般是棋盘问题。
坐标变换数组：deltaX, deltaY
一般需要一个 inBound 函数用于判断下一步是否出界了
一般需要两个for循环去扫描棋盘数组的每个位置，然后选择从某些个位置出发开始BFS，在BFS的时候记录visited=set()，所以bfs函数往往是def bfs(grid, i, j, visited)
棋盘上带层序遍历的BFS的模板为(必须背诵)(eg: 骑士在棋盘上的最短路径问题，word ladder问题)：
    visited = set()
    # bsf 层序遍历，输出层数
    def bfs(self, x, y, visited):
        steps = 0
        q = collections.deque()
        q.append((x, y))
        visited.add((x, y))     # 一对孪生兄弟
        while q:
            lens = len(q)   # 层序遍历必备句式1
            steps += 1      # 层序遍历必备句式2
            for _ in range(lens):   # 层序遍历必备句式之最重要
                (curr_x, curr_y) = q.popleft()    # 层序遍历必备句式4
                for delta_x, delta_y in self.MOVES:   # 层序遍历必备句式3
                    new_x = curr_x + delta_x          # 层序遍历必备句式5
                    new_y = curr_y + delta_y          # 层序遍历必备句式6
                    if self.inBound(new_x, new_y) and (new_x, new_y) not in visited:
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))     # 孪生兄弟
                        
这个题目从两端bfs的解法非常重要！！
                        
                      
棋盘上不需要层序遍历的BFS的模板为(必须背诵) (eg: 200. Number of Islands)：
与上面的模板相比就是少了一句lens = len(q) 和一个for循环 for _ in range(lens):
    visited = set()
    def bfs(self, grid, x, y, visited):
        q = collections.deque()
        q.append((x, y))
        visited.add((x, y))  # visited最好与append同事出现，像一对孪生兄弟
        while q:
            (x, y) = q.popleft()
            # 这一步相当于之前图里面的for neighbor in neighbors
            for delta_x, delta_y in self.MOVES:
                next_x = x + delta_x
                next_y = y + delta_y
                if self.isBound(next_x, next_y, grid) and grid[next_x][next_y] == "1" and (next_x, next_y) not in visited:
                    q.append((next_x, next_y))
                    visited.add((next_x, next_y))  # visited最好与append同事出现，像一对孪生兄弟











  
