### Google top 200
#### 12/30

- [0843. Guess the Word](Solutions/0843.Guess-the-Word.py) (!!!H Google) <br>
Repeatedly choose a word to guess, and then eliminate all words that do not have the same number of matches as the guessed word. 
In this way, the wordlist is narrowed down each time we do a guess.
How to choose a word: solution 1: random guess; 2. choose the guess word wisely (Heuristically). Soltion 2: Each time we guess, we choose the word that has the most common chars (overlaps) with other words in the candidates list. This is just a hueristic estimation, hard to prove why it works. But indeed it works much better than random guess.
- [1423. Maximum Points You Can Obtain from Cards](Solutions/1423.Maximum-Points-You-Can-Obtain-from-Cards.py) (!!!M Google) <br>
sliding window with fix size problem, the only difference is that some part of the window is at the beginning of the list and some are at the end. 我们可以转化为 find the minimum points you can get within window with fixed size: lens-k. 套用模板即可 Google真是滑窗控
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](Solutions/1438.Longest-Continuous-Subarray-With-Absolute-Diff-Less-Than-or-Equal-to-Limit.py) (!!!M Google) <br>
总结：如果题目需要我们在window里更新最大值或最小值，我们往往需要maintian一个mono increasing or mono decreasing deque.
这个题目我们maintain an increasing dq and a decreasing dq. step 1: 更新maxdq, just like what we did for monostack; step 2: 更新mindq, 套用mono stack模板; step 3: sliding window to update res - 套用sliding window模板
- [0727. Minimum Window Subsequence](Solutions/0727.Minimum-Window-Subsequence.py) (!!!H) <br>
solution 1: sliding window - O(MN) 这题subseq与上题substring不同，上题只需要freq都满足了就行，这题不仅如此，而且还是讲究顺序的，; solution 2: dp. dp[i][j] = the min window subsequence that ends with ith ch in t, and jth ch in s. If t[i-1] == s[j-1]: dp[i][j] = dp[i-1][j-1] + 1; else: dp[i][j] = dp[i][j-1] + 1
- [0946. Validate Stack Sequences](Solutions/0946.Validate-Stack-Sequences.py) (!!!M Google) <br>
需要一个 __辅助栈st__ 来模拟push和pop的过程，用一个指针在popped list里面跑，如果popped[i]==st[-1]那就一直pop, 最后判断st能不能pop为空
- [0359. Logger Rate Limiter](Solutions/0359.Logger-Rate-Limiter.py) (!!!E Google) <br>
很简单，用一个dictionary存(message, last timestamp when message was printed)就可以了。Google followup: input在K长度内无序的，但是时间t+K之后的输入一定出现在t之后。比如K是5，
[4, foo], [1, foo], [0, bar], [6, bar] => 在[4, foo], [1, foo], [0, bar]内是无序的，但是[6, bar]一定出现在[0, bar]之后，因为6>0+5.
也就是短程无序，长程有序。这时候该怎么print输出呢？
用一个heapq, heapq里面存(timestamp, message), 用一个deque里面也存(timestamp, message), 当发现下一个时间大于当前最小时间+K，就pop出当前的最小的放入到deque里面去, 这样deque里面存的就是长短程都有序的了
- [1153. String Transforms Into Another String](Solutions/1153.String-Transforms-Into-Another-String.py) (!!!H Google) <br>
step 1: Map each character in str1 to what it needs to be in str2. If any of these mappings collide (e.g. str1 = "aa", str2 = "bc", "a" needs to become both "b" and "c"),
we immediately return False since the transformation is impossible. Next, we check the number of unique characters in str2. If all 26 characters are represented, there are no characters available to use for temporary conversions, and the transformation is impossible.
- [1548. The Most Similar Path in a Graph](Solutions/1548.The-Most-Similar-Path-in-a-Graph.py) (!!!H Google) <br>
similar with 100320-Diff Between Two Strings - __DP to find path__
Step 1: build a DP table in order to find the minimum edit distance to targetPath; Step 2: we traverse __reversely the build DP table__ to find which path did we take 
in order to get the minimum edit distance. At last, we return res[::-1]. dp[i][u] = the min edit distance if we take i steps, with u as the last city visited; dp[i][u] = min(dp[i-1][v] for v in graph[u]) + 0 if names[u] == targetPath[i] else 1; then min(dp[m]) is our minimum edit distance overall. O(MN^2)
- [0809. Expressive Words](Solutions/0809.Expressive-Words.py) (!!!M Google) <br>
pre-calculate how many successive same chars are there at each idx: "heeellooo" --> {0: 1, 1: 3, 2: 2, 3: 1, 4: 2, 5: 1, 6: 3, 7: 2, 8: 1}
- [0465. Optimal Account Balancing](Solutions/0465.Optimal-Account-Balancing.py) (!!H Google) <br> 
step 1: find all the balance information for each person; step 2: we care only those person who own or owe money - put them in a list; backtrack to update the minimum transaction needed. backtrack传入(curr_idx, curr_cnt)
- [0471. Encode String with Shortest Length](Solutions/0471.Encode-String-with-Shortest-Length.py) (!!!H Google) <br>
solution dp. dp[i][j] is the encode of substring including index i to index j. dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j], potential_candidate) in terms of length.
potential_candidate = "k[repeating_pattern]",  where pattern is the repeating string in substring s[i:j+1] and k is the number of repeating times. 
initializaton: dp[i][j] = s[i:j+1] originally, return dp[0][n-1]
- [0715. Range Module](Solutions/0715.Range-Module.py) (!!!H) <br>
Store intervals in a 1D sorted array. Use bisect_left and bisect_right to locate where the incoming interval should be. addRange and removeRange takes O(N). queryRange can also use bisect to locate where the interval location is, [left, right]必须在某一个且同一个range内才return True - O(logN),  这题需要很细致，没有完全弄明白。
- [0846. Hand of Straights](Solutions/0846.Hand-of-Straights.py) (!!!M Google) <br>
same as 1296. 用以一个hashmap记录frequency. 由于必须固定长度为W, 所以我们每次都去连W个就可以了
- [0722. Remove Comments](Solutions/0722.Remove-Comments.py) (!!M Google) <br>
String manipulation. manipulate string line by line.
- [1060. Missing Element in Sorted Array](Solutions/1060.Missing-Element-in-Sorted-Array.py) (!!!M Google) <br>
定义一个function missing(idx) to find the number of number missing before idx. so that we can compare missing(mid) with k. Google真的把binary search 玩出花了！
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](Solutions/1477.Find-Two-Non-overlapping-Sub-arrays-Each-With-Target-Sum.py) (!!!!M Google) <br>
prefix sum + dp. step 1: construct a pre_sum and a suf_sum. Step 2: then use the pre_sum and suf_sum to construct two lists: pre_min[i] = minimum lens of valid subarray that ends before i. suf_min[i] = minimum lens of valid subarray that starts after i. step 3: find the ans as we iterate the arr
- [0528. Random Pick with Weight](Solutions/0528.Random-Pick-with-Weight.py) (!!!M Google) <br>
step 1: create a __prefix sum arr__; step 2: generate a rand_idx; step 3: __binary search__ to find where the idx is in the prefix_sum arr; follow up 是设计一个class支持修改已有元素的权重, 可能要用到数的结构实现o(logn)吧，没弄明白
- [1056. Confusing Number](Solutions/1056.Confusing-Number.py) (E) <br>
use a hashmap
- [1088. Confusing Number II](Solutions/1088.Confusing-Number-II.py) (!!H Google) <br>
solution 2: Only 0, 1, 6, 8, 9 are the valid set of digits, do a backtracking to generate all the numbers containing this digits and check they are valid.
time complexity: O(5^M), where M is how many digits are there in str(N), which scales with ~logN, where log is 10-based.
- [0551. Student Attendance Record I](Solutions/0551.Student-Attendance-Record-I.py) (E Google) <br>
warm up for 552. Student Attendance Record II.
- [0552. Student Attendance Record II](Solutions/0552.Student-Attendance-Record-II.py) (!!!H Google) <br>
dfs + memo. solution 1: typical backtrack - O(3^N); solution 2: dp - O(n). dp[i] = how many ways for i. If we don't have "A" in the record, then we have below: dp[i] = dp[i-1] if choose ith ch to be "P". dp[i] = dp[i-2] if choose the last two ch to be "PL"
dp[i] = dp[i-3] if choose last three ch to be "PLL", note that cannot be "LLL". so dp[i] = dp[i-1] + dp[i-2] + dp[i-3] for the case there is not "A" in the record. Now we have the dp[i] for the case with out "A". Since we can add "A" anywhere, so the res = sum(dp[i-1] * dp[n-i]).
- [1138. Alphabet Board Path](Solutions/1138.Alphabet-Board-Path.py) (!!!M Google) <br>
bfs. 最短距离问题
- [0833. Find And Replace in String](Solutions/0833.Find-And-Replace-in-String.py) (!!!M Google) <br>
String manipulation.
- [0995. Minimum Number of K Consecutive Bit Flips](Solutions/0995.Minimum-Number-of-K-Consecutive-Bit-Flips.py) (!!H Google) <br>
q 记录区间[i-k, i]内被反转了的idx, 遍历过程中把里i很远的idx都pop出来，保持窗口小于等于K, 此时len(q)就是位置i已经被翻转的次数，如果为奇数表示i已经从0翻到1或者从1翻到0了
- [0489. Robot Room Cleaner](Solutions/0489.Robot-Room-Cleaner.py) (!!!H Google) <br>
遍历机器人的四个方向即可，唯一需要注意的是每次都需要调整机器人的朝向才能move一下，毕竟是机器人嘛. backtrack函数需要传入(curr_i, curr_j, curr_facing). 另外需要定义一个go_back function so that we can go back to the original position and facing for backtracking purpose.
- [0753. Cracking the Safe](Solutions/0753.Cracking-the-Safe.py) (!!!H) <br>
思路： dfs取cur_res的最后n-1个数字，加上k中的一个新的数字来组新的combination, 判断这个combination是否已经cover到了. dfs的结束条件是if len(covered) == k ** n
- [0308. Range Sum Query 2D - Mutable](Solutions/0308.Range-Sum-Query-2D-Mutable.py) (H) <br>
solution: segment tree. 代码裸长115行，我去NMLGB! 放弃这题算了
- [1110. Delete Nodes And Return Forest](Solutions/1110.Delete-Nodes-And-Return-Forest.py) (!!!M Google) <br>
we update res as we traverse the tree. we append a node into res if two conditions are satisfied: 1. the node should not be deleted; 2. the node has not parent (meaning it's the root of a forest). In order to check if a node has parent or not, we need to pass has_parent bool into dfs arguments. If a node is in to_delete list, then the node should pass the information to it's children that it has been deleted and it's children has no parent now.
- [0085. Maximal Rectangle](Solutions/0085.Maximal-Rectangle.py) (!!!H Google) <br>
step 1: construct a heights list for each row; step 2: calculate the largestRectangularHistogram of each height using the same method in 84; Should think about dynamic programming solution also.
- [0690. Employee Importance](Solutions/0690.Employee-Importance.py) (!!E Google) <br>
simple dfs 可破, use a dictionary to map employee_id with employee, so that looking for employee by id takes O(1)
- [1146. Snapshot Array](Solutions/1146.Snapshot-Array.py) (!!!M Google) <br>
solution 1: sparse array. Since 题目说了 initially, each element equals 0.
we treated it as a sparse matrix: use a dictionary to store only the non-zero values.
- [1293. Shortest Path in a Grid with Obstacles Elimination](Solutions/1293.Shortest-Path-in-a-Grid-with-Obstacles-Elimination.py) (!!!H Google) <br>
bfs. q 里面需要放入当前用了多少eliminations. q.append((next_i, next_j, curr_elimination_cnt))
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (!!!M) <br>
这个题目要做三个判断：1. 判断seqs的拓扑排序是否存在，只需判断len(res) 是否等于len(graph) or len(inDegrees), 如果小于说明有孤立节点，如果大于说明有环，两者都不存在拓扑排序; 2. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素, 即每一层只有一个选择: if len(q)>1: return False; 3. 最后判断这个唯一的拓扑排序res是否等于org
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](Solutions/1368.Minimum-Cost-to-Make-at-Least-One-Valid-Path-in-a-Grid.py) (!!!H Google) <br>
由于我们可以选择四个方向都可以走，所以不能用dp. 如果只能朝右下方向走才能用dp. 可以朝四个方向走只能用bfs/dfs. 由于我们需要maitain min_cost, 所以可以用Dijkstra's. heapq stores (curr_cost, curr_i, curr_j). 
- [1231. Divide Chocolate](Solutions/1231.Divide-Chocolate.py) (!!!H Google) <br>
minimum of maximum / maximum of minimum 的问题: 与上一题类似，把array分成K份，求max of min subarray sum. Divide the nums into K+1 subarrays, and make sure each subarray has a sum at least S. Find the max S. so it's a OOXXX problem finding the last O.
- [1631. Path With Minimum Effort](Solutions/1631.Path-With-Minimum-Effort.py) (!!M) <br>
Obviously, it is a minimum of max_val problem, which is typical Dijkstra's. maintain a heapq to store (the max_diff in the path so far till the curr_pos, curr_pos). Each time, we push (max(next_diff, curr_max_diff), next_pos). 注意需要一个visited set to store the pos we visited.
- [0315. Count of Smaller Numbers After Self](Solutions/0315.Count-of-Smaller-Numbers-After-Self.py) (!!H Google) <br>
Segment Tree solution: O(NlogN) time and O(N) space. 从右往左遍历add num into the tree one by one， at the same time update the cnt of smaller number after self. Follow up: how to solve Spare Segment Tree problem? - Merge sort. 正解是solution 2: merge sort O(nlogn)
- [1377. Frog Position After T Seconds](Solutions/1377.Frog-Position-After-T-Seconds.py) (!!H Google) <br>
dfs, 虚拟一个节点零出来，从0节点出发做dfs. dfs the graph and update the dist of target and the prob of reaching target
- [0001. Two Sum](Solutions/0001.Two-Sum.py) (!!E) <br>
九章算法：对于求 2 个变量如何组合的问题可以循环其中一个变量，然后研究另外一个变量如何变化, 普世的方法是：for循环一个变量a，然后看另外一个变量target-a是不是在一个hashmap中
- [1277. Count Square Submatrices with All Ones](Solutions/1277.Count-Square-Submatrices-with-All-Ones.py) (M Google) <br>
DP. very similar with 221.Maximal-Square. dp[i][j] 表示以 (i, j) 结尾所组成的最大正方形的边长。dp[i][j] 也表示以 (i, j) 结尾能组成的正方形的个数。
- [1376. Time Needed to Inform All Employees](Solutions/1376.Time-Needed-to-Inform-All-Employees.py) (!!!M Google) <br> 
Same as Path Sum II except it's a N-arry tree.
- [0329. Longest Increasing Path in a Matrix](Solutions/0329.Longest-Increasing-Path-in-a-Matrix.py) (!!!H Google) <br>
solution 1: 从每一个点开始做backtrack - next candidate valid的条件是matrix[next_i][next_j] > matrix[curr_i][curr_j].  - O(MN2^(MN)).  solution 2: 由于题目并不要求算出path, 所以可以用recurssion with memorization to memorize the LIP from (curr_i, curr_j) (top down dp). Time complexity : O(MN). solution 3: buttom up dp.
- [1240. Tiling a Rectangle with the Fewest Squares](Solutions/1240.Tiling-a-Rectangle-with-the-Fewest-Squares.py) (!!!H Google) <br>
backtrack. The basic idea is to fill the entire block bottom up.  In every step, find the lowest unfilled square first, and select a square with different possible sizes to fill it.  What is the nodes in the graph? It is a height array (skyline) height_arr!!!!! 
The start_node is height_arr = [0, 0, 0...], the end_node is height_arr = [m, m, m...]. Pruning: 1. When the current cnt has exceeded the value of the current global optimal solution, then no need to move forward. 2. Try largest square possible first (improves time by a lot).
- [1504. Count Submatrices With All Ones](Solutions/1504.Count-Submatrices-With-All-Ones.py) (!!!M Google) <br>
Monostack. solution 1: dp. O(M^2N) 固定以up_row为长方形上边，然后去探寻不同下边的情况, 每次探寻一个下边，我们都计算一次从up_row到down_row可能有多少个valid_submatrices,
我们把这个计算转换成一维来计算，对于每一个up_row, 都构建一个一位数组arr.  arr[j] = 1 if from up_row to down_row, all values in column j are 1. 只要up_row到down_row有一个value is 0，
我们就设置arr[j] = 0, 表示不可能以up_row为上边以down_row为下边以j为右col构造valid submatrce. solution 2: 与84.Largest-Rectangle-in-Histogram, 85.Maximal-Rectangle很类似.
先构造histogram. 以j结尾的submatrices的个数等于heights[j] * (j - 向左找第一个height小于heights[j]的idx).
- [0729. My Calendar I](Solutions/0729.My-Calendar-I.py) (！！M Google) <br>
Maitian a intervals list. The problem is to find the overlap of two intervals. We loop over the intervals. 
一个interval与另一个interval的位置关系就三种情况(1. 没有交集; 2. 一个包含了另一个; 3. 有交集但是没有谁能完全包含谁). 
这里我们只要遇到case 2 or case 3, then there is an overlap, return False
- [0877. Stone Game](Solutions/0877.Stone-Game.py) (!!M Google) <br>
dp. dp[i][j] = how many more scores can someone have when left stones are [i, j] inclussive. dp[i][i] = piles[i]. dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]). return dp[0][n-1]
- [1140. Stone Game II](Solutions/1140.Stone-Game-II.py) (!!M Google) <br>
dp + suffix sum. dp[i][j] = the max score one can get with [i:] piles and M = j. dp[i][j] = max(sum(piles[i:]) - dp[i+x][max(j, x)] for x in range(1, min(2* j, n)). dp[i][n] = sum(piles[i:])
- [1406. Stone Game III](Solutions/1406.Stone-Game-III.py) (!!M Google) <br>
dp. similar with 394. Coins in a Line.  dp[i] = __the max one can win with [i:] stones left__. dp[i] = max(stones[i] - dp[i+1], stones[i] + stones[i+1] - dp[i+2], stones[i] + stones[i+1], stones[i+2] - dp[i+3])
- [1510. Stone Game IV](Solutions/1510.Stone-Game-IV.py) (H Google) <br>
dp. dp[j] = can one win with j. dp[j] = True if not dp[j - i* i] for i in range(1, sqrt(j)). O(N^1.5)
- [1563. Stone Game V](Solutions/1563.Stone-Game-V.py) (H Google) <br>
dp. dp[i][j] = the number of scores Alice can get for [i, j]. dp[i][i] = for k in range(i, j) max(dp[i][k], dp[k+1][j]) + min(sums[i, k], sums[k+1, j]). O(N^3)
- [0900. RLE Iterator](Solutions/0900.RLE-Iterator.py) (!!!M Google) <br>
stack. one stack store cnt, one stack store num
- [0695. Max Area of Island](Solutions/0695.Max-Area-of-Island.py) (M) <br>
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a dfs/bfs.
- [0562. Longest Line of Consecutive One in Matrix](Solutions/0562.Longest-Line-of-Consecutive-One-in-Matrix.py) (!!!M Google) <br>
hashset. each time we meet a 1, we explore horizontally, vertically and diagonally.
Use set to store the nodes that were horizontally visited, vertically visited and diagonally visited. 
- [1499. Max Value of Equation](Solutions/1499.Max-Value-of-Equation.py) (!!!H Google) <br>
__maintain previous min/max problem__ solution 1: heapq; solution 2: monodeque - O(N). 如果题目需要我们在window里更新最大值或最小值，我们往往需要maintian一个mono increasing or mono decreasing deque.  在mono deque中会有两个while loop，第一个while loop从左端pop作为sliding window去限定window size, 第二个while loop从右端pop作为monostack去maintain 最大值/最小值
- [0792. Number of Matching Subsequences](Solutions/0792.Number-of-Matching-Subsequences.py) (!!M Google) <br>
solution 1: compare each word with source string using two pointers. O(nmk), where n = len(s), m = len(words) and k = average lens of word in words. solution 2: use binary search in s, similar with 1055.  O(mklogn)
- [0652. Find Duplicate Subtrees](Solutions/0652.Find-Duplicate-Subtrees.py) (!!M Google) <br>
If two subtrees have the same string representation, then they are duplicated subtress.  solution 1: serialize the every subtree using bfs, and put (string presentation of subtree --> subtree node) into a hashmap. Since serialization takes O(N), so the overall algorithm takes O(N^2). solution 2: serialize the binary tree using post-order traversal.  Since we can update the mapping during the traversal, the whole algorith takes O(N)
- [0767. Reorganize String](Solutions/0767.Reorganize-String.py) (!!M Google) <br>
这种间隔k个位置安排座位的问题，都是task schedule的做法！这一题k=1. 用一个hq保存最大的freq, 然后按要求排座位，注意add_back. # case 1: if we can put seat ch into res, then go ahead and seat it it; # case 2: if there is already to same ch on top of res, then we cannot seat the 1st_freq ch, instead, we seat the 2nd highest freq
- [0146. LRU Cache](Solutions/0146.LRU-Cache.py) (!!!M youtubed) <br>
use a double linked list and a dictionary; Double linkedlist: newest node append to tail, eldest node remove from head, so that the operation is O(1); Hashmap: key is key, value is the corresponding double linkedlist node
- [0460. LFU Cache](Solutions/0460.LFU-Cache.py) (!!!H Google) <br>
其实是在LRU的基础上加了一个frequency的要求。Use a dictionary to store (key, freq) pair. Use another dicitonary to store (freq, list of keys) pair, where list of keys could be OrderedDict like LRU to enable O(1) operations. Use a self.min_freq to store the min_freq. Follow up 变形题snapchat：在一个data stream 中find top K most frequent number用LFU来解，也可以用heapq O(Nlogk) or quick select O(N).
- [1444. Number of Ways of Cutting a Pizza](Solutions/1444.Number-of-Ways-of-Cutting-a-Pizza.py) (!!!H Google) <br>
dfs + memo. memo[(i, j, k)] returns the number of ways to cut pizza[i:n][j:m] into k pieces.
Step 1: In order to fast get how many apples are there in the down-right corner pizza[i:n][j:m] block,
construct suff_sum similar with 304. Range Sum Query 2D - Immutable. Step 2: dfs + memo.
- [0527. Word Abbreviation](Solutions/0527.Word-Abbreviation.py) (!!!H Google) <br>
Trie. step 1: 建立一个abbrev函数：从idx开始，对 word 做abbreviation. step 2: 建立一个abbr2word保存 abbr-->word. step 3: 遍历建立好了的abbr2word。 for abbr, word_lst in abbr2word.items(), 
如果len(word_lst)==1, 那说明这个abbr是unique的，直接res.append(abbr); 如果len(word_lst)>1, 那说明这个abbr不是unique的，我们需要去寻找每一个word的unique prefix, 所以对这个word_lst就一个Trie, Trie中写一个find_idx函数 to where the prefix for word is unique (cur_node.cnt == 1)
Time Complexity: O(C) where C is the number of characters across all words in the given array. Space Complexity: O(C).
- [0777. Swap Adjacent in LR String](Solutions/0777.Swap-Adjacent-in-LR-String.py) (!!M Google) <br>
观察之后可以发现每次replace "XL" to "LX"都是相当于把"L"向左移动。
所以"L"一直向左移动，并且不会跨越其他"L" or "R". 而"R"一直向右移动，并且不会跨越其他"R" or "L".
- [0752. Open the Lock](Solutions/0752.Open-the-Lock.py) (!!M Google) <br>
题目蛮有意思的, 带层序遍历的bfs, If next_node is deadend, then we don't put it into q, find neighbor 函数比较有意思，这里第一次学到了yield;
- [0834. Sum of Distances in Tree](Solutions/0834.Sum-of-Distances-in-Tree.py) (!!H) <br> 
sums(Y) = sums(X) + cnt(X) - cnt(Y) = sums(X) + (N - cnt(Y) - cnt(Y) = sums(X) + N - 2* cnt(X).
cnt[X]可以通过dfs遍历一次算出来存到一个list里面，这样我们如果已知sums(0)的话，
那么其余的sums(X)都可以通过上述公式算出来了
- [0911. Online Election](Solutions/0911.Online-Election.py) (!!M Google) <br>
Precomputed Answer + Binary Search.
Constructor: O(N). each query: O(logN). 我们将每一个时刻的winner放到self.res中，这种提前计算好的思想非常重要！
- [1244. Design A Leaderboard](Solutions/1244.Design-A-Leaderboard.py) (M) <br>
use a dictionary for fast addscore and reset. use a heapq to find top K elements
- [0299. Bulls and Cows](Solutions/0299.Bulls-and-Cows.py) (!!!M Google) <br>
use a digit_to_cnt hashmap for digit. one pass to update A_cnt, another pass to update B_cnt.
- [0642. Design Search Autocomplete System](Solutions/0642.Design-Search-Autocomplete-System.py) (!!!H Google) <br>
与1268很像，只不过输入input_str是流数据，需要不断更新hotness. In TrieNode, there should be self.child, self.is_end, self.sentence, self.hotness. In Trie, there should be a method to insert a sentence into the trie; there should also be 
a method to search for all the possible autocomplete words of a given input string; 这个search mehtod分三步，第一步是遍历找到需要search的input_str在trie中所在的node, 第二步是从这个node出发，找到其所有能到达的endNode, 显然是backtrack来做，第三步是对所有能达到的endNode.hotness排个序，取前三作为输出。
- [0130. Surrounded Regions](Solutions/0130.Surrounded-Regions.py) (!!M) <br>
Solution 1: dfs/bfs: Step 1: Start from border, do a bfs for "O", mark all the "O" that can be reached from the border. We can either mark by putting them into a visited set, or just change it to some symbol "#". Step 2: 2nd pass, we change to "X" tha "O" that could not be visited from the border.  Solution 2: Union Find.  Step 1: Union all the "O" that are neighborign with each other. We do a weighted union, meaning when we union, we also choose to point to the one that is on the border. Step 2: 2nd pass, we change to "X" tha "O" that has a root not on border.  bfs只从border出发做bfs, 很中间的"O"就不用管了，而Union Find中间的也需要union, 所以bfs 比union find 更快。Solution 3: dfs interatively, only change one line in the bfs solution. Solution 4: dfs recurssively.
- [1254. Number of Closed Islands](Solutions/1254.Number-of-Closed-Islands.py) (M) <br>
与130出重复了
- [0394. Decode String](Solutions/0394.Decode-String.py) (!!M Google) <br>
定义一个numStack, 一个strStack 存nums和parenthesis. if it's a digit, should use a while loop to add the num in case there are multiple digits; if it's a ch, then put it into strStack; if it's a [, then put the num in numStack and re-initialize the tempNum and tempStr for calculation inside the []; if it's a ], then pop the resStack and signStack and update res.
- [1296. Divide Array in Sets of K Consecutive Numbers](Solutions/1296.Divide-Array-in-Sets-of-K-Consecutive-Numbers.py) (!!!M Google) <br>
用以一个hashmap记录frequency. 由于必须固定长度为k, 所以我们每次都去连k个就可以了
- [0165. Compare Version Numbers](Solutions/0165.Compare-Version-Numbers.py) (M Google) <br>
two pointers.  split the version by "." first before processing.
- [1074. Number of Submatrices That Sum to Target](Solutions/1074.Number-of-Submatrices-That-Sum-to-Target.py) (H) <br>
也可以先把行处理好，让每一行里面保存上面所有行的和，接下来就是在每一行里面去求560问题了，注意一点不同的是需要遍历upRow和downRow的, 如果不遍历就是solution 3的错误写法举一个反例想明白solution 3为什么行不通，自然就会改成solution 2了O(MMN)
- [0295. Find Median from Data Stream](Solutions/0295.Find-Median-from-Data-Stream.py) (!!H) <br>
定义两个heap: self.leftHq as a maxheap to store the nums that are smaller than median; and self.rightHq as a minheap store the nums that are larger then median.  每次新增一个数num的时候，先根据比 maxheap 中最后一个数大还是小丢到对应的 heap 里。丢完以后，再处理左右两边的平衡性:如果左边太少了，就从右边拿出一个最小的丢到左边。如果右边太少了，从左边拿出一个最大的丢到右边。时间复杂度是O(logN). Follow up questions are important. 
Follow up: leetcode 1093
- [0679. 24 Game](Solutions/0679.24-Game.py) (!!H Google) <br>
方法：两个for loop在nums中取两个数nums[i] and nums[j]. 算出nums[i] and nums[j]这两个数加减乘除可能得到的数，
将这些可能得到的数放进next_nums里面进行递归。递归的结束条件是len(nums)==1即无法再跟其他书加减乘除了。
如果len(nums)==1 and nums[0]==24, then return True
- [0379. Design Phone Directory](Solutions/0379.Design-Phone-Directory.py) (M) <br>
self.available_pool = set(i for i in range(maxNumbers)), set除了可以set.remove(item)之外，还可以set.pop() a random item.
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.Longest-Arithmetic-Sequence.py) (!!M) <br>
dp[i] = {key:diff, val:lens of arithmetic sequence ended with i and diff as 公差}; dp[j][nums[j]-nums[i]] = dp[i][nums[j] - nums[i]] + 1
- [0963. Minimum Area Rectangle II](Solutions/0963.Minimum-Area-Rectangle-II.py) (!!M Google) <br>
如果两条对角线相等，且平分对方，则这两条对角线可以组成矩形. use a hashmap to map (对角线的长度, 对角线的中点坐标) to a list of (对角线连接的两点的坐标) - O(n^2), O(n^2)
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (!!M) <br>
solution 1: 利用对称性质: x,y=abs(x),abs(y); q.append(neighbor) only if (-2 <= next_x <= x + 2 and -2 <= next_y <= y + 2); 1816 ms<br>
solution 2!!!: 从source和destination两端同时进行bfs!!!!注意双端bfs传进去的参数包含q and visited, bfs返回值是updated q and visited. cnt+=1的操作在主函数中进行. while true的结束条件: if visited_src & visited_des: return cnt_src + cnt_des; 452 ms <br>
solution 3 dp才是正解: recurrsion with memorization: cache[(x, y)] = min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1; 60 ms
- [0688. Knight Probability in Chessboard](Solutions/0688.Knight-Probability-in-Chessboard.py) (!!M Google)
dp[i][j][k]表示在棋盘(i, j)位置上走完k步数还留在棋盘上的走法总和(注意是走法，不是步数). dp[i][j][k] += dp[next_i][next_j][k-1] for next_i and next_j in bound.
- [Similar with 688. Knight Probability in Chessboard](Solutions/Google_Similar-with-688.Knight-Probability-in-Chessboard.py) (!!!M Google) <br>
dp.  dp[i][j][k] = from (i, j) the number of ways you to end up at the original coordinate with k steps.
dp[i][j][k] = dp[i - 1][j][k - 1] + dp[i][j - 1][k - 1] + dp[i + 1][j][k - 1] + dp[i][j + 1][k - 1]
- [0840. Magic Squares In Grid](Solutions/0840.Magic-Squares-In-Grid.py) (!!!M Google) <br>
Array. 找规律就可以了
- [0056. Merge Intervals](Solutions/0056.Merge-Intervals.py) (!!M) <br>
这种interval的题目首先都需要sort, 因为我们总不可能一会处理前面的，一会处理后面的区间。 Sort the intervals first. Loop over the intervals:
If the curr_interval start time is larger than the largest end time in res, then the interval cannot be merged. 
If cannot be merged, then res.append(curr_interval), else then update the new end time: res[-1][1] = max(res[-1][1], curr_interval_end). 
Merge interval的算法非常重要，后面的题经常用到！！！
- [0992. Subarrays with K Different Integers](Solutions/0992.Subarrays-with-K-Different-Integers.py) (!!H) <br>
exactly(K) = atMost(K) - atMost(K-1). Helper function is exactly the same as 340. Longest Substring with At Most K Distinct Characters
- [1218. Longest Arithmetic Subsequence of Given Difference](Solutions/1218.Longest-Arithmetic-Subsequence-of-Given-Difference.py) (!!!M Google) <br>
dp, similar with. solution 1: O(N^2), dp[i] = the LAS ended with arr[i]. dp[j] = dp[i] + 1 for i < j and arr[j] - arr[i] == diff. O(N) use hashmap, like two sum problem. dp[arr[j]] = dp[arr[j] - diff] + 1 if arr[j] - diff in dp else 1.
- [0351. Android Unlock Patterns](Solutions/0351.Android-Unlock-Patterns.py) (!!!M Google) <br>
backtrack: 跟普通的backtrack不同的是From a number in the keypad we can reach any other number, but can't reach the one's that have a number as obstacle in between. 
For example, for (1 to 3), the obstacle is 2. 所以在判断要不要把next_num作为下一个valid candidates的时候如果(curr_num, next_num) in cannot_pass那就不行。
- [1223. Dice Roll Simulation](Solutions/1223.Dice-Roll-Simulation.py) (!!!M Google) <br>
solution 1: backtrack - O(6^N) in worst case. 不需要传入curr_comb, 只需要last_num和the repeat time of last_num. solution 2: backtrack + memo - O(6n^2). 套backtrack + memo的模板即可
- [0818. Race Car](Solutions/0818.Race-Car.py) (!!H) <br>
层序遍历的bfs. 这个graph的nodes比较特殊，nodes是(curr_pos, curr_speed). strong pruning that is 100 times faster: 我们是有条件的回退，只有在超过了target的情况下我们才回退
- [0174. Dungeon Game](Solutions/0174.Dungeon-Game.py) (!!H Google) <br>
find the max of mininum_sum in all the paths.这题不能像1102.Path-With-Maximum-Minimum-Value那样用Dijkstra's (mnlogn)因为这题不是四个方向都能走的，也就是说选择了一个方向就不能回到原来的位置了，所以只能dp -O(mn). 假设我们能到达(m, n)房间，我们需要的最小血量是dp[m][n] = 1 if A[m][n] >= 0 else 1- A[m][n], 这是我们的base case.
那我们就知道了我们到达(m-1, n)房间所需的最小血量是dp[m-1][n] = 到达(m, n)房间所需要的血量减去在(m-1, n)房间的损耗，
即dp[m-1][n] =max(dp[m][n] - A[m-1][n], 1); 到达(m, n-1)房间所需的最小血量是dp[m][n-1] = max(dp[m][n] - A[m][n-1], 1).
所以我们是从终点倒着往起点推。
- [0428. Serialize and Deserialize N-ary Tree](Solutions/0428.Serialize-and-Deserialize-N-ary-Tree.py) (!!H Google) <br>
solution: level order bfs.  This is very similar with serialize and deserialze a binary tree. In binary tree, we know after visit left and right of a node, we can move to another node, but in Nary tree, we don't know when to finish visiting a node cuz there could be multiple children for a node. So we need to do  some trick to mark the end of a level.  The trick is, when we do bfs to serialze, we append "#" into a res when we switch from one parent to another parent. In deserialize, while res[idx] != "#" 就说明还要继续给curr_node添加child，而res[idx] == "#"意味着要换node append child了, idx += 1
- [0949. Largest Time for Given Digits](Solutions/0949.Largest-Time-for-Given-Digits.py) (!!M Google) <br>
backtrack. step 1: find all possible permutations - O(4!). step 2: update max_possible time that can be constructed from the permutations.
- [1219. Path with Maximum Gold](Solutions/1219.Path-with-Maximum-Gold.py) (!!M)<br>
尝试每一个pos出发backtrack所有可能的path比较哪一条path能得到最多的gold - O(4^N). 注意backtrack遍历得到的是每一条path的curr_sum, 而不是像普通dfs那样得遍历的是整个区域的. 对比这一题与200. Number of islands. 我们可以看到求path一定需要用backtrack. backtrack与dfs相比其实就是多了一步visited.remove(next_candidate). 这就导致dfs的时间复杂度是O(N), while backtrack的时间复杂度是O(4^N), where N is the number of cells in the matrix. 4 is the number of next_nodes in the for next_candidate in ...
- [0068. Text Justification](Solutions/0068.Text-Justification.py) (!!H Google) <br>
String manipulation. use curr_line = [] to record curr words in curr_line; use curr_width = 0 to record curr total number of chars in curr_line. Iterate the word in words, if too many words to fit in one line, we first justify that line and update res, then start over the curr_line = [] and curr_width = 0 for the next line. Lastly, we deal with the last line seperately.
- [0609. Two Sum - Less than or equal to target](Solutions/0609.Two-Sum-Less-than-or-equal-to-target.py) (!!E Lintcode) <br>
反向双指针：if nums[i] + nums[j] <= target: cnt += j - i		# 注意这里是 cnt += j - i 表示nums[i] 加上 (i 到 j之间的任何数)，一定也是小于等于target的
- [0951. Flip Equivalent Binary Trees](Solutions/0951.Flip-Equivalent-Binary-Trees.py) (!!!H Google) <br>
recursion - O(min(N1, N2))
- [0298. Binary Tree Longest Consecutive Sequence](Solutions/0298.Binary-Tree-Longest-Consecutive-Sequence.py) (!!M) <br> 
helper function returns (the LCS ended with root, without root)
- [1131. Maximum of Absolute Value Expression](Solutions/1131.Maximum-of-Absolute-Value-Expression.py) (M) <br>
根据正负符号分为4个situations. 对于每一个situation, 我们用121. Best time to buy stock problem: maintain 一个prev_min
- [1255. Maximum Score Words Formed by Letters](Solutions/1255.Maximum-Score-Words-Formed-by-Letters.py) (!!H Google) <br>
find all subsets, similar with 78. Subsets. O(26* 2^n), n = len(words)
- [1314. Matrix Block Sum](Solutions/1314.Matrix-Block-Sum.py) (!!M Google) <br>
prefix sum 2D version. similar with 304. Range Sum Query 2D - Immutable
- [0149. Max Points on a Line](Solutions/0149.Max-Points-on-a-Line.py) (H) <br>
y = kx + b, points on a line share the same slope k and same intercept b.
So we can use a dictionary to store the (k, b) as key and points pos as value.
- [0729. My Calendar I](Solutions/0729.My-Calendar-I.py) (！！M Google) <br>
Maitian a intervals list. The problem is to find the overlap of two intervals. We loop over the intervals. 
一个interval与另一个interval的位置关系就三种情况(1. 没有交集; 2. 一个包含了另一个; 3. 有交集但是没有谁能完全包含谁). 
这里我们只要遇到case 2 or case 3, then there is an overlap, return False
- [0731. My Calendar II](Solutions/0731.My-Calendar-II.py) (M) <br>
We maintain two interval lists: a calendar list and a overlap list. In book method, we first check if [start, end] is in an overlap,
if it is, then we return False directly.
If it's not, then we return True, before return true, we should update the calendar list and overlap list accordingly.
update calendar: just append [start, end] cuz we don't need the calendar be sorted.
update overlap: find where the overlap is by go through the calendar list, and update it.
- [0732. My Calendar III](Solutions/0732.My-Calendar-III.py) (H) <br>
Do do exactly the same as the airplane in the sky problem to count how many overlapping are there - O(N). Maintain a start_time list and end_time list and keep them sorted by using binary search each time we insert a time. Solution 2: we can use a segment tree, each query takes O(logn). Should know but don't need to implement.
- [1095. Find in Mountain Array](Solutions/1095.Find-in-Mountain-Array.py) (H) <br>
step 1: Binary find peak in the mountain - 852. Peak Index in a Mountain Array.
step 2: Binary find the target in strict increasing/left part.
step 3: Binary find the target in strict decreasing/right part.
- [1048. Longest String Chain](Solutions/1048.Longest-String-Chain.py) (!!M Google) <br>
dp = dict, key is word, val is the longest chain lens ended with word; prevWord = word[:i]+word[i+1:]; if prevWord in dp: dp[word] = max(dp[redesessor]+1)
- [0726. Number of Atoms](Solutions/0726.Number-of-Atoms.py) (!!H Google) <br>
Parenetheses. 与394.Decode String非常类似, 我们需要反向遍历，这样只要遇到upper case的ch就可以加到dictionary了
- [0659. Split Array into Consecutive Subsequences](Solutions/0659.Split-Array-into-Consecutive-Subsequences.py) (!!!M Google) <br>
这道题我们遍历nums的时候只要当前的num被前面的顺子需要，就把num连上去，顺子连得越长越好，这就是greedy所在，使用两个 HashMap，第一个 HashMap 用来建立某个数字和其出现次数之间的映射 freq，
第二个用来建立某个数字被前面顺子所需要的次数之间的映射 need。
- [1057.Campus-Bikes.py](Solutions/1057.Campus-Bikes.py) (!!M) <br>
brutal force solution O(MNlog(MN)): find the distance of all combinations, and sort them.
. bucket sort solution O(MN): find the distance of all combinations, and put them into bucket based on their distance. 
In this way, the distances are represented by idx, which were sort by nature. <br>
- [1066. Campus Bikes II](Solutions/1066.Campus-Bikes-II.py) (!!M Google) <br>
backtracking with memorization, 由于必须把assigned_bike set放入到state中，所以是指数级别的复杂度, solution 2: backtrack + Dijkstra's <br>
Extention: __Campus Bikes III (minimize max) - Dijkstra's__
- [0053. Maximum Subarray](Solutions/0053.Maximum-Subarray.py) (!!E) <br>
step 1: 构造前缀和pre_sum; 
step 2: the same as 127. Best time to buy and sell stock
- [1592. Rearrange Spaces Between Words](Solutions/1592.Rearrange-Spaces-Between-Words.py) (E Google) <br>
Easy heasy!
- [0222. Count Complete Tree Nodes](Solutions/0222.Count-Complete-Tree-Nodes.py) (!!M) <br>
solution 1: dfs to visit every node; solution 2: use the property of complete Tree: 通过比较left sub tree height and right sub tree height 可以之直接算出左边或者右边nodes的个数 - O(logN* logN). solution 3: similar with Check if value exists in level-order sorted complete binary tree: use gray code to enable binary search in the last level - O(logN* logN)
- [0420. Strong Password Checker](Solutions/0420.Strong-Password-Checker.py) (!!H Google) <br>
Greedy. 分三个区间讨论：1. n <= 5: return max(6 - n, missing_types), 用三个小Helper function to calculate three missing_types;2. 6 <= n <= 20: just need to return how many replacements are needed to avoid consecutive chars: number_of_replacements += num_of_consecutives // 3; 3. n > 20: step 1: calculate how many replacements are neededto avoid consecutive chars; step 2: calculate how many deletions can be used to save replacements - greedy.好难呀
- [0031. Next Permutation](Solutions/0031.Next-Permutation.py) (!!M) <br>
step 1: sweeping from right to left, find the first decreasing element nums[i]; Step 2: sweep from right to left, find the first element larger just than nums[i], then swap nums[i] and nums[j], then swap all the items starting from i+1
- [0378. Kth Smallest Element in a Sorted Matrix](Solutions/0378.Kth-Smallest-Element-in-a-Sorted-Matrix.py) (!!M) <br>
利用sorted matrix的性质，从左上角第一个元素开始，添加进heap，然后heap当然自动排序了，然后pop出最小的，然后把最小的那个数的右边和下边的元素分别入heap，这样可以保证每次pop出来的都是最小的。1. use a heap to store (num, (row, col)); 2. use a set to check if row + 1, col + 1 visited already before push into the heap; Solution 2: binary search 了解一下。<br>
- [0418. Sentence Screen Fitting](Solutions/0418.Sentence-Screen-Fitting.py) (!M Google) <br>
string. fit the sentence in line by line
- [1044. Longest Duplicate Substring](Solutions/1044.Longest-Duplicate-Substring.py) (H) <br>
step 1: find the lens of longest duplicated substring using binary search - 1062. Longest Repeating Substring;
step 2: use the longest lens to find the substring - 187. Repeated DNA Sequences
- [0638. Shopping Offers](Solutions/0638.Shopping-Offers.py) (!!M) <br>
solution 1: backtrack - 套用backtrack模板，backtrack加入的参数有(curr_bought, curr_cost).
backtrack结束条件是if all(curr_bought[i] >= needs[i] for i in range(len(needs))).
backtrack的剪枝很重要 - skip deals that exceed needs: if any(special[i] > needs[i] - curr_bought[i] for i in range(len(needs)))
O(2^M* L* N) where L is len(prices), M is how many specials are there, N is value of needs; solution 2: dfs + memorization
- [1237. Find Positive Integer Solution for a Given Equation](Solutions/1237.Find-Positive-Integer-Solution-for-a-Given-Equation.py) (E Google) <br>
反向双指针. 
- [0844. Backspace String Compare](Solutions/0844.Backspace-String-Compare.py) (!!!E) <br>
这种双指针处理比较双序列问题很常见。由于题目"#"可以删掉前面的ch, We can use a pointer traverse from __right to left__, and use a counter to count how many "#" we got so far. 一般要求用O(1) space解决。Google follow up: 加一个按键是类似caps lock，即按了之后所有的字母小写变大写，再按一下大写变小写。
思路：定义caps cnt，先扫一遍看多少个caps lock，比较s1.charAt(i) == s2.charAt(j) && caps1 == caps2
- [0224. Basic Calculator](Solutions/0224.Basic-Calculator.py) (!!H) <br>
if it's a digit, should use a while loop to add the num in case there are multiple digits, eg: 322 - 16; if it's a sign, then use 1 or -1 to represent it; if it's a (, then append the previous res and sign into the numStack and signStack, and initialize the sign and num for calculation inside the (); if it's a ), then pop the numStack and signStack and update res.
- [0406. Queue Reconstruction by Height](Solutions/0406.Queue-Reconstruction-by-Height.py) (!!M) <br>
Greedy: Since short people will not disturb/affect the relative order of taller people so we can start from tallest guy(s). Then for each person [i,j], we insert it into res based on j.
- [0907. Sum of Subarray Minimums](Solutions/0907.Sum-of-Subarray-Minimums.py) (!!M) <br>
我们其实关心的是以某个数字结尾时的子数组最小值之和，
可以用一个一维数组 dp，其中 dp[i] 表示以数字 A[i] 结尾的所有子数组最小值之和，
遍历A, 更新 dp[i] = dp[idx] + A[i] * (i-idx)，其中idx是往左寻找第一个比当前A[i]小的数的idx，
最终的结果 res 就是将 dp 数组累加起来即可.
为了更快速得到往左寻找第一个比当前A[i]小的数的 idx, 我们可以提前算好存起来，怎样算：monostack
- [1145. Binary Tree Coloring Game](Solutions/1145.Binary-Tree-Coloring-Game.py) (M) <br>
The best move y must be immediately adjacent to x, since it locks out that subtree. check the 3 nodes that are adjacent to node x, find the number of nodes each subtree has.
Then check if palcing ynode at the 3 nodes adjacent to x will end up with more subtree nodes for y.
- [0057. Insert Interval](Solutions/0057.Insert-Interval.py) (!!H Google) <br>
Solution 1: Append the new interval to the intervals, and then do the merge interval problem. O(nlogn). Solution 2: add the interval as we run. If there is overlap, we update the new interval. 画个图会好理解很多。
- [0304. Range Sum Query 2D - Immutable](Solutions/0304.Range-Sum-Query-2D-Immutable.py) (!!M) <br>
a 2D version prefix sum. O(1) for query.
- [0317. Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (!!H) <br>
Use reachable_cnt[i][j] to record how many times a 0 grid has been reached and use dist[][] to record the sum of distance from all 1 grids to this 0 grid. Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS. in the bfs, we do level bfs and update the reachable_cnt matrix and dist matrix. 遇到obstacle不放进q就可以了. each bfs, all position are visited, so O(MNk) where k is how many building are there or how many bfs are triggered. Finnaly return the min of dist[i][j] if reachable_cnt[i][j] = total number of buildings. Strong Prune: if if starting from building (i, j), can reach all other building? if not, that means at least one building is isolated and can not be reached, then return -1 directly: in each BFS we use reachableBuildings to count how many 1s we reached. If reachableBuldings != totalBuildings - 1 then we know not all 1s are connected are we can return -1 immediately, which greatly improved speed.
- [0306. Additive Number](Solutions/0306.Additive-Number.py) (!!M) <br>
套backtrack模板即可，backtrack传入的参数有(curr_idx, prev_num, curr_num, curr_cnt). 结束条件是if curr_idx == len(s) - 1 and curr_cnt > 2
- [0424. Longest Repeating Character Replacement](Solutions/0424.Longest-Repeating-Character-Replacement.py) (!!M) <br>
340 的变形题 this problem is to find the max_lens of substring so that (length of substring - number of times of the maximum occurring character in the substring) is at most K.
- [0393. UTF-8 Validation](Solutions/0393.UTF-8-Validation.py) (M) <br>
- [0323. Number of Connected Components in an Undirected Graph](Solutions/0323.Number-of-Connected-Components-in-an-Undirected-Graph.py) (M) <br>
Union Find: With path compression, it takes ~O(1) to find and union. So the time complexity for Union Find is O(V+E).
O(V) comes from constructing the graph, O(E) comes from connecting each edge
- [1383. Maximum Performance of a Team](Solutions/1383.Maximum-Performance-of-a-Team.py) (!!!H) <br>
将workers按照efficiency降序排序，这样我们只需要从第k个worker开始，
取他的efficiency去乘以(他之前所有workers选k个能组成的最大的speed)，
这个因为他的efficiency一定是这k个worker里面最小的。
可以保持一个k size的heap来存(他之前所有workers), 如果size>k就把min_speed的worker踢出去
- [0857. Minimum Cost to Hire K Workers](Solutions/0857.Minimum-Cost-to-Hire-K-Workers.py) (!!!H Google) <br>
generally, a team cost is ∑wi = w/q * ∑qi where w/q is the maximum wage/quality ratio in that team. 我们发现与1383. Maximum Performance of a Team是类似的。
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M) <br>
dp[i][j]=以(i, j)为右下角的最大正方形的边长; dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j]=1 
- [0265. Paint House II](Solutions/0265.Paint-House-II.py) (!!H) <br> 
dp[i][j]=minimum cost to paint the ith house the be color j; dp[i][j] = dp(min in the (i-1)th row) + costs[i][j]. In order to find dp(min in the (i-1)th row), we can find the position for the 1st and 2nd min in the i-1 th row first, then in the ith row calcuation, if j==1st_min_pos, then dp[i][j]=2nd_min + costs[i][j], else dp[i][j]=1st_min + costs[i][j]
- [0198. House Robber](Solutions/0198.House-Robber.py) (E) <br>
f[i]=the max profit when reaching ith house; f[i] = max(rob ith = f[i-2]+nums[i], not rob ith = f[i-1]) <br>
空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]
- [0213. House Robber II](Solutions/0213.House-Robber-II.py) (!!M) <br>
房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：1. 房子1没偷：问题变成了对房子2:N做House robber I的问题; 2. 房子N没偷：问题变成了对房子1:N-1做House robber I的问题
- [0337. House Robber III](Solutions/0337.House-Robber-III.py) (!!M) <br>
树状的house.递归： def with_without_rob(self, root): return a tuple, the 1st element in the tuple is the max profift with_rob_root， the 2nd element in the tuple is the max profit without_rob_root. 递归公式：with_rob_root = root.val + without_rob_left + without_rob_right; without_rob_root = max(with_rob_left, without_rob_left) + max(with_rob_right, without_rob_right)
- [1514. Path with Maximum Probability](Solutions/1514.Path-with-Maximum-Probability.py) (!!M) <br>
把probability换成log表示就变第一种情况最大/最小 sum of the path
- [0211. Add and Search Word - Data structure design](Solutions/0211.Add-and-Search-Word-Data-structure-design.py) (!!M) <br>
addWord mehtod is the same as 208 insert method. But search mehtod is a little different than search method in 208, cuz "." is a wildcard that can represent any char. So we use a queue to store (currNode, idx), then append layer by layer.
- [1041. Robot Bounded In Circle](Solutions/1041.Robot-Bounded-In-Circle.py) (!!M) <br>
The robot stays in the circle if (looking at the final vector!!!), it changes direction (ie. doesn't stay pointing north), or it moves 0
- [0346. Moving Average from Data Stream](Solutions/0346.Moving-Average-from-Data-Stream.cs) (!!E Google) <br>
In C#, Queue class is by default a deque, with two methods: 1. enqueue, meaning push to the back of the queue; 2. dequeue, meaning pop from the front of the queue. They are all O(1).
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](Solutions/1031.Maximum-Sum-of-Two-Non-Overlapping-Subarrays.py) (!!!M Google) <br>
这一题是把提前计算好的思想运用到了极致。
Step 1: 提前计算好prefix_sum and suffix_sum;
Step 2: using the prefix_sum and suffix_sum, 提前计算好 the prefix_max_L, where prefix_max_L[i] = the max subarray sum with window size L before i, 
and do the same for suffix_max_L;
Step 3: travel the pre_sum and update M-long subarray sum and max_sum using the pre-calulated prefix_max_L and suffix_max_L.
Solution 2: DP可以做到O(1) space. 具体做法与下一题689类似
- [1312. Minimum Insertion Steps to Make a String Palindrome](Solutions/1312.Minimum-Insertion-Steps-to-Make-a-String-Palindrome.py) (!!H Google) <br>
dp 1143.Longest Common- Subsequence. 题目其实是求 n - (the longest palindromic subsequence in s); 也就是 to find the longest common subsequence between s and s[::-1]. which is same as 1143.Longest Common- Subsequence.
- [0157. Read N Characters Given Read4](Solutions/0157.Read-N-Characters-Given-Read4.py) (E) <br>
step 1: read file to buf4; step 2: write buf4 into buf
- [0158. Read N Characters Given Read4 II - Call multiple times](Solutions/0158.Read-N-Characters-Given-Read4-II-Call-multiple-times.py) (!!H Google) <br>
Get data from read4 and store it in a queue. When read data, transfer data from queue to buf.
- [0769. Max Chunks To Make Sorted](Solutions/0769.Max-Chunks-To-Make-Sorted.py) (!!M) <br>
Iterate the array, if the max(A[0] ~ A[i]) = i, then we can cut it at this index.,
so that it the chunk ended with i. - just some game about number.
- [0253. Meeting Rooms II](Solutions/0253.Meeting-Rooms-II.py) (!!M) <br>
solution 1: 扫描线；minimum meeting rooms required could be understood us maximum meeting rooms in use
Then this problem is exaclty the same as the lintcode 0391. Number of Airplanes in the Sky <br> solution 2: 先把interval进行sort: intervals.sort(key = lambda x: (x[0], x[1])), 然后以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间
- [1170. Compare Strings by Frequency of the Smallest Character](Solutions/1170.Compare-Strings-by-Frequency-of-the-Smallest-Character.py) (E Google) <br>
hashmap. step 1: calculate the f(q) for each q in queries f_q, and f(w) for each w in words f_w. step 2: sort the f_w. step 3: ieterate queries and do binary search in f_w to update res.   
- [0362. Design Hit Counter](Solutions/0362.Design-Hit-Counter.py) (!!M) <br>
很简单，用一个queue存hit的timestamp就可以了, 这种拿分题一定要细心，这里容易漏掉self.q是否为空的判断，导致扣分，要养成好习惯，用q[0]之前一定要判断q是否为空。Follow up:
What if the number of hits per second could be very large? Does your design scale?
这里不是用deque吗？deque里面默认是每一个时间戳hit了一次，如果需要记录每秒钟有几次hit，我们需要用到dictionary, 但是同时有需要deque一样的有序，
所以自然而然想到OrderedDict. 这样可以保证最多使用O(300)的空间, 还是要熟悉OrderedDict的方法的。
OrderedDict是deque的增强版，这一点在LRU那题中已经体现。
当然这一题也可以在q里面存(timestamp, how many hits are there in this timestamp)
- [1326. Minimum Number of Taps to Open to Water a Garden](Solutions/1326.Minimum-Number-of-Taps-to-Open-to-Water-a-Garden.py) (!!H Twitter) <br>
We build a list reachable to store the max range it can be watered from each index. reachable[idx] = start from idx, where we can reach
Then it becomes Jump Game II, where we want to find the minimum steps to jump from 0 to n.
每跳一步就相当于开一个水龙头. 所以我们可以看到45. Jump Game II, 1024. Video Stitching和这题其实是一个题。
- [0721. Accounts Merge](Solutions/0721.Accounts-Merge.py) (M) <br>
union find: if email under the same name, then connect emails, or if email under name_1 equals to email under name_2, connect emails.
In this way, we build a graph, then we map each disjoint_component into one name.
Step 1: use a dictionary to store email_to_name map. Step 2: iterate the edges to connect them. Step 3: use the email_to_name map and the graph to generage a new list where each name corresponding to a disjoint_component. 如何从已经连接好的uf图中得到连在一起的nodes没有想到，其实就是建立root_email to emails dictionary as we go over uf.father.
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (!!M) <br>
node是某个单词，_get_next(curr_node)是这一题的难点，构造一个dictionary, key is all possible combination of the word, value is the word, 这样就可以快速查询了。Time complexity: O(NL^2), where N is the number of words in word_set, and L is avg length of words
- [0126. Word Ladder II](Solutions/0126.Word-Ladder-II.py) (!!H) 打印/输出所有满足条件的路径必用backtrack. 
Step 1. 从end_word到start_word做bfs，记录每一个节点到end节点的距离，存入hashmap中 eg: distance["dog"] = 2 <br>
Step 2. 从start到end做backtrack，每走一步都必须确保离end的distance越来越近(if distance[next_word] >= distance[curr_word]: continue)
想想210题的Google follow up.
- [0002. Add Two Numbers](Solutions/0002.Add-Two-Numbers.py) (!!M) <br>
本题的考点是关于如何新建一个linked list, 要用someNode.next = ListNode(someVal), 而不是简单的修改value; 还考察了是否细心, 最后很容易漏掉carryBit != 0的判断"
- [0827. Making A Large Island](Solutions/0827.Making-A-Large-Island.py) (!!H) <br>
solution 1: dfs. step 1: get all the islands and store all their positions. step 2: sweep the matrix and change each WATER to LAND one by one to update max_size.  solution 2: UnionFind O(MN) - 要注意每次将0变1都会改变uf的图，所以要提前用一个temp_father=uf.father来保存father的信息
- [1091. Shortest Path in Binary Matrix](Solutions/1091.Shortest-Path-in-Binary-Matrix.py) (!!M) <br>
solution 1: 带层序遍历的bfs, if grid[next_x][next_y] == BLOCK 那就continue掉不放进q; solution 2: bi-directional bfs; solution 3: A*, __A* is better than bfs in finding the shorted path from source node to end node.__ 在A* 算法中，需要两个数据结构：**I. A heapq; II. A dictionary.** I. heapq stores (1. curr_heuristic_estimation of min # of steps from source to target if 经过currNode; 2. curr_steps from source to curr_node; 3. curr_pos)), where curr_heuristic_estimation = curr_steps + heuristic estimation of minimum distance from curr_pos to desitination. II. dictionary stores the the position ---> steps taken from source to the position.
- [0968. Binary Tree Cameras](Solutions/0968.Binary-Tree-Cameras.py) (!!H) <br> 
helper function returns minimum number of cameras needed to cover all the node's children with (node not covered, node covered: 1. with a camera on node, 2. without a camera on node)
- [0706. Design HashMap](Solutions/0706.Design-HashMap.py) (!!M) <br>
Resolve hash collision: approach 1: Seperate chaining; approach 2: Open addressing.  We implement seperate chaining: we use an arr of linked list to sore the keys: self.hashmap = [ListNode(-1, -1) for _ in range(self.SIZE)], store linked list head in the arr,ListNode(-1, -1)是一个dummy node, 方便后续操作. Time complexity for seach/put/get is O(n/m) on average, where m is the talbe size, n is number of keys in the table.
- [0044. Wildcard Matching](Solutions/0044.Wildcard-Matching.py) (H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配； 画个图会很明了，详见九章算法动态规划双序列型DP。
情况一：B[j-1]不是"星": if (B[j-1]="?" or A[i-1]=B[j-1]): f[i][j] = f[i-1][j-1]  <br>
情况二：B[j-1]是"星"：可以让"星"表示0个字符，那就让A[0..i)去和B[0..j-1)匹配： f[i][j] = f[i][j-1]；也可以让"星"表示字符，A[i-1]肯定是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j]
- [0871. Minimum Number of Refueling Stops](Solutions/0871.Minimum-Number-of-Refueling-Stops.py) (!!H Google) <br>
像这种求极值的问题，十有八九要用动态规划 Dynamic Programming 来做，
但是这道题的 dp 定义式并不是直接来定义需要的最少加油站的个数，那样定义的话不太好推导出状态转移方程。
正确的定义应该是根据加油次数能到达的最远距离，我们就用一个一维的 dp 数组，其中 dp[i] 表示加了i次油能到达的最远距离，
dp[i+1] = max(dp[i] + stations[j][1] among all the station that dp[i] can reach) - O(n^2);
return the first i where dp[i] >= target. 
solution 2: heapq - O(nlogn)
heapq stores the fuel at the station. 这题的关键是不要考虑到达的那个station的位置，
我们永远只需要考虑从0出发，中途能加多少油，加的油越多跑得越远. 维护一个possible_coverage变量表示能跑多远. 这个题目用hq的方式跟Dikstra's有点像，都是要贪心地pop出最优解！
- [0076. Minimum Window Substring](Solutions/0076.Minimum-Window-Substring.py) (!!H) <br>
维护一个sourceFreqDict, 用来记录i->j中的char的频率，套用模板时满足的条件是sourceFreqDict all included in targetFreqDict; 更新j: sourceDict[s[j]] += 1, 更新i: sourceDict[s[i]] -= 1.  time complexity is O(MN). solution 2: O(N), instead of using self.allIncluded(sourceDict, targetDict) to check matched or not,  we use a int missing to keep track of how many chars are still needed in order to match, this reduce the time from O(M) to O(1). also, instead of using s[i:j] everytime when we renew res, we use start, end to renew the idx, which reduce time from O(N) to O(1)
- [0152. Maximum Product Subarray](Solutions/0152.Maximum-Product-Subarray.py) (!!M) <br>
最大值问题。maxDP[i]表示以i为结尾的subarray的最大的正数，minDP[i]表示以i为结尾的subarray的最小负数. 根据nums[i]的正负, 更新maxDP[i]和minDP[i]
- [0417. Pacific Atlantic Water Flow](Solutions/0417.Pacific-Atlantic-Water-Flow.py) (!!M) <br>
题目的意思是外围一圈的地方是water进来的地方，左上角的外围是pacific ocean water进来的地方，右下角的外围是atlantic ocean water进来的地方。
step 1: 从左上角外围的每个点出发做dfs, next_pos is a valid candidate if matrix[curr_pos] <= matrix[next_pos], 
如果能visited就存起来表示pacific ocean water可以到达这个pos；
step 2: 同样的方法记录atlantic ocean water可以达到的pos.  然后用2nd pass 来找到哪些点是两个ocean都能到达的。
- [0723. Candy Crush](Solutions/0723.Candy-Crush.py) (!!M Google) <br>
Recurssion. step 1: check horizontal and vertical crush and changed the board[i][j] that needs to be crushed to negative.
step 2: do gravity to modify the board.
step 3: recurssively modify the board until is there is crush needed. O((MN)^2)
- [0124. Binary Tree Maximum Path Sum](Solutions/0124.Binary-Tree-Maximum-Path-Sum.py) (!!H) <br>
题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter. 方法是定义一个self.maxSum在helper函数中去打擂台。helper 函数return the maxPathSum for tree ended with root: return max(left of root, right of root) + root.val; 打擂台: self.maxSum = max(self.maxSum, leftmax + rightMax + root.val). 注意打擂台的self.maxSum和非打擂台的变量和helper function return的变量是不一样的，这是本题的难点。
- [0459. Repeated Substring Pattern](Solutions/0459.Repeated-Substring-Pattern.py) (E) <br>
step 1: find all possible divisible lens - O(n^0.5); step 2: try each possible divisible lens to see is it's a valid divide - O(n^1.5).
- [0535. Encode and Decode TinyURL](Solutions/0535.Encode-and-Decode-TinyURL.py) (M Google) <br>
Hashmap. Convert long url to short url via hashing. Look up long url from short url in hash table. # hash(str) returns the hash_code for the str
- [1162. As Far from Land as Possible](Solutions/1162.As-Far-from-Land-as-Possible.py) (!!M) <br>
The max distance is the max steps to change all WATER to LAND. So we firslty put all land in a q, than do bfs layer by layer to change WATER to LAND in-place - O(MN).  solution 2: DP same as 542. 01 matrix




























































