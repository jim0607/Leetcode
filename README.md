## 二刷：先把做过的做一遍，再把每个tag的高频前8题都做掉！

# [Binary Search](/Binary-Search.py)
- [0704. Binary Search](Solutions/0704.Binary-Search.py) (!!E) <br>
九章模板: 1. while start + 1 < end; 2. mid = start + (end - start) // 2; 3. 循环内只写两个分支； 4. 往左逼find the first X; 5. 往右逼find the last X
- [0702. Search in a Sorted Array of Unknown Size](Solutions/0702.Search-in-a-Sorted-Array-of-Unknown-Size.py) (M) <br>
Find end point using "double method", same as dynamic array
- [0069. Sqrt(x)](Solutions/0069.Sqrt(x).py) (E) <br>
两种方法：1. Binary Search; 2. Newton's Method. x<sub>k+1</sub> = (x<sub>k</sub> + x/x<sub>k</sub>) / 2; O(logN) since the set converges quadratically
- [0034. Find First and Last Position of Element in Sorted Array](Solutions/0034.Find-First-and-Last-Position-of-Element-in-Sorted-Array.py) (!!M) <br>
想找first position of target，要保证两点：1. while循环里的判断要往左逼，也就是if nums[mid] **>=** target: end = mid； 2. 就把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉，因为start肯定是小于end的。
- [0035. Search Insert Position](Solutions/0035.Search-Insert-Position.py) (E) <br>
This is to implement bisect.bisect_left(nums, target), which returns the position of inserting target in order to keep nums sorted
- [0278. First Bad Version](Solutions/0278.First-Bad-Version.py) (E)
- [0153. Find Minimum in Rotated Sorted Array](Solutions/0153.Find-Minimum-in-Rotated-Sorted-Array.py) (!!M) <br>
解法一：nums[mid]可以与nums[0]比较；解法二：也可以与nums[-1]比较；解法三：也可以与nums[end]比较
- [0154. Find Minimum in Rotated Sorted Array II](Solutions/0154.Find-Minimum-in-Rotated-Sorted-Array-II.py) (H) <br>
与153类似，只是array里可能有duplicates，采用153的解法三，唯一不同的是：nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半，因为eg: nums=[2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2........], 由于不知道mid是1前面的2还是1后面的2，所以无法确定是drop前面还是drop后面，只能保险地把end往前挪一位，所以154这题in extreme case, 时间复杂度是O(N)
- [0039. Recover Rotated Sorted Array](Solutions/0039.Recover-Rotated-Sorted-Array.py) (M LintCode) <br>
154 相同方法binary search找到minPos, 然后三步反转法recover
- [0033. Search in Rotated Sorted Array](Solutions/0033.Search-in-Rotated-Sorted-Array.py) (M) 画个图分几个区间讨论就可以了！
- [0852. Peak Index in a Mountain Array](Solutions/0852.Peak-Index-in-a-Mountain-Array.py) (E)<br>
- [0162. Find Peak Element](Solutions/0162.Find-Peak-Element.py) (M) <br>
OOXX问题，找到第一个出现的X，X是the first position of 递减的序列
- [0875. Koko Eating Bananas](Solutions/0875.Koko-Eating-Bananas.py) (M) <br>
If Koko can finish eating all the bananas (within H hours) with an eating speed of K, she can finish with a larger speed too. So it is a OOOXXX problem trying to find the first X. end is set to be max(piles). Every time find if it posible to eat all the bananas with speed mid. if yes, then drop the right part, if no, then drop the left."""
- [0074. Search a 2D Matrix](Solutions/0074.Search-a-2D-Matrix.py) (M) <br>
Think it as a long 1D array with MxN element, then we can use binary search; row = mid // n, col = mid % n; O(log(MN)), O(1)
- [0240. Search a 2D Matrix II](Solutions/0240.Search-a-2D-Matrix-II.py) (M) <br>
start from left bottom, head up to right top, each comparism rule out a row (i-1=1) or rule out a col (j+=1)
- [0050. Pow(x, n)](Solutions/0050.Pow(x,n).py) (M) <br>
if mod == 0: res *= x^div; else: res *= x^div * x
- [0029. Divide Two Integers](Solutions/0029.Divide-Two-Integers.py) (M) <br>
eg: 10//3, 每次通过右移3 << 1的方法将3乘以2,这种算法是O(N), 每次都右移几次3 << x, 相当于3x2x2x2...,直到3x2x2x2...>10, 然后取余数继续这个算法
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) <br>
target是随着i的移动而变化的binary search



# [Binary Tree, Divide and Conquer](/Binary-Tree-Divide-and-Conquer.py) <br>
- [0144. Binary Tree Preorder Traversal](Solutions/0144.Binary-Tree-Preorder-Traversal.py) (M) memorize the iterative version using stack
- [0094. Binary Tree Inorder Traversal](Solutions/0094.Binary-Tree-Inorder-Traversal.py) (M) memorize the iterative version using stack
- [0104. Maximum Depth of Binary Tree](Solutions/0104.Maximum-Depth-of-Binary-Tree.py) (!!E) Divide and Conquer vs Traverse
- [0257. Binary Tree Paths](Solutions/0257.Binary-Tree-Paths.py) (!!E) <br>
- [0112. Path Sum](Solutions/0112.Path-Sum.py) (E) <br>
- [0113. Path Sum II](Solutions/0113.Path-Sum-II.py) (!!M) 碰到打印所有路径的问题，第一反应就是带backtracking the dfs
- [0437. Path Sum III](Solutions/0437.Path-Sum-III.py) (E) 递归需要恶补呀！
- [0596. Minimum Subtree](Solutions/0596.Minimum-Subtree.py) (LintCode) <br>
Divide and Conquer的方法输出以root为根的subTree的subSum，然后每次与minSum打擂台进行比较，注意python中定义全局变量可以用self.minSum = float("inf"), self.minNode = None，在主函数中定义这两个变量就可以了
- [0597. Subtree with Maximum Average](Solutions/0597.Subtree-with-Maximum-Average.py) (LintCode) 同上 Divide and Conquer
- [0124. Binary Tree Maximum Path Sum](Solutions/0124.Binary-Tree-Maximum-Path-Sum.py) (H) <br>
题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter. 方法是定义一个self.maxSum在helper函数中去打擂台。
- [0110. Balanced Binary Tree](Solutions/0110.Balanced-Binary-Tree.py) (E) <br>
定义一个全局变量self.is_balanced; 养成好习惯，把叶子节点单独做判断if not root.left and not root.right: return 1; if abs(leftDepth - rightDepth) > 1: self.is_balanced = False
- [0235. Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py) (E) <br>
- [0236. Lowest Common Ancestor of a Binary Tree](Solutions/0236.Lowest-Common-Ancestor-of-a-Binary-Tree.py) (M) <br>
- [0700. Search in a Binary Search Tree](Solutions/0700.Search-in-a-Binary-Search-Tree.py) (E) <br>
- [0938. Range Sum of BST](Solutions/0938.Range-Sum-of-BST.py) (E) <br>
- [0226. Invert Binary Tree](Solutions/0226.Invert-Binary-Tree.py) (E) <br>
STEP 1. divide 先局部有序; STEP 2. conquer 再整体有序
- [0617. Merge Two Binary Trees](Solutions/0617.Merge-Two-Binary-Trees.py) (E) <br>
- [0124. Binary Tree Maximum Path Sum](Solutions/0124.Binary-Tree-Maximum-Path-Sum.py)（H） 
题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter
- [0108. Convert Sorted Array to Binary Search Tree](Solutions/0108.Convert-Sorted-Array-to-Binary-Search-Tree.py) (!!E) <br>
we can always choose the left middle number as root, or always choose right middle number as root, or sometimes left sometimes right as root. That is why the answer is not unique
- [0098. Validate Binary Search Tree](Solutions/0098.Validate-Binary-Search-Tree.py) (M) <br>
注意判断条件不是leftValid and rightValid and left.val<root.val<right.val而是max of left < root < min of right; helper函数返回以root为根的树(是不是BST，max and min value in the tree); if isLeftBST and isRightBST and maxLeft < root.val < minRight: return True, max(maxLeft, maxRight, root.val), min(minLeft, minRight, root.val) 
- [0426. Convert Binary Search Tree to Sorted Doubly Linked List](Solutions/0426.Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List.py) (M)  <br>
solution 1: 定义两个全局变量self.head, self.curr，进行in order traversal的过程中不断更新curr的位置并hook up nodes
- [0114. Flatten Binary Tree to Linked List](Solutions/0114.Flatten-Binary-Tree-to-Linked-List.py) (M) <br>
helper函数每次都输出最后的一个node
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (M) <br>
use a stack with controlled recursion, some part of the algorithm is similar with the in order traversal of a tree using a stack; this algorithm has space complexity of O(h)
- [0285. Inorder Successor in BST](Solutions/0285.Inorder-Successor-in-BST.py) (M) <br>
Divide and conquer: if p.val < root.val: return left if left else root; else: return right
- [0701. Insert into a Binary Search Tree](Solutions/0701.Insert-into-a-Binary-Search-Tree.py) (M) <br>
if val > root.val则更新root.right: root.right = self.insertIntoBST(root.right, val); else: root.left = self.insertIntoBST(root.left, val); return root
- [0450. Delete Node in a BST](Solutions/0450.Delete-Node-in-a-BST.py) (M) <br>
- [1214. Two Sum BSTs](Solutions/1214.Two-Sum-BSTs.py) (M) <br>
binary tree traversal using iterative way and store the val in a hash map; time complexity: O(M + N)
- [1038. Binary Search Tree to Greater Sum Tree](Solutions/1038.Binary-Search-Tree-to-Greater-Sum-Tree.py) (M) <br>
do a in order traversal (reversed version) to keep track the sums
- [0096. Unique Binary Search Trees](Solutions/0096.Unique-Binary-Search-Trees.py) (M) Catalan Number


# [Breadth First Search](/Breadth-First-Search.py)
### [BFS in Trees](/Breadth-First-Search.py)
- [0102. Binary Tree Level Order Traversal](Solutions/0102.Binary-Tree-Level-Order-Traversal.py) (!!M, youtubed) <br>
BFS的铁律就是用queue, 在while q: 循环里做两件事 1. 处理这一层。那就需要把这一层的node逐个pop出，然后append到res里，有时候需要用for循环for _ in range(len(q))来遍历这一层所有的node; 2. append下一层进q。BFS is O(N) since each node is processed exactly once
- [0103. Binary Tree Zigzag Level Order Traversal](Solutions/0103.Binary-Tree-Zigzag-Level-Order-Traversal.py) (M) <br>
same as 102, 在res.append(level)的时候间隔性选择res.append(level) or res.append(level[::-1])
- [0107. Binary Tree Level Order Traversal II](Solutions/0107.Binary-Tree-Level-Order-Traversal-II.py) (E) <br>
same as 102，只是题目要求从下至上输出，只需要return res[::-1]即可
- [0199. Binary Tree Right Side View](Solutions/0199.Binary-Tree-Right-Side-View.py) (M) <br>
same as 102，只需要res.append(level[-1])即可
- [0111. Minimum Depth of Binary Tree](Solutions/0111.Minimum-Depth-of-Binary-Tree.py) (E) <br>
solution 1: recursion; soluiton 2: BFS; for _ in range(lens): if not node.left and not node.right: return depth
- [0297. Serialize and Deserialize Binary Tree](Solutions/0297.Serialize-and-Deserialize-Binary-Tree.py) (!!H) <br>
should practice more times!

### [BFS in Graphs](/Breadth-First-Search.py)
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (!!M) <br>
判断图是不是一棵树（不一定非要是二叉树）需要满足两点:1. 首先点的数目一定比边的数目多一个; 2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目, 如果小于则说明有的节点被访问不到，如果大于说明有环，则不是树
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (M) <br>
第一步：找到所有的点，用BFS实现; 第二步：复制所有的node，存到mapping中，边可以先设为空; 第三步：复制所有节点对应的边/邻居
- [0127. Topological Sorting](Solutions/0127.Topological-Sorting.py) (!!LintCode) <br>
必考，其实也非常模板化，一定要记住。Three steps: 1. 从数字关系求出每个节点的inDegrees（就是找节点与相邻节点的依赖关系） (inDegrees = collections.defaultdict())，key是node, val是这个node的indegree; 2. 和每个节点的neighbors （neighbors = collections.defaultdict(list)), key是node, val是装有这个node的neighbor的list; 3. 然后 BFS，背诵模板就可以了。
- [0207. Course Schedule](Solutions/0207.Course-Schedule.py) (!!M) <br>
套用模板分三步：1. collect the inDegree of each node; 2. collect the neighbors information; 3. topological sort - BFS
- [0210. Course Schedule II](Solutions/0210.Course-Schedule-II.py) (!!M) <br>
套用模板 return res if len(res) == numCourses else []
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (!!M) <br>
这个题目要做三个判断：1. 判断seqs的拓扑排序是否存在，只需判断len(res) 是否等于len(neighbors) or len(inDegrees), 如果小于说明有孤立节点，如果大于说明有环，两者都不存在拓扑排序; 2. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素, 即每一层只有一个选择: if len(q)>1: return False; 3. 最后判断这个唯一的拓扑排序res是否等于org
- [0269. Alien Dictionary](Solutions/0269.Alien-Dictionary.py) (!!H) <br>
只需要比较word[i]与word[i+1]即可得到inDegree的关系以及neighbors的关系

### [BFS in Matrix](/Breadth-First-Search.py) (隐式图搜索问题!!!)
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (!!M, youtubed) <br>
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
- [0994. Rotting Oranges](Solutions/0994.Rotting-Oranges.py) (M) <br>
在class solution(): 后面定义全局变量 EMPTY = 0; FRESH = 1; MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
- [286. Walls and Gates](Solutions/0286.Walls-and-Gates.py) (M) <br>
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (!!M) <br>
solution 1: 利用对称性质: x,y=abs(x),abs(y); q.append(neighbor) only if (neighbor_x>=-2 and neighbor_y>=-2); 1816 ms<br>
solution 2!!!: 从source和destination两端同时进行bfs!!!! if visited_src & visited_des: return cnt_src + cnt_des; 452 ms<br>
solution 3: dp: cache[(x, y)] = min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1; 60 ms<br>
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (!!M) <br>
定义一个wordSet = set(wordList)来降低时间寻找下一个neighborWord的复杂度到O(26L); 利用双端BFS大大提高速度，在双端BFS的过程中判断if not q_src or not q_des: 则说明q_src或q_des里面的所有possible neighbor都不在wordList里面，也就是没有必要继续进行了
- [1162. As Far from Land as Possible](Solutions/1162.As-Far-from-Land-as-Possible.py) (M) <br>
bfs: the maximum distance is steps needed to change all "0" to be "1"; solution 2: DP same as 542. 01 matrix
- [0317. Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (!!H) <br>
Use reachable_cnt[i][j] to record how many times a 0 grid has been reached and use distSum[][] to record the sum of distance from all 1 grids to this 0 grid. Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS. Prune: if not all 1s can be reached, return -1, during the BFS we use reachableBuildings to count how many 1s we reached. If reachableBuldings != totalBuildings - 1 then we know not all 1s are connected are we can return -1 immediately, which greatly improved speed.



# [Depth First Search](/Depth-First-Search.py)
### [Combination](/Depth-First-Search.py)
- [0078. Subsets](Solutions/0078.Subsets.py) (!!M) <br>
C(m, n)：m个里面找出n个的组合问题; 模板的DFS + back tracking求combination问题 O(NS), S是solution的个数，这里S=2^N; 注意两点：1.res.append(curr.copy()); has to be a deep copy; 2. self.dfs(nums, i + 1, curr, res) 要从i+1开始cuz不能回头找会重复
- [0090. Subsets II](Solutions/0090.Subsets-II.py) (!!M)<br>
如果输入存在重复元素，[1, 2, 2]的遍历中，我们只取前面的那个2，对于后面的那个2，如果不是挨着前面那个2选的，也就是说i != startIndex，那么就不要放后面那个2，这样会造成重复出现[1,第一个2],[1,第二个2], 注意可以挨着第一个2来选第二个2是可以的，因为允许出现[1,2,2]作为答案。if i != 0 and nums[i] == nums[i-1] and i != startIndex: continue
- [0039. Combination Sum](Solutions/0039.Combination-Sum.py) (M) <br>
start是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
- [0040. Combination Sum II](Solutions/0040.Combination-Sum-II.py) (M) <br>
输入中存在重复元素，避免重复输出的方法与Subsets II一样
- [0518. Coin Change 2](Solutions/0518.Coin-Change-2.py) (M) <br>
与Combination Sum一模一样，只是题目不要求输出所有可能组合，只要求输出可能组合的数目，所以可以用DP解。不理解DP解的for循环顺序。
- [0216. Combination Sum III](Solutions/0216.Combination-Sum-III.py) (M)<br>
self.dfs(nums, k - 1, n - nums[i], i + 1, curr, res)   # 不能出现重复数字，所以从i+1开始
- [0090. k Sum II](Solutions/0090.k-Sum-II.py) (M Lintcode)<br>
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (M)<br>
self.dfs(nums, target - nums[i], 0, curr, res)  # 顺序不重要（(1, 3)和(3, 1)都可以，所以让i从0开始
- [0131. Palindrome Partitioning](Solutions/0131.Palindrome-Partitioning.py) (!!M) <br>
递归的定义：从s中的start位置开始，挑一些位置切割，判断从start到i的部分是否为回文，如果是就放入curr中，如果i到了string末尾了则说明此事curr是一种组合方式，放入res中

### [Permutation](/Depth-First-Search.py)
- [0046. Permutations](Solutions/0046.Permutations.py) (!!M)<br>
与combination相比少了一个startIndex参数，加入visited用于防止重复出现; append之后需要将visited[i]变为True; pop出来之后将visited[i]再变回False
- [0047. Permutations II](Solutions/0047.Permutations-II.py) (M) <br>
输入里面有重复，都需要先把数组排序一下; 去重方法与Subsets是类似的: if visited[i] or (i != 0 and nums[i] == nums[i-1] and not visited[i-1]): continue
- [0267. Palindrome Permutation II](Solutions/0267.Palindrome-Permutation-II.py) (M)  <br>
- [0052. NQueens II](Solutions/0052.N-Queens-II.py) (!!H) <br>
排列问题：先打印出数组[0, 1, 2, 3....n]中所有的可能排列：[[0,1,2,3], [1,3,0,2].....]，其中的每一个子数组表示一种可能的方法，子数组中的数字表示在哪个数字的地方放一个Queen，数字对应的下标位置是放那个Queen的行，数字的值是放那个Queen的列。由于Queen可以很冲直撞，所以列是不能相同的，所以需要去重，用visited标记就可以。又由于Queen还可以斜着走，所以横纵坐标的和与差不能相同，也需要用visited标记。用三个字典visited_col, visited_sum, visited_diff分别存储列号，横纵坐标之和，横纵坐标之差有没有被用过
- [0051. N-Queens](Solutions/0051.N-Queens.py) (H)<br>


### [图上的搜索](/Depth-First-Search.py) <br>
- [0126. Word Ladder II](Solutions/0126.Word-Ladder-II.py) (!!H) 打印/输出所有满足条件的路径必用DFS
Step 1. 从end到start做BFS，记录每一个节点到end节点的距离，存入hashmap中 eg: distance["dog"] = 2 <br>
Step 2. 从start到end做DFS，每走一步都必须确保end的distance越来越近。最后将路径都存入到res里



# [Linked List](/Linked-List)
- [0021. Merge Two Sorted Lists](Solutions/0021.Merge-Two-Sorted-Lists.py) (E) <br>
如果需要return一个新的headNode，一般定义一个dummyNode = ListNode(0), curr = dummyNode; 最后return dymmyNode.next
- [0148. Sort List](Solutions/0148.Sort-List.py) (!!M) <br>
step1: divide: 先找到mid, 然后在mid处cut成左右half, 再分别sort left and right; step 2: merge, 同21
- [0206. Reverse Linked List](Solutions/0206.Reverse-Linked-List.py) (!!E) 需要熟背理解
- [0092. Reverse Linked List II](Solutions/0092.Reverse-Linked-List-II.py) (M) <br>
reverse node from m to n: step 1: find node_m and node_m_minus; find node_n and node_n_plus; step 2. reverse the nodes from m to n; 3. hook up node_m_minus with node_n, node_m with node_n_plus
- [0024. Swap Nodes in Pairs](Solutions/0024.Swap-Nodes-in-Pairs.py) (M) <br>
想要reverse n1->n2->n3->n4->n5->n6 in pairs: step 1: 在n1前面添加一个dummy n0, 然后在while curr循环里每次都调用reverse函数，reverse函数做的事情是操作四个节点n0->n1->n2->n3, 将其变成n0->n2->n1->n3, 然后return n1，注意每次都是return想要swap的两个节点的前一个节点！step 2: curr = return的n1，然后继续循环
- [0025. Reverse Nodes in k-Group](Solutions/0025.Reverse-Nodes-in-k-Group.py) (!!H) <br>
similar with 24, 在reverse函数中要做的事情是reverse n0->n1->n2------>nk->n_k+1 to be n0->nk------>n2->n1->n_k+1 and return n1; 也是分两步: 首先翻转n1->n2------>nk, 然后hook up n0 with n_k, n1 with n_k+1
- [0138. Copy List with Random Pointer](Solutions/0138.Copy-List-with-Random-Pointer.py) (!!M) <br>
step 1: create new node and interleave new node into original node; step 2: link the random pointer for the new nodes; step 3: seperate the interleaved old nodes and new nodes
- [0141. Linked List Cycle](Solutions/0141.Linked-List-Cycle.py) (E) <br>
在做环形list的题目时, while slow != fast是很常用的句型
- [0142. Linked List Cycle II](Solutions/0142.Linked-List-Cycle-II.py) (!!M) <br>
step 1: 快慢指针找到相遇的点; step 2: 重新定义两根指针p1, p2分别从head和上面相遇的点出发，然后p1,p2相遇的地方就是环的入口
- [0287. Find the Duplicate Number](Solutions/0287.Find-the-Duplicate-Number.py) (M) <br>
把这个数组的每一个数num看成这样一个linked list node: num的下标代表.val, num的值代表.next指向下一个node。那么如果存在重复的num，那就表示有两个不同node都指向了同一个公共，也就是成环的地点。这么想这个题目就和142一样了，具体实现过程中对p取一个nums[p]，就相当于取一个p.next
- [0160. Intersection of Two Linked Lists](Solutions/0160.Intersection-of-Two-Linked-Lists.py) (E) <br>
两个指针currA, currB; if not currA: currA = headB; if not currB: currB = headA
- [0002. Add Two Numbers](Solutions/0002.Add-Two-Numbers.py) (!!M) <br>
本题的考点是关于如何新建一个linked list, 要用someNode.next = ListNode(someVal), 而不是简单的修改value; 还考察了是否细心, 最后很容易漏掉carryBit != 0的判断"
<br> 23. Merge k Sorted Lists: heapq to find the minimum of the k lists. O(NlogK) https://www.youtube.com/watch?v=Uz4fTr34270 <br>


# [SubArray](/SubArray.py)
- [0053. Maximum Subarray](Solutions/0053.Maximum-Subarray.py) (!!E) <br>
Maintian a prefixSum and minPrefixSum, so that maxSubSum = max(maxSubSum, prefixSum - minPrefixSum)
- [0724. Find Pivot Index](Solutions/0724.Find-Pivot-Index.py) (E) <br>
leftSum = prefixSum[i] # prefixSum[i]是不包括nums[i]的; ightSum = prefixSum[-1] - prefixSum[i] - nums[i] 
- [0560. Subarray Sum Equals K](Solutions/0560.Subarray-Sum-Equals-K.py) (!!M) <br>
新建一个prefixSumDict = {0: 1}, key是prefixSum, val是how many times the prefixSum appears; if prefixSum - k in prefixSumDict: 等价于if prefixSum[j+1]-prefixSum[i] == k
- [0523. Continuous Subarray Sum](Solutions/0523.Continuous-Subarray-Sum.py) (M) <br>
prefixSumMap = {0: -1} # key: prefixSum[j], val: j/position, initial position should be -1; prefixSum += num; prefixSum = prefixSum % k 因为题目要求要能被subArray Sum 要能被k整除
- [0974. Subarray Sums Divisible by K](Solutions/0974.Subarray-Sums-Divisible-by-K.py) (M) <br>
prefixSumDict = {0: 1} # key is the prefixSum, val is how many times the prefixSum appears; prefixSum += num; prefixSum %= K
- [0139. Subarray Sum Closest](Solutions/0139.Subarray-Sum-Closest.py) (Lintcode) <br>
题目要求NlogN, 那就是疯狂暗示要sort, prefixSumList = [(0, -1)] # (0, 1) are prefixSum and index; 对prefixSum来进行sort，这样最小的subArrSum (或者prefixSums[j+1][0] - prefixSums[i][0])就一定来自于相邻的两个prefisxSums了


# [Sort](/Sort.py) 
- [0912. Sort an Array](Solutions/0912.Sort-an-Array.py) (!!M Youtubed) <br>
quick sort: 用partition function先整体有序，返回pivotPos，然后再pivotPos两边分边局部有序
merge sort: 用mid分成左右两部分，leftArr和righArr分别记录局部的有序数组，然后merge到arr数组
- [0179. Largest Number](Solutions/0179.Largest-Number.py) (M) <br>
quick sort, self-define comparing two strings by: if s1 + s2 <= s2 + s1: return True else False
- [0969. Pancake Sorting](Solutions/0969.Pancake-Sorting.py) (M) <br>
for i in range(lens-1, -1, -1 ): Find maxIndex -> flip max to top -> flip max to bottom of the whole arr -> repeat
<br> 147. Insertion sort a linked list <br>

### [Partition and quick select](/Sort.py) 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode) 好多细节
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M Youtubed)  <br>
solution 1: quick select O(N) in average; solution 2: heap O(NlogK): heapq.heappush(numsHeap, num); heapq.heappop(numsHeap)
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E) <br>
solution 1: 同向双指针； solution 2: 反向双指针同上题
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
STEP 1: 反向双指针（或同向双指针）对[-1,-2,4,,5,-3,6]进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]; STEP 2: 再正负正负安插
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) <br>
同向双指针: move '2's to the right first, then move '1's to the middle

### [Sorted Array](/Sort.py) 
- [0056. Merge Intervals](Solutions/0056.Merge-Intervals.py) (M) <br>
sort the intervals first, res = []; for interval in intervals: if the interval start time is larger than the largest end time in res, then the interval cannot be merged, then res.append(interval), else then res[-1][1] = max(res[-1][1], interval[1])
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) <br>
target是随着i的移动而变化的binary search



# [Two Pointers](/Two-pointers.py)
### [反向双指针](/Two-pointers.py)
- [0977. Squares of a Sorted Array](Solutions/0977.Squares-of-a-Sorted-Array.py) (E) <br>
three pointers: i starts from beginning of A; j starts from the end of A; k starts from end of res 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode) <br>
note 1: temp = nums[i], 出循环后需要nums[i] = temp回来; note 2: 先判断j, j-=1出来后nums[i]=nums[j] 
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) <br>
solution 1: 同上31的方法做partition; solution 2: 同向双指针: anchor and curr, swap A[anchor] and A[curr] when A[curr] is even
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode)
STEP 1: 反向双指针进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]; STEP 2: 再来进行正负正负正负安插
- [0561. Array Partition I](Solutions/0561.Array-Partition-I.py) <br>
sort the arr first, then the maximum sum of pairs is the sum of every other num
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) <br>
solution 1: typical partition problem, step 1: 先把0放到最前面; step 2: 再把2放到最后
solution 2: 同向双指针的方法也应该理解掌握！
- [0011. Container With Most Water](Solutions/0011.Container-With-Most-Water.py) (!!M) <br>
Start with the maximum width container and go to a shorter width container; This way we are compromising on the width but we are looking forward to a longer length container.


### [同向双指针](/Two-pointers.py)
- [0088. Merge Sorted Array](Solutions/0088.Merge-Sorted-Array.py) <br>
modify nums1 in-place, use i, j, k = m - 1, n - 1, m + n -1; 把最大的数放到nums1的后面
- [0283. Move Zeroes](Solutions/0283.Move-Zeroes.py) <br>
anchor keeps all the non-zero numbers, while curr runs forward; whenever curr equals a non-zero number, switch it to anchor.  Solution 2: partition using the method in 31, but not accepted cuz partition changes the original order of non-zero numbers
- [0026. Remove Duplicates from Sorted Array](Solutions/0026.Remove-Duplicates-from-Sorted-Array.py) (!!E) 典型的同向双指针
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) <br>
同向双指针法，如果碰到符合条件的，把j往前挪到不重复的元素去。dfs解subset问题里的去重是怎么做的：前面的3用到了，后面的3就跳过就可以了。
- [0042. Trapping Rain Water](Solutions/0042.Trapping-Rain-Water.py (!!H) <br>
首先找到最高highestBar的位置。然后从左边往最高的位置扫，同时maintain一个指针记录leftHighest的高度，如果扫到的地方i小于这个leftHighest的高度，
则说明i这个地方可以蓄水，可蓄水量为leftHighest的高度减去i的高度；如果扫到的地方i大于这个leftHighest的高度，则说明i这个地方不可以蓄水，所以这时候要更新leftHighest为i的高度。同理对右边做同样的操作


# [Two Sum]()
- [0001. Two Sum](Solutions/0001.Two-Sum.py) (E) 
- [0167. Two Sum II - Input array is sorted](Solutions/0167.Two-Sum-II-Input-array-is-sorted.py) (E)
- [0170. Two Sum III - Data structure design](Solutions/0170.Two-Sum-III-Data-structure-design.py) (E)
- [0653. Two Sum IV - Input is a BST](Solutions/0653.Two-Sum-IV-Input-is-a-BST.py) (E)
- [1099. Two Sum Less Than K](Solutions/1099.Two-Sum-Less-Than-K.py) (E) 
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) (求和用反向双指针，求差用同向双指针)
- [0609. Two Sum - Less than or equal to target](Solutions/0609.Two-Sum-Less-than-or-equal-to-target.py) (E) 
- [0015. 3Sum](Solutions/0015.3Sum.py) (!!M) 
- [0016. 3Sum Closest](Solutions/0016.3Sum-Closest.py) (M) 
- [0259. 3Sum Smaller](Solutions/0259.3Sum-Smaller.py) (M) 
- [0018. 4Sum](Solutions/0018.4Sum.py) (M) 
- [0454. 4Sum II](Solutions/0454.4Sum-II.py) (M) 


# [Data Structure](/Data-Structure.py)
### [Stack and Queue](/Data-Structure.py)
- [0232. Implement Queue using Stacks](Solutions/0232.Implement-Queue-using-Stacks.py) (E) 
- [0225. Implement Stack using Queues](Solutions/0225.Implement-Stack-using-Queues.py) (E) 
- [0155. Min Stack](Solutions/0155.Min-Stack.py) (!!E) 
- [0716 (没搞懂！)] (E) 
- [0394. Decode String](Solutions/0394.Decode-String.py) (M) 
### [Iterator](/Data-Structure.py)
- [0341. Flatten Nested List Iterator](Solutions/0341.Flatten-Nested-List-Iterator.py) (M) 
- [0251. Flatten 2D Vector](Solutions/0251.Flatten-2D-Vector.py) (M)
- [0281. Zigzag Iterator](Solutions/0281.Zigzag-Iterator.py) (M)
- [0284. Peeking Iterator](Solutions/0284.Peeking-Iterator.py) (M)
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (M)
#### [单调栈](/Data-Structure.py)
84. Largest Rectangle in Histogram  (H) (should understand later)

### [Hashmap/Dictionary](/Data-Structure.py)
- [0146. LRU Cache](Solutions/0146.LRU-Cache.py) (!!M)

### [Heap/Heapq](/Data-Structure.py)
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!M)
- [0347. Top K Frequent Elements](Solutions/0347.Top-K-Frequent-Elements.py) (M)
- [0253. Meeting Rooms II](Solutions/00253.Meeting-Rooms-II.py) (!!M) (以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间)
- [0973. K Closest Points to Origin](Solutions/0973.K-Closest-Points-to-Origin.py) (M) （以squre来构建heap就可以了，heap中的元素是(square, point)）
- [0378. Kth Smallest Element in a Sorted Matrix](Solutions/0378.Kth-Smallest-Element-in-a-Sorted-Matrix.py) (M)
- [0264. Ugly Number II](Solutions/0264.Ugly-Number-II.py) (M)


# [Dynamic Programming](Dynamic-Programming.py)
- [0322. Coin Change](Solutions/0322.Coin-Change.py) (!!M) <br>
最小值问题。状态: f[X]=最少用多少枚硬币拼出X; 转移方程：f[X] = min(f[X-2]+1, f[X-5]+1, f[X-7]+1)
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (!!M) <br>
存在性问题。状态: dp[j]=能不能跳到位置j; 转移方程：dp[j]=True if dp[i] and i+nums[i]>=j) (TLE)
- [0152. Maximum Product Subarray](Solutions/0152.Maximum-Product-Subarray.py) (M) <br>
最大值问题。用一个数组记录最大的正数maxDP[i]，另一个数组记录最小的负数minDP[i], maxDP[i] = max(nums[i], maxDP[i-1]*nums[i]) if nums[i]>0

<br> 542, <br> 1162

### [坐标型DP](/Dynamic-Programming.py)
- [0062. Unique Paths](Solutions/0062.Unique-Paths.py) (!!M) <br>
状态: f[i][j]=有多少种方式从左上角走到(i, j); 转移方程：f[i][j] = f[i][j-1]+f[i-1][j]
- [0063. Unique Paths II](Solutions/0063.Unique-Paths-II.py) (M) <br> 
转移方程：f[i][j] = 0 if it is obstacle else f[i][j-1]+f[i-1][j])
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (M) <br> 
dp[i][j]=the minimum path sum to (i, j); dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j])
- [0120. Triangle](Solutions/0120.Triangle.py) (M) <br>
dp[i][j] = min(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1])
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M) <br>
dp[i][j]=以(i, j)为右下角的最大正方形的边长; dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j]=1 
- [0403. Frog Jump](Solutions/0403.Frog-Jump.py) (M) <br>
dp[stone]为set，记录青蛙可以通过哪些步跳到stone。用bottom up方法。状态转移方程为：跳k-1到stone+k-1: dp[stone+k-1].add(k-1); 跳k到stone+k: dp[stone+k].add(k); 跳k+1到stone+k+1: dp[stone+k+1].add(k+1)

### [序列型DP](/Dynamic-Programming.py)
- [0256. Paint House](Solutions/0256.Paint-House.py) (E) <br>
dp[i][j] means the minimum cost to paint house i to be color j; dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
- [0265. Paint House II](Solutions/0265.Paint-House-II.py) (E) <br> 
dp[i][j]=minimum cost to paint the ith house the be color j; dp[i][j] = tempMin + costs[i][j])
- [0198. House Robber](Solutions/0198.House-Robber.py) (E) <br>
f[i]=the max profit when reaching ith house; f[i] = max(rob ith = f[i-2]+nums[i], not rob ith = f[i-1]) <br>
空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]
- [0213. House Robber II](Solutions/0213.House-Robber-II.py) (E) <br>
房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：1. 房子1没偷：问题变成了对房子2:N做House robber I的问题; 2. 房子N没偷：问题变成了对房子1:N-1做House robber I的问题

### [Buy and sell stock DP问题](/Dynamic-Programming.py)
- [0121. Best Time to Buy and Sell Stock](Solutions/0121.Best-Time-to-Buy-and-Sell-Stock.py) (E) <br>
Only one transaction is allowed.  Maintain a minPrice and a maxProfit; maxProfit = max(maxProfit, price - minPrice)
- [0122. Best Time to Buy and Sell Stock II](Solutions/0122.Best-Time-to-Buy-and-Sell-Stock-II.py) (E) <br>
As many transaction as possible.  make a transaction every time price[i]>price[i-1]
- [0123. Best Time to Buy and Sell Stock III](Solutions/0123.Best-Time-to-Buy-and-Sell-Stock-III.py) (H) <br>
Only two transactions are allowed.  Maintain buy1=the minimum money you can own after the first buy, sell1=the maximum money you can earn after the first sell, also, buy2, sell2, and update them together in a for loop
- [0188. Best Time to Buy and Sell Stock IV](Solutions/0188.Best-Time-to-Buy-and-Sell-Stock-IV.py) (H) <br>
Only k transactions are allowed.   Maintain buy=[]*k, sell=[]*k, and update them together in a for loop
- [0309. Best Time to Buy and Sell Stock with Cooldown](Solutions/0309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py) (M) <br>
Has to rest for one day before buy another stock.  **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益 <br>
hold[i] = max(hold[i-1], unhold[**i-2**]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i])
- [0714. Best Time to Buy and Sell Stock with Transaction Fee](Solutions/0714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) (M) <br>
There is transaction fee when you sell. **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益 <br>
hold[i] = max(hold[i-1], unhold[i-1]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i] **- fee**)

###  [最长子序列问题](/Dynamic-Programming.py)
- [0674. Longest Continuous Increasing Subsequence](Solutions/0674.Longest-Continuous-Increasing-Subsequence.py) (E) <br>
dp[i] = 以i结尾(包括i)的最长连续子序列; dp[i] = dp[i-1] + 1 if nums[i]>nums[i-1]
- [0300. Longest Increasing Subsequence](Solutions/0300.Longest-Increasing-Subsequence.py) (!!M) <br>
不需要连续，所以不是dp[i] = dp[i-1] + 1，而是所有的j之前的i都有可能, 所以转移方程是 dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]) <br>
dp + binary search (O(NlogN))的算法也很重要！与354. 俄罗斯套娃问题一样！
- [0673. Number of Longest Increasing Subsequence](Solutions/0673.Number-of-Longest-Increasing-Subsequence.py) (M) <br>
 dp=以i为结尾的最大的长度; cnt=以i为结尾的最大的长度的个数; cnt[j]+=cnt[i] if dp[j]=dp[i]+1
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.Longest-Arithmetic-Sequence.py) (M) <br>
dp[i][j]=以i结尾的等差数列且以j为公差的长度; dp = [collections.defaultdict(lambda: 1) for _ in range(lens)]
- [0873. Length of Longest Fibonacci Subsequence](Solutions/0873.Length-of-Longest-Fibonacci-Subsequence.py) (M) <br>
dp[i][j]=以i, j为最后两个数字的fib的长度; dp[j][index of (A[i]+A[j])]=dp[i][j]+1; index of (A[i]+A[j])是(A[i]+A[j])在A中的位置，为了快速找到index of (A[i]+A[j])，用一个dict存储索引即可
- [0354. Russian Doll Envelopes](Solutions/0354.Russian-Doll-Envelopes) (M) <br>
Similiar with 300. LIS; here we not only compare nums[j]>nums[i], but instead both the width and height; TLE, should 300. LIS using DP+binary search (O(NlogN))
- [0334. Increasing Triplet Subsequence](Solutions/0334.Increasing-Triplet-Subsequence.py) (M) <br>
Similiar with 300. LIS; dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]); if dp[j]>=3 return True

### [区间型DP](/Dynamic-Programming.py)
- [0005. Longest Palindromic Substring](Solutions/0005.Longest-Palindromic-Substring.py) (!!M) <br>
Return the longest substr: dp[i][j]=from i to j (including j), is it a palindr? if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]): dp[i][j]=True; 注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i，所以i is from (j, 0)
- [0516. Longest Palindromic Subsequence](Solutions/0516.Longest-Palindromic-Subsequence.py) (!!M) <br>
Return the longest length: dp[i][j]=longest palindr from i to j; dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1]);注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i，所以i is from (j, 0)
- [0312. Burst Balloons](Solutions/0312.Burst-Balloons.py) (H) <br>
带memo的recursion比DP更好懂; left = self.memoSearch(nums, i, k, memo); right=self.memoSearch(nums, k, j, memo); maxCoins = max(maxCoins, left + right + nums[i]*nums[k]*nums[j])

###  [划分型DP](/Dynamic-Programming.py)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M) <br>
f[i]=number of decode ways until i; f[i]=f[i-1]+f[i-2] if int(s[i-1:i+1])<=26 else f[i-1]
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (M) <br>
f[i]=the least number of perfect square numbers which sum to i; f[j] = min(f[j-i^2]+1) for i^2<=j; Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5)
- [0132. Palindrome Partitioning II](Solutions/0132.Palindrome-Partitioning-II.py) (!!M) <br>
f[j]=the minimum number of total palindrome till the jth character (not including j); f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome： 划分型的dp的状态一般都not include j, 这样就有一个buffer layer可以用。

### [博弈型DP](/Dynamic-Programming.py)
- [0394. Coins in a Line](Solutions/0394.Coins-in-a-Line.py) (M) <br>
f[i]=面对i个石子，先手是必胜吗; f[i]=True if f[i-1] or f[i-2]都是False
- [0486. Predict the Winner](Solutions/0486.Predict-the-Winner.py) (M) <br>
f[i][j]=当石子还剩i到j时，先手最多能赢多少; f[i][j] = max(取左边A[i]-f[i+1][j], 取右边A[j]-f[i][j-1])

### [背包型DP](/Dynamic-Programming.py)
- [0092. Backpack](Solutions/0092.Backpack.py) (!!M Lintcode) <br>
f[i][m]=能否用前i个物品拼出重量m; f[i][m] = f[i-1][m] (表示前i-1个物品就可以拼出m) or f[i-1][m-A[i-1]] (表示前i-1个物品可以拼出m-A[i-1])
- [0563. Backpack-V](Solutions/0563.Backpack-V.py) (!!M Lintcode) <br>
f[i][m]=前i个物品能拼出重量m有多少种方式。f[i][m] = f[i-1][m] + f[i-1][m-A[i-1]]
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (!!M) <br>
f[i]=how many ways to combine to number i; 背包问题一定要把总承重放到状态里！！ f[i]=f[i-A1]+f[i-A2]+f[i-A3].... <br>
- [0125. Backpack II](Solutions/0125.Backpack-II.py) (!!M Lintcode) <br>
这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。用子问题定义状态：即f[i][j]表示前i件物品拼出重量j可以获得的最大价值。
f[i][j]=max{f[i-1][j] (不放入),f[i-1][j-A[i]]+V[i] (放入)}; return f[lens-1][M]
- [0089. k Sum](Solutions/0089.k-Sum.py) (M Lintcode) <br>
f[i][j][s]表示有多少种方法可以在前i个数中选出j个，使得它们的和是s; 情况一:（A[n-1]不选入）：需要在前n-1个数中选K个数，使得它们的和是Target: f[i][j][s] += f[i-1][j][s]; 情况二（A[n-1]选入）：需要在前n-1个数中选K-1个数，使得它们的和是Target-A[n-1]: f[i][j][s] += f[i-1][j-1][s-A[i-1]]
- [0416. Partition Equal Subset Sum](Solutions/0416.Partition-Equal-Subset-Sum.py) (M) <br>
背包问题：将A中的物品放入容量为target的背包中，问是否存在？ f[i][t]=将前i个物品放入背包中，能否拼出t (背包问题重量一定要入状态); f[i][t]=True if 不放最后一个进背包: f[i-1][t]=True or 放最后一个进背包: f[i-1][t-A[i-1]]=True

### [位操作型DP](/Dynamic-Programming.py)
- [0338. Counting Bits](Solutions/0338.Counting-Bits.py) (M) <br>
状态f[i]=i的二进制中有多少个1; dp[i] = dp[i >> 1] + i % 2

### [双序列型DP](/Dynamic-Programming.py)
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (!!M) <br>
f[i][j]为A前i个字符A[0..i)和B前j个字符[0..j)的最长公共子串的长度，注意不包括i和j，前面有一层buffer layer非常重要，就像sputtering那样重要！ f[i][j]=max(f[i][j-1], f[i-1][j], f[i-1][j-1] when A[i-1]=B[j-1])
- [0097. Interleaving String](Solutions/0097.Interleaving-String.py) (!!H) <br>
f[i][j]=s3的前[0..i+j)个字符能否由s1前i个字符[0..i)和s2前j个字符[0..j)交错形成; f[i][j]=True when (s3[i+j-1]=s1[i-1] 且 f[i-1][j]=True 即s3的前[0..i+j-1)个字符能否由s1前i-1个字符[0..i-1)和s2前j个字符[0..j)交错形成) or (s3[i+j-1]=s2[j-1] and f[i][j-1]=True)
- [0072. Edit Distance](Solutions/0072.Edit-Distance.py) (!!H) <br>
f[i][j]=A前i个字符[0..i)和B前j个字符[0..j)的最小编辑距离; f[i][j]=min{1. f[i-1][j]+1 (f[i-1][j]表示A[0..i-1)就可以拼成B[0..j)了，所以A[0..i)要拼成B[0..j)需要删掉A[0..i)的最后一个字母); 2. f[i][j-1]+1 (B[0..j)需要删掉最后一个字母，即A[0..i)的后面需要增加一个字母); 3. f[i-1][j-1]+1 (A[0..i)的后面需要replace一个字母); 4. f[i-1][j-1] (if A[i-1]=B[j-1] 就不需要任何操作直接就是了)}
- [0115. Distinct Subsequences](Solutions/0115.Distinct-Subsequences.py) (H) <br>
f[i][j]=B前i个字符B[0..i)在A前j个字符A[0..j)中出现多少次; f[i][j] += f[i][j-1] if B[i-1]!=A[j-1] else += f[i-1][j-1] + f[i][j-1] 
- [0044. Wildcard Matching](Solutions/0044.Wildcard-Matching.py) (H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配； 画个图会很明了，详见九章算法动态规划双序列型DP。
情况一：B[j-1]不是"星": f[i][j] = f[i-1][j-1] if (B[j-1]="?" or A[i-1]=B[j-1])
情况二：B[j-1]是"星"：可以让"星"表示0个字符，那就让A[0..i)去和B[0..j-1)匹配： f[i][j] = f[i][j-1]；也可以让"星"表示字符，A[i-1]肯定是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j]
- [0010. Regular Expression Matching](Solutions/0010.Regular-Expression-Matching.py) (!!H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配; 情况一：B[j-1]不是"星": f[i][j] = f[i-1][j-1] if (B[j-1]="." or A[i-1]=B[j-1]); 情况二：B[j-1]是"星"：可以让"星"表示0个前面的字符，那就让A[0..i)去和B[0..j-2)匹配： f[i][j] = f[i][j-2]；也可以让"星"表示几个前面的字符，A[i-1]是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j] if (B[j-2]="." or B[j-2]=A[i-1])


### [Other DP Problems](https://juejin.im/post/5d556b7ef265da03aa2568d5)
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M)
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (M)
- [0718. Maximum Length of Repeated Subarray](Solutions/0718.Maximum-Length-of-Repeated-Subarray.py) (M)
- [1049. Last Stone Weight II](Solutions/1049.Last-Stone-Weight-II.py) (M)
- [1024. Video Stitching](Solutions/1024.Video-Stitching.py) (M)
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
- [0983. Minimum Cost For Tickets](Solutions/0983.Minimum-Cost-For-Tickets.py) (M)
- [0688. Knight Probability in Chessboard](Solutions/0688.Knight-Probability-in-Chessboard.py) (M)
- [0361. Bomb Enemy](Solutions/0361.Bomb-Enemy.py) (M)
- [0467. Unique Substrings in Wraparound String](Solutions/0467.Unique-Substrings-in-Wraparound-String.py) (M)
- [0898. Bitwise ORs of Subarrays](Solutions/0898.Bitwise-ORs-of-Subarrays.py) (M)
- [0343. Integer Break](Solutions/0343.Integer-Break.py) (M)
- [1223. Dice Roll Simulation](Solutions/1223.Dice-Roll-Simulation.py) (M)
- [1105. Filling Bookcase Shelves](Solutions/1105.Filling-Bookcase-Shelves.py) (M)
- [0464. Can I Win](Solutions/0464.Can-I-Win.py) (M)


# Other Algorithms
### [Rabin Karp]()
- [0028. Implement strStr()](Solutions/0028.Implement-strStr().py) (E) (Rabin Karp Algorithm O(M+N), use Hashcode, ord(ch)-ord("a"))



# Sliding window
