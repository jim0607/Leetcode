# [Data Structure](/Data-Structure.py)
## [Hashmap/Dictionary](/Data-Structure.py) 
- [0146. LRU Cache](Solutions/0146.LRU-Cache.py) (!!!M youtubed) <br>
use a double linked list and a dictionary; Double linkedlist: newest node append to tail, eldest node remove from head, so that the operation is O(1); Hashmap: key is key, value is the corresponding double linkedlist node
- [0460. LFU Cache](Solutions/0460.LFU-Cache.py) (!!!H Google) <br>
其实是在LRU的基础上加了一个frequency的要求。Use a dictionary to store (key, freq) pair. Use another dicitonary to store (freq, list of keys) pair, where list of keys could be OrderedDict like LRU to enable O(1) operations. Use a self.min_freq to store the min_freq. Follow up 变形题snapchat：在一个data stream 中find top K most frequent number用LFU来解，也可以用heapq O(Nlogk) or quick select O(N).
- [0432. All O(1) Data Structure](Solutions/0432.All-O`one-Data-Structure.py) (H) <br>
use a Double Linked list, a hashmap to store (key, cnt) pair, use a hashmap to store (cnt, node) pair.  node is a DLL node, there is a node.key_set = set() which stores all the keys with that cnt.  The rest is to update the dll, the two hashmaps in each method call. similar with LRU.
- [1153. String Transforms Into Another String](Solutions/1153.String-Transforms-Into-Another-String.py) (!!H Google) <br>
Map each character in str1 to what it needs to be in str2. If any of these mappings collide (e.g. str1 = "aa", str2 = "bc", "a" needs to become both "b" and "c"),
we immediately return False since the transformation is impossible.
- [0895. Maximum Frequency Stack](Solutions/0895.Maximum-Frequency-Stack.py) (!!H) <br>
O(1) solution: self.freq = collections.defaultdict(int), # key is num, val is freq of the num; self.mapping = collections.defaultdict(list), key is freq, val is a stack of num of that freq; self.max_freq = 0; we update the 3 global variables in push method and pop method.
- [0166. Fraction to Recurring Decimal](Solutions/0166.Fraction-to-Recurring-Decimal.py) (!!M Facebook) <br>
令人虎躯一震的好题，模拟除法的过程很有意思，Idea is to put every remainder into the hash table as a key, and the position where the remainder appears as val.
如果remainder重复出现了，就说明找到循环的部分了，循环的部分就是从dict[remainder]到最后的部分
- [0957. Prison Cells After N Days](Solutions/0957.Prison-Cells-After-N-Days.py) (M) <br>
找重复出现的pattern就可以了
- [0953. Verifying an Alien Dictionary](Solutions/0953.Verifying-an-Alien-Dictionary.py) (!!M Facebook) <br>
hashmap存 the position of ch in the list. we traverse the words list and check adjacent word.
- [0149. Max Points on a Line](Solutions/0149.Max-Points-on-a-Line.py) (H) <br>
y = kx + b, points on a line share the same slope k and same intercept b.
So we can use a dictionary to store the (k, b) as key and points pos as value.
- [1152. Analyze User Website Visit Pattern](Solutions/1152.Analyze-User-Website-Visit-Pattern.py) (!!M) <br>
use a dictionary to store user_to_website, and then for all the possible 3-sequences, we use a counter to record how many times they appeared. Choose the max_cnt one and return.
- [0562. Longest Line of Consecutive One in Matrix](Solutions/0562.Longest-Line-of-Consecutive-One-in-Matrix.py) (!!!M Google) <br>
hashset. each time we meet a 1, we explore horizontally, vertically and diagonally.
Use set to store the nodes that were horizontally visited, vertically visited and diagonally visited. 
- [0299. Bulls and Cows](Solutions/0299.Bulls-and-Cows.py) (!!!M Google) <br>
use a digit_to_cnt hashmap for digit. one pass to update A_cnt, another pass to update B_cnt.
- [0049. Group Anagrams](Solutions/0049.Group-Anagrams.py) (!!M) <br>
dictionary: key is a tuple keeping track of the cnt of all 26 letters, val is the word list corresponding to the tuple
- [0249. Group Shifted Strings](Solutions/0249.Group-Shifted-Strings.py) (!!M Google) <br>
hashmap. similar with 49. Group Anagrams.
the key of the hashmap is a tuple of the list [ord(ch)-ord(first_ch) for ch in each string]
- [0535. Encode and Decode TinyURL](Solutions/0535.Encode-and-Decode-TinyURL.py) (M Google) <br>
Hashmap. Convert long url to short url via hashing. Look up long url from short url in hash table. # hash(str) returns the hash_code for the str
- [1170. Compare Strings by Frequency of the Smallest Character](Solutions/1170.Compare-Strings-by-Frequency-of-the-Smallest-Character.py) (E Google) <br>
hashmap. step 1: calculate the f(q) for each q in queries f_q, and f(w) for each w in words f_w. step 2: sort the f_w. step 3: ieterate queries and do binary search in f_w to update res.   
- [1146. Snapshot Array](Solutions/1146.Snapshot-Array.py) (!!!M Google) <br>
solution 1: sparse array. Since 题目说了 initially, each element equals 0.
we treated it as a sparse matrix: use a dictionary to store only the non-zero values.
- [1400. Construct K Palindrome Strings](Solutions/1400.Construct-K-Palindrome-Strings.py) (!!M) <br>
Since we don't need to find each pandidromes, we don't need to use backtrack. 
algoritm: we can form k palindromes if there are k or less than k chars that has odd cnt.
- [0036. Valid Sudoku](Solutions/0036.Valid-Sudoku.py) (M) <br>
use a row_dict to record each row, a col_dict to record each col; a block_dict to record each 3x3 block. block_id is (row // 3, col // 3)
- [0811. Subdomain Visit Count](Solutions/0811.Subdomain-Visit-Count.py) (E) <br>
用一个hashmap存sub-domains --> cnt. 剩下的就是string processing了
- [1629. Slowest Key](Solutions/1629.Slowest-Key.py) (E) <br>
maitain 一个max_duration, 遍历string去更新就可以了
- [1483. Kth Ancestor of a Tree Node](Solutions/1483.Kth-Ancestor-of-a-Tree-Node.py) (H) <br>
just memo it. dfs + binary search, or binary lifting can realize O(logk) time for getKthAncester





## [Stack and Queue](/Data-Structure.py)
- [0232. Implement Queue using Stacks](Solutions/0232.Implement-Queue-using-Stacks.py) (E) <br>
use two stack, 要学会写raise IndexError("queue is empty") 的语句
- [0225. Implement Stack using Queues](Solutions/0225.Implement-Stack-using-Queues.py) (E) <br>
use two deques; 要学会抛出error: in pop function, if the stack is empty then raise IndexError("stack is empty");
也可以用一个list实现，每次push进去的时候，把元素插入到最前面即可，与两个queue相比，时间复杂度也还是O(N)
- [0155. Min Stack](Solutions/0155.Min-Stack.py) (!!E) <br>
use two stacks, a stack is to store all items, a minStack to store min items. If a num is less than minStack[-1] then we should append to minStack.
- [0716. Max Stack](Solutions/0716.Max-Stack.py) (E) <br>
Solutino 1: just use one list. Since we have to implement popMax method, we have to find the maxItem pos in the stack, it takes O(N).  Solution 2: by using double linked list and heapq, we can realize O(logN) for push, pop and popMax. Use a doubly linkedlist for popMax.
- [0346. Moving Average from Data Stream](Solutions/0346.Moving-Average-from-Data-Stream.cs) (!!E Google) <br>
In C#, Queue class is by default a deque, with two methods: 1. enqueue, meaning push to the back of the queue; 2. dequeue, meaning pop from the front of the queue. They are all O(1).
- [1086. High Five](Solutions/1086.High-Five.py) (E) <br>
we can use heapq, but we can also just sort.
- [0933. Number of Recent Calls](Solutions/0933.Number-of-Recent-Calls.py) (E) <br>
use a queue so that we can remove the calls that happens long time ago.
- [0946. Validate Stack Sequences](Solutions/0946.Validate-Stack-Sequences.py) (!!!M Google) <br>
需要一个 __辅助栈st__ 来模拟push和pop的过程，用一个指针在popped list里面跑，如果popped[i]==st[-1]那就一直pop, 最后判断st能不能pop为空
- [0735. Asteroid Collision](Solutions/0735.Asteroid-Collision.py) (M) <br>
stack store the number after collision as we iterate the list
- [0900. RLE Iterator](Solutions/0900.RLE-Iterator.py) (!!!M Google) <br>
stack. one stack store cnt, one stack store num
- [0157. Read N Characters Given Read4](Solutions/0157.Read-N-Characters-Given-Read4.py) (E) <br>
step 1: read file to buf4; step 2: write buf4 into buf
- [0158. Read N Characters Given Read4 II - Call multiple times](Solutions/0158.Read-N-Characters-Given-Read4-II-Call-multiple-times.py) (!!H Google) <br>
Get data from read4 and store it in a queue. When read data, transfer data from queue to buf.




### [Parentheses](/)
- [1047. Remove All Adjacent Duplicates In String](Solutions/1047.Remove-All-Adjacent-Duplicates-In-String.py) (!!E) <br>
use a st to store 左边等待消掉的chars. loop the string s, if s[i] == st[-1], then pop. else append.
- [1209. Remove All Adjacent Duplicates in String II](Solutions/1209.Remove-All-Adjacent-Duplicates-in-String-II.py) (M) <br>
use a st to store 左边等待消掉的k-1 个chars. loop the string s.
if s[i] == st最上面k-1个char, then pop all k-1 个 char. 
To make it more efficient, use a pair to store the value and the count of each character.
- [0020. Valid Parentheses](Solutions/0020.Valid-Parentheses.py) (!!E) <br>
不能用简单的用三个counter, 会过不了这种情况: "([)]".
这题的题眼是a sub-expression of a valid expression should also be a valid expression. 所以用stack. parentheses的题目一般都可以用一个st来存左括号！！！
- [0678. Valid Parenthesis String](Solutions/0678.Valid-Parenthesis-String.py) (!!M)  <br>
注意这题不能像20题那样，因为例子"(* )(", 因为出现在()里面的"* "也救不了后面(需要匹配的). 正解Greedy: the whole idea is to check if "(" could be paired. Maintain two variables: cmin and cmax. cmin is the minimum number of "(" that MUST be paired later.
cmax is the maximum number of "(" that COULD possibly be paired later.
After interate the while s, if cmin == 0 then return True.
- [0022. Generate Parentheses](Solutions/0022.Generate-Parentheses.py) (!!M)  <br>
Very similar with permutation problem. if leftCnt == n and rightCnt == n: self.res.append(curr) return; if leftCnt < rightCnt: return  # 这个判断尤为关键！
- [0301. Remove Invalid Parentheses](Solutions/0301.Remove-Invalid-Parentheses.py) (H)  <br>
这题只能brutal force. solution: dfs 解法跟22. Generate parentheses是一样的，给你这么多括号，去生成所有的valid parentheses, 然后取其中最长的valid parentheses就可以了；
只能暴力generate出所有的valid parenthsis，每个括号都有可能加或不加进去，所以是O(2^N).
- [0032. Longest Valid Parentheses](Solutions/0032.Longest-Valid-Parentheses.py) (H)  <br>
solution 1: stack.  use a stack to store the idx, maintain a start idx to record the start idx of a valid parentheses; solution 2: dp; solution 3: greedy: O(N) O(1): 正向扫一遍，反向扫一遍, 真TM niubi呀
- [0921. Minimum Add to Make Parentheses Valid](Solutions/0921.Minimum-Add-to-Make-Parentheses-Valid.py) (!!M)  <br>
solution 1: use a st to store the "(". parentheses的题目一般都可以用一个st来存左括号！！！ solution 2: 简化一下，就用left_cnt代替stack
- [1249. Minimum Remove to Make Valid Parentheses](Solutions/1249.Minimum-Remove-to-Make-Valid-Parentheses.py) (M)  <br>
solution 1: use a st to store "(". parentheses的题目一般都可以用一个st来存左括号！！！ solution 2: 借鉴32. Longest Valid Parentheses的做法：first sweep left to right, and store the ")" that should be deleted, eg: "())", the last ")" should be deleted; then sweep right to left, and store "(" that should be deleted, eg: eg: "(()", the first "(" should be deleted;  lastly delete the prarentheses that should be deleted.
- [0856. Score of Parentheses](Solutions/0856.Score-of-Parentheses.py) (!!M)  <br>
solution 1: use a ch_st to store left parentheses. use num_st to stores res, num_st初始化一个0进去垫底。
if ch == "(": num_st.append(0); else: 弹出top of num_st 并更新 num_st[-1].
通过比较ch与prev_ch来判断是乘以2还是加上1. solution 2: 题目说the string is balanced, so we don't need a ch_st.
- [0150. Evaluate Reverse Polish Notation](Solutions/0150.Evaluate-Reverse-Polish-Notation.py) (!!M) <br>
stack存num就可以了
- [0224. Basic Calculator](Solutions/0224.Basic-Calculator.py) (!!H) <br>
if it's a digit, should use a while loop to add the num in case there are multiple digits, eg: 322 - 16; if it's a sign, then use 1 or -1 to represent it; if it's a (, then append the previous res and sign into the numStack and signStack, and initialize the sign and num for calculation inside the (); if it's a ), then pop the numStack and signStack and update res.
- [0227. Basic Calculator II](Solutions/0227.Basic-Calculator-II.py) (!!M) <br>
用一个opt_st存所有的operator, 一个num_st存所有的num. 1. 如果ch.isdigit()就while loop得到num, 紧接着判断这个num前面的operator是不是"* /", 如果是就不需要等，可以马上计算。 2. 如果not ch.isdigit()那ch就是operator, 就把operator放进opt_st里。
这样处理之后到最后opt_st里面装的全是"+-", 我们要左往右计算最后的res.
- [0772. Basic Calculator III](Solutions/0772.Basic-Calculator-III.py) (!!H) <br>
这道题是基本计算器系列的第三道，前两道分别为 Basic Calculator 和 Basic Calculator II，
区别是，第一道只有加减法跟括号，第二道只有加减乘除法，而这第三道既有加减乘除法又有括号运算。
但是好就好在我们可以将括号里的内容当作一个整体调用递归函数来处理。而其他部分，就跟第二道一模一样了。
--------------640. Solve the Equation-----------
- [1096. Brace Expansion II](Solutions/1096.Brace-Expansion-II.py) (!!H) <br>
solution: Use stack to store calculated results.  Maintain two lists: 1. the previous list before ","; 2. the current list that is still growing. 有点难，没弄明白
- [0071. Simplify Path](Solutions/0071.Simplify-Path.py) (!!M) <br>
stack保存string, 处理stack的问题往往需要提前split the path by ("/"): path = path.split("/"), 这个很重要，一般处理path都需要提前split一下
- [0388. Longest Absolute File Path](Solutions/0388.Longest-Absolute-File-Path.py) (!!M) <br>
solution 1: use a hashmap to store the (depth, lens) pair. firstly, find the depth, 
secondly, update the map[depth]: map[depth] = map[depth - 1] + len(name) - depth.  This is more of a dp way.  solution 2: stack存the lens of the dir or file names, everytime we append a dir of file name into the stack, we need to go back to the correct depth where it belongs.
- [0636. Exclusive Time of Functions](Solutions/0636.Exclusive-Time-of-Functions.py) (!!M) <br>
use a stack to store the id of start funciton, and a prev_time to keep track of the prev_time.
if type is "start", then we should update the res[st[-1]], and st.append(id), and update pre_time;
if type is "start", then we should update the res[st[-1]], and st.pop(), and update pre_time.
- [1021. Remove Outermost Parentheses](Solutions/1021.Remove-Outermost-Parentheses.py) (E Google) <br>
parentheses. solution 1: stack; solution 2: use a cnt for "("
- [0682. Baseball Game](Solutions/0682.Baseball-Game.py) (E Google) <br>
calculator. 
- [0394. Decode String](Solutions/0394.Decode-String.py) (!!M Google) <br>
定义一个numStack, 一个strStack 存nums和parenthesis. if it's a digit, should use a while loop to add the num in case there are multiple digits; if it's a ch, then put it into strStack; if it's a [, then put the num in numStack and re-initialize the tempNum and tempStr for calculation inside the []; if it's a ], then pop the resStack and signStack and update res.
- [0726. Number of Atoms](Solutions/0726.Number-of-Atoms.py) (!!H Google) <br>
Parenetheses. 与394.Decode String非常类似, 我们需要反向遍历，这样只要遇到upper case的ch就可以加到dictionary了
- [1612. Check If Two Expression Trees are Equivalent](Solutions/1612.Check-If-Two-Expression-Trees-are-Equivalent.py) (M) <br>
warm up for __binary expression tree__ problem.
- [1628. Design an Expression Tree With Evaluate Function](Solutions/1628.Design-an-Expression-Tree-With-Evaluate-Function.py) (!!!M) <br>
With careful obervation, we'll see the operator tree node cannot be leaf, and the number tree node can only be leaf. With that, we can easily implement:
In building a tree, since we are given __post-order expression__, we can use a stack to store the operator tree nodes.
In evaluate the result, we just do divide and conquer.
- [1597. Build Binary Expression Tree From Infix Expression](Solutions/1597.Build-Binary-Expression-Tree-From-Infix-Expression.py) (!!!H) <br>
since we are given __in-order expression__, Divide and conquer - O(NlogN) in best case: 每次都能通过O(N)时间将问题分成2T(N/2)问题, O(N^2) in worst case: ((((((1)))))).
- [1381. Design a Stack With Increment Operation](Solutions/1381.Design-a-Stack-With-Increment-Operation.py) (!!!M) <br>
Use an additional array to record the increment value - O(1). inc[i] means for all elements st[0] ~ st[i], we should plus inc[i] when popped from the stack.
When we pop, we should set inc[i-1] += inc[i], so that we can accumulate the increment inc[i] for the bottom elements and the following pops.



## [Iterator](/Data-Structure.py)
- [0341. Flatten Nested List Iterator](Solutions/0341.Flatten-Nested-List-Iterator.py) (!!M) <br>
solution 1: 用一个辅助函数把nested_list flatten掉存到一个q中就可以了，用递归去flatten既可以了. Solution 2: use a q to partially flatten the list in hasnext function.
- [0251. Flatten 2D Vector](Solutions/0251.Flatten-2D-Vector.py) (!!M) <br>
Solution 1: use a queue to flatten the 2D vector first. Solution 2: use two pointers, one for row, one for col. O(1) space.  In the hasNext function, we need to do two things: 1. skip all the empty rows; 2. return True if has next
- [0281. Zigzag Iterator](Solutions/0281.Zigzag-Iterator.py) (!!M) <br>
use two pointers and a flag. What if you are given k 1d vectors? How well can your code be extended to such cases? Solution: We append all the list into one queue. Every time we call next(), we pop a list first, then pop the first num from the list, and then re-add it to the end to deque so that we can call it again after k next calls.
- [0284. Peeking Iterator](Solutions/0284.Peeking-Iterator.py) (!!M) <br>
define a self.iterator, and a self.next_item to record the top item of the iterator, 相当于提前预支next_item.
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (!!M) <br>
用stack实现binary search tree的in order traversal的方法类似, 用一个stack存最小的node, 需要额外定义一个 def getLeftMost(self, root)



## [Monotonic stack](/Data-Structure.py) 
#### 用于向左/向右寻找第一个比自己大/小的数 
- [0496. Next Greater Element I](Solutions/0496.Next-Greater-ElementI.py) (!!M) <br>
maitain a moono decreasing st. whenever we found a smaller element, we append.
whenever we found a larger element, we pop, and this curr element is the next greater element of the popped element.
- [0503. Next Greater Element II](Solutions/0503.Next-Greater-Element-II.py) (!!M ByteDance) <br>
solution 1: Double the nums first, then maintian a decreasing st. st store the (num, idx) pair so that we can easily update res. solution 2: should also know the soution that don't need to double the nums. 方法是for idx in range(2* lens): 对长度lens取模，i = idx % lens 
- [0556. Next Greater Element III](Solutions/0556.Next-Greater-Element-III.py) (!!M) <br>
very similar with 31. Next Permutation. # step 1: 从右至左找到第一个降序的； # step 2: swap the nums[idx] with the num just larger than it; # step 3: reverse/sort the rest of the list
- [0739. Daily Temperatures](Solutions/0739.Daily-Temperatures.py) (!!M) <br>
维护一个单调递减栈即可, stack里面存(temperature, idx)
- [0901. Online Stock Span](Solutions/0901.Online-Stock-Span.py) (!!!M) <br>
维护一个单调递减栈即可, __init__ 函数中需要用到的有self.idx = 0, self.st = [], store the price and idx, mono-decreasing; self.res = collections.defaultdict(lambda: 1), store the res at each idx; we update the res by res = self.mapping[top_idx] + self.idx - top_idx 
- [1130. Minimum Cost Tree From Leaf Values](Solutions/1130.Minimum-Cost-Tree-From-Leaf-Values.py) (!!M) <br>
维护一个单调递减栈 The main idea is that you want to use the two smallest as leaf nodes to construct a root node. 
So, here we loop through the entire array, whenever we find stack[-1] <= currNum, 
which means that this top element stack[-1] is a local minimum. 
So we use this element with its left or right to construct a root node. (res += min(drop * currNum, drop * stack[-1])). You can think this is a greedy algorithm. 真尼玛难理解，操！
- [0402. Remove K Digits](Solutions/0402.Remove-K-Digits.py) (!!M) <br>
维护一个递增栈，碰到更小的就把前面的删掉，这样排在前面的就都是最小的了
- [0084. Largest Rectangle in Histogram](Solutions/0084.Largest-Rectangle-in-Histogram.py) (!!H) <br>
非单调栈算法：从左向右遍历数组，然后每遍历到一个高度h，向左边找第一个比自己小的的高度在位置i，向右边找第一个比自己小的的高度在位置j，
那此时的面积就是h*(j-i). 这个算法需要向左向右找第一个比自己小的元素，这类问题就要想到用monostack. 
step 1: 寻找左边第一个比自己小的idx并存起来;
step 2: 寻找右边第一个比自己小的idx并存起来;
step 3: calculate the area
- [0085. Maximal Rectangle](Solutions/0085.Maximal-Rectangle.py) (!!!H Google) <br>
step 1: construct a heights list for each row; step 2: calculate the largestRectangularHistogram of each height using the same method in 84; Should think about dynamic programming solution also.
- [1504. Count Submatrices With All Ones](Solutions/1504.Count-Submatrices-With-All-Ones.py) (!!!M Google) <br>
Monostack. solution 1: dp. O(M^2N) 固定以up_row为长方形上边，然后去探寻不同下边的情况, 每次探寻一个下边，我们都计算一次从up_row到down_row可能有多少个valid_submatrices,
我们把这个计算转换成一维来计算，对于每一个up_row, 都构建一个一位数组arr.  arr[j] = 1 if from up_row to down_row, all values in column j are 1. 只要up_row到down_row有一个value is 0，
我们就设置arr[j] = 0, 表示不可能以up_row为上边以down_row为下边以j为右col构造valid submatrce. solution 2: 与84.Largest-Rectangle-in-Histogram, 85.Maximal-Rectangle很类似.
先构造histogram. 以j结尾的submatrices的个数等于heights[j] * (j - 向左找第一个height小于heights[j]的idx).
- [0907. Sum of Subarray Minimums](Solutions/0907.Sum-of-Subarray-Minimums.py) (!!M) <br>
我们其实关心的是以某个数字结尾时的子数组最小值之和，
可以用一个一维数组 dp，其中 dp[i] 表示以数字 A[i] 结尾的所有子数组最小值之和，
遍历A, 更新 dp[i] = dp[idx] + A[i] * (i-idx)，其中idx是往左寻找第一个比当前A[i]小的数的idx，
最终的结果 res 就是将 dp 数组累加起来即可.
为了更快速得到往左寻找第一个比当前A[i]小的数的 idx, 我们可以提前算好存起来，怎样算：monostack
- [0975. Odd Even Jump](Solutions/0975.Odd-Even-Jump.py) (!!H Google) <br>
In order to reach the end, We need to jump higher and lower alternately. solution monostack + dp
We can use st to find the next_higher and next_lower for each pos - using mono stack, like 496. Next Greater Element
Then we tarverse the nums and update using dp.
- [0456. 132 Pattern](Solutions/0456.132-Pattern.py) (!!H) <br>
solution: 从右往左，维护一个单调递减栈，iterate the arr, 来一个num就把他当做是one用, 如果小于two的话那就return True, 如果大于two, 那就当three用，用while loop里找比他小但尽量大的数作为two, 这样下一个进来的num就更容易小于two了
- [0316. Remove Duplicate Letters](Solutions/0316.Remove-Duplicate-Letters.py) (!!H) <br>
we use a stack to store the solution we have built as we iterate over the string.
We remove a ch if two conditions are meet:1. the ch can occur later on; 2. the ch is greater than the curr ch;
Need to use a dictionary to pre-record the last pos a ch appears.  Also need a included set to mark the chars that are already in the st.
- [1081. Smallest Subsequence of Distinct Characters](Solutions/1081.Smallest-Subsequence-of-Distinct-Characters.py) (M) <br>
与316. Remove Duplicate Letters出重复了
- [0654. Maximum Binary Tree](Solutions/0654.Maximum-Binary-Tree.py) (!!M) <br>
solution 1: simple recursion - O(n^2); solution 2: monostack 通过观察发现规律，对于每个node的父亲节点 = min(左边第一个比它大的，右边第一个比它大的), 维护一个降序数组，可以实现对这个min的快速查找,maintain a mono decreasing stack, the items in the stack are nodes - O(N)
- [0962. Maximum Width Ramp](Solutions/0962.Maximum-Width-Ramp.py) (!!!M) <br>
solution 1: sort the num_pos and then do 121. best time to buy and sell stock - O(nlogn). 
This is "Last Greater Element" problem. monostack - O(n).
Step 1: put valid candidates into stack: loop from left to the right, if there's a value greater than a value to the left, 
it doesn't make sense to use it. So we create a stack in descending order. 
这里跟sort很像，但是我们是把unordered的num直接不要，而不是把它放到该有的地方。
Step 2: now go backwards on A, and compare the values to the stack to see the max_lens we can have.



# [Two Pointers](/Two-pointers.py)
### [反向双指针](/Two-pointers.py)
- [EPI book](Solutions/) (E) <br>
Question: given an array, move all the even numbers to the left while all the odd numbers to the right.
Solution: two pointers, the same process of merge part in merge sort.
- [0977. Squares of a Sorted Array](Solutions/0977.Squares-of-a-Sorted-Array.py) (E) <br>
three pointers: i starts from beginning of A; j starts from the end of A; k starts from end of res 
- [0011. Container With Most Water](Solutions/0011.Container-With-Most-Water.py) (!!M) <br>
if height[i] > height[j]: j -= 1  # meaning that 右边的栅栏更低，所以把右边指针移动一下，希望能用长度去compromise宽度，即寄希望于min(height[i], height[j])会变大，来compromise掉(j - i)的变小. 为什么不移左边指针呢？因为移动左边的话，min(height[i], height[j])不会变大，但是(j - i)一定变小，所以面积一定变小.
 


### [同向双指针](/Two-pointers.py)
- [0415. Add Strings](Solutions/0415.Add-Strings.py) (E) <br>
similar with leetcode 2.  while i >= 0 and j >= 0:  循环之后，还要check while i >= 0: ;  while i >= 0: ; 最后还要check if carryBit > 0:
- [0088. Merge Sorted Array](Solutions/0088.Merge-Sorted-Array.py) (E) <br>
modify nums1 in-place, 由于nums1有足够空间，我们可以从nums1的尾部开始排，use i, j, k = m - 1, n - 1, m + n -1; 把最大的数放到nums1的后面
- [0283. Move Zeroes](Solutions/0283.Move-Zeroes.py) (E) <br>
anchor is the first zero element, __anchor keeps all the non-zero numbers on it's left, that is the reason the pointer is called anchor__. while curr runs forward, whenever curr equals a non-zero number, switch it to anchor, and move anchor one step forward.  __注意怎样maintain non-zero numbers的relative order非常的tricky__.  Solution 2: partition using the method in 31, but not accepted cuz partition changes the original order of non-zero numbers. Beacuase quick sort is a ramdomized sorting algorithm.
- [0026. Remove Duplicates from Sorted Array](Solutions/0026.Remove-Duplicates-from-Sorted-Array.py) (!!E) <br>
典型的同向双指针 on the left of anchor (including anchor) are the maintained array without duplicates
- [0083. Remove Duplicates from Sorted List](Solutions/0083.Remove-Duplicates-from-Sorted-List.py) (!!E) <br>
- [0082. Remove Duplicates from Sorted List II](Solutions/0082.Remove-Duplicates-from-Sorted-List-II.py) (M) <br>
要把duplicates都去掉一个不留，anchor stays where on it's left there is only distinct numbers，需要比较prev,curr,curr.next的val来判断一个数是不是合格的
- [0203. Remove Linked List Elements](Solutions/0203.Remove-Linked-List-Elements.py) (!!E) <br>
anchor keeps all not_equal_val nodes on its left
- [0532. K-diff Pairs in an Array](Solutions/0532.K-diff-Pairs-in-an-Array.py) (E) <br>
同向双指针法，注意题目需要去重，如果碰到符合条件的，把i和j往前挪到不重复的元素去。有点像3-sum去重的问题
- [0042. Trapping Rain Water](Solutions/0042.Trapping-Rain-Water.py) (!!H) <br>
首先找到最高highestBar的位置。然后从左边往最高的位置扫，同时maintain一个指针记录leftHighest的高度，如果扫到的地方i小于这个leftHighest的高度，
则说明i这个地方可以蓄水，可蓄水量为leftHighest的高度减去i的高度；如果扫到的地方i大于这个leftHighest的高度，则说明i这个地方不可以蓄水，所以这时候要更新leftHighest为i的高度。同理对右边做同样的操作
- [0165. Compare Version Numbers](Solutions/0165.Compare-Version-Numbers.py) (M Google) <br>
two pointers.  split the version by "." first before processing.
- [0925. Long Pressed Name](Solutions/0925.Long-Pressed-Name.py) (E) <br>
two pointers


### [Linked List](/Linked-List)
- [0138. Copy List with Random Pointer](Solutions/0138.Copy-List-with-Random-Pointer.py) (!!M) <br>
Solution 1 O(N), O(N): Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, make sure you are not making multiple copies of the same node. we can use extra space to keep old node --> new node mapping to prevent creating multiples copies of same node.   Solution 2 O(N), O(1): use 3 steps, each step requires iterate the loop one time.  step 1: create new node and interleave new node into original node; step 2: link the random pointer for the new nodes; step 3: seperate the interleaved old nodes and new nodes
- [0430. Flatten a Multilevel Doubly Linked List](Solutions/0430.Flatten-a-Multilevel-Doubly-Linked-List.py) (!!M) <br>
递归即可，易错点是return head之前别忘了把head.child设置成None
- [0021. Merge Two Sorted Lists](Solutions/0021.Merge-Two-Sorted-Lists.py) (E) <br>
如果需要return一个新的headNode，一般定义一个dummyNode = ListNode(0), curr = dummyNode; 最后return dymmyNode.next
- [0148. Sort List](Solutions/0148.Sort-List.py) (!!M) <br>
step1: divide: 先找到mid, 然后在mid处cut成左右half, 再分别sort left and right; step 2: merge, 同21
- [0086. Partition List](Solutions/0086.Partition-List.py) (!!M) <br>
注意这里要用两个dummy node, 左边一个，右边一个，将左边和右边分开！！！左右分别用两个指针一个往前跑，另一个留守head的位置
- [0206. Reverse Linked List](Solutions/0206.Reverse-Linked-List.py) (!!E) <br>
需要熟背理解solution 1: interrative: 注意初始化 __prev, curr = None, head__ 因为head需要point to None; solution 2: recurssive: 非常容易漏掉 head.next = None
- [0092. Reverse Linked List II](Solutions/0092.Reverse-Linked-List-II.py) (M) <br>
reverse node from m to n: step 1: find node_m and node_m_minus; find node_n and node_n_plus; step 2. reverse the nodes from m to n; 3. hook up node_m_minus with node_n, node_m with node_n_plus
- [0024. Swap Nodes in Pairs](Solutions/0024.Swap-Nodes-in-Pairs.py) (M) <br>
Solution 1: recursion, easier to implement. Solution 2: iterative. 想要reverse n1->n2->n3->n4->n5->n6 in pairs: step 1: 在n1前面添加一个dummy n0, 然后在while curr循环里每次都调用reverse函数，reverse函数做的事情是操作四个节点n0->n1->n2->n3, 将其变成n0->n2->n1->n3, 然后return n1，注意每次都是return想要swap的两个节点的前一个节点！step 2: curr = return的n1，然后继续循环
- [0025. Reverse Nodes in k-Group](Solutions/0025.Reverse-Nodes-in-k-Group.py) (!!H) <br>
Solution 1: recursion: step 1: exit of recursion: when less than k elements left, return head directly; step 2: reverse the first k elements; step 3: revursivey find the new head of the reversed list
- [0141. Linked List Cycle](Solutions/0141.Linked-List-Cycle.py) (E) <br>
在做环形list的题目时,模板是 __slow, fast = head, head; while fast and fast.next:__
- [0202. Happy Number](Solutions/0202.Happy-Number.py) (!!E) <br>
solution 1: 用一个hashset记录number, if next number is in visited, 说明成环了，就return False - O(N), O(N);
solution 2: slow, fast双指针往前跑，fast跑两步，如果slow == fast说明成环了，return False - O(N), O(1).
- [0142. Linked List Cycle II](Solutions/0142.Linked-List-Cycle-II.py) (!!M) <br>
step 1: 快慢指针找到相遇的点; step 2: 重新定义两根指针p1, p2分别从head和上面相遇的点出发，然后p1,p2相遇的地方就是环的入口
- [0287. Find the Duplicate Number](Solutions/0287.Find-the-Duplicate-Number.py) (!!M) <br>
[1,5,3,6,2,2,4]: 1 -> 5 -> 2 -> 3 -> 6 -> 4 -> 2.... 形成了环. 把这个数组的每一个数num看成这样一个linked list node: num的下标代表.val, num的值代表.next指向下一个node。那么如果存在重复的num，那就表示有两个不同node都指向了同一个公共，也就是成环的地点。这么想这个题目就和142一样了，具体实现过程中对p取一个nums[p]，就相当于取一个p.next
- [0160. Intersection of Two Linked Lists](Solutions/0160.Intersection-of-Two-Linked-Lists.py) (E) <br>
两个指针currA, currB; if not currA: currA = headB; if not currB: currB = headA
- [0002. Add Two Numbers](Solutions/0002.Add-Two-Numbers.py) (!!M) <br>
本题的考点是关于如何新建一个linked list, 要用someNode.next = ListNode(someVal), 而不是简单的修改value; 还考察了是否细心, 最后很容易漏掉carryBit != 0的判断"
- [0445. Add Two Numbers II](Solutions/0445.Add-Two-Numbers-II.py) (M) <br>
Follow up: What if you cannot modify the input lists? In other words, reversing the lists is not allowed. solution: use two stacks to store the numbers in two linked lists.
- [0023. Merge k Sorted Lists](Solutions/0023.Merge-k-Sorted-Lists.py) (!!H) <br>
正解 Solution 1: divide and conquer. solution 2: maintain一个heapq，初始化将每个list的head放入，然后每次pop出一个最小的，再把最小的那个的.next push进heapq, O(NlogK); we need to override ListNode compare function __ lt __ to make customized compare happens: compare ListNode. 
- [0234. Palindrome Linked List](Solutions/0234.Palindrome-Linked-List.py) (E) <br>
题目要求O(n) time and O(1) space: 我们只能reverse 一半的linked list，先找到中点，然后reverse the left part，最后比较判断是否为panlindrome
- [0019. Remove Nth Node From End of List](Solutions/0019.Remove-Nth-Node-From-End-of-List.py) (M) <br>
fast 比 slow 先出发 n 步即可
- [0061. Rotate List](Solutions/0061.Rotate-List.py) (M) <br>
fast 比slow先出发k步
- [0143. Reorder List](Solutions/0143.Reorder-List.py) (M) <br>
step 1: cut the list into two halves; step 2: reverse the 2nd half; step 3: connect the 1st and 2nd half
- [0328. Odd Even Linked List](Solutions/0328.Odd-Even-Linked-List.py) (!!M) <br>
把dummy指向head.next的地方，因为一会儿会丢失掉head.next的位置, 害怕什么node的位置会丢掉就拿一个dummy指向那个位置




### [双指针处理双序列问题](/Two-pointers.py)
- [0844. Backspace String Compare](Solutions/0844.Backspace-String-Compare.py) (!!!E) <br>
这种双指针处理比较双序列问题很常见。由于题目"#"可以删掉前面的ch, We can use a pointer traverse from __right to left__, and use a counter to count how many "#" we got so far. 一般要求用O(1) space解决。Google follow up: 加一个按键是类似caps lock，即按了之后所有的字母小写变大写，再按一下大写变小写。
思路：定义caps cnt，先扫一遍看多少个caps lock，比较s1.charAt(i) == s2.charAt(j) && caps1 == caps2

- [0809. Expressive Words](Solutions/0809.Expressive-Words.py) (!!!M Google) <br>
pre-calculate how many successive same chars are there at each idx: "heeellooo" --> {0: 1, 1: 3, 2: 2, 3: 1, 4: 2, 5: 1, 6: 3, 7: 2, 8: 1}




### [Two Sum]()
- [0001. Two Sum](Solutions/0001.Two-Sum.py) (!!E) <br>
九章算法：对于求 2 个变量如何组合的问题可以循环其中一个变量，然后研究另外一个变量如何变化, 普世的方法是：for循环一个变量a，然后看另外一个变量target-a是不是在一个hashmap中
- [0167. Two Sum II - Input array is sorted](Solutions/0167.Two-Sum-II-Input-array-is-sorted.py) (E) <br>
sorted 就用反向双指针
- [0170. Two Sum III - Data structure design](Solutions/0170.Two-Sum-III-Data-structure-design.py) (E) <br>
self.numsDict = collections.defaultdict(lambda: 0) # val is num val, key is how namy times the val was added
- [1099. Two Sum Less Than K](Solutions/1099.Two-Sum-Less-Than-K.py) (E) <br>
最优解是sort之后用反向双指针O(nlogn); solution 2: bucket sort: O(n)? coudl be a good follow up question.
- [0609. Two Sum - Less than or equal to target](Solutions/0609.Two-Sum-Less-than-or-equal-to-target.py) (!!E Lintcode) <br>
反向双指针：if nums[i] + nums[j] <= target: cnt += j - i		# 注意这里是 cnt += j - i 表示nums[i] 加上 (i 到 j之间的任何数)，一定也是小于等于target的
- [0653. Two Sum IV - Input is a BST](Solutions/0653.Two-Sum-IV-Input-is-a-BST.py) (E) <br>
iterative in-order traversal of a tree要背熟
- [1214. Two Sum BSTs](Solutions/1214.Two-Sum-BSTs.py) (M) <br>
Iteratively do an inorder traversal for root1, and store the val in a hashSet; then itteratively do an inorder traversal for root2, and at the same time check if a target-val is in the hashSet. time complexity: O(M + N). 算法跟two sum是一样的，如果闭着眼睛能写要会iterative in-order traversal的哈！
- [0015. 3Sum](Solutions/0015.3Sum.py) (!!M) <br>
step 1: sort the list; step 2: 背模板，注意点一：对i去重；注意点二：left, right=i+1, lens-1; 注意点三：left和right的初始值；注意点三：对left和right去重
- [0016. 3Sum Closest](Solutions/0016.3Sum-Closest.py) (M) <br>
- [0259. 3Sum Smaller](Solutions/0259.3Sum-Smaller.py) (M) <br>
优化：if nums[i] * 3 >= target: break；解法类似609
- [0018. 4Sum](Solutions/0018.4Sum.py) (M) <br>
solution 1: O(N^3): 3Sum模板双指针法。注意这里给j去重不能从j>=1开始，因为要至少让j先取上第一个值i+1之后才能与前一个数比较！不然[0,0,0,0], 0就通不过了；solution 2: O(N^2): hashmap. for循环a, b,保存a+b的值进hashmap, 再for循环c, d, 判断c+d是否在hashmap中
- [0454. 4Sum II](Solutions/0454.4Sum-II.py) (M) <br>
有四个数组，不好用双指针，所以就使用hashmap，用一个hashmap 保存a + b
- [0089. k Sum](Solutions/0089.k-Sum.py) (!!H Lintcode) <br>
采用动态规划，用dp[i][j][t]表示前i个数里选j个和为t的方案数。dp[i][j][t] = 选A[i-1]: dp[i-1][j-1][t-A[i-1]] + 不选 A[i-1]: dp[i-1][j][t]; initialize: dp[i][0][0] = 1; return dp[lens][k][target]






# [Sliding Window (同向双指针)](/Sliding-window.py)
#### 第一种模板：at least problem; 第二种模板：at most problem.
- [1234. Replace the Substring for Balanced String](Solutions/1234.Replace-the-Substring-for-Balanced-String.py) (!!M) <br>
find the minimum substring so that outside the substring, condition all(four chars has frequency less than n//4) is satisfied.
第一种模板：find min subarray size for at least problem, 后面的指针去远离前面的指针
- [0209. Minimum Size Subarray Sum](Solutions/0209.Minimum-Size-Subarray-Sum.py) (!!M) <br>
这题是第一种模板：find min subarray size for at least problem. 写法是while loop里让后面的指针逐渐远离前面的指针；
Can we solve in O(NlogN)? Yes, we can traverse the the list, say at i, we search the fisrt j that satisfy sum(nums[i:]>=s), so it is a OOXX probelm, which could be solved using binary search. Follow up: 如果有负数怎么办？那就不能用sliding window了, 只能用pre_sum / deque, 详见862.
- [1358. Number of Substrings Containing All Three Characters](Solutions/1358.Number-of-Substrings-Containing-All-Three-Characters.py) (M) <br>
at least problem, 第一种模板：find min subarray size for at least problem. 写法是while loop里让后面的指针逐渐远离前面的指针
- [1208. Get Equal Substrings Within Budget](Solutions/1208.Get-Equal-Substrings-Within-Budget.py) (!!M) <br>
step 1: construct a cost arr; step 2: sliding window 第二种模板：find max subarray size for at most problem. 写法是while loop里让前面的指针去追后面的指针
- [0713. Subarray Product Less Than K](Solutions/0713.Subarray-Product-Less-Than-K.py) (M) <br>
Note that the numbers are positive, so we can use sliding window. 这题是sum at most s problem, 写法是while loop里让前面的指针去追后面的指针
- [1248. Count Number of Nice Subarrays](Solutions/1248.Count-Number-of-Nice-Subarrays.py) (!!M) <br>
exactly(K) = atMost(K) - atMost(K-1); 第二种模板：find max subarray size for at most problem. 写法是while loop里让前面的指针去追后面的指针
- [0930. Binary Subarrays With Sum](Solutions/0930.Binary-Subarrays-With-Sum.py) (!!M) <br>
(number of subarrays having sum S) = (number of subarrays having sum at most S) - (number of subarrays having sum at most S-1)
这题是sum at most s problem, 写法是while loop里让前面的指针去追后面的指针
- [0487. Max Consecutive Ones II](Solutions/0487.Max-Consecutive-Ones-II.py) (!!!M) <br>
sliding window solution: longest subarray with at most one 0s. 这题是at most problem, 写法是while loop里让前面的指针去追后面的指针. solution 2: record prev_lens and curr_lens for the previous lens of consecutive 1s and curr lens of consecutive 1s. update them we there is a new 0 coming, otherwise curr_lens += 1.
- [1004. Max Consecutive Ones III](Solutions/1004.Max-Consecutive-Ones-III.py) (M) <br>
same as 487: longest subarray with at most k 0s. 这题是at most problem, 写法是while loop里让前面的指针去追后面的指针. 
- [0340. Longest Substring with At Most K Distinct Characters](Solutions/0340.Longest-Substringwith-At-Most-K-Distinct-Characters.py) (!!H) <br>
维护一个charDict, 用来记录i->j中的char的频率，这题是sum at most s problem, 写法是while loop里让前面的指针去追后面的指针; 更新j: charDict[s[j]+=1; 更新i: charDict[s[i]] -= 1, if charDict[s[i]] == 0: del charDict[s[i]]
- [0159. Longest Substring with At Most Two Distinct Characters](Solutions/0159.Longest-Substring-with-At-Most-Two-Distinct-Characters.py) (M) <br>
Exactly the same as 340.
- [0904. Fruit Into Baskets](Solutions/0904.Fruit-Into-Baskets.py) (M) <br>
Exactly the same as 159.
- [0424. Longest Repeating Character Replacement](Solutions/0424.Longest-Repeating-Character-Replacement.py) (!!M) <br>
340 的变形题 this problem is to find the max_lens of substring so that (length of substring - number of times of the maximum occurring character in the substring) is at most K.
- [0992. Subarrays with K Different Integers](Solutions/0992.Subarrays-with-K-Different-Integers.py) (!!H) <br>
exactly(K) = atMost(K) - atMost(K-1). Helper function is exactly the same as 340. Longest Substring with At Most K Distinct Characters
- [0003. Longest Substring Without Repeating Characters](Solutions/0003.Longest-Substring-Without-Repeating-Characters.py) (!!M) <br>
维护一个included=set(), 用来记录i->j中include的char，套模板时满足的条件是s[j] not in included; 更新j: included.add(s[j]); 更新i: included.remove(s[i])
- [1100. Find K-Length Substrings With No Repeated Characters](Solutions/1100.Find-K-Length-Substrings-With-No-Repeated-Characters.py) (!!M) <br>
Brutal force / sliding window with fixed length: O(26N); Sliding window O(N): find the substring longer than K that has no repeating chars.
- [0076. Minimum Window Substring](Solutions/0076.Minimum-Window-Substring.py) (!!H) <br>
维护一个sourceFreqDict, 用来记录i->j中的char的频率，套用模板时满足的条件是sourceFreqDict all included in targetFreqDict; 更新j: sourceDict[s[j]] += 1, 更新i: sourceDict[s[i]] -= 1.  time complexity is O(MN). solution 2: O(N), instead of using self.allIncluded(sourceDict, targetDict) to check matched or not,  we use a int missing to keep track of how many chars are still needed in order to match, this reduce the time from O(M) to O(1). also, instead of using s[i:j] everytime when we renew res, we use start, end to renew the idx, which reduce time from O(N) to O(1)
- [0727. Minimum Window Subsequence](Solutions/0727.Minimum-Window-Subsequence.py) (!!!H) <br>
solution 1: sliding window - O(MN) 这题subseq与上题substring不同，上题只需要freq都满足了就行，这题不仅如此，而且还是讲究顺序的，; solution 2: dp. dp[i][j] = the min window subsequence that ends with ith ch in t, and jth ch in s. If t[i-1] == s[j-1]: dp[i][j] = dp[i-1][j-1] + 1; else: dp[i][j] = dp[i][j-1] + 1
- [0395. Longest Substring with At Least K Repeating Characters](Solutions/0395.Longest-Substring-with-At-Least-K-Repeating-Characters.py) (!!!M) <br>
solution 1: sliding window: for each i in range(1, 27), use sliding window technique to find the longest substring to satisfy two conditions: 1. the number of total unique characters in substring is i; 2. at least k repeating characters. 第二种模板：find max subarray size for at most problem. 写法是while loop里让前面的指针去追后面的指针 solution 2: use those char which counting is smaller than k as a 'wall' to divide the string into two parts and use recursion on the two parts.
- [0228. Summary Ranges](Solutions/0228.Summary-Ranges.py) (M) <br>
sliding window可解
- [0163. Missing Ranges](Solutions/0163.Missing-Ranges.py) (M) <br>
这题是上一题的延伸，跟sliding window没啥关系
- [0862. Shortest Subarray with Sum at Least K](Solutions/0862.Shorteast-Subarray-with-Sum-at-Least-K.py) (!!!H) <br>
不能像209. Minimum Size Subarray Sum那样用sliding window因为209那题是positive numbers, 这题可以为负值。
这题的最优解是mono deque. O(N). 先构造一个presum list, 接下来方法与239类似的，
两个while循环，一个while loop do sliding window to update res, 从队首pop, 同时更新res, 
另一个while loop do monostack to maintain an increasing dq, 从队尾pop, 对deq进行清理。
- [1237. Find Positive Integer Solution for a Given Equation](Solutions/1237.Find-Positive-Integer-Solution-for-a-Given-Equation.py) (E Google) <br>
反向双指针. 

### Sliding window with fixed size
- [1456. Maximum Number of Vowels in a Substring of Given Length](Solutions/1456.Maximum-Number-of-Vowels-in-a-Substring-of-Given-Length.py) (M) <br>
套 sliding window with fixed size 模板即可
- [0242. Valid Anagram](Solutions/0242.Valid-Anagram.py) (E) <br>
string s and t are anagram with each other when all the ch in s have the same count as that in t
- [0567. Permutation in String](Solutions/0567.Permutation-in-String.py) (M) <br>
solution 1: 由于我们要求的substring时固定长度的，所以最好maintina a fixed size window - 套用fix window模板
- [0438. Find All Anagrams in a String](Solutions/0438.Find-All-Anagrams-in-a-String.py) (!!M) <br>
由于我们要求的substring时固定长度的，所以最好maintina a fixed size window. same as 567
- [0030. Substring with Concatenation of All Words](Solutions/0030.Substring-with-Concatenation-of-All-Words.py) (H) <br>
固定长度的sliding window: solution: use two hashmaps to record the frequency of word.
O(len(s)* len(words)* len(words[0]))
- [1052. Grumpy Bookstore Owner](Solutions/1052.Grumpy-Bookstore-Owner.py) (M) <br>
Since the window size is fixed, the problem is easier to implement. We only need to update the max_gain,
which represents how man ymore people can be satisfied if the owner use X minites magic card
- [1151. Minimum Swaps to Group All 1's Together](Solutions/1151.Minimum-Swaps-to-Group-All-1s-Together.py) (M) <br>
Find the substring with lens=k and minimum 0s in it. use a fix window to find minimum number of 0s.
- [1423. Maximum Points You Can Obtain from Cards](Solutions/1423.Maximum-Points-You-Can-Obtain-from-Cards.py) (!!!M Google) <br>
sliding window with fix size problem, the only difference is that some part of the window is at the beginning of the list and some are at the end. 我们可以转化为 find the minimum points you can get within window with fixed size: lens-k. 套用模板即可 Google真是滑窗控
- [0683. K Empty Slots](Solutions/0683.K-Empty-Slots.py) (!!M Google) <br>
The problem is to find a fixed sized window, where any num in the window [i, i+k], are smaller than days[i-1] and also smaller than days[i+k+1].


# [SubArray/Prefix Sum](/SubArray.py)
- [0053. Maximum Subarray](Solutions/0053.Maximum-Subarray.py) (!!E) <br>
step 1: 构造前缀和pre_sum; 
step 2: the same as 127. Best time to buy and sell stock
- [0724. Find Pivot Index](Solutions/0724.Find-Pivot-Index.py) (E) <br>
if pre_sum[i-1] == pre_sum[-1] - pre_sum[i]: return i - 1
- [0560. Subarray Sum Equals K](Solutions/0560.Subarray-Sum-Equals-K.py) (!!M Google) <br>
新建一个prefixSumDict = {0: 1}, key是prefixSum, val是how many times the prefixSum appears; if prefixSum - k in prefixSumDict: 等价于if prefixSum[j+1]-prefixSum[i] == k
- [0325. Maximum Size Subarray Sum Equals k](Solutions/0325.Maximum-Size-Subarray-Sum-Equals-k.py) (!!M) <br>
由于arr中有正数有负数，所以不能用sliding window, 只能用prefix sum + hashmap. pre_sum_dict stores (pre_sum --> idx where the pre_sum occured)
- [0525. Contiguous Array](Solutions/0525.Contiguous-Array.py) (!!M) <br>
将0都变成-1，题目就变成了max subarray size with sum == 0, which is exactly the same as 325. Maximum Size Subarray Sum Equals k.
由于arr中有正数有负数，所以不能用sliding window, 只能用prefix sum + hashmap
- [0974. Subarray Sums Divisible by K](Solutions/0974.Subarray-Sums-Divisible-by-K.py) (!!M) <br>
subarray sum的问题都要往prefix sum方面去想： pre_sum_dict is (pre_sum --> how many time pre_sum occured); prefixSum += num; prefixSum %= K
- [0523. Continuous Subarray Sum](Solutions/0523.Continuous-Subarray-Sum.py) (M) <br>
prefixSumMap = {0: -1} # key: prefixSum[j], val: j/position, initial position should be -1; prefixSum += num; prefixSum = prefixSum % k 因为题目要求要能被subArray Sum 要能被k整除
- [0139. Subarray Sum Closest](Solutions/0139.Subarray-Sum-Closest.py) (!!M Lintcode) <br>
题目要求NlogN, 那就是疯狂暗示要sort, 对pre_sum来进行sort，这样最小的subArrSum就一定来自于相邻的两个prefix sum了, 注意pre_sum里面要把idx信息带上，不然一会儿sort了之后会丢掉
- [0238. Product of Array Except Self](Solutions/0238.Product-of-Array-Except-Self.py) (M Pramp) <br>
pre-calculate pre_prod, where pre_prod[i] = product before i (not including i),
also pre-calculate suf_prod, where suf_prod[i] = product after i (not including i);
then traversal the arr and update Product of Array Except Self
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](Solutions/1031.Maximum-Sum-of-Two-Non-Overlapping-Subarrays.py) (!!!M Google) <br>
这一题是把提前计算好的思想运用到了极致。
Step 1: 提前计算好prefix_sum and suffix_sum;
Step 2: using the prefix_sum and suffix_sum, 提前计算好 the prefix_max_L, where prefix_max_L[i] = the max subarray sum with window size L before i, 
and do the same for suffix_max_L;
Step 3: travel the pre_sum and update M-long subarray sum and max_sum using the pre-calulated prefix_max_L and suffix_max_L.
Solution 2: DP可以做到O(1) space. 具体做法与下一题689类似
- [0689. Maximum Sum of 3 Non-Overlapping Subarrays](Solutions/0689.Maximum-Sum-of-3-Non-Overlapping-Subarrays.py) (!!!H) <br>
这一题是把提前计算好的思想运用到了极致。
Step 1: 提前计算好prefix_sum and suffix_sum;
Step 2: using the prefix_sum and suffix_sum, 提前计算好 the prefix_max_k, where prefix_max_k[i] = the max subarray sum with window size k before i, 
and do the same for suffix_max_k;
Step 3: travel the pre_sum and update 中间的 k-long subarray sum and max_sum using the pre-calulated prefix_max_L and suffix_max_L.
- [1124. Longest Well-Performing Interval](Solutions/1124.Longest-Well-Performing-Interval.py) (!!M) <br>
step 1: 大于8小时的工作时间定义为1， 小于定义为-1， 这样就得到了一个nums，
step 2: now the problem is to find the longest subarray with sum > 0. 
since there is negative numbers, we cannot use sliding window, for subarray sum at least/most k problem with negative number, we use prefix sum + mono deque. 
因为这一题我们只需要check pre_sum - 1 in pre_sum_dict. 所以其实是一个subarray sum equals problem. for subarray sum equals k problem with negative number, we use prefix sum + hashmap. 
- [1074. Number of Submatrices That Sum to Target](Solutions/1074.Number-of-Submatrices-That-Sum-to-Target.py) (H) <br>
也可以先把行处理好，让每一行里面保存上面所有行的和，接下来就是在每一行里面去求560问题了，注意一点不同的是需要遍历upRow和downRow的, 如果不遍历就是solution 3的错误写法举一个反例想明白solution 3为什么行不通，自然就会改成solution 2了O(MMN)
- [0363. Max Sum of Rectangle No Larger Than K](Solutions/0363.Max-Sum-of-Rectangle-No-Larger-Than-K.py) (!!H) <br>
2D version of prefx sum - O(m* m* n* n). 构建2D pre_sum比较复杂需要考虑行的和列的和以及公共部分的和：pre_sum[i+1][j+1] = pre_sum[i][j+1] + pre_sum[i+1][j] - pre_sum[i][j] + matrix[i][j].   Solution 2: binary search to achieve O(n^3logn)
- [Binary Searchable](Solutions/Google__BinarySearchable.py) (!!M Google) <br>
prefix sum + binary search.  一个数是binary searchable的必须满足的条件是：前面的数都比他小，后面的数都比他大
- [Max Absolute Difference of Subarrays](Solutions/Google__Max_Absolute_Difference_of_Subarrays.py) (!!M Google) <br>
prefix sum + dp.  step 1: maintain一个prefix_sum list和一个suffix_sum list. step 2: 用这两个list计算出dp1 list and dp2 lsit, dp1[i] = the max subarray sum before i, dp2[i] = the min subarray sum before i; dp3[i] = the min subarray sum after i, dp4[i] = the max subarray sum after i. step 3: 从左到右遍历一遍，比较i左右两边的min 和 max, 更新max_abs_diff即可。O(N), O(N)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](Solutions/1477.Find-Two-Non-overlapping-Sub-arrays-Each-With-Target-Sum.py) (!!!!M Google) <br>
prefix sum + dp. step 1: construct a pre_sum and a suf_sum. Step 2: then use the pre_sum and suf_sum to construct two lists: pre_min[i] = minimum lens of valid subarray that ends before i. suf_min[i] = minimum lens of valid subarray that starts after i. step 3: find the ans as we iterate the arr
- [1352. Product of the Last K Numbers](Solutions/1352.Product-of-the-Last-K-Numbers.py) (!!M Google) <br>
prefix sum.  Keep all prefix products of numbers in an array, then calculate the product of last K elements in O(1) complexity. When a zero number is added, we need to reset the array of prefix products.
- [1314. Matrix Block Sum](Solutions/1314.Matrix-Block-Sum.py) (!!M Google) <br>
prefix sum 2D version. similar with 304. Range Sum Query 2D - Immutable
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](Solutions/1292.Maximum-Side-Length-of-a-Square-with-Sum-Less-than-or-Equal-to-Threshold.py) (!!M Google) <br>
prefix sum 2D version + binary search. solution 1: max problem - binary search O(mnlogmn). solution 2: prefix sum




## [Mono Deque](/Data-Structure.py) 
#### 首先while loop 左端作为sliding window去限定window size， 然后while loop 右端作为stack or monostack for fast access of previous min/max
- [0239. Sliding Window Maximum](Solutions/0239.Sliding-Window-Maximum.py) (!!H) <br>
heapq的方法是O(NK)因为需要从前面remove; monostack O(N): Iterate over the array. At each step: I. Clean the deque: 1. Remove the items that are outside the curr window and keep only the indexes of elements from the current sliding window; 2. Remove indexes of all elements smaller than the current one, since they will not be the maximum ones. eg: [1,2,7,3,5,4], k = 3, because of 7, 1 and 2 will never be in res; II. Append the current element to the deque. Append deque[0] to the output.
我们回头看看这题其实就是mono st多了一步保持窗口大小的步骤，而这个保持窗口大小的步骤需要从前面pop, 这就是为什么不直接用st, 而是用dq的原因. 总结：如果题目需要我们在window里更新最大值或最小值，我们往往需要maintian一个mono increasing or mono decreasing deque.
- [0751. John's business](Solutions/0751.John's-business.py) (!!M Lintcode) <br>
Solution 1: sliding window minimum - use a mono deque - O(n). similar with 239. Sliding Window Maximum.min_vals[i]表示以i结尾的window的minimum value, 特别注意sliding window maximum/minimum 都是以以i为dq window的最右端 构造 mono deque. solution 2: segment tree - O(nlogk). Maintain a self.min_num in building the SegmentTree.
- [0862. Shortest Subarray with Sum at Least K](Solutions/0862.Shorteast-Subarray-with-Sum-at-Least-K.py) (!!H) <br>
不能像209. Minimum Size Subarray Sum那样用sliding window因为209那题是positive numbers, 这题可以为负值。
这题的最优解是mono deque. O(N). 先构造一个presum list, 接下来方法与239类似的，
两个while循环，一个while loop do sliding window to update res, 从队首pop, 同时更新res, 
另一个while loop do monostack to maintain an increasing dq, 从队尾pop, 对deq进行清理。
- [0995. Minimum Number of K Consecutive Bit Flips](Solutions/0995.Minimum-Number-of-K-Consecutive-Bit-Flips.py) (!!H Google) <br>
q 记录区间[i-k, i]内被反转了的idx, 遍历过程中把里i很远的idx都pop出来，保持窗口小于等于K, 此时len(q)就是位置i已经被翻转的次数，如果为奇数表示i已经从0翻到1或者从1翻到0了
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](Solutions/1438.Longest-Continuous-Subarray-With-Absolute-Diff-Less-Than-or-Equal-to-Limit.py) (!!!M Google) <br>
总结：如果题目需要我们在window里更新最大值或最小值，我们往往需要maintian一个mono increasing or mono decreasing deque.
这个题目我们maintain an increasing dq and a decreasing dq. step 1: 更新maxdq, just like what we did for monostack; step 2: 更新mindq, 套用mono stack模板; step 3: sliding window to update res - 套用sliding window模板
- [1499. Max Value of Equation](Solutions/1499.Max-Value-of-Equation.py) (!!!H Google) <br>
__maintain previous min/max problem__ solution 1: heapq; solution 2: monodeque - O(N). 如果题目需要我们在window里更新最大值或最小值，我们往往需要maintian一个mono increasing or mono decreasing deque.  在mono deque中会有两个while loop，第一个while loop从左端pop作为sliding window去限定window size, 第二个while loop从右端pop作为monostack去maintain 最大值/最小值

---------- 1425. Constrained Subsequence Sum (lee215 solution is good) -------





# [Heap/Heapq](/Data-Structure.py) 
- [Heapq implementation](Solutions/Implement_Heapq.py) (!!M) <br>
- [0703. Kth Largest Element in a Stream](Solutions/0703.Kth-Largest-Element-in-a-Stream.py) (E) <br>
heap solution: maintain a hq with size k, the kth largest is always hq[0] - O(logk) for add function.
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!!M) <br>
solution 1: heapq, time: O(N+KlogK), N 来自于for循环，logK来自于heap的长度是K，heap 的push 和pop都是logK; heapq适合做第K大，第K小，前K大，前K小问题; solution 2: quick select: O(N) - O(N^2).  solution 3: bucket sort O(N). use frequency as idx to store number.
- [0347. Top K Frequent Elements](Solutions/0347.Top-K-Frequent-Elements.py) (!!M) <br>
需要一个freqDict来记录每个数出现的freq， heapq, heapq中放入的是(freq, key)对; 按照freq来做heapq，这样就保证了可以筛选出most freqent k item; solution 2: quick select should implement; solution 3: bucket sort O(N) faster then solution 2, cuz solution 2 is O(N^2) in worst case.
- [Pramp__121820__Word-Count-Engine](Solutions/Pramp__121820__Word-Count-Engine.py) (!!M) <br>
use freq as idx to do bucket sort. 做过了347结果还fail掉这题，真的是耻辱！
- [0692. Top K Frequent Words](Solutions/0692.Top-K-Frequent-Words.py) (!!M) <br>
heapq solution: O(N + klogN); quick select solution: O(N + klogk)
- [0973. K Closest Points to Origin](Solutions/0973.K-Closest-Points-to-Origin.py) (M) <br>
（以squre来构建heap就可以了，heap中的元素是(square, point)） quick select is only O(N), I guess all the kth largest problem can use quick select.
- [0658. Find K Closest Elements](Solutions/0658.Find-K-Closest-Elements.py) (M) <br>
step 1: binary search to find the idx where x should be; step 2: put the closest k elements in a hq - O(klogk); step 3: output - O(klogk)
- [0378. Kth Smallest Element in a Sorted Matrix](Solutions/0378.Kth-Smallest-Element-in-a-Sorted-Matrix.py) (!!M) <br>
利用sorted matrix的性质，从左上角第一个元素开始，添加进heap，然后heap当然自动排序了，然后pop出最小的，然后把最小的那个数的右边和下边的元素分别入heap，这样可以保证每次pop出来的都是最小的。1. use a heap to store (num, (row, col)); 2. use a set to check if row + 1, col + 1 visited already before push into the heap; Solution 2: binary search 了解一下。<br>
- [0023. Merge k Sorted Lists](Solutions/0023.Merge-k-Sorted-Lists.py) (!!H) <br>
maintain一个heapq，初始化将每个list的head放入，然后每次pop出一个最小的，再把最小的那个的.next push进heapq, O(NlogK); we should overriding ListNode compare function ____ lt__ to make customized compare happens: compare ListNodeSolution 2: divide and conquer, the same as merge sort. O(NlogK) 如果不记得override ____ lt__ 怎么写的话就乖乖写merge sort 吧
- [0373. Find K Pairs with Smallest Sums](Solutions/0373.Find-K-Pairs-with-Smallest-Sums.py) (M) <br>
heap solution: klogk, very simlilar with merge k sorted list. 方法二：将两个list各挑一个数出来的加和做成一个2D Array, 由于两个list都是sorted, 那么这个2D array就是与378同样sorted array了, 然后按照378那样解就可以了。
- [0632. Smallest Range Covering Elements from K Lists](Solutions/0632.Smallest-Range-Covering-Elements-from-K-Lists.py) (!!H) <br>
题目实际上是在问从所有的list中各取一个数，这些数里的[min, max]就是我们合格的range.
求最小的合格range是什么？
这种关注diff的题其实变相的是在关注max_val和min_val, 我们往往可以通过一个hq来快速获取max_val， 
另一个hq来快速获取min_val。heapq solution: O(m+nlogm) where m is len(nums), n is len(lst). hq stores (the item in the lst, the lst_idx of where lst is in the nums, the num_idx where the num is in the lst). whenver a min_val is popped, we compare the max_val-min_val with the previous diff. 
Then we push (nums[lst_idx][num_idx+1], lst_idx, num_idx+1) into the heapq and update max_val in the heapq.
- [0621. Task Scheduler](Solutions/0621.Task-Scheduler.py) (!!M) <br>
we only need to be concerned about tasks with higher frequencies. This makes it a perfect candidate for a Priority Queue, or a Max-Heap. 维护一个最大堆 by using negative freq
- [0358. Rearrange String k Distance Apart](Solutions/0358.Rearrange-String-k-Distance-Apart.py) (!!H) <br>
这种间隔k个位置安排座位的问题，都是task schedule的做法！similar with task schedule, 我们按频率从大到小去坐k个位置，pop出来之后需要将freq-=1然后push回去, pop出来再push回去的思想很重要！！
-----------1054. Distant Barcodes-----------
- [0767. Reorganize String](Solutions/0767.Reorganize-String.py) (!!M Google) <br>
这种间隔k个位置安排座位的问题，都是task schedule的做法！这一题k=1. 用一个hq保存最大的freq, 然后按要求排座位，注意add_back. # case 1: if we can put seat ch into res, then go ahead and seat it it; # case 2: if there is already to same ch on top of res, then we cannot seat the 1st_freq ch, instead, we seat the 2nd highest freq
- [1405. Longest Happy String](Solutions/1405.Longest-Happy-String.py) (!!M) <br>
这种间隔k个位置安排座位的问题，都是task schedule的做法！similar with task schedule, 对于这题，我们先判断把最high freq的ch pop出来加入res, 然后freq-1放回hq中. # case 1: if we can put seat ch into res, then go ahead and seat it it; # case 2: if there is already to same ch on top of res, then we cannot seat the 1st_freq ch, instead, we seat the 2nd highest freq
- [0263. Ugly Number](Solutions/0263.Ugly-Number.py) (E) <br>
warm up for the next question.
- [0264. Ugly Number II](Solutions/0264.Ugly-Number-II.py) (M) <br>
维护一个heapq，让它记录从小到大的ugly number, 每次pop出一个currMin，然后生成三个数2* currMin, 3*currMin, 5*currMin, 如果not in seen, 就push进heapq
- [0313. Super Ugly Number](Solutions/0313.Super-Ugly-Number.py) (M) <br>
Exactly the same as 264
- [0407. Trapping Rain Water II](Solutions/0407.Trapping-Rain-Water-II.py) (!!H) <br>
Similar with 42. 1D trapping rain water. 1D trapping rain water 是用双指针，一个指针记录左边漏水或储水的可能情况，一个指针记录右边漏水或储水的可能情况。 Step 1: store all the outliners of the matrix in heapq.  Maintain a visited set to mark all the visited locations. Step 2: starting from the min height position, do BFS the 4 possible moves. If found a height < the min Height, then we can store water, else we cannot store water and we should update this leaking point by putting the new height into the heapq
- [0295. Find Median from Data Stream](Solutions/0295.Find-Median-from-Data-Stream.py) (!!H) <br>
定义两个heap: self.leftHq as a maxheap to store the nums that are smaller than median; and self.rightHq as a minheap store the nums that are larger then median.  每次新增一个数num的时候，先根据比 maxheap 中最后一个数大还是小丢到对应的 heap 里。丢完以后，再处理左右两边的平衡性:如果左边太少了，就从右边拿出一个最小的丢到左边。如果右边太少了，从左边拿出一个最大的丢到右边。时间复杂度是O(logN). Follow up questions are important. 
Follow up: leetcode 1093
- [0480. Sliding Window Median](Solutions/0480.Sliding-Window-Median.py) (!!H) <br>
Solution 1: maitain a sorted window.  We can use binary search for remove and insert. 
the overall time complexity is O(nk), because insert takes O(k).
Solution 2: similar with LC 295, we need to maintain two heaps in the window, leftHq and rightHq. 
To slide one step is actually to do two things: step 1. add a number, which is exactly the same as that in LC 295, which is O(logk)
step 2. remove the number that is outside the window; there is not a remove method in heapq, so it takes O(k).
Solution 3: use a SortedList structure, which was implemented using self-balanced tree.  
SortedList enables O(logk) add and remove.  So the total time complexity is O(nlogk) 
- [0871. Minimum Number of Refueling Stops](Solutions/0871.Minimum-Number-of-Refueling-Stops.py) (!!H Google) <br>
像这种求极值的问题，十有八九要用动态规划 Dynamic Programming 来做，
但是这道题的 dp 定义式并不是直接来定义需要的最少加油站的个数，那样定义的话不太好推导出状态转移方程。
正确的定义应该是根据加油次数能到达的最远距离，我们就用一个一维的 dp 数组，其中 dp[i] 表示加了i次油能到达的最远距离，
dp[i+1] = max(dp[i] + stations[j][1] among all the station that dp[i] can reach) - O(n^2);
return the first i where dp[i] >= target. 
solution 2: heapq - O(nlogn)
heapq stores the fuel at the station. 这题的关键是不要考虑到达的那个station的位置，
我们永远只需要考虑从0出发，中途能加多少油，加的油越多跑得越远. 维护一个possible_coverage变量表示能跑多远. 这个题目用hq的方式跟Dikstra's有点像，都是要贪心地pop出最优解！
- [DIDI OA. Min Deletions to Make Frequency of Each Letter Unique](Solutions/DIDI_OA.py) (!!M) <br>
- [1167. Minimum Cost to Connect Sticks](Solutions/1167.Minimum-Cost-to-Connect-Sticks.py) (M) <br>
我们需要实时地保证选出两个数是最小的, heappop可以保证这一点，所以用heapq



# [Intervals/Sweep-Line](/Sweep-Line.py) <br>
- [0252. Meeting Rooms](Solutions/0252.Meeting-Rooms.py) (E) <br>
O(nlogn). 题目问一个人能不能参加所有的meeting, a person could attaned all meetings if there is not intervals overlapping, 只需要sort the intervals比较前一个end time与后一个start time即可
- [0391. Number of Airplanes in the Sky](Solutions/0391.Number-of-Airplanes-in-the-Sky.py) (M Lintcode) <br>
扫描线做法：碰到interval的start，也就是起飞一架飞机，当前天上的飞机数++。碰到interval的end，也就是降落一架飞机，当前天上的飞机数--。
Step 1: 我们分别把所有的start和所有的end放进两个数组，并排序。Step 2: 然后从第一个start开始统计，碰到start较小就加一，碰到end较小就减一。并且同时维护一个最大飞机数的max。
- [0253. Meeting Rooms II](Solutions/0253.Meeting-Rooms-II.py) (!!M) <br>
solution 1: 扫描线；minimum meeting rooms required could be understood us maximum meeting rooms in use
Then this problem is exaclty the same as the lintcode 0391. Number of Airplanes in the Sky <br> solution 2: 先把interval进行sort: intervals.sort(key = lambda x: (x[0], x[1])), 然后以end时间来构造最小堆，每次进来一个interval比较其start与最小的end，如果start较小就需要开新房间
- [1094. Car Pooling](Solutions/1094.Car-Pooling.py) (!!M) <br>
这题可以叫meeting root III. 我们以end pos构造一个heapq, 每次把end pos小于start pos的pop出来. 以前觉得sweep line is better for meeting room II. 现在觉得solution 2 heapq 更具有普适性 for interval problems
- [0435. Non-overlapping Intervals](Solutions/0435.Non-overlapping-Intervals.py) (!!M) <br>
This is actually greedy algorithm: always pick the interval with the earliest end time. 
Step 1: sort the list based on the end time of the intervals, cuz we want to pick up the earliest end time.
step 2: maintain a min_end_time as we sweep over the intervals. each time, we compare the start time with the pointer.
if the current start time is larger than the pointer, then renew the pointer to be the new end time;
else then we will have to remove the current interval in order to to keep the end time as small as possible,  removed_cnt += 1
- [0452. Minimum Number of Arrows to Burst Balloons](Solutions/0452.Minimum-Number-of-Arrows-to-Burst-Balloons.py) (!!M) <br>
Step 1: sort the intervals by end time;
Step 2: sweep line: maintain a min_end time, at each interval, we compare the pointer with the interval start time.
if end >= interval start time: then there is overlap and we should wait so that later we can shot them together;
if end < interval start time, then we can shot the previously 积累下来的interveals, shots += 1, and move the end to the new interval end time
- [1288. Remove Covered Intervals](Solutions/1288.Remove-Covered-Intervals.py) (M) <br>
sort the intervals by the start time. Then compare each interval with previous intervals,
to see if curr interval has a smaller end time than any of the previous intervals.
we only need to compare with the largest end time in previous intervals.
we can maintain a hq for the end time of the previous intervals 
- [0056. Merge Intervals](Solutions/0056.Merge-Intervals.py) (!!M) <br>
这种interval的题目首先都需要sort, 因为我们总不可能一会处理前面的，一会处理后面的区间。 Sort the intervals first. Loop over the intervals:
If the curr_interval start time is larger than the largest end time in res, then the interval cannot be merged. 
If cannot be merged, then res.append(curr_interval), else then update the new end time: res[-1][1] = max(res[-1][1], curr_interval_end). 
Merge interval的算法非常重要，后面的题经常用到！！！
- [0759. Employee Free Time](Solutions/0759.Employee-Free-Time.py) (!!H) <br>
这题是merge interval的变形题: step 1: obtain all intervals of all employees; step 2: sort the intervals by start time; step 3: do 56. merge intervals, to update free time.
- [0616. Add Bold Tag in String](Solutions/0616.Add-Bold-Tag-in-String.py) (!!M) <br>
step 1: store the (start_idx, end_idx) for every appearance of substring in s.  Algorithm: 28. Implement strStr() Rabin Karp - O((M+N)* W), where N is len(s), M is avg lens of words in dict, and W is len(dict). step 2: now we have a list of (start, end) intervals, we merge interval so that we don't have overlaps anymore.  Algorithm: 56. merge intervals. step 3: add <b> and </b> pair to generate res
- [0057. Insert Interval](Solutions/0057.Insert-Interval.py) (!!H Google) <br>
Solution 1: Append the new interval to the intervals, and then do the merge interval problem. O(nlogn). Solution 2: add the interval as we run. If there is overlap, we update the new interval. 画个图会好理解很多。
- [0986. Interval List Intersections](Solutions/0986.Interval-List-Intersections.py) (!!M) <br>
这题是找两个Interval的overlaps, 和merge interval有点像，we update res as res.append([max_start, min_end]).
然后两个sweep line的指针，谁的end比较小，谁先往前挪一步
- [0352. Data Stream as Disjoint Intervals](Solutions/0352.Data-Stream-as-Disjoint-Intervals.py) (!!H) <br>
Solution 1: merge intervals. In addNum method, we just need to append a new interval [val, val] to the intervals - O(1).
In the getIntervals method, we do merge interval just lke 56. Merge intervals - almost O(n) to sort an almost sorted list using insertion sort.
- [0715. Range Module](Solutions/0715.Range-Module.py) (!!!H) <br>
Store intervals in a 1D sorted array. Use bisect_left and bisect_right to locate where the incoming interval should be. addRange and removeRange takes O(N). queryRange can also use bisect to locate where the interval location is, [left, right]必须在某一个且同一个range内才return True - O(logN),  这题需要很细致，没有完全弄明白。
- [1272. Remove Interval](Solutions/1272.Remove-Interval.py) (M) <br>
loop over the intervals, and compare each interval with the to_be_removed interval and update res.
一个interval与另一个interval的位置关系就三种情况(1. 没有交集; 2. 一个包含了另一个; 3. 有交集但是没有谁能完全包含谁)
- [1229. Meeting Scheduler](Solutions/1229.Meeting-Scheduler.py) (M) <br>
to find the overlap of two intervals. We loop over the two intervals. 
一个interval与另一个interval的位置关系就三种情况(1. 没有交集; 2. 一个包含了另一个; 3. 有交集但是没有谁能完全包含谁).
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
- [1897. Meeting Room III](Solutions/1897.Meeting-Room-III.py) (!!M Lintcode) <br>
sweep line + pre calculation solution: O(1) for queery. O(M + N) overall, M = len(intervals), N = len(ask)
- [1353. Maximum Number of Events That Can Be Attended](Solutions/1353.Maximum-Number-of-Events-That-Can-Be-Attended.py) (!!M) <br>
Sort events. use a min hq stores the end time of events cuz we want to pop the min end time first.
loop over the curr_time from 1 to max day 100000, each day, we do: 1. add new events that start before curr_time to hq so that we can attend the event;  2. remove the events that are already ended before curr_time; 3. greedily attend the event that ends soonest by popping from the hq, and update cnt += 1.
- [0630. Course Schedule III](Solutions/0630.Course-Schedule-III.py) (!!H) <br>
首先给课程排个序，按照结束时间的顺序来排序，我们维护一个当前的时间，对于每一个遍历到的课程，将该课程持续时间放入优先数组中,
并选择参加这个课程：更新结束时间，然后我们判断更新后的结束时间是否大于该课程的结束时间，如果大于，说明这门课程无法被如期完成，
此时我们要选择一门课gvie up掉，那么问题是我们该gvie up掉哪门课呢？
注意我们并不是直接gvie up掉这门课，而是选择gvie up掉用时最长的一门课，这也make sense，
因为我们的目标是尽可能的多上课，既然非要去gvie up掉一门课，那肯定是去掉耗时最长的课，
这样省下来的时间说不定能多上几门课呢
- [0218. The Skyline Problem](Solutions/0218.The-Skyline-Problem.py) (!!H) <br>
不难发现这些关键点的特征是：竖直线上轮廓升高或者降低的终点, 所以核心思路是：从左至右遍历建筑物，记录当前的最高轮廓，如果产生变化则记录一个关键点  
- [0699. Falling Squares](Solutions/0699.Falling-Squares.py) (!!H) <br>
solution 1: O(N^2). Every time a new square falls down, we check all the previous squares to see if there is any square beneath the current falling square. If we found that we have squares i intersect with the current falling one, which means my current square will go above to that square. Then we should update the max_h. solution 2: segment tree O(NlogN) https://leetcode.com/problems/falling-squares/discuss/409304/Python-Diffenrent-Concise-Solutions
- [0757. Set Intersection Size At Least Two](Solutions/0757.Set-Intersection-Size-At-Least-Two.py) (!!H) <br>
Greedy algorithm, 按结束为止排序，当两个结束位置相同时，起始位置大的排前面先处理，这也符合我们先处理小区间的原则, 用个数组v来表示集合S, 遍历intervals, case 1: 当前interval 与v没有任何交集；case 2: 有一个数字的交集；case 3: 已经有两个相同的数字了
- [1109. Corporate Flight Bookings](Solutions/1109.Corporate-Flight-Bookings.py) (!!M) <br>
solution 1: brutal force O(MN). solution 2: DP: O(m+n). for each interval [i, j, k], we need k more seats at day i, and we need k less seats at day j.
so we can pre-calculate how many more we need on each day and store in a list need.
dp[i]=how man yseats booked on day i. dp[i]=dp[i-1]+need[i]
- [0850. Rectangle Area II](Solutions/0850.Rectangle-Area-II.py) (!!H Google) <br>
sweep line solution: O(N^2logN).
This is two sweep line problem pieced together.



###  [Desgin](/)
- [0359. Logger Rate Limiter](Solutions/0359.Logger-Rate-Limiter.py) (!!!E Google) <br>
很简单，用一个dictionary存(message, last timestamp when message was printed)就可以了。Google followup: input在K长度内无序的，但是时间t+K之后的输入一定出现在t之后。比如K是5，
[4, foo], [1, foo], [0, bar], [6, bar] => 在[4, foo], [1, foo], [0, bar]内是无序的，但是[6, bar]一定出现在[0, bar]之后，因为6>0+5.
也就是短程无序，长程有序。这时候该怎么print输出呢？
用一个heapq, heapq里面存(timestamp, message), 用一个deque里面也存(timestamp, message), 当发现下一个时间大于当前最小时间+K，就pop出当前的最小的放入到deque里面去, 这样deque里面存的就是长短程都有序的了
- [0362. Design Hit Counter](Solutions/0362.Design-Hit-Counter.py) (!!M) <br>
很简单，用一个queue存hit的timestamp就可以了, 这种拿分题一定要细心，这里容易漏掉self.q是否为空的判断，导致扣分，要养成好习惯，用q[0]之前一定要判断q是否为空。Follow up:
What if the number of hits per second could be very large? Does your design scale?
这里不是用deque吗？deque里面默认是每一个时间戳hit了一次，如果需要记录每秒钟有几次hit，我们需要用到dictionary, 但是同时有需要deque一样的有序，
所以自然而然想到OrderedDict. 这样可以保证最多使用O(300)的空间, 还是要熟悉OrderedDict的方法的。
OrderedDict是deque的增强版，这一点在LRU那题中已经体现。
当然这一题也可以在q里面存(timestamp, how many hits are there in this timestamp)
- [0355. Design Twitter](Solutions/0355.Design-Twitter.py) (!!M) <br>
self.time = 0; self.follows = collections.defaultdict(set)  # key is user, val is a set of users that this use follows; self.tweets = collections.defaultdict(collections.deque)   # key is user, val is a deque of (time, tweetsId). 题目要求求top 10 recent posted tweetsId, 所以我们需要一个self.time记录时间，然后用heapq来求解top K问题
- [0353. Design Snake Game](Solutions/0353.Design-Snake-Game.py) (M) <br>
为了考虑到蛇太长转太多弯会咬到自己的情况，我们需要记录蛇的尾巴的位置，所以需要用一个deque.
Each time we eat a food, we update the head pos as new head pos, and update the tail pos as stay the same pos, 
if not eating a food, then update the head pos as new head pos, and update the tail pos by simply popping it out of the deque. 
- [0379. Design Phone Directory](Solutions/0379.Design-Phone-Directory.py) (M) <br>
self.available_pool = set(i for i in range(maxNumbers)), set除了可以set.remove(item)之外，还可以set.pop() a random item.
- [0676. Implement Magic Dictionary](Solutions/0676.Implement-Magi-Dictionary.py) (M) <br>
find all combination of input word, and search if one of them is in the word_set.
O(26L^2), where L is the lens of word that we want to serach. 也可以用Trie来解，但是比较麻烦不推荐。
- [0348. Design Tic-Tac-Toe](Solutions/0348.DesignTic-Tac-Toe.py) (M) <br>
use a hashmap for player1: key is row/col/dia, val is how many taken by player1 at row/col/dia; use another hashmap for player 2. 
then each time we place a position, we update the hashmap, which takes O(1)
- [1396. Design Underground System](Solutions/1396.Design-Underground-System.py) (M) <br>
one hashmap to store the checkin info: id -> (start station, start time).
another hashmap to store the travel info: (start station, end station) -> (total travel cnt, total time)
- [0635. Design Log Storage System](Solutions/0635.Design-Log-Storage-System.py) (M) <br>
use an arr self.log = [] to store the (id, timestamp) information. put method just append a new (id, timestamp) to list, retrieve method just O(N) travel the list.
Follow up: can we do better for retrieve method?
In put mehod, we can maitain a sorted list, using binary search to find where we should insert the new timestamp - O(N) (if use sotedList in Python, then O(logN)).
In retrive method, we can use binary search to find where the start time locates and where the end time locates. It takes O(logN)
- [1472. Design Browser History](Solutions/1472.Design-Browser-History.py) (M) <br>
one list store the browse history, one pointer point at where we are at the list.
- [1244. Design A Leaderboard](Solutions/1244.Design-A-Leaderboard.py) (M) <br>
use a dictionary for fast addscore and reset. use a heapq to find top K elements
- [1286. Iterator for Combination](Solutions/1286.Iterator-for-Combination.py) (M) <br>
use backtrack to find all the possible combinations, then put them in a deque so that we can output in lexicographical order.
- [1172. Dinner Plate Stacks](Solutions/1172.Dinner-Plate-Stacks.py) (!!H) <br>
use a stack to store all the stacks.  
Use a heapq to store all the leftmost available-to-push stack, by storing their idx.
- [0622. Design Circular Queue](Solutions/0622.Design-Circular-Queue.py) (!!M) <br>
we can use a Singly-Linked List. 也可以用double-linked-list这把宰牛刀也非常快
enqueue: we append the value to the tail; dequeue: we remove node from head.
front: the head; rear: the tail; isempty: cnt=0; isFull: cnt = k
- [0641. Design Circular Deque](Solutions/0641.Design-Circular-Deque.py) (!!M) <br>
queue就用singly-linked list, deque就用doubly-linked list. 1. create a dummy head and a dummy tail; For insertFront mehtod, 注意insert到dummy head后面而不是前面
- [0706. Design HashMap](Solutions/0706.Design-HashMap.py) (!!M) <br>
Resolve hash collision: approach 1: Seperate chaining; approach 2: Open addressing.  We implement seperate chaining: we use an arr of linked list to sore the keys: self.hashmap = [ListNode(-1, -1) for _ in range(self.SIZE)], store linked list head in the arr,ListNode(-1, -1)是一个dummy node, 方便后续操作. Time complexity for seach/put/get is O(n/m) on average, where m is the talbe size, n is number of keys in the table.
- [0705. Design HashSet](Solutions/0705.Design-HashSet.py) (E) <br>
similar with design hashmap, we use seperate chaining to resovle collision.
- [1206. Design Skiplist](Solutions/1206.Design-Skiplist.py) (!!H) <br>
Each node has 2 pointers: "next" targets to the next node in the same level, "down" targets the "next" level node. We need to define a helper function to find the largest node that is smaller than search target in all levels. If you add a node in a level, all levels after that also need to be added.  In add mehtod, we need to use random function to randomly choose if we want to add the node into upper levels.


# [Big Data]()
- [0349. Intersection of Two Arrays](Solutions/0349.Intersection-of-Two-Arrays.py) (!!E) <br>
Facebook follow up: what if the lists are sorted and you are requred to use O(1) space. Approach: two-pointers solution, 注意去重的方法！！
- [0350. Intersection of Two Arrays II](Solutions/0350.Intersection-of-Two-Arrays-II.py) (!!E) <br>
Fackbook follow up 1: what if sorted? solution is using two-pointers. Follow up 2: what if size of nums1 is small? solution is binary search.  Follow up 3: what if nums2 is so large that it cannot fit in the memory? solution: Divide nums2 into n chunks of 1/n size and load 1/n piece each time. Follow up 4: What if neither nums1 or nums2 can fully fit in memory? solution: external sort + n chunks + two pointers.
- [1213. Intersection of Three Sorted Arrays](Solutions/1213.Intersection-of-Three-Sorted-Arrays.py) (E) <br>
sorted arr, three-pointers 就可以了
- [1570. Dot Product of Two Sparse Vectors](Solutions/1570.Dot-Product-of-Two-Sparse-Vectors.py) (!!!M Facebook) <br>
solution 1: use list to store the non-zero items then two pointers. O(M + N + m + n) where M is how many items in nums, m is how many non-zero items in nums.
solution 2: use dictionary to store the non-zero items. O(M + N + min(m, n))
- [0311. Sparse Matrix Multiplication](Solutions/0311.Sparse-Matrix-Multiplication.py) (!!!M Facebook) <br>
Sparse matrices, which are common in scientific applications, are matrices in which most elements are zero. To save space and running time it is critical to only store the nonzero elements. Many real world applications of vectors include sparse vectors. An example of it in Machine Learning is the popular one-hot encoding method for categorical computation. We can use a dictinoary to store the index and value of non-zero values, O(M+N + mn), O(M+N), M is the number of elements in matrix A, m is the number of non-zero elements in A.
- [0289. Game of Life](Solutions/0289.Game-of-Life.py) (M) <br>
solution 1: O(MN), O(MN) solution, should be noted that we cannot use shallow copy for 2D nested list. Have to use deep copy.  Solution 2: O(MN), O(1) solution, Two traversals. Traversal 1: dead -> live: mark as 2; live -> dead: -1  can be whatever number you want, it's just for mark.
Traversal 2: re-mark 2 to 1, -1 to 0.  Follow up: what if the board is infinite and matrix is sparse? If matrix is sparse, we use a dictionary to store the position of 1s. If the board is infinite and we cannot read the whole board into the memory, then we can read three rows each time because the live or dead state only depends on the up row and down row.
- [0849. Maximize Distance to Closest Person](Solutions/0849.Maximize-Distance-to-Closest-Person.py) (E) <br>
step 1: check what is the distace if he sits at two ends;
step 2: check what is the distance if he sits in the middle, two pinters: same method as 245. Shortest Word Distance III. warm up for next question.
- [0855. Exam Room](Solutions/0855.Exam-Room.py) (M) <br>
Use a sorted list to record the index of seats where people sit, so that we can save tons of space if the seats is sparse;
seat(): 1. find the biggest distance at the start, at the end and in the middle. 2. insert index of seat into the idx list. 3. return index.
leave(p): pop out p.
- [0609. Find Duplicate File in System](Solutions/0609.Find-Duplicate-File-in-System.py) (!!M) <br>
build a content_to_dir dictionary where key is content in txt file, val is a list of dir holding the content eg: ["root/a/1.txt"];
需要用到string.split(char), string.index(substring). Super important follow up questions for big data.
- [0766. Toeplitz Matrix](Solutions/0766.Toeplitz-Matrix.py) (!!E Google) <br>
Big data. 遍历整个matrix, 每次都与其右下角的数进行比较. 遇到这么简单的题，follow up 就不会太简单了, 三个follow up很重要！！




# [Data Stream and Multiple Query]()
- [0243. Shortest Word Distance](Solutions/0243.Shortest-Word-Distance.py) (E) <br>
Should know both two pass solution and One pass solution. follow up 1:  如果word1在words中很少只有两个，word2在words中很多有1 million个，怎么优化算法？那么这时候solution 1就派上用场了，我们可以存下idx1 和 idx2两个list. eg: idx1 = [10, 50000]; idx2 = [.......], 那么我们可以在idx2中binary search离10最近的数，然后binary search离50000最近的数。这样时间复杂度就是O(MlogN)了。
Follow up 2: 如果题目改成不是求两个word的最短距离而是是求K个word的最短距离呢？ solution 1: leetcode 76. Minimum Window Substring.  O(N) where N is the the lens of words.  soltution 2: leetcode 23. Merge k Sorted Lists.  O(NlogK), 方法与solution 1类似，只是为了知道k个idx list中哪根指针需要往前移动一下, 我们需要一个heapq, heapq中最小的那个往前挪动一步.
- [0244. Shortest Word Distance II](Solutions/0244.Shortest-Word-Distance-II.py) (!!M) <br>
如果题目要求multiple query with unlimited time, 那么一定考察的是precomputation!! precomputation记录结果一般都需要一个hash map!! 
这个思想非常重要！！这个题用dictionary记录每个word在words中的位置，这样如果这次需要query a and b, 下次需要query c and d, 
我们都可以很快找到他们的位置。    # 注意可能会有重复的query，比如第一次query a and b, 第三次又需要query a and b, 这时候为了为了避免重复计算，我们可以直接用memo/cache保存query a and b 的结果, 这个思想非常重要！！这个思想成立的前提是memory不值钱！Follow up 1: 
你都用两个额外空间去存结果以达到加速的目的了（一个是dictinoary存放每个word在words中的位置，另一个是cache/memo记录已经query过的a and b的结果）,可是面试官还不开心，他还希望调用 query method 能更快一些，怎么办？那咱们就采用最极端的方法：把所有words里可能的word1 and word2组合的结果都算出来存到cache中，这样所有的query 就都是O(1)了这个方法的前提是words list是不会变的，如果重新instantiate一个class把constrcutor里的words list变了那之前的所有结果就都白算了。
- [245. Shortest Word Distance III](Solutions/0245.Shortest-Word-Distance-III.py) (M) <br>
word1 and word2 may be the same and they represent two individual words in the list. 分word1等于和不等于两种情况讨论就可以了。
- [0460. LFU Cache](Solutions/0460.LFU-Cache.py) (!!!H) <br>
Use a dictionary to store (key, freq) pair.
Use another dicitonary to store (freq, list of keys) pair, where list of keys could be OrderedDict like LRU to enable O(1) operations.
其实是在LRU的基础上加了一个frequency的要求。
Follow up 变形题snapchat：在一个data stream 中find top K most frequent number用LFU来解，也可以用heapq O(Nk).



# [Random/Sampling](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
### [Shuffle]()
- [0384. Shuffle an Array](Solutions/0384.Shuffle-an-Array.py) (!!M Google) <br>
step 1: generate a random idx after i;
step 2: swap the num in i with random idx after i, then we have got the random num for ith pos;
step 3: keep going forward until we generate all the random num using the generated random idx;
follow up是写test方案证明自己写的shuffle符合要求
- [0528. Random Pick with Weight](Solutions/0528.Random-Pick-with-Weight.py) (!!!M Google) <br>
step 1: create a __prefix sum arr__; step 2: generate a rand_idx; step 3: __binary search__ to find where the idx is in the prefix_sum arr; follow up 是设计一个class支持修改已有元素的权重, 可能要用到数的结构实现o(logn)吧，没弄明白
- [Google Random Point in Non-overlapping intervals](Solutions/Google__Random-Point-in-Non-overlapping-intervals.py) (!!!M Google) <br>
Given a list of non-overlapping intervals, generate a number that is drawn uniformly from one of the intervals. <br>
Similar with random pick with weight, here we use number of points in the interval as weight.
Firslty, create a weight list w, where w[i] is the number of points in the interval. 
Secondly, use a prefix_sum list to store the prefix_sum of the weight list.
Then generate a rand_int and use binary search to find which rectangle the rand_int belongs to. 
- [0497. Random Point in Non-overlapping Rectangles](Solutions/0497.Random-Point-in-Non-overlapping-Rectangles.py) (!!!M) <br>
Similar with random pick with weight, here we use number of points in the rectangle as weight.
Firslty, create a weight list w, where w[i] is the number of points in the rectangle. 
Secondly, use a prefix_sum list to store the prefix_sum of the weight list.
Then generate a rand_int and use binary search to find which rectangle the rand_int belongs to. 
- [0380	Insert Delete GetRandom O(1)](Solutions/0380.Insert-Delete-GetRandom-O(1).py) (!!!M Google) <br>
这道题让我们在常数时间范围内实现插入删除和获得随机数操作，如果这道题没有常数时间的限制，那么将会是一道非常简单的题，直接用一个 HashSet 就可以搞定所有的操作。
但是由于时间的限制，无法在常数时间内实现获取随机数，所以只能另辟蹊径。此题的正确解法是利用到了一个一维数组和一个 HashMap，
其中数组用来保存数字，HashMap 用来建立每个数字和其在数组中的位置之间的映射，
对于插入操作，先看这个数字是否已经在 HashMap 中存在，如果存在的话直接返回 false，不存在的话，将其插入到数组的末尾，然后建立数字和其位置的映射。
删除操作是比较 tricky 的，还是要先判断其是否在 HashMap 里，如果没有，直接返回 false。由于 HashMap 的删除是常数时间的，而数组并不是，为了使数组删除也能常数级，
实际上将要删除的数字和数组的最后一个数字调换个位置，然后修改对应的 HashMap 中的值，这样只需要删除数组的最后一个元素即可，保证了常数时间内的删除。
而返回随机数对于数组来说就很简单了，只要随机生成一个位置idx，返回该位置上的数字即可.
Google follow up: 对一棵二叉树做增删改node操作，如何get random node，可能把树的node加到list里面吧
- [0381. Insert Delete GetRandom O(1) - Duplicates allowed](Solutions/0381.Insert-Delete-GetRandom-O(1)-Duplicates-allowed.py) (!!H) <br>
这题是之前那道 Insert Delete GetRandom O(1) 的拓展，与其不同的是，之前那道题不能有重复数字，而这道题可以有，
那么就不能像之前那道题那样建立每个数字和其坐标的映射了，但是我们可以建立数字和其所有出现位置的集合set之间的映射，
虽然写法略有不同，但是思路和之前那题完全一样。
对于 insert 函数，我们在数组 nums 末尾加入 val，然后将val所在 nums 中的位置idx加入 dict[val] set中。
remove 函数是这题的难点，我们首先看 HashMap 中有没有 val，或者有val但是对应的idx set 为空，则直接返回 false。
然后跟380是一样的。我们取出 nums 的尾元素和要删除的元素调换位置，
如果dict[val]有多个元素，那我们就pop set中的一个元素，当然要记录其对应的idx然后把idx的位置填上last_num, 还要更新last_num在pos_dict中的新位置。
- [0710. Random Pick with Blacklist](Solutions/0710.Random-Pick-with-Blacklist.py) (H) <br>
建立一个tricky的一一映射。
既然数字总共有N个，那么减去黑名单中数字的个数，就是最多能随机出来的个数。比如N=6，黑名单中有两个数{2, 4}，那么我们最多只能随机出四个随机数0,1,3,5，
但是我们如果直接randrange(4)的话会得到0,1,2,3, 我们发现有两个问题，一是黑名单中的2可以随机到，二是数字5没法随机到。
那么我们想，能不能随机到0,1,3就返回其本身，而当随机到2到时候，我们返回的是5， __我们需要建立这样的映射把2映射到5, 这就是使用HashMap的动机啦__
- [0519. Random Flip Matrix](Solutions/0519.Random-Flip-Matrix.py) (M) <br>
没搞明白想干嘛


### [Reservoir Sampling]()
- [0398. Random Pick Index](Solutions/0398.Random-Pick-Index.py) (!!M)  <br>
Reservoir Sampling solution reservoir sampling 特点是来一个算一下，因此适用于data stream with unknown length. 算法：
来第一个num: 选第一个num的概率为1/1；<br>
来第二个num: 选第二个num的概率为1/2; 选第一个num的概率为(1-1/2)* 1/1 = 1/2 <br>
来第三个num: 选第三个num的概率为1/3; 选第一个num的概率为(1-1/3)* 1/2 = 1/3; 选第一个num的概率为(1-1/3)* 1/2 = 1/3 <br>
来第四个num: 选第四个num的概率为1/4; 选第一个num的概率为(1-1/4)* 1/3 = 1/4; 选第二个num的概率为(1-1/4)* 1/3 = 1/4; 选第三个num的概率为(1-1/4)* 1/3 = 1/4; <br>
来第m个num: 选第m个num的概率为1/m; 选第一个num的概率为(1-1/m)* 1/(m-1) = 1/m..........
- [0382. Linked List Random Node](Solutions/0382.Linked-List-Random-Node.py) (!!M Google) <br>
Linkedlist has unknow length so we use reservior sampling: O(1), O(n). It is good for really large linkedlist and the linkedlist dynamically changing length; solution 2: O(n), O(1) just use an arr to store all the node vals


### [Rejection Sampling]()
- [0470. Implement Rand10() Using Rand7()](Solutions/0470.Implement-Rand10-Using-Rand7.py) (!!M) <br>
This solution is based upon Rejection Sampling. 
The main idea is when you generate a number in the desired range, output that number immediately. 
If the number is out of the desired range, reject it and re-sample again. 
Step 1: generate one rand_int1 in range (1, 7),  step 2: generate another rand_int2 in range (1, 7). Then from 7 * rand_int1 + rand_int2, we can get a random number in range (1, 49).
- [0478. Generate Random Point in a Circle](Solutions/0478.Generate-Random-Point-in-a-Circle.py) (!!!M) <br>
we use Polar coodinates. step 1: generate one rand_int1 for radius; step 2: generate anoter rand_int2 for angle. 注意对rand_int1要取平方根, 这是因为random.randrange()取的点在线性范围内是uniform的，但是在2D圆内不是



# [Recursion](/Binary-Tree-Divide-and-Conquer.py) <br> 
### [Recursion in Array](/Binary-Tree-Divide-and-Conquer.py) <br> 
- [0723. Candy Crush](Solutions/0723.Candy-Crush.py) (!!M Google) <br>
Recurssion. step 1: check horizontal and vertical crush and changed the board[i][j] that needs to be crushed to negative.
step 2: do gravity to modify the board.
step 3: recurssively modify the board until is there is crush needed. O((MN)^2)
- [0412. Fizz Buzz](Solutions/0412.Fizz-Buzz.py) (E) <br>
How to do it without for-loop: recursion
- [0679. 24 Game](Solutions/0679.24-Game.py) (!!H Google) <br>
方法：两个for loop在nums中取两个数nums[i] and nums[j]. 算出nums[i] and nums[j]这两个数加减乘除可能得到的数，
将这些可能得到的数放进next_nums里面进行递归。递归的结束条件是len(nums)==1即无法再跟其他书加减乘除了。
如果len(nums)==1 and nums[0]==24, then return True
- [Pramp__121920__Flatten-a-Dictionary](Solutions/Pramp__121920__Flatten-a-Dictionary.py) (M) <br>


### [Binary Tree](/Binary-Tree-Divide-and-Conquer.py) <br> 
- [0144. Binary Tree Preorder Traversal](Solutions/0144.Binary-Tree-Preorder-Traversal.py) (M) memorize the iterative version using stack
- [0094. Binary Tree Inorder Traversal](Solutions/0094.Binary-Tree-Inorder-Traversal.py) (M) memorize the iterative version using stack
solution 2: in order traversal of BST (iteratively) - O(k+H) where H is height of tree. solution 1: trivial - in order traversal of BST - O(N), O(N).
- [0104. Maximum Depth of Binary Tree](Solutions/0104.Maximum-Depth-of-Binary-Tree.py) (E) <br>
rootDepth = max(leftDepth, rightDepth) + 1
- [0226. Invert Binary Tree](Solutions/0226.Invert-Binary-Tree.py) (E) <br>
- [0617. Merge Two Binary Trees](Solutions/0617.Merge-Two-Binary-Trees.py) (E) <br>
- [0257. Binary Tree Paths](Solutions/0257.Binary-Tree-Paths.py) (!!E) <br>
求path, 第一反应当然是dfs了
- [0112. Path Sum](Solutions/0112.Path-Sum.py) (E) <br>
求path, 第一反应当然是dfs了
- [0113. Path Sum II](Solutions/0113.Path-Sum-II.py) (!!M) <br> 
Solution 1: 碰到打印所有路径的问题，第一反应就是带backtracking the dfs
- [0437. Path Sum III](Solutions/0437.Path-Sum-III.py) (!!M) <br>
不需要从根节点出发，solution 1: dfs every node in the tree. at each node, do a backtrack to find how many root-to-any_node paths are there. 
solution 2: dfs + memorization. 用 HashMap 来建立路径之和跟其个数之间的映射，即路径之和为 curSum 的个数为 m[curSum].
- [0129. Sum Root to Leaf Numbers](Solutions/0129.Sum-Root-to-Leaf-Numbers.py) (!!M) <br> 
solution 1: similar with 113, backtrack;
solution 2: Morris Preorder Traversal  O(N), O(1).
- [0596. Minimum Subtree](Solutions/0596.Minimum-Subtree.py) (LintCode) <br>
Divide and Conquer的方法输出以root为根的subTree的subSum，然后每次与minSum打擂台进行比较，注意python中定义全局变量可以用self.minSum = float("inf"), self.minNode = None，在主函数中定义这两个变量就可以了. 这种题应该是送分题！
- [0597. Subtree with Maximum Average](Solutions/0597.Subtree-with-Maximum-Average.py) (LintCode) 同上 Divide and Conquer
- [0124. Binary Tree Maximum Path Sum](Solutions/0124.Binary-Tree-Maximum-Path-Sum.py) (!!H) <br>
题意应该是任何path都可以，只要点和点连接在一起就算一个path，起点和终点doesn't matter. 方法是定义一个self.maxSum在helper函数中去打擂台。helper 函数return the maxPathSum for tree ended with root: return max(left of root, right of root) + root.val; 打擂台: self.maxSum = max(self.maxSum, leftmax + rightMax + root.val). 注意打擂台的self.maxSum和非打擂台的变量和helper function return的变量是不一样的，这是本题的难点。
- [0687. Longest Univalue Path](Solutions/0687.Longest-Univalue-Path.py) (!!M) <br>
在binary tree里求longest path问题，如果任何path都算数的话，那么我们在divide and conquer的时候要分成两种情况讨论：1. path ended with root; 2: path not ended with root. 我们往往需要在helper函数中返回end_w和end_wo两种情况的值, 有时候也可以将case 2细分为: I. path pass the root, and II. path without the root.
- [0298. Binary Tree Longest Consecutive Sequence](Solutions/0298.Binary-Tree-Longest-Consecutive-Sequence.py) (!!M) <br> 
helper function returns (the LCS ended with root, without root)
- [0549. Binary Tree Longest Consecutive Sequence II](Solutions/0549.Binary-Tree-Longest-Consecutive-Sequence-II.py) (!!M) <br> 
helper function returns (the LCS ended with root decreasing, increasing, without root, pass root)
- [0968. Binary Tree Cameras](Solutions/0968.Binary-Tree-Cameras.py) (!!H) <br> 
helper function returns minimum number of cameras needed to cover all the node's children with (node not covered, node covered: 1. with a camera on node, 2. without a camera on node)
- [0834. Sum of Distances in Tree](Solutions/0834.Sum-of-Distances-in-Tree.py) (!!H) <br> 
sums(Y) = sums(X) + cnt(X) - cnt(Y) = sums(X) + (N - cnt(Y) - cnt(Y) = sums(X) + N - 2* cnt(X).
cnt[X]可以通过dfs遍历一次算出来存到一个list里面，这样我们如果已知sums(0)的话，
那么其余的sums(X)都可以通过上述公式算出来了
- [0110. Balanced Binary Tree](Solutions/0110.Balanced-Binary-Tree.py) (E) <br>
helper function return (if the tree is balanced, maxDepth); rootIsBalan = leftIsBalan and rightIsBalan and abs(leftMaxDepth - rightMaxDepth) <= 1
- [0543. Diameter of Binary Tree](Solutions/0543.Diameter-of-Binary-Tree.py) (!!E Facebook) <br>
helper function 是 104. Maximum Depth of Binary Tree, 在helper function 中用 self.maxDmtr 去打擂台, self.maxDmtr = max(self.maxDmtr, leftDepth + rightDepth).
注意这一题很容易错：可能root.left只有一个节点，而root.right有很多节点，这很多个节点中可能有很多左节点，所以max_diameter可能只发生在root的右半边
- [0236. Lowest Common Ancestor of a Binary Tree](Solutions/0236.Lowest-Common-Ancestor-of-a-Binary-Tree.py) (!!M) <br>
LCS都求不出来的话就别说自己会二叉树
- [Google Distance between two nodes in a binary tree](Solutions/Google__Distance-between-two-nodes-in-a-binary-tree.py) (!!M) <br>
Distance between two nodes in a binary tree. LCA_ndoe, return (node 1 to LCA_node distance) + (node 2 to LCA_node distance)
- [0235. Lowest Common Ancestor of a Binary Search Tree](Solutions/0235.Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py) (E) <br>
因为是BST, 所以if p.val < root.val < q.val or q.val < root.val < p.val or p.val == root.val or q.val == root.val: return root; Otherwise 要么去左边找要么去右边找。
- [0250. Count Univalue Subtrees](Solutions/0250.Count-Univalue-Subtrees.py) (!!M Google) <br>
root is a univalue subtree if left is and right is and root.val = left.val = right.val;
heper function returns (is root a univalue subtree, cnt of univalue subtrees for root)
- [0116. Populating Next Right Pointers in Each Node](Solutions/0116.Populating-Next-Right-Pointers-in-Each-Node.py) (M) <br>
BFS solution using q is trivial. Follow up: what if only use constant extra space?
我们可以设立两个指针，一根leftmost一直往下走，一根head在一层之中一直往右走，边走边连，zu以每次都是去连left_most下一层的Nodes
- [0117. Populating Next Right Pointers in Each Node II](Solutions/0117.Populating-Next-Right-Pointers-in-Each-Node-II.py) (M) <br>
BFS solution using q
- [0662. Maximum Width of Binary Tree](Solutions/0662.Maximum-Width-of-Binary-Tree.py) (M) <br>
涉及到处理level的信息，就用bfs, q里面存放(node, the postion of the node), 注意这里的pos到下一层的转换关系: q.append((node.left, 2* pos))
- [0655. Print Binary Tree](Solutions/0655.Print-Binary-Tree.py) (M) <br>
DFS, pass the depth and pos into the dfs arguments.
- [1104. Path In Zigzag Labelled Binary Tree](Solutions/1104.PathIn-Zigzag-Labelled-Binary-Tree.py) (M) <br>
完全一个数学找规律的题，没啥意思
- [0637. Average of Levels in Binary Tree](Solutions/0637.Average-of-Levels-in-Binary-Tree.py) (M) <br>
level order traversal using a q.
- [0404. Sum of Left Leaves](Solutions/0404.Sum-of-Left-Leaves.py) (E) <br>
dfs 中把is_left传入即可
- [1110. Delete Nodes And Return Forest](Solutions/1110.Delete-Nodes-And-Return-Forest.py) (!!!M Google) <br>
we update res as we traverse the tree. we append a node into res if two conditions are satisfied: 1. the node should not be deleted; 2. the node has not parent (meaning it's the root of a forest). In order to check if a node has parent or not, we need to pass has_parent bool into dfs arguments. If a node is in to_delete list, then the node should pass the information to it's children that it has been deleted and it's children has no parent now.
- [0814. Binary Tree Pruning](Solutions/0814.Binary-Tree-Pruning.py) (M) <br>
solution 1: my own solution: dfs visit each node, at each node, use a should_delete(node) function to tell
if this node should be deleted. - O(N^2).  solution 2: my own solution: divide and conquer, conquer: if not root.left and not root.right and root.val == 0: root = None
- [0563. Binary Tree Tilt](Solutions/0563.Binary-Tree-Tilt.py) (!!E) <br>
helper function return the sum of subtree, and the tilt of the subtree
- [0872. Leaf-Similar Trees](Solutions/0872.Leaf-Similar-Trees.py) (E) <br>
in order traversal to find the leaves of the tree and put them into a list
- [0366. Find Leaves of Binary Tree](Solutions/0366.Find-Leaves-of-Binary-Tree.py) (!!M) <br>
我们将leaf node的level定义为0, 那么紧紧邻接leaf node的level定义为1；
那么我们只需要将level相同的nodes存在一起就可以了；所以选用dict, key is level, val is a list of nodes on the level.
helper function returns the current level.
- [1145. Binary Tree Coloring Game](Solutions/1145.Binary-Tree-Coloring-Game.py) (M) <br>
The best move y must be immediately adjacent to x, since it locks out that subtree. check the 3 nodes that are adjacent to node x, find the number of nodes each subtree has.
Then check if palcing ynode at the 3 nodes adjacent to x will end up with more subtree nodes for y.
- [0971. Flip Binary Tree To Match Preorder Traversal](Solutions/0971.Flip-Binary-Tree-To-Match-Preorder-Traversal.py) (!!M) <br>
Return whether or not it matches to voyage. as we traverse the tree, use an index to in voyage v.
If current node == null, it's fine, we return true; If current node.val != arr[i], doesn't match wanted value, return false; If node.val != arr[i+1], flip left and right child.
- [0572. Subtree of Another Tree](Solutions/0572.Subtree-of-Another-Tree.py) (!!E) <br>
solution 1: brutal force: dfs to visit every node, at each node, stop and check if the subtree rooted
as that node is the same as t - O(MN); solution 2: O(M+N).  we can in order traversal the two trees and turn them into two strings s and t. 
Then the problem becomes exactly the same as finding a substring in s that equals t, which is 28. Implement strStr().
Use rolling hash, we can realize O(M+N) solution.
- [0156. Binary Tree Upside Down](Solutions/0156.Binary-Tree-Upside-Down.py) (M) <br>
不停的对左子节点调用递归函数，直到到达最左子节点开始翻转，翻转好最左子节点后，开始回到上一个左子节点继续翻转
- [0314. Binary Tree Vertical Order Traversal](Solutions/0314.Binary-Tree-Vertical-Order-Traversal.py) (M) <br>
record the position of each node as we dfs to traverse the tree. 记录在遍历过程中记录node位置的思想非常重要！
- [0987. Vertical Order Traversal of a Binary Tree](Solutions/0987.Vertical-Order-Traversal-of-a-Binary-Tree.py) (M) <br>
same as 314. in 314, left nodes output first, in 987, smaller value comes first. So the only difference is at sort
- [1026. Maximum Difference Between Node and Ancestor](Solutions/1026.Maximum-Difference-Between-Node-and-Ancestor.py) (!!M) <br>
helper function return max, min in root tree.  self.max_diff 打擂台.
- [0105. Construct Binary Tree from Preorder and Inorder Traversal](Solutions/0105.Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.py) (!!M) <br>
solution 1中需要O(N^2)的原因是1. preorder.pop(0) takes O(N). We can convert preorder into a deque and popleft. 2. finding the idx in inorder list takes O(N). We can use a hash table to store num-to-idx pair in advance. This leads to solution 2, which takes O(N) instead of O(N^2).
- [0106. Construct Binary Tree from Inorder and Postorder Traversal](Solutions/0106.Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal.py) (!!M) <br>
solution 1 takes O(N^2) because each time we find idx in inorder, it takes O(N). 算法：root = postorder.pop(), root.right = 处理inorder idx的右边, root.left = 处理inorder idx的左边. We can use a hash table to store the num-to-idx pair in advance. This leads to solution 2, which is O(N) instead of O(N^2).
- [0889. Construct Binary Tree from Preorder and Postorder Traversal](Solutions/0889.Construct-Binary-Tree-from-Preorder-and-Postorder-Traversal.py) (!!M) <br>
把这棵树画出来pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1] 自然就明白了代码怎么写了. O(N^2) solution and O(N) solution by storing idx in a hashmap in advance. 
- [1008. Construct Binary Search Tree from Preorder Traversal](Solutions/1008.Construct-Binary-Search-Tree-from-Preorder-Traversal.py) (!!M) <br>
the root is the arr[0], root.left = [1: idx] and root.right = [idx:], where idx is the first num that is larger than arr[0].
- [1028. Recover a Tree From Preorder Traversal](Solutions/1028.Recover-a-Tree-From-Preorder-Traversal.py) (!!H) <br>
step 1: store the (depth, node_val) information in a list; step 2: use that list to construct a Tree.
- [1469. Find All The Lonely Nodes](Solutions/1469.Find-All-The-Lonely-Nodes.py) (E) <br> 
simple dfs to visit every node, check if it is a lonely node when visit it.
- [1302. Deepest Leaves Sum](Solutions/1302.Deepest-Leaves-Sum.py) (M) <br> 
first dfs find the max depth, 2nd dfs get the sum of all nodes with max depth.
solution 2: level order bfs, 每次都在while循环里初始化max_depth_sums就可以保证输出的是最后一层的sums了，只需一次遍历
- [0979. Distribute Coins in Binary Tree](Solutions/0979.Distribute-Coins-in-Binary-Tree.py) (!!M) <br> 
The algorithm is: one node by another, try to balance node from down to top.
helper function returns how many coins should the node receive from it's parent in order to balance itself.
用一个全局变量打擂台记录移动了多少个coins
- [0894. All Possible Full Binary Trees](Solutions/0894.All-Possible-Full-Binary-Trees.py) (!!M) <br>
Good example of recurssion
- [0951. Flip Equivalent Binary Trees](Solutions/0951.Flip-Equivalent-Binary-Trees.py) (!!!H Google) <br>
recursion - O(min(N1, N2))
- [Check if value exists in level-order sorted complete binary tree](Solutions/Google__Check-if-value-exists-in-level-order-sorted-complete-binary-tree.py) (!!! Google) <br>
binary search and tree. step 1: find the level of the num by going check the left path; binary search on the located level. This is the hard part because unlike the conventional binary search, the nodes of this level cannot be accessed directly. we need to use gray code to locate the mid node in the level.
- [0222. Count Complete Tree Nodes](Solutions/0222.Count-Complete-Tree-Nodes.py) (!!M) <br>
solution 1: dfs to visit every node; solution 2: use the property of complete Tree: 通过比较left sub tree height and right sub tree height 可以之直接算出左边或者右边nodes的个数 - O(logN* logN). solution 3: similar with Check if value exists in level-order sorted complete binary tree: use gray code to enable binary search in the last level - O(logN* logN)

--------------1245. Tree Diameter---------



### [BST](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
- [0700. Search in a Binary Search Tree](Solutions/0700.Search-in-a-Binary-Search-Tree.py) (E) <br>
- [0669. Trim a Binary Search Tree](Solutions/0669.Trim-a-Binary-Search-Tree.py) (!!E) <br>
- [0270. Closest Binary Search Tree Value](Solutions/0270.Closest-Binary-Search-Tree-Value.py) (E) <br>
iterative vs. recursion. 我们可以直观地看到: BST这种树结构的search一般都是O(h)的, 因为我们是一路往下search的
- [0938. Range Sum of BST](Solutions/0938.Range-Sum-of-BST.py) (E) <br>
- [0108. Convert Sorted Array to Binary Search Tree](Solutions/0108.Convert-Sorted-Array-to-Binary-Search-Tree.py) (!!E) <br>
we can always choose the left middle number as root, or always choose right middle number as root, or sometimes left sometimes right as root. That is why the answer is not unique
- [0109. Convert Sorted List to Binary Search Tree](Solutions/0109.Convert-Sorted-List-to-Binary-Search-Tree.py) (!!M) <br>
这题是Linkedlist. 先分为左中右三个部分，然后divide and conquer - O(NlogN); 上述方法需要 O(NlogN)的原因是每次寻找中间点mid的时间都是O(N), 我们可以把linked list转化为arr,
这样我们找mid就只需要O(1)了, 这时候再根据Master's theorem: 我们通过O(1)的时间将T(N)的任务变成了2T(N/2)的任务，
所以总的时间复杂度是O(N)
- [0230. Kth Smallest Element in a BST](Solutions/0230.Kth-Smallest-Element-in-a-BST.py) (M) <br>
要会默写iterative version of in-order-traversal
- [0098. Validate Binary Search Tree](Solutions/0098.Validate-Binary-Search-Tree.py) (M) <br>
注意判断条件不仅仅是left.val<root.val<right.val而是max of left < root < min of right; helper函数返回以root为根的树(是不是BST，max and min value in the tree); if (isLeftBST and isRightBST and maxLeft < root.val < minRight): return True
- [0897. Increasing Order Search Tree](Solutions/0897.Increasing-Order-Search-Tree.py) (E) <br>
divide and conquer is good - O(N), O(1) 左连右连而已，很简单
- [0114. Flatten Binary Tree to Linked List](Solutions/0114.Flatten-Binary-Tree-to-Linked-List.py) (!!M) <br>
divide and conquer: root.right = leftHead; root.left = None; 找到tail并让tail.right = rightHead
- [0426. Convert Binary Search Tree to Sorted Doubly Linked List](Solutions/0426.Convert-Binary-Search-Tree-to-Sorted-Doubly-Linked-List.py) (!!M)  <br>
solution 1: 定义两个全局变量self.head, self.curr，进行in order traversal的过程中不断更新curr的位置并hook up nodes
- [0173. Binary Search Tree Iterator](Solutions/0173.Binary-Search-Tree-Iterator.py) (!!M) <br>
use a stack to store the left path nodes, some part of the algorithm is similar with the in order traversal of a tree using a stack; define a getLeftMost function, each time we call next function, we pop the smallestNode from stack and run getLeftMost function for the smallestNode.right if smallestNode.right exist.  this algorithm has space complexity of O(h)
- [0285. Inorder Successor in BST](Solutions/0285.Inorder-Successor-in-BST.py) (!!M) <br>
Divide and conquer: if p.val < root.val: return left if left else root; else: return right
- [0510. Inorder Successor in BST II](Solutions/0510.Inorder-Successor-in-BST-II.py) (!!M) <br>
Intersting problem, 题目input没有给Tree, 只给了node, 然后去找node's successor. 方法是找right_node, if not right_node就找parent_node.
- [0701. Insert into a Binary Search Tree](Solutions/0701.Insert-into-a-Binary-Search-Tree.py) (M) <br>
if val > root.val则更新root.right: root.right = self.insertIntoBST(root.right, val); else: root.left = self.insertIntoBST(root.left, val); return root.  这题的recursion exist should be: if not rot: return TreeNode(val). 另外, Time complexity: O(H), where H is a tree height. That results in O(logN) in the average case. So it takes O(logN) to insert an element into a BST.
- [0450. Delete Node in a BST](Solutions/0450.Delete-Node-in-a-BST.py) (!!M) <br>
Case 1: if node is a leaf, simply delete it Case 2: If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then delete the successor in the right subtree root.right = deleteNode(root.right, root.val). Case 3: If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val). define a function to find successor: find the successor of the root by taking one step right and always left, cuz the successor is the node just larger than the root. define a function to find predecessor: find the predecessor of the root by taking one step left and then always right. Delete a node in BST takes O(logN).
- [1214. Two Sum BSTs](Solutions/1214.Two-Sum-BSTs.py) (!!M) <br>
Iteratively do an inorder traversal for root1, and store the val in a hashSet; then itteratively do an inorder traversal for root2, and at the same time check if a target-val is in the hashSet. time complexity: O(M + N). 算法跟two sum是一样的，如果闭着眼睛能写要会iterative in-order traversal的哈！
- [0095. Unique Binary Search Trees II](Solutions/0095.Unique-Binary-Search-Trees-II.py) (!!M) <br>
helper(start, end): return the trees from start to end.  Finally return helper(1, n). Time complexity: The main computations are to construct all possible trees with a given root, that is actually Catalan number Gn (超纲).
- [0096. Unique Binary Search Trees](Solutions/0096.Unique-Binary-Search-Trees.py) (!!M) <br>
solution 1: brutal force, same as 95, return len(helper(1, n)). If we defind dp[i] = how many trees possible in a range with width == i, then we have
dp[j] = sum for (dp[i] * dp[j - i - 1] for all i < j)
- [0241. Different Ways to Add Parentheses](Solutions/0241.Different-Ways-to-Add-Parentheses.py) (!!M) <br>
similar with 95, in helper function, return all the different results to add parentheses for input, for i in range(len(s)): divide into leftResults and rightResults. Optimization: use a memo dictionary in the helper function to memorize the input that has already been calculated.
- [0530. Minimum Absolute Difference in BST](Solutions/0530.Minimum-Absolute-Difference-in-BST.py) (E) <br>
solution 1: in order traversal the BST and compare the prev_node and curr_node as we go. 
Need to use a global prev_node while doing in_order traversal. maintain a global prev_node的思想非常重要
- [0501. Find Mode in Binary Search Tree](Solutions/0501.Find-Mode-in-Binary-Search-Tree.py) (!!E) <br>
Trivial solution: dfs to visit every node and put their freq in a dict - O(N), O(N); Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count). solving BST problems is very similar with solving sorted arr problems, we just need to do in order traversal of the tree - O(N), O(1). 我们需要记录全局变量self.prev_node, self.curr_cnt, self.max_cnt.
- [0099. Recover Binary Search Tree](Solutions/0099.Recover-Binary-Search-Tree.py) (!!H) <br>
想想我们有一个sorted list, 里面有两个num被调换了，我们怎么恢复，当然是先遍历一遍list找到两个被调换的num, 然后调换过来。做BST的题目就是在做sorted list的题目，我们先in order traversal the list找到被调换了的list, 然后调换过来就可以了，Similar with the previous mode problem, we need to use a global prev_node, so that we can compare the adjacent nodes in the sorted arr. And we need self.first_swapped_node and self.second_swapped_node as global variable too.
- [0538. Convert BST to Greater Tree](Solutions/0538.Convert-BST-to-Greater-Tree.py) (E) <br>
use a global self.pre_sum as we reverse_in_order traversal the tree recurssively or iteratively.
- [1038. Binary Search Tree to Greater Sum Tree](Solutions/1038.Binary-Search-Tree-to-Greater-Sum-Tree.py) (M) <br>
和上一题出重复了



### [Nary Tree](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
- [0589. N-ary Tree Preorder Traversal](Solutions/0589.N-ary-Tree-Preorder-Traversal.py) (E) <br>
solution 1: Recurrsion; Solution 2: Iteration using a stack
- [0590. N-ary Tree Postorder Traversal](Solutions/0590.N-ary-Tree-Postorder-Traversal.py) (E) <br>
solution 1: Recurrsion; Solution 2: Iteration using a stack
- [0429. N-ary Tree Level Order Traversal](Solutions/0429.N-ary-Tree-Level-Order-Traversal.py) (E) <br>
Level order bfs using a queue
- [0559. Maximum Depth of N-ary Tree](Solutions/0559.Maximum-Depth-of-N-ary-Tree.py) (E) <br>
- [0431. Encode N-ary Tree to Binary Tree](Solutions/0431.Encode-N-ary-Tree-to-Binary-Tree.py) (H) <br>
The left child of a binary node is the subtree encoding all the children of the corresponding n-ary node.
The right child of a binary node is a chain of the binary root nodes encoding each sibling of the n-ary node.
Solution 1: bfs using q; Solution 2: dfs using recursion
Step 1). Link all siblings together, like a singly-linked list.
Step 2). Link the head of the obtained list of siblings with its parent node.




### [Trie](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
- [0208. Implement Trie (Prefix Tree)](Solutions/0208.Implement-Trie-(Prefix-Tree).py) (!!M) <br>
Firstly we need to define a TrieNode class, a TrieNode class hs two properties: 1. self.child = collections.defaultdict(TrieNode), use a defaultdict, key is char, value is TrieNode corresponding to the char.  2. self.isEnd = False   # return True if reached the end of the Trie.  Then implement 3 methods: insert(word), search(word), startWith(prefix); 注意currNode往下遍历时currNode = currNode.child[char]
- [0211. Add and Search Word - Data structure design](Solutions/0211.Add-and-Search-Word-Data-structure-design.py) (!!M) <br>
addWord mehtod is the same as 208 insert method. But search mehtod is a little different than search method in 208, cuz "." is a wildcard that can represent any char. So we use a queue to store (currNode, idx), then append layer by layer.
- [0677. Map Sum Pairs](Solutions/0677.Map-Sum-Pairs.py) (!!M) <br>
In TrieNode, define a self.sums 代表所有的子node所代表的string的val的和。
- [1233. Remove Sub-Folders from the Filesystem](Solutions/1233.Remove-Sub-Folders-from-the-Filesystem.py) (!!M) <br>
define has_prefix function in the Trie class, which returns whether or not there is already a string in the Trie that is the prefix of the word. step 1: sort the strings by lens. step 2: loop over all the words and check the has_prefix(word).
- [1166. Design File System](Solutions/1166.Design-File-System.py) (!!M) <br>
solution 1: In TrieNode class 定义一个self.val in TrieNode, 这样可以记录the value at the end of a word.  In Trie class, 定义一个self.get(word)函数，返回这个word对应的val. 像这种method里面函数很少的情况，需要额外写一些helper funciton, 还不如开一个Trie class 出来
- [0588. Design In-Memory File System](Solutions/0588.Design-In-Memory-File-System.py) (!!H) <br>
Trie solution: search/add/insert都是O(L)的时间复杂度，L是filePath的长度. 像这种method里面函数很多的情况，不需要额外写一些helper funciton, 最好直接把Trie的实现在已经给定的class里面
- [0820. Short Encoding of Words](Solutions/0820.Short-Encoding-of-Words.py) (!!M) <br>
find the words with common suffix using a Trie, we only keep the longest word among all the words that share the same suffix, so we need to sort the input words reversely by lens.
- [0745. Prefix and Suffix Search](Solutions/0745.Prefix-and-Suffix-Search.py) (!!H) <br>
solution 1: Trie. construct a pref-trie and a suff-trie. In the trie node, we should indlude the idx.  node.idx is a list consist of the idx of word in words.  solution 2: hashmap. pre-calculate the all the possible combination of prefix+"#"+suffix --> idx and store them in a dictionary. so that each query only takes O(1). This takes more space than the Trie solution, but much faster. 这一题体现了trade-off in performance between Trie solution and Hashmap solution. 像这种multiple query的题，由于query很频繁，所以hashmap就更有优势了
- [1032. Stream of Characters](Solutions/1032.Stream-of-Characters.py) (!!H) <br>
If we really think about it, this is a suffix problem: each time we query, we go back to the previous queried letters and check if they can form a word. Construct a Trie takes O(∑w_i) where w_i is the the lens of word in words.
- [0212. Word Search II](Solutions/0212.Word-Search-II.py) (!!H) <br>
we put the words into a trie. Then we loop over the board, whenever we found a letter==word[0], we trigger a backtrak. Backtrack 的结束条件是if curr_node.is_end. 打印所有路径所以用Trie + Backtracking DFS. 非常经典的题呀！
- [0425. Word Squares](Solutions/0425.Word-Squares.py) (!!H Google) <br>
Trie的解法怎样一步一步来的很重要！！把这题多写几遍backtrack+Trie+hashmap就都有更深的理解！
- [0648. Replace Words](Solutions/0648.Replace-Words.py) (M) <br>
这题是用prefix build一个Trie, 而通过这个Trie来query输入word的prefix. 因为需要输出prefix. 所以在TrieNode calss里面不是简单地用self.is_end来存是不是end, 而是需要self.word来存下这个word
- [0421. Maximum XOR of Two Numbers in an Array](Solutions/0421.Maximum-XOR-of-Two-Numbers-in-an-Array.py) (M) <br>
在TrieNode里面要定义一个self.val保存这个number的值，首先把所有的数的二进制存到 Trie 里面去，然后对于数组中的每个数 x，和 x 一起异或结果最大的 y 就是用 x 的二进制的反码在Trie 里面搜索，尽可能的与 x 的反码匹配，这样当走到叶子节点时，叶子节点对应的数就是 y。然后遍历一遍数组，求出 max(x ^ y), solution 写的很差，但是图画的很好！
O(32N), where N is len(nums), 32 is the height of the trie using format(num, '032b') to convert to 32 bit
- [0720. Longest Word in Dictionary](Solutions/0720.Longest-Word-in-Dictionary.py) (E) <br>
首先insert所有的word进Trie, 然后再将words list按照长度反向sort, 最后遍历words, 如果发现有一个word can_be_built, then return the word. 需要在Trie class里面写一个can_be_built(word)函数
- [0336. Palindrome Pairs](Solutions/0336.Palindrome-Pairs.py) (!!H) <br>
不用trie的解法更好做一些，有点动态规划的意思。遍历words, 对于某一个word1, 分成左右两部分left and right, 如果left等于另一个word2[::-1], 并且right is palindrome, then word1+word2可以组成一个panlindrome pair.
- [1268. Search Suggestions System](Solutions/1268.Search-Suggestions-System.py) (!!M) <br>
In TrieNode, there should be self.words = [], which stores a list of words that pass curr node.
- [0642. Design Search Autocomplete System](Solutions/0642.Design-Search-Autocomplete-System.py) (!!!H Google) <br>
与1268很像，只不过输入input_str是流数据，需要不断更新hotness. In TrieNode, there should be self.child, self.is_end, self.sentence, self.hotness. In Trie, there should be a method to insert a sentence into the trie; there should also be 
a method to search for all the possible autocomplete words of a given input string; 这个search mehtod分三步，第一步是遍历找到需要search的input_str在trie中所在的node, 第二步是从这个node出发，
找到其所有能到达的endNode, 显然是backtrack来做，第三步是对所有能达到的endNode.hotness排个序，取前三作为输出。
- [0527. Word Abbreviation](Solutions/0527.Word-Abbreviation.py) (!!!H Google) <br>
Trie. step 1: 建立一个abbrev函数：从idx开始，对 word 做abbreviation. step 2: 建立一个abbr2word保存 abbr-->word. step 3: 遍历建立好了的abbr2word。 for abbr, word_lst in abbr2word.items(), 
如果len(word_lst)==1, 那说明这个abbr是unique的，直接res.append(abbr); 如果len(word_lst)>1, 那说明这个abbr不是unique的，我们需要去寻找每一个word的unique prefix, 所以对这个word_lst就一个Trie, Trie中写一个find_idx函数 to where the prefix for word is unique (cur_node.cnt == 1)
Time Complexity: O(C) where C is the number of characters across all words in the given array. Space Complexity: O(C).




# [Union-Find](Union-Find-and-Trie.py)
像trie, union-find这样的数据结构，可以现在UnionFind class里面先把interface写好，然后再写主程序，写完主程序之后再回来写这些interface.
- [0589. Connecting Graph](Solutions/0589.connecting-graph.java) (!!M Lintcode) <br>
将a和b connect: 只需要将a和b的father connect就好；query a和b有没有连接:其实就是判断a和b在不在同一个集合里面，只需要判断find(a) == find(b)
- [0590 Connecting Graph II](Solutions/0590.Connecting-Graph-II.java) (!!M Lintcode) <br>
需要query 点a所在集合的元素个数，所以需要用一个list or dictionary self.sz 用来记录每个father节点所在集合的点的个数，在union i 和 j 的时候: father[i] = j, sz[j] += sz[i]; 在query点a所在集合的元素个数的时候: return self.sz[root of a]
- [0591. Connecting Graph III](Solutions/0591.Connecting-Graph-III.py) (!!M Lintcode) <br>
需要query 整个图中有多少个集合，所以需要一个self.counter, 用来记录图中集合的个数，在add(i)进图的时候, self.counter+=1, 在union i 和 j 的时候: father[i] = j, self.counter-=1;
- [0323. Number of Connected Components in an Undirected Graph](Solutions/0323.Number-of-Connected-Components-in-an-Undirected-Graph.py) (M) <br>
Union Find: With path compression, it takes ~O(1) to find and union. So the time complexity for Union Find is O(V+E).
O(V) comes from constructing the graph, O(E) comes from connecting each edge
- [0200. Number of Islands](Solutions/0200.Number-of-Islands.py) (!!M, youtubed) <br>
Solution 1: Union Find: think the grid as a graph, find how may isolated components in the graph, 注意uf连接的是坐标，而不是数，we traversal the whole gird, whenever find a 1, we connect all the 4 adjacent 1s. 方法同LC 323.
- [081420-Island Count](Solutions/Pramp__081420-Island-Count.py) (M) <br>
两点不好的地方需要改进：1. should we ask yourself a question before implementing the code for dfs?
answer should be: we want to avoid visiting the same node again and again, one way is to use a set to mark the visited nodes, the other way to modify the matrix in-place. 2. 一定要在代码结束之后主动run test case, 首先需要run test case orally. 然后写一个print()出来打印结果像上面那样！！
- [0305. Number of Islands II](Solutions/0305.Number-of-Islands-II.py) (!!H) <br>
Union-Find 算法是解决动态连通性（Dynamic Conectivity）问题的一种算法. 这里的island可以看做是一个图. 每放置一个1, 就将其与其上下左右四个点的1连接起来。
- [0547 Friend Circles](Solutions/0547.Friend-Circles.py) (!!M) <br>
Solution 1: Union-Find, 与LC 200 Nubmer of islands其实是同一题，只是这题给的是adjcency matrix representaion of a graph.
- [0734. Sentence Similarity](Solutions/0734.Sentence-Similarity.py) (E) <br>
用dictionary map similar words即可, warm up for 737. Sentence Similarity II
- [0737. Sentence Similarity II](Solutions/0737.Sentence-Similarity-II.py) (M) <br>
Different from Sentence SImilarity I, similarity relation is transitive. Two words are similar if they are the same, or are in the same connected component of this graph.  So we can use union find to connect all the similar words. 注意将word add到图中之前要判断其是否已经在图中了，不然重复加入x的时候会改变father的值，而导致father出错！！
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (!!M) <br>
union find O(V+E): 两个判断标准: 1. 无环, if uf.connected(i, j): return False. 2. 整张图只有一个disjoint_cnt, return self.disjoint_cnt == 1.; Solution 2: BFS  判断图是不是一棵树（不一定非要是二叉树）需要满足两点: 1. 首先点的数目一定比边的数目多一个; 2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目, 如果小于则说明有的节点被访问不到，如果大于说明有环，则不是树
- [0684. Redundant Connection](Solutions/0684.Redundant-Connection.py) (M) <br>
和261. Graph Valid Tree类似，union find: if uf.connected(edge[0], edge[1]), there edge is redundant.
- [0685. Redundant Connection II](Solutions/0685.Redundant-Connection-II.py) (!!H) <br>
undirected graph 变成了 directed graph - 这时需要分三种情况，第一种：无环，但是有结点入度为2的结点; 第二种：有环，没有入度为2的结点; 第三种：有环，且有入度为2的结点. 算法：step 1: construct an uf graph; step 2: 找出入度为2的点所对应的边cand_edge1, cand_edge2; step 3: 找环, 判断出三种情况
- [0721. Accounts Merge](Solutions/0721.Accounts-Merge.py) (M) <br>
union find: if email under the same name, then connect emails, or if email under name_1 equals to email under name_2, connect emails.
In this way, we build a graph, then we map each disjoint_component into one name.
Step 1: use a dictionary to store email_to_name map. Step 2: iterate the edges to connect them. Step 3: use the email_to_name map and the graph to generage a new list where each name corresponding to a disjoint_component. 如何从已经连接好的uf图中得到连在一起的nodes没有想到，其实就是建立root_email to emails dictionary as we go over uf.father.
- [0959. Regions Cut By Slashes](Solutions/0959.Regions-Cut-By-Slashes.py) (!!M) <br>
把一个小格子斜刀分成四部分，把这四部分分别加到图中, each part is a uf component. 如果遇到"/", 我们就把上部分和左部分连接起来, also把下部分和右部分连接起来
- [0128. Longest Consecutive Sequence](Solutions/0128.Longest-Consecutive-Sequence.py) (!!!H) <br>
Solution 1: Greedy O(N) 使用一个集合HashSet存入所有的数字，然后遍历数组中的每个数字，如果其在集合中存在，那么将其移除，然后分别用两个变量pre和next算出其前一个数跟后一个数，然后在集合中循环查找，如果pre在集合中，那么将pre移除集合，然后pre再自减1，直至pre不在集合之中，对next采用同样的方法，那么next-pre-1就是当前数字的最长连续序列，更新res即可; Follow up question: what if we can add a number into the nums list, and each time we add a number, we need to query the longest consecutive seqence? Answer: we need to realize dynamic connection.  We can choose UnionFind. Solution 2: Union find: O(N). 需要query 点a所在集合的元素个数，所以需要用一个dictionary self.size 用来记录每个father节点所在集合的点的个数，在union i 和 j 的时候: father[i] = j, sz[j] += sz[i].  算法是我们遍历nums, 对于每一个num, 我们connect num and num - 1, also connect num and num + 1
- [0924. Minimize Malware Spread](Solutions/0924.Minimize-Malware-Spread.py) (!!H) <br>
实际上这道题的本质还是遍历这个无向图，遍历的方法就有 DFS 和 BFS 两种。方法是先尝试去掉一个node，然后看有多少可以感染；
然后尝试去掉另一个node，看看多少可以感染；比较去掉哪一个node能使得感染的最少。O(M* N^2). solution 3: union find.
step 1: connect the original graph, so that we have multiple connected components and we keep track of size of each component.
step 2: traverse the initial infected list, and check which node in the list has the largest connected component size.
The one in the largest connected component size can infect the most nodes, so we should delete it.
- [0928. Minimize Malware Spread II](Solutions/0928.Minimize-Malware-Spread-II.py) (!!H) <br>
the difference of this problem is when we remove a node from the list, that node cannot be infected anymore in later malware spread. 需要从一个图中完全remove掉某个node, 只需要在做bfs/dfs的时候保证next_node != removed_node就可以了 - O(M^2N^2)
- [1102. Path With Maximum Minimum Value](Solutions/1102.Path-With-Maximum-Minimum-Value.py) (!!!M) <br>
Solution 2: Union-Find, step 1: sort the array by the values descendingly; step 2: union one-by-one, until (0, 0) and (m-1, n-1) are connected. 算法其实有一点点类似Krusal求MST.  Solution 1: Dijkstra's : 每次都把目前为止最小值最大的那个path的那个cueeNode pop出来，从那个currNode开始往后走. maintain a heapq to store (the negative of the minimum value in the path so far till the currPos, currPos); each time, we push (-min(nextVal, currMinVal), nextPos); O(MNlogMN), O(MN). 
- [0947. Most Stones Removed with Same Row or Column](Solutions/0947.Most-Stones-Removed-with-Same-Row-or-Column.py) (!!M) <br>
Use two for loops to compare each pos with another pos in the list, if two positions share same row or col,
then we should union them, each time there is a union, it means we can do one removal, then we set cnt+=1. This takes O(n^2).  Solution 2: improved Union Find which takes O(N):  when we see a stone that appears in a row or a column at the first time, we define this stone as the parent of this row and column, next time we see a new stone, just union it with its parent, which stores in the hashmap, thus we can do it in one pass.
- [0765. Couples Holding Hands](Solutions/0765.Couples-Holding-Hands.py) (!!H) <br>
solution 1 暴力法：从左至右依次配对好 - O(N^2); solution 2: union find - O(N). 
step 1: initialize by connecting 0-1, 2-3, 4-5....
step 2: we traverse the row, and union row[i] and row[i+1],
if needs to be unioned, then that means needs one swap to make it row[i] and row[i+1] a couple.
- [0839. Similar String Groups](Solutions/0839.Similar-String-Groups.py) (!!H) <br>
can use bfs/dfs/union-find to traverse the graph.
since we want to output disconnected components, union-find is quite straight forward - O(L* N^2).
dfs/bfs也可以做，只需要用visited记录遍历过的就可以了
- [1101. The Earliest Moment When Everyone Become Friends](Solutions/1101.The-Earliest-Moment-When-Everyone-Become-Friends.py) (!!M) <br>
算法有点像MST, 首先sort by cost, 然后union one by one as we loop over the logs.
if uf.disjoint_cnt == 1, then that means all nodes are connected.
- [0419. Battleships in a Board](Solutions/0419.Battleships-in-a-Board.py) (!!M) <br>
solution 1: unionfind. solutoin 2: O(1) space solution
whenever we meet a "X", we check if it is the top left corner of a battleship,
if it is cnt += 1
- [817. Linked List Components](Solutions/0817.Linked-List-Components.py) (M) <br>
solution 1: 直接遍历linked list, 如果curr.val in nums_set and curr.next.val in nums_set, 那就disjoint_cnt -= 1. solution 2: union find

----------------1202. Smallest String With Swaps------------


### [Minimum Spanning Tree - Kruskal's and Prim's](/)
- [1135. Connecting Cities With Minimum Cost](Solutions/1135.Connecting-Cities-With-Minimum-Cost.py) (!!M) <br>
This problem is to find the minimum path to connect all nodes, so it is a minimum spanning tree (MST) problem.
There are two defferent algorithms to solve MST problem, one is Prim's, the other is Kruskal's.
The Kruskul's algorithm is easy to implement using Union-Find, with O(ElogE) time and O(V) space.
Step 1: add all vertices to UnionFind obj;
Step 2: sort the graph by edge weights;
Step 3: add the smallest edge into the MST if adding the edge do not form a cycle;
(if the two vertices of the edge was already connected, then adding the edge will form a cycle);
Step 4: keep step 3 until all the edges are collected (E = V-1 or only one disjoint_cnt = 1)
- [1168. Optimize Water Distribution in a Village](Solutions/1168.Optimize-Water-Distribution-in-a-Village.py) (!!H) <br>
这个题目比较tricky的地方是需要想像有一个虚拟的house_0, house_0是出水的house, 这样house_1自己打井需要的cost就相当于从house_0连接到house_1所需的cost了.  Other than hte tricky part, everything is exactly the same as 1135.
- [Amazon 2019. Min Cost to Repair Edges](Solutions/Amazon_Min_Cost_to_Repair_Edges.py) (!!H) <br>
Apply Kruskal's algorithm: Just take existing edges to have 0 cost and broken edges have their given cost.
And find minimum spanning tree cost will be the answer.



# [Graph](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
## [Graph Basics](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
- [0997. Find the Town Judge](Solutions/0997.Find-the-Town-Judge.py) (!!E) <br>
one dict to store the inDegree (beingTrusted), one dict to store the outDegree (trustOthers). there exsit a town judge only if there is a node with inDegree==N-1(beiing trusted by all others), and at the same time the node should have outDegree==0(not trust anyone)
- [0277. Find the Celebrity](Solutions/0277.Find-the-Celebrity.py) (!!M) <br>
main algorithm: each comparing kowns(i, j), we are sure either i is definitely not a celebrity (knows(i, j)=True), or j is definitely not a celebrity (knows(i, j)=False). step 1: one pass, find a candidate by making sure other people are not candidates; step 2: one pass, double check the candidate selected in step 1 is indeed a celebrity
- [1267. Count Servers that Communicate](Solutions/1267.Count-Servers-that-Communicate.py) (M) <br>
one pass to store the number of servers in each row and each col. another pass to find the __isolated severs__.
- [0531. Lonely Pixel I](Solutions/0531.Lonely-Pixel-I.py) (!!M) <br>
same as the above problem. one pass to store number of "B" in col_cnt and row_cnt; another pass to find the isolated pixels
- [1153. String Transforms Into Another String](Solutions/1153.String-Transforms-Into-Another-String.py) (!!!H Google) <br>
step 1: Map each character in str1 to what it needs to be in str2. If any of these mappings collide (e.g. str1 = "aa", str2 = "bc", "a" needs to become both "b" and "c"),
we immediately return False since the transformation is impossible. Next, we check the number of unique characters in str2. If all 26 characters are represented, there are no characters available to use for temporary conversions, and the transformation is impossible.



## [Breadth First Search](/Breadth-First-Search.py)
### [BFS in Trees](/Breadth-First-Search.py) 
##### 总结：Tree中需要一层一层输出的都用BFS
- [0102. Binary Tree Level Order Traversal](Solutions/0102.Binary-Tree-Level-Order-Traversal.py) (!!M, youtubed) <br>
BFS的铁律就是用queue, 在while q: 循环里做两件事 1. 处理这一层。那就需要把这一层的node逐个pop出，然后append到res里，有时候需要用for循环for _ in range(len(q))来遍历这一层所有的node; 2. append下一层进q。BFS is O(N) since each node is processed exactly once
- [0103. Binary Tree Zigzag Level Order Traversal](Solutions/0103.Binary-Tree-Zigzag-Level-Order-Traversal.py) (M) <br>
same as 102, 在res.append(level)的时候间隔性选择res.append(level) or res.append(level[::-1])
- [0107. Binary Tree Level Order Traversal II](Solutions/0107.Binary-Tree-Level-Order-Traversal-II.py) (E) <br>
same as 102，只是题目要求从下至上输出，只需要return res[::-1]即可, or use a deque to appendleft
- [0199. Binary Tree Right Side View](Solutions/0199.Binary-Tree-Right-Side-View.py) (M) <br>
same as 102，只需要res.append(level[-1])即可
- [0513. Find Bottom Left Tree Value](Solutions/0513.Find-Bottom-Left-Tree-Value.py) (M) <br>
首先想到的是要求bottom的node, 所以用bfs渠道最下面一层，然后要求left_most, 所以我们可以在bfs append下一层的时候先append right, then append left, 这样最后一个node就是botoom left node了
- [0515. Find Largest Value in Each Tree Row](Solutions/0515.Find-Largest-Value-in-Each-Tree-Row.py) (M) <br>
- [1161. Maximum Level Sum of a Binary Tree](Solutions/1161.Maximum-Level-Sum-of-a-Binary-Tree.py) (M) <br>
- [0111. Minimum Depth of Binary Tree](Solutions/0111.Minimum-Depth-of-Binary-Tree.py) (!!!E) <br>
solution 1: recursion; soluiton 2: BFS; for _ in range(lens): if not node.left and not node.right: return depth
- [0297. Serialize and Deserialize Binary Tree](Solutions/0297.Serialize-and-Deserialize-Binary-Tree.py) (!!H) <br>
Serialize: just do a bfs to put ch level by level. Note that we use "#" to represent None. Deserialize: do a bfs, use an idx to keep track of where have we reached in the input list. deserialize不要层序遍历. 注意pre_order (dfs), post_order (dfs), level_order(bfs) 都可以做，但是in_order不可以！
- [0449. Serialize and Deserialize BST](Solutions/0449.Serialize-and-Deserialize-BST.py) (!!H) <br>
Same as 297.  Solution says since BST, the answer could be as compact as possible.  Don't know how?
- [0652. Find Duplicate Subtrees](Solutions/0652.Find-Duplicate-Subtrees.py) (!!M Google) <br>
If two subtrees have the same string representation, then they are duplicated subtress.  solution 1: serialize the every subtree using bfs, and put (string presentation of subtree --> subtree node) into a hashmap. Since serialization takes O(N), so the overall algorithm takes O(N^2). solution 2: serialize the binary tree using post-order traversal.  Since we can update the mapping during the traversal, the whole algorith takes O(N)
- [0428. Serialize and Deserialize N-ary Tree](Solutions/0428.Serialize-and-Deserialize-N-ary-Tree.py) (!!H Google) <br>
solution: level order bfs.  This is very similar with serialize and deserialze a binary tree. In binary tree, we know after visit left and right of a node, we can move to another node, but in Nary tree, we don't know when to finish visiting a node cuz there could be multiple children for a node. So we need to do  some trick to mark the end of a level.  The trick is, when we do bfs to serialze, we append "#" into a res when we switch from one parent to another parent. In deserialize, while res[idx] != "#" 就说明还要继续给curr_node添加child，而res[idx] == "#"意味着要换node append child了, idx += 1






## [BFS in Graphs](/Breadth-First-Search.py)
##### 只有一种情况必须用bfs: 需要层序遍历求最短路径问题(find min steps/time/swaps/moves, or Topo sort, or Dijkstra, A*). 其余情况都用dfs.
- [0994. Rotting Oranges](Solutions/0994.Rotting-Oranges.py) (M) <br>
求最短路径问题，必须用bfs. Step 1. append the rotten ones to the first level（多源节点）, Step 2: 层序遍历的bfs to turn the adjacent fresh ones into rotten ones. 必须层序遍历才能保证最少时间make all fresh ones rotten 在class solution(): 后面定义全局变量 EMPTY = 0; FRESH = 1;
- [0286. Walls and Gates](Solutions/0286.Walls-and-Gates.py) (M) <br>
求最小距离问题，必须用bfs. Step 1: append all the gates into the queue; Step 2: change all the EMPTY rooms to a value that equals the layer number, 必须层序遍历才可以保证每次都能变成最小距离
- [1162. As Far from Land as Possible](Solutions/1162.As-Far-from-Land-as-Possible.py) (!!M) <br>
The max distance is the max steps to change all WATER to LAND. So we firslty put all land in a q, than do bfs layer by layer to change WATER to LAND in-place - O(MN).  solution 2: DP same as 542. 01 matrix
- [0542. 01 Matrix](Solutions/0542.01-Matrix.py) (M) <br>
方法是先把所有0放入q的第一层，然后一层层遍历，同时更新遇到的1为当前的层数，层数就是1离0的距离 - O(MN); solution 2: DP same as 542. 01 matrix
- [0317. Shortest Distance from All Buildings](Solutions/0317.Shortest-Distance-from-All-Buildings.py) (!!H) <br>
Use reachable_cnt[i][j] to record how many times a 0 grid has been reached and use dist[][] to record the sum of distance from all 1 grids to this 0 grid. Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS. in the bfs, we do level bfs and update the reachable_cnt matrix and dist matrix. 遇到obstacle不放进q就可以了. each bfs, all position are visited, so O(MNk) where k is how many building are there or how many bfs are triggered. Finnaly return the min of dist[i][j] if reachable_cnt[i][j] = total number of buildings. Strong Prune: if if starting from building (i, j), can reach all other building? if not, that means at least one building is isolated and can not be reached, then return -1 directly: in each BFS we use reachableBuildings to count how many 1s we reached. If reachableBuldings != totalBuildings - 1 then we know not all 1s are connected are we can return -1 immediately, which greatly improved speed.
- [0127. Word Ladder](Solutions/0127.Word-Ladder.py) (!!M) <br>
node是某个单词，_get_next(curr_node)是这一题的难点，构造一个dictionary, key is all possible combination of the word, value is the word, 这样就可以快速查询了。Time complexity: O(NL^2), where N is the number of words in word_set, and L is avg length of words
- [0433. Minimum Genetic Mutation](Solutions/0433.Minimum-Genetic-Mutation.py) (!!M) <br>
same as 127. Word Ladder. O(4NL^2)
- [0854. K-Similar Strings](Solutions/0854.K-Similar-Strings.py) (!!H) <br>
求一个状态到另一个状态的最短路径: bfs, 想要速度更快？双端 + Prune! How to prune? there are so many swaps, how to make sure we choose swaps that are leading next_node cloaser to B?1. while S[i]==B[i], we don't need to swap them, until we found S[i]!=B[i], then ith pos needs to be swapped; 2. swapped with whom? we find S[j]==B[i], then swap j and i in S, now B[i]==S[i], and S is getting closer to B!
- [0815. Bus Routes](Solutions/0815.Bus-Routes.py) (!!H Google) <br>
Shortest path problem: bfs. 与word ladder那题类似，构造一个busstop_to_route的dictionary是的get_next_stop更快
- [0752. Open the Lock](Solutions/0752.Open-the-Lock.py) (!!M Google) <br>
题目蛮有意思的, 带层序遍历的bfs, If next_node is deadend, then we don't put it into q, find neighbor 函数比较有意思，这里第一次学到了yield;
- [1129. Shortest Path with Alternating Colors](Solutions/1129.Shortest-Path-with-Alternating-Colors.py) (!!M) <br>
这一题的题眼是visiting the same node with same color is not allowed, with same color is not. 所以color信息要放到adjacency list 里，也要放到q里，还要放到visited里
- [0773. Sliding Puzzle](Solutions/0773.Sliding-Puzzle.py) (!!H) <br>
最短路径问题用bfs: 从单源节点出发到终节点的最短路径问题。这题的起点是给定的board, 终点是最终想生成的board. 所以node就是某一个board, node的neighbors就是通过一次交换可以生成的board. 这个题就是_get_next(curr_node)比较不容易想到
- [0818. Race Car](Solutions/0818.Race-Car.py) (!!H) <br>
层序遍历的bfs. 这个graph的nodes比较特殊，nodes是(curr_pos, curr_speed). strong pruning that is 100 times faster: 我们是有条件的回退，只有在超过了target的情况下我们才回退
- [1197. Minimum Knight Moves](Solutions/1197.Minimum-Knight-Moves.py) (!!M) <br>
solution 1: 利用对称性质: x,y=abs(x),abs(y); q.append(neighbor) only if (-2 <= next_x <= x + 2 and -2 <= next_y <= y + 2); 1816 ms<br>
solution 2!!!: 从source和destination两端同时进行bfs!!!!注意双端bfs传进去的参数包含q and visited, bfs返回值是updated q and visited. cnt+=1的操作在主函数中进行. while true的结束条件: if visited_src & visited_des: return cnt_src + cnt_des; 452 ms <br>
solution 3 dp才是正解: recurrsion with memorization: cache[(x, y)] = min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1; 60 ms
- [0864. Shortest Path to Get All Keys](Solutions/0864.Shortest-Path-to-Get-All-Keys.py) (!!H) <br>
BFS algorithm can be used to solve a lot of problems of finding shortest distance.
In this problem, we may visit a point more than one times, simply storing visited position is not enough.
We need to save (pos, keys_collected) in the visited set, because visiting the same pos without getting new key is not allowed,
but in order to get a new key, we may visit a certain pos, after getting the key, we may go back and visit the pos again.
这是bfs最难的一题了
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (!!M) <br>
f[j]=the least number of perfect square numbers which sum to i; f[j] = min(f[j-i^2]+1) for i^2<=j; Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5); solution 2: level order BFS. Given a N-ary tree, where each node represents a __remainder__ of the number n subtracting a square number, our task is to find a node in the tree, which should meet the conditions or remainder=0.  bfs的层数就代表了所需要perfect squares的个数. Time complexity: 比较复杂最后是 O(n^(h/2)), where h is the height of the N-ary tree, h is 0 to 4.
- [1293. Shortest Path in a Grid with Obstacles Elimination](Solutions/1293.Shortest-Path-in-a-Grid-with-Obstacles-Elimination.py) (!!!H Google) <br>
bfs. q 里面需要放入当前用了多少eliminations. q.append((next_i, next_j, curr_elimination_cnt))
- [1138. Alphabet Board Path](Solutions/1138.Alphabet-Board-Path.py) (!!!M Google) <br>
bfs. 最短距离问题
- [1345. Jump Game IV](Solutions/1345.Jump-Game-IV.py) (!!!H Google) <br>
bfs. 最短距离问题 - O(N). pruning makes hard.

--------------1210. Minimum Moves to Reach Target with Rotations--------------


### [Topological Sort](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
- [0127. Topological Sorting](Solutions/0127.Topological-Sorting.py) (!!LintCode) <br>
有向图的问题，可以检测有向图是否有环！必考，其实也非常模板化，一定要记住。Three steps: 1. 从数字关系求出每个节点的inDegrees（就是找节点与相邻节点的依赖关系） (inDegrees = collections.defaultdict(int))，key是node, val是这个node的indegree值; 2. 和每个节点的neighbors （neighbors = collections.defaultdict(list)), key是node, val是装有这个node的neighbor的list; 3. 然后 BFS，背诵模板就可以了。
- [0207. Course Schedule](Solutions/0207.Course-Schedule.py) (!!M) <br>
套用模板分三步：1. construct a dictoinary of adjacency list for the graph; 2. get in_degree information for all nodes; 3. topological sort - bfs: step I: initialze q by putting all in_degree = 0 into q; step II: keep adding in_degree = 0 node into q and pop out while updating res
- [0210. Course Schedule II](Solutions/0210.Course-Schedule-II.py) (!!M) <br>
套用模板 return res if len(res) == numCourses else [].  Google follow up: 打印出所有可能的选课组合，感觉有点像word ladder I and II.
- [0444. Sequence Reconstruction](Solutions/0444.Sequence-Reconstruction.py) (!!!M) <br>
这个题目要做三个判断：1. 判断seqs的拓扑排序是否存在，只需判断len(res) 是否等于len(graph) or len(inDegrees), 如果小于说明有孤立节点，如果大于说明有环，两者都不存在拓扑排序; 2. 判断是否只存在一个拓扑排序的序列, 只需要保证队列中一直最多只有1个元素, 即每一层只有一个选择: if len(q)>1: return False; 3. 最后判断这个唯一的拓扑排序res是否等于org
- [0269. Alien Dictionary](Solutions/0269.Alien-Dictionary.py) (!!H) <br>
只需要比较word[i]与word[i+1]中每个char，即可得到inDegree的关系以及neighbors的关系
- [0310. Minimum Height Trees](Solutions/0310.Minimum-Height-Trees.py) (!!M) <br>
想想如果是一个很大的图，那minimum height trees的root就应该是这个图的最中心，所以我们就去找图的最中心就可以了，采用从外围(inDegree=1的node)往中间走的方法，解法类似topological sort, 走到最后留下的顶点就是最中心的顶点，也就是距离所有外围顶点最小的顶点。
- [0802. Find Eventual Safe States](Solutions/0802.Find-Eventual-Safe-States.py) (M) <br>
在环内的node可能永远都跳不出环，所以这一题是寻找不在环里的nodes, 其实就是其实就是topological sort for out_degree!
- [1203. Sort Items by Groups Respecting Dependencies](Solutions/1203.Sort-Items-by-Groups-Respecting-Dependencies.py) (!!H Google) <br>
topo sort. step 1: put -1 into idependent groups; step 2: build the item_graph and item_degrees, and group_graph and group_degrees; step 3: topological sort for the two graphs we built; step 4: get the res: 先宏观有序，再微观有序
- [Google construct the original array from subsets](Solutions/Google__construct_the_original_array_from_subsets.py) (!!M Google) <br>
Given a list of subsets from an array A, construct the original array. The original array may contain duplicate elements.




### [Dijkstra](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
##### 有权图最值路径问题，最值分两种：1. 最大/最小 sum of the path; 2. 最大/最小 min/max in the path. <br>
##### 第一种需要在heapq中存放(curr_sum, curr_node); 第二种需要在heapq中存放(-curr_min_val, curr_node) or (curr_max_val, curr_node). 第二种也可以用UnionFind来做
- [0743. Network Delay Time](Solutions/0743.Network-Delay-Time.py) (!!M) <br>
**带权值**的**有向图**求**单源节点**出发的最短路径问题马上就想到Dijkstra, **O(VlogV + E)** N is # nodes, E is # edges <br>
Dijkstra就是贪心版的bfs, bfs是勤勤恳恳一层一层推进，一层没访问完绝不访问下一层。Dijkstra就很贪心了，才不一层一层地走呢，他每次都想走最low cost的。如何实现每次走最low cost的呢？用一个heapq来store a pair: (currCost to reach the node, node), 这样每次pop出来的就都最low cost的node了，再去访问这个node的neighbors，把这些neighbors都加到hq中，代码比较短。思路其实与23. Merge k Sorted Lists非常类似，把23里的linked list加上一个虚拟头节点连接所有的头节点，然后把Linked list node的val改成边的权值，那就变成了单源节点出发求访问到所有节点的最短路径。
- [0787. Cheapest Flights Within K Stops](Solutions/0787.Cheapest-Flights-Within-K-Stops.py) (!!M) <br>
有向图，带权值，找从单源出发最佳路径问题：Dijkstra's algorithm <br> 
hq 需要 store (curr_cost, curr_stops, curr_city), 与743相比少了一个currNode in costs: continue 因为次好路径也可能是最后的结果，这是由于最好(low cost)路径可能不满足stops < K; 这题需要加一个 if currStops >= K: continue
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](Solutions/1334.Find-the-City-With-the-Smallest-Number-of-Neighbors-at-a-Threshold-Distance.py) (!!M) <br>
从每一个节点单独出发做一个Dijkstra, 比较每一个节点出发能到达的neighbors node的个数即可
- [1514. Path with Maximum Probability](Solutions/1514.Path-with-Maximum-Probability.py) (!!M) <br>
把probability换成log表示就变第一种情况最大/最小 sum of the path
- [0490. The Maze](Solutions/0490.The-Maze.py) (!!M) <br>
since the ball cannot stop at an empty place, must stop at wall, the tricky part is from the curr_stoppable position, find the next_stoppable position: use a while loop to find where is the next stop position. 
- [0505. The Maze II](Solutions/0505.The-Maze-II.py) (!!M) <br>
need to find the shortest path to reach destination. So dfs won't work. solution 1: Each stoppable pos is the node, while the steps needed from one stoppable pos to another stoppable pos is the weight in the graph. We use Dijkstra's to find path from source to destination. 这个题比普通的Dijkstra's就只是多了一步找下一个node的步骤.  solution 2: just use a bfs, every time we reach the destination, we cannot return directly, because第二次到达的steps可能还更小，所以我们需要记录所有达到destination所用的步数. 
- [0499. The Maze III](Solutions/0499.The-Maze-III.py) (!!H) <br>
similar iwth 505 solution 2, use Dikstra's algorithm. hq needs to store the path: (curr_dist, curr_pos, curr_path). So when curr_pos == destination: instead of return curr_dist, we return curr_path.
- [0882. Reachable Nodes In Subdivided Graph](Solutions/0882.Reachable-Nodes-In-Subdivided-Graph.py) (H) <br>
每次pop出来的都是剩余步数最多（即离soure node最近）的node. hq stores (currently how many moves left, curr_node); use a dictionary to store node--->how many moves left.
- [1102. Path With Maximum Minimum Value](Solutions/1102.Path-With-Maximum-Minimum-Value.py) (!!M) <br>
Solution 1: Dijkstra's : 我们要的是path里面的最大的最小值, 所以我们把每个path里面的最小值放入max heap, 这样我们每次pop出来的都是path里面最大的那个最小值. maintain a heapq to store (__negative of the minimum value in the path so far till the currPos__, currPos); each time, we push (-min(nextVal, currMinVal), nextPos); O(MNlogMN), O(MN). Solution 2: Union-Find, step 1: sort the array by the values descendingly; step 2: union one-by-one, until (0, 0) and (m-1, n-1) is connected; solution 3: dfs + binary search. <br>
想想174. Dungeon Game那题，其实也是找maximum of minimum value in a path, 不同的是只能往右走和往下走，也就是说不能回头，所以情况更简单可以用DP O(mn)解决 <br>
- [1631. Path With Minimum Effort](Solutions/1631.Path-With-Minimum-Effort.py) (!!M) <br>
Obviously, it is a minimum of max_val problem, which is typical Dijkstra's. maintain a heapq to store (the max_diff in the path so far till the curr_pos, curr_pos). Each time, we push (max(next_diff, curr_max_diff), next_pos). 注意需要一个visited set to store the pos we visited.
- [Google. Maximum Safty for the Soldier](Solutions/Google.Maximum-Safty-for-the-Soldier.py) (!!M) <br>
Google 面经：有一个nxn矩阵，信使从(0, 0)出发，想走到(n-1, n-1)去报信，中途会有一些狮子/敌营，我们离狮子的距离越远越安全，问为了尽可能到达目的地，离狮子最大的最近距离是多少？
- [Student Cheating sheet](Solutions/Google__Student_Cheating_sheet.py) (!!M Google) <br>
Dijkstra's.
问从a到b被捉概率最小的传递路线。本质上是weighted edge shortest path，因为不是DAG 所以用dijkstra
- [0778. Swim in Rising Water](Solutions/0778.Swim-in-Rising-Water.py) (!!H) <br>
find a path with the minimum max-height in the path. 采用Dikstra, 每次pop出来的都是min height就可了 - O(N^2* log(N^2)), where N is the lens of grid. solution 2: union find is also quite straigt-forward
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](Solutions/1368.Minimum-Cost-to-Make-at-Least-One-Valid-Path-in-a-Grid.py) (!!!H Google) <br>
由于我们可以选择四个方向都可以走，所以不能用dp. 如果只能朝右下方向走才能用dp. 可以朝四个方向走只能用bfs/dfs. 由于我们需要maitain min_cost, 所以可以用Dijkstra's. heapq stores (curr_cost, curr_i, curr_j). 
- [1697. Checking Existence of Edge Length Limited Paths](Solutions/1697.Checking-Existence-of-Edge-Length-Limited-Paths.py) (H) <br>
loop over the queries, each query is a dijkstra's to find min_max problem. O(QVlogV), Q is how many queries are there, V is how many nodes are there.


### [A*  / Heuristic](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
- [1091. Shortest Path in Binary Matrix](Solutions/1091.Shortest-Path-in-Binary-Matrix.py) (!!M) <br>
solution 1: 带层序遍历的bfs, if grid[next_x][next_y] == BLOCK 那就continue掉不放进q; solution 2: bi-directional bfs; solution 3: A*, __A* is better than bfs in finding the shorted path from source node to end node.__ 在A* 算法中，需要两个数据结构：**I. A heapq; II. A dictionary.** I. heapq stores (1. curr_heuristic_estimation of min # of steps from source to target if 经过currNode; 2. curr_steps from source to curr_node; 3. curr_pos)), where curr_heuristic_estimation = curr_steps + heuristic estimation of minimum distance from curr_pos to desitination. II. dictionary stores the the position ---> steps taken from source to the position.
- [1263. Minimum Moves to Move a Box to Their Target Location](Solutions/1263.Minimum-Moves-to-Move-a-Box-to-Their-Target-Location.py) (H) <br>
思路：这个题是从源节点到目标节点的最短路径问题，所以想到用bfs, 源节点是对boxPos, 目标节点是targetPos, 从源节点出发做带层序遍历的bfs_1, return 层数即可。注意在判断nextBoxPos是否可以append到q的时候需要兼顾考虑到player能不能到nextBoxPos的相反方向去推box, 所以需要找到从currPlayerPos到oppositeNextBoxPos的可能路径，这是一个从源节点到目标节点的问题，源节点是对currPlayerPos, 目标节点是oppositeNextBoxPos, 需要做bfs_2, 如果能到就返回true. 总体思路就是上述了，需要注意的是bfs_1中由于box每移动一下boxPos会变playerPos也会变，所以要把boxPos和playerPos都入队列。另外易错点：visited里面只装boxPos. 这是不对的, 因为box从不同的方向被推到同一个地方是允许的，因此visited里面应该装入(boxPos, the pos where the boxPos comes from). <br>
Solution 2: 无权图单源节点的最短路径问题，自然想到A-star search algorithm. use manhatan distance as Heuristic esitimation for A-star algorithm: steps + (abs(nextBoxPos[0]-targetPos[0]) + abs(nextBoxPos[1]-targetPos[1])).  put the heuristic estimation in the hq, together with steps, so the hq stores (heristic estimation of hte minimum steps needed from source to target, steps, boxPos, playerPos).  in A* algorithm, do not do level order bfs, do non-level order bfs.  
- [0843. Guess the Word](Solutions/0843.Guess-the-Word.py) (!!!H Google) <br>
Repeatedly choose a word to guess, and then eliminate all words that do not have the same number of matches as the guessed word. 
In this way, the wordlist is narrowed down each time we do a guess.
How to choose a word: solution 1: random guess; 2. choose the guess word wisely (Heuristically). Soltion 2: Each time we guess, we choose the word that has the most common chars (overlaps) with other words in the candidates list. This is just a hueristic estimation, hard to prove why it works. But indeed it works much better than random guess.



## [Depth First Search](/Depth-First-Search.py)
### [Backtrack - Combination and Permutation](/Depth-First-Search.py)
- [0078. Subsets](Solutions/0078.Subsets.py) (!!M) <br>
C(m, n)：m个里面找出n个的组合问题; 模板的back tracking求combination问题, S是solution的个数，这里S=2^N. Copy takes O(N), so overall O(N* S); 注意两点：1.res.append(curr.copy()); has to be a deep copy; 2. self.dfs(i + 1, curr) 要从i+1开始cuz不能回头找会重复. 因为subsets, subarray, substring都是讲究顺序的
- [0077. Combinations](Solutions/0077.Combinations.py) (!!M) <br>
C(m, n)：m个里面找出n个的组合问题; C_m_n = (n!)/( (m!)* (n-m)! )
- [0090. Subsets II](Solutions/0090.Subsets-II.py) (!!M)<br>
如果输入存在重复元素，[1, 2, 2]的遍历中，我们只取前面的那个2，对于后面的那个2，如果不是挨着前面那个2选的，也就是说i != startIndex，那么就不要放后面那个2，这样会造成重复出现[1,第一个2],[1,第二个2], 注意可以挨着第一个2来选第二个2是可以的，因为允许出现[1,2,2]作为答案。所以contraint是: if (i >= 1 and nums[i] == nums[i-1]) and i != startIndex: continue
- [0039. Combination Sum](Solutions/0039.Combination-Sum.py) (!!M) <br>
这里从curr_idx开始的，而不是subsets里面的curr_idx+1, 这是因为Subsets同一个数只能选一次，这里同一个数可以选很多次
- [0040. Combination Sum II](Solutions/0040.Combination-Sum-II.py) (M) <br>
输入中存在重复元素，避免重复输出的方法与Subsets II一样; 模板 find_solution: if target == 0; is_not_valid: if (nums[i] > target) or (i >= 1 and nums[i] == nums[i-1]) and i != startIdx
- [0216. Combination Sum III](Solutions/0216.Combination-Sum-III.py) (M)<br>
一个数只能选一次，所以从curr_idx + 1开始
- [0090. k Sum II](Solutions/0090.k-Sum-II.py) (M Lintcode) <br>
exactly the same as 216.
- [0518. Coin Change 2](Solutions/0518.Coin-Change-2.py) (!!!!!!!!!!M) <br>
与Combination Sum一模一样，只是题目不要求输出所有可能组合，只要求输出可能组合的数目，所以可以用DP解。 __DP解的for循环顺序很重要，由于(1,3)和(3,1)被认为是同一解，所以coin的加入顺序很重要，所以for coin in coins:是主循环，for num in range(1, amount + 1):是次循环。__ 因为当coin遍历到coin=1的时候，dp[4]+=d[3]此时的dp[3]=0所以dp[4]实际上加的是0；而当coin遍历到coin=3的时候，dp[4]+=d[1]，此时d[1]被更新过一次。所以真个过程dp[4]只被更新一次，不会重复更新。
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (M)<br>
self.dfs(nums, target - nums[i], 0, curr, res)  (1, 3)和(3, 1)被认为是不同解，所以让i从0开始; solution 2: dp. __DP解的for循环顺序很重要， 由于(1,3)和(3,1)被认为是不同解，所以coin的加入顺序不重要，所以for m in range(target + 1): 是主循环，for num in nums:是次循环，这么写可以保证(1,3)可以进solution, (3,1)也可以进solution, 所以符合题意。__
- [1255. Maximum Score Words Formed by Letters](Solutions/1255.Maximum-Score-Words-Formed-by-Letters.py) (!!H Google) <br>
find all subsets, similar with 78. Subsets. O(26* 2^n), n = len(words)
- [0698. Partition to K Equal Sum Subsets](Solutions/0698.Partition-to-K-Equal-Sum-Subsets.py) (!!!M) <br>
套backtrack模板即可，backtrack里面需要传入(curr_sum, curr_idx, curr_cnt).
结束条件是已有curr_cnt=k段满足条件了. 
Time complexity: we basically iterate over nums and for each element either use it or drop it, 
which is O(2^n). We are doing the same for each subset. Total subsets are k. 
So Time Complexity becomes O(k*(2^n))
- [0254. Factor Combinations](Solutions/0254.Factor-Combinations.py) (M) <br>
solution 1: step 1. we get a list of factors first; step 2. then we do a dfs like combination sum
- [0046. Permutations](Solutions/0046.Permutations.py) (!!M)<br>
与combination相比少了一个startIndex参数，加入visited存idx用于防止重复出现; 
- [0047. Permutations II](Solutions/0047.Permutations-II.py) (M) <br>
模板: is_not_valid: if i in self.visited: continue; if (i > 0 and nums[i] == nums[i-1]) and (i-1) not in self.visited: continue
- [1079. Letter Tile Possibilities](Solutions/1079.Letter-Tile-Possibilities.py) (!!M) <br>
用47. Permutations II中的方法去重, 需要先sort!!!!!!!!
- [0996. Number of Squareful Arrays](Solutions/0996.Number-of-Squareful-Arrays.py) (!!H)  <br>
本质还是求permutation Constrained permutation problem. 只是多了一个条件就是nums[cur_idx] +nums[next_idx]必须是square number.
- [0052. N Queens II](Solutions/0052.N-Queens-II.py) (!!H) <br>
本质还是permutation问题Constrained permutation problem：先打印出数组[0, 1, 2, 3....n]中所有的可能排列：[[0,1,2,3], [1,3,0,2].....]，其中的每一个子数组表示一种可能的方法，子数组中的数字表示在哪个数字的地方放一个Queen，数字对应的下标位置是放那个Queen的行，数字的值是放那个Queen的列。由于Queen可以很冲直撞，所以列是不能相同的，所以需要去重，用visited标记就可以。又由于Queen还可以斜着走，所以横纵坐标的和与差不能相同，也需要用visited标记。用三个字典visited_col, visited_sum, visited_diff分别存储列号，横纵坐标之和，横纵坐标之差有没有被用过
- [0051. N Queens](Solutions/0051.N-Queens.py) (H)<br>
- [0031. Next Permutation](Solutions/0031.Next-Permutation.py) (!!M) <br>
step 1: sweeping from right to left, find the first decreasing element nums[i]; Step 2: sweep from right to left, find the first element larger just than nums[i], then swap nums[i] and nums[j], then swap all the items starting from i+1
- [0267. Palindrome Permutation II](Solutions/0267.Palindrome-Permutation-II.py) (!!M)  <br>
step 1: put the characters that have seen two times in the char list; now we have a charList that only holds char that appears even times, eg: "aabbbbcc" now becomes "abbc", Step 2: we only need to do permutation for this charList, so the time complexity is O((n/2)!), which is quite an improve. Step 3: when return the results, we just use the permuation generated in steps 2 + permuation[::-1]
- [0060. Permutation Sequence](Solutions/0060.Permutation-Sequence.py) (!!H)  <br>
It really is all about pattern finding; 只需要用 k // (n-1)! 去找到k所在的位置
- [0054. Spiral Matrix](Solutions/000054.Spiral-Matrix.py) (!!M) <br>
每一个转弯的点是dfs的node, dfs helper function 需要传入的参数有(min_row, max_row, min_col, max_col, curr_dir)




### [Backtrack](/Depth-First-Search.py)
__在写代码之前一定要先写下三点：1. 什么是backtrack的结束条件; 2. next_candidate有哪些constraint; 3. 将什么传入backtrack函数__
- [1056. Confusing Number](Solutions/1056.Confusing-Number.py) (E) <br>
use a hashmap
- [1088. Confusing Number II](Solutions/1088.Confusing-Number-II.py) (!!H Google) <br>
solution 2: Only 0, 1, 6, 8, 9 are the valid set of digits, do a backtracking to generate all the numbers containing this digits and check they are valid.
time complexity: O(5^M), where M is how many digits are there in str(N), which scales with ~logN, where log is 10-based.
- [0246. Strobogrammatic Number](Solutions/0246.Strobogrammatic-Number.py) (E) <br>
Two pointers. similar with 1056. Confusing Number.
- [0247. Strobogrammatic Number II](Solutions/0247.Strobogrammatic-Number-II.py) (!!M Google) <br>
Backtrack. find all combinations for n//2 lens, using backtrack.
- [0248. Strobogrammatic Number III](Solutions/0248.Strobogrammatic-Number-III.py) (H) <br>
解法：每次都按照一个lens做backtrack. 每次添加next_ch都在curr_comb前面和后面添加
backtrack end consition: if len(curr_comb) == lens, check if curr_comb in range(low, high)
constraints on next_candidates: next_comb = ch + curr_comb + mapping[ch], cannot have leading zero
arguments pass into backtrack function: curr_comb
- [1239. Maximum Length of a Concatenated String with Unique Characters](Solutions/1239.Maximum-Length-of-a-Concatenated-String-with-Unique-Characters.py) (!!M)<br>
subsets问题的变形 - constraint subsets
- [0526. Beautiful Arrangement](Solutions/0526.Beautiful-Arrangement.py) (!!M)<br>
Constrained permutation problem. THe constrain is: nums[next_idx] % (len(curr_comb) + 1) == 0 or (len(curr_comb) + 1) % nums[next_idx] == 0.  For constrained permutation problem, the time complexity is O(valid solutions)
- [1219. Path with Maximum Gold](Solutions/1219.Path-with-Maximum-Gold.py) (!!M)<br>
尝试每一个pos出发backtrack所有可能的path比较哪一条path能得到最多的gold - O(4^N). 注意backtrack遍历得到的是每一条path的curr_sum, 而不是像普通dfs那样得遍历的是整个区域的. 对比这一题与200. Number of islands. 我们可以看到求path一定需要用backtrack. backtrack与dfs相比其实就是多了一步visited.remove(next_candidate). 这就导致dfs的时间复杂度是O(N), while backtrack的时间复杂度是O(4^N), where N is the number of cells in the matrix. 4 is the number of next_nodes in the for next_candidate in ...
- [0784. Letter Case Permutation](Solutions/0784.Letter-Case-Permutation.py) (!!E)<br>
backtrack. 注意这个题目next_idx不能往回找 - O(2^N) which the total number of solutions.
- [1087. Brace Expansion](Solutions/1087.Brace-Expansion.py) (!!M) <br>
套用dfs模板即可 - O(M^N), where N is len(lst), M is avg how many choices we have for each string in lst.
- [0351. Android Unlock Patterns](Solutions/0351.Android-Unlock-Patterns.py) (!!!M Google) <br>
backtrack: 跟普通的backtrack不同的是From a number in the keypad we can reach any other number, but can't reach the one's that have a number as obstacle in between. 
For example, for (1 to 3), the obstacle is 2. 所以在判断要不要把next_num作为下一个valid candidates的时候如果(curr_num, next_num) in cannot_pass那就不行。
- [0093. Restore IP Addresses](Solutions/0093.Restore-IP-Addresses.py) (!!M)  <br>
套backtrack的模板，这里的结束条件有两个: curr_intervals == 4 and curr_idx == len(s) - 1, 所以cur_interval数目和curr_idx都要传进backtrack里
- [0017. Letter Combinations of a Phone Number](Solutions/0017.Letter-Combinations-of-a-Phone-Number.py) (!!M) <br>
经典的backtrack题，in dfs template, find solution: if currIdx == len(digits); for next_candidate in list_of_candidates: for ch in self.phone[digits[next_idx]];
- [0282. Expression Add Operators](Solutions/0282.Expression-Add-Operators.py) (!!H) <br>
套用backtrack的模板， 这里的backtrack里面需要传入(curr_idx, curr_num, curr_sum, curr_combo). find solution is: curr_sum == target and curr_idx == len(s) - 1. overall O(N* 4^N)
- [0079. Word Search](Solutions/0079.Word-Search.py) (!!M) <br>
套用backtrack的模板，backtrack 里面要传入(curr_i, curr_j, curr_idx on word). find solution: if board[next_i][next_j] == word[curr_idx + 1].  if find a solution, backtrack函数输出True. if valid: if board[next_i][next_j] == word[curr_idx + 1]. 需要一个visited set来标记已经走过的路径避免走重复的路径。
Time Complexity: O(N* 4^L) where N is the number of cells in the board and L is the length of the word to be matched.
- [0113. Path Sum II](Solutions/0113.Path-Sum-II.py) (!!M) <br> 
Solution 1: 碰到打印所有路径的问题，第一反应就是带backtrack. 套用backtrack的模板即可
- [1376. Time Needed to Inform All Employees](Solutions/1376.Time-Needed-to-Inform-All-Employees.py) (!!!M Google) <br> 
Same as Path Sum II except it's a N-arry tree.
- [0980. Unique Paths III](Solutions/0980.Unique-Paths-III.py) (!!H youtube with path-I and II) <br>
套用backtrack模板就可以了. 每一个位置都有3种可能，所以time complexity O(3^N). 
- [0332. Reconstruct Itinerary](Solutions/0332.Reconstruct-Itinerary.py) (!!M) <br>
有向图的遍历问题，LeetCode关于有向图的题只有两道Course Schedule和Course Schedule II，而那两道是关于有向图的顶点的遍历的，而本题是关于有向图的边的遍历。每张机票都是有向图的一条边，我们需要找出一条经过所有边的路径，那么DFS不是我们的不二选择. Recurssive backtracking.  Worst case: O(E^d), where E is # of edges, d is is the maximum number of flights from an airport.  Solution 2: 因为只需要输出一种包含所有边的路径，所以可以用另一种图的解法 Eulerian Path - every edge is visited exactly once. Eulerian path 使用的算法叫做 Hierholzer algorithm. Hierholzer algorithm 不做backtrack, 所以每一条边只访问一次，所以时间复杂度是O(E), where E is the # of edges.
- [0131. Palindrome Partitioning](Solutions/0131.Palindrome-Partitioning.py) (!!!M) <br>
要求输出所有的可能组合，所以只能backtrack. O(L* 2^L), where L is the lens of string, 2 is two choices: 这这里分还是不分。  
如果题目只是要求输出所有可能组合的数目，那就dp - O(L^2)
- [0306. Additive Number](Solutions/0306.Additive-Number.py) (!!M) <br>
套backtrack模板即可，backtrack传入的参数有(curr_idx, prev_num, curr_num, curr_cnt). 结束条件是if curr_idx == len(s) - 1 and curr_cnt > 2
- [0842. Split Array into Fibonacci Sequence](Solutions/0842.Split-Array-into-Fibonacci-Sequence.py) (!!M) <br>
套backtrack模板即可，backtrack传入的参数有(curr_idx, curr_comb). 
结束条件是if curr_idx == len(s) - 1 and len(curr_comb) > 2:
- [0212. Word Search II](Solutions/0212.Word-Search-II.py) (!!H) <br>
要求打印所有路径所以：Trie + Backtracking. we put the words into a trie. Then we loop over the board, whenever we found a char in root.child, we trigger a backtrak. Backtrack 里面应该传入参数 (curr_i and curr_j in board, curr_node in trie, curr_word). backtrack 的结束条件是if curr_node.is_end. 注意找到到案之后千万不要return, 然单词health找到之后就不再继续找单词healthy了
- [0425. Word Squares](Solutions/0425.Word-Squares.py) (!!H Google) <br>
Trie的解法怎样一步一步来的很重要！！把这题多写几遍backtrack+Trie+hashmap就都有更深的理解！这题的题眼是：我们想加在第五行加单词，那这个单词必须满足prefix是前4行的第四列组成的。hashmap是最快的 - O(N* 26^L). build a hashmap so that 我们可以快速O(1)地从prefix找到可以得到的第五行可以加哪些单词
- [0126. Word Ladder II](Solutions/0126.Word-Ladder-II.py) (!!H) 打印/输出所有满足条件的路径必用backtrack. 
Step 1. 从end_word到start_word做bfs，记录每一个节点到end节点的距离，存入hashmap中 eg: distance["dog"] = 2 <br>
Step 2. 从start到end做backtrack，每走一步都必须确保离end的distance越来越近(if distance[next_word] >= distance[curr_word]: continue)
想想210题的Google follow up.
- [0290. Word Pattern](Solutions/0290.Word-Pattern.py) (E) <br>
similar with 1153. String Transforms Into Another Strin. use a mapping to map ch to str, and use another mapping to map str to ch.  warm up for 291.
- [0291. Word Pattern II](Solutions/0291.Word-Pattern-II.py) (!!H) <br>
backtrack传入参数(curr_s_idx, curr_p_idx, ch_to_str, str_to_ch).
backtrack结束条件: if curr_s_idx == len(s) - 1 and curr_p_idx == len(pattern) - 1.
is valid: if ch_to_str[next_ch] == next_word and str_to_ch[next_word] == next_ch.
- [0320. Generalized Abbreviation](Solutions/0320.Generalized-Abbreviation.py) (!!M) <br>
backtrack中传入的参数(curr_idx, curr_num, curr_word). 
backtrack结束条件: if curr_idx == len(word)-1. 
分两种情况: case 1: treat word[next_idx] as a letter; case 2: treat word[next_idx] as a number
- [0037. Sudoku Solver](Solutions/0037.Sudoku-Solver.py) (!!H) <br> 
use rows, cols, boxes dictionary to record the numbers in each row, each col and each small box, then do standard backtrack
- [0465. Optimal Account Balancing](Solutions/0465.Optimal-Account-Balancing.py) (!!H Google) <br> 
step 1: find all the balance information for each person; step 2: we care only those person who own or owe money - put them in a list; backtrack to update the minimum transaction needed. backtrack传入(curr_idx, curr_cnt)
- [0437. Path Sum III](Solutions/0437.Path-Sum-III.py) (M) <br>
不需要从根节点出发，solution 1: dfs every node in the tree. at each node, do a backtrack to find how many root-to-any_node paths are there. 
solution 2: presum solution: O(N). Use a presum to record presum --> how many paths have this presum accured
- [1240. Tiling a Rectangle with the Fewest Squares](Solutions/1240.Tiling-a-Rectangle-with-the-Fewest-Squares.py) (!!!H Google) <br>
backtrack. The basic idea is to fill the entire block bottom up.  In every step, find the lowest unfilled square first, and select a square with different possible sizes to fill it.  What is the nodes in the graph? It is a height array (skyline) height_arr!!!!! 
The start_node is height_arr = [0, 0, 0...], the end_node is height_arr = [m, m, m...]. Pruning: 1. When the current cnt has exceeded the value of the current global optimal solution, then no need to move forward. 2. Try largest square possible first (improves time by a lot).
- [0488. Zuma Game](Solutions/0488.Zuma-Game.py) (!H Google) <br>
backtrack. Each crushed board is a node in backtrack. from curr_crushed_board to next_crushed_board, we need to do a crush recurssively similar with 723. Candy Crush
- [0949. Largest Time for Given Digits](Solutions/0949.Largest-Time-for-Given-Digits.py) (!!M Google) <br>
backtrack. step 1: find all possible permutations - O(4!). step 2: update max_possible time that can be constructed from the permutations.
- [1125. Smallest Sufficient Team](Solutions/1125.Smallest-Sufficient-Team.py) (!!H Google) <br>
backtrack. "The Set Cover Problem": find the min number of subsets to cover the entire set.
This famous "Set Cover Problem" is actually a NP Complete problem.
NP-complete problem: any of a class of computational problems for which no efficient solution algorithm has been found.
solution 1: backtrack - the subset problem 78. Subsets: find the subset that is valid.
O(m* 2^n), where m = len(req_skills), n = len(people)





## [dfs/bfs](/Depth-First-Search.py)
##### 凡是能用bfs和dfs解的题，一律都用dfs解
- [0261. Graph Valid Tree](Solutions/0261.Graph-Valid-Tree.py) (!!M) <br>
判断图是不是一棵树（不一定非要是二叉树）需要满足两点:1. 首先点的数目一定比边的数目多一个; 2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，也就是visited的数目要等于节点数目, 如果小于则说明有的节点被访问不到，如果大于说明有环，则不是树. 遍历节点的方法可以是dfs/bfs. solution 2: Union Find
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (!!!M) <br>
用一个mapping 保存node-->node_copy. 然后一边dfs一边新建copied nodes 
- [0785. Is Graph Bipartite?](Solutions/0785.Is-Graph-Bipartite.py) (!!M)  <br>
solution 1: bfs, use a colormap in which key is the node, value is the color.  visit every node layer by layer and label their color every other step. O(V+E); 
solution 2: dfs.  dfs is better for this problem. O(V+E)
- [0886. Possible Bipartition](Solutions/0886.Possible-Bipartition.py) (!!M Google) <br>
Assign the first person RED, then anyone the first person doesn't like should be assigned BLUE. Then anyone those BLUE persons don't like should be assigned to RED.
If a person has to be both BLUE and RED, then it is impossible. 
Solution 1: dfs - Time: O(V+E); Space: O(V+E); solution 2: 层序遍历bfs; Google两个follow up 很难
- [1042. Flower Planting With No Adjacent](Solutions/1042.Flower-Planting-With-No-Adjacent.py) (!!M) <br>
start from garden 1, do dfs, assign along the way the correponding color,
assign which color? the color that is not in the exclude_color list
- [0399. Evaluate Division](Solutions/0399.Evaluate-Division.py) (!!M) <br>
Solution 1: bfs 去做path compression; 注意这里构建图的时候采用hashmap构建邻接表 graph = collections.defaultdict(dict), in graph, key is node1, val is a dict of (key: node2, val: node1/node2), 然后每次query其实就是从单源节点出发寻求不带权值最短路径问题。  Soltution 2: DFS;
- [1236. Web Crawler](Solutions/1236.Web-Crawler.py) (!!M) <br>
简单bfs/dfs可破，nextUrl必须与currUrl在同一个domain里
- [1242. Web Crawler Multithreaded](Solutions/1242.Web-Crawler-Multithreaded.py) (!!M) <br>
bfs + multi-thread + MapReduce, use ThreadPoolExecutor with 10 worker threads
- [0695. Max Area of Island](Solutions/0695.Max-Area-of-Island.py) (M) <br>
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a dfs/bfs.
- [0339. Nested List Weight Sum](Solutions/0339.Nested-List-Weight-Sum.py) (E) <br>
simple dfs or bfs is ok.
- [0364. Nested List Weight Sum II](Solutions/0364.Nested-List-Weight-Sum-II.py) (M) <br>
do a dfs to find the depth first, then another dfs to do 339. Nested List Weight Sum I
- [0690. Employee Importance](Solutions/0690.Employee-Importance.py) (!!E Google) <br>
simple dfs 可破, use a dictionary to map employee_id with employee, so that looking for employee by id takes O(1)
- [0733. Flood Fill](Solutions/0733.Flood-Fill.py) (!!E) <br>
Solution 1: dfs recurssively, don't need a set to record visited nodes, cuz we can modify the matrix in place; Solution 2: bfs; Solution 3: dfs iteratively; Solution 4: Union Find; 
- [0841. Keys and Rooms](Solutions/0841.Keys-and-Rooms.py) (!!M) <br>
dfs. 这题不能用union find来解
- [0130. Surrounded Regions](Solutions/0130.Surrounded-Regions.py) (!!M) <br>
Solution 1: dfs/bfs: Step 1: Start from border, do a bfs for "O", mark all the "O" that can be reached from the border. We can either mark by putting them into a visited set, or just change it to some symbol "#". Step 2: 2nd pass, we change to "X" tha "O" that could not be visited from the border.  Solution 2: Union Find.  Step 1: Union all the "O" that are neighborign with each other. We do a weighted union, meaning when we union, we also choose to point to the one that is on the border. Step 2: 2nd pass, we change to "X" tha "O" that has a root not on border.  bfs只从border出发做bfs, 很中间的"O"就不用管了，而Union Find中间的也需要union, 所以bfs 比union find 更快。Solution 3: dfs interatively, only change one line in the bfs solution. Solution 4: dfs recurssively.
- [1254. Number of Closed Islands](Solutions/1254.Number-of-Closed-Islands.py) (!!M) <br>
与130出重复了, one pass solution很重要
- [1020. Number of Enclaves](Solutions/1020.Number-of-Enclaves.py) (M) <br>
very similar with 1254. 用一个全局变量self.is_touching_border来判断是否touching border.
- [0417. Pacific Atlantic Water Flow](Solutions/0417.Pacific-Atlantic-Water-Flow.py) (!!M) <br>
题目的意思是外围一圈的地方是water进来的地方，左上角的外围是pacific ocean water进来的地方，右下角的外围是atlantic ocean water进来的地方。
step 1: 从左上角外围的每个点出发做dfs, next_pos is a valid candidate if matrix[curr_pos] <= matrix[next_pos], 
如果能visited就存起来表示pacific ocean water可以到达这个pos；
step 2: 同样的方法记录atlantic ocean water可以达到的pos.  然后用2nd pass 来找到哪些点是两个ocean都能到达的。
- [0694. Number of Distinct Islands](Solutions/0694.Number-of-Distinct-Islands.py) (!!M) <br>
When we start a dfs on the top-left square of some island, the path taken by dfs will be the same if and only if the shape is the same. So path is the signature of shape.
So we can record the path, and count how many distinct path. 特别注意易错的是要在for loop 走完了加上"#", to mark the end of a path.  solution 2: use the relative lacation of each "1" with respect to the staring point as the signature of shape.
- [0711. Number of Distinct Islands II](Solutions/0711.Number-of-Distinct-Islands-II.py) (H) <br>
step 1: use the relative lacation of each "1" with respect to the staring point as the signature of shape. this step is exactly the same as 694.
step 2: rotate and reflect+rotate them against (0,0) in 8 directions, to get hte signature of the rotated shapes.
step 3: choose the smallest among 8 directions to hash.
- [0934. Shortest Bridge](Solutions/0934.Shortest-Bridge.py) (!!M) <br>
setp 1: 用outliners_1, outliners_2 = set(), set()找到两个island的outliner. 
step 2: 接下来是多源节点出发求最短路径问题 - bfs.
这题的关键是怎样找一个岛屿的outliners.
- [0827. Making A Large Island](Solutions/0827.Making-A-Large-Island.py) (!!H) <br>
solution 1: dfs. step 1: get all the islands and store all their positions. step 2: sweep the matrix and change each WATER to LAND one by one to update max_size.  solution 2: UnionFind O(MN) - 要注意每次将0变1都会改变uf的图，所以要提前用一个temp_father=uf.father来保存father的信息
- [0863. All Nodes Distance K in Binary Tree](Solutions/0863.All-Nodes-Distance-K-in-Binary-Tree.py) (M) <br>
step 1: use dfs, change a tree to a graph with adjacency list representation; 
step 2: start from target, use bfs/dfs to find the nodes with distance == K
- [0529. Minesweeper](Solutions/0529.Minesweeper.py) (M) <br>
in dfs: step 1: check how many MINES are there in adjacent to (curr_i, curr_j);
step 2: based on adj_mine, we choose either continue dfs or stop
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](Solutions/1466.Reorder-Routes-to-Make-All-Paths-Lead-to-the-City-Zero.py) (!!M Google) <br>
solution dfs. 问题等价于原来0不能到达所有的nodes, 现在需要改变一些connections使得0可以到达所有nodes. 建一个graph和一个anti_graph. 从0出发，先在anti_graph里面找next_node一直往前走，然后从graph里面找next_node, 从graph里面找说明需要反向，所以self.cnt += 1
- [1377. Frog Position After T Seconds](Solutions/1377.Frog-Position-After-T-Seconds.py) (!!H Google) <br>
dfs, 虚拟一个节点零出来，从0节点出发做dfs. dfs the graph and update the dist of target and the prob of reaching target
- [0753. Cracking the Safe](Solutions/0753.Cracking-the-Safe.py) (!!!H) <br>
思路： dfs取cur_res的最后n-1个数字，加上k中的一个新的数字来组新的combination, 判断这个combination是否已经cover到了. dfs的结束条件是if len(covered) == k ** n
- [1192. Critical Connections in a Network](Solutions/1192.Critical-Connections-in-a-Network.py) (!!H) <br>
solution 1: brutal force: 每次都是尝试去掉一条边，然后看去掉之后connected comonents的个数是不是还是只有一个 - O(E^2).
solution 2: Tarjan's algorithm. In Tarjan's algorithm we keep a list min_steps[i].
min_steps[i]表示节点i所见到过的除了目前的父节点之外的所有节点中步数最小的那一个的步数. dfs 需要传入参数dfs(curr_node, prev_node, steps)






## [dfs + memoization/top down DP](/https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
##### 最重要的是memo状态的定义和递归返回值的定义. memo的key是状态, 往往跟backtrack的状态定义是一样的, val是我们想求的东西与递归返回值是一样的
- [0494. Target Sum](Solutions/0494.Target-Sum.py) (!!M) <br>
solution 1: naive dfs - O(2^n); solution 2: naive dfs + memorization - 从backtrack到memorization只需要将memo dict的key定义为backtrack的arguments, val是需要return的东西。
time complexty is how many diferent keys are possible there - O(n * t) where n is len(nums), t is largest sum possible.
- [0139. Word Break](Solutions/0139.Word-Break.py) (!!M) <br>
solution 1: dp[i]=can partition until ith char?, not including i; dp[j]=true if (for i < j, there is dp[i]=True and s[i:j]is in wordDict). solution 2: bfs, solution 3: dfs + memorization (top-down dp)
- [0140. Word Break II](Solutions/0140.Word-Break-II.py) (!!H) <br>
套用backtrack模板即可.  O(2^m + m^2 + n), where m is the lens of string, n is the lens of word_dict.
O(2^m) comes from backtracking on the string, cuz each 每个ch之间我们可以选择切一刀或不切一刀.
O(m^2) comes from the checking for wordBreakI.  O(n) for converting word_dict to a set.
- [0472. Concatenated Words](Solutions/0472.Concatenated-Words.py) (!!H) 打印/输出所有满足条件的路径必用DFS
dfs + memorization - Top down DP.  与139, 140构成砍单词三部曲！
- [0638. Shopping Offers](Solutions/0638.Shopping-Offers.py) (!!M) <br>
solution 1: backtrack - 套用backtrack模板，backtrack加入的参数有(curr_bought, curr_cost).
backtrack结束条件是if all(curr_bought[i] >= needs[i] for i in range(len(needs))).
backtrack的剪枝很重要 - skip deals that exceed needs: if any(special[i] > needs[i] - curr_bought[i] for i in range(len(needs)))
O(2^M* L* N) where L is len(prices), M is how many specials are there, N is value of needs; solution 2: dfs + memorization
- [0514. Freedom Trail](Solutions/0514.Freedom-Trail.py) (!!H) <br>
dfs+memo的关键是memo的定义，跟dp的关键是状态的定义是一样的。
这题的定义为memo[(curr_ring, curr_idx)] = minimum step needed to reach target)
then memo[(curr_ring, curr_idx)] = min(memo[(curr_ring, curr_idx)], steps + 1 + dfs(next_ring, curr_idx + 1, memo))
- [0293. Flip Game](Solutions/0293.Flip-Game.py) (E) <br>
- [0294. Flip Game II](Solutions/0294.Flip-Game-II.py) (!!M) <br>
dfs+memo: O(N^2); memo = (curr_state-->guarantee a win)
- [0329. Longest Increasing Path in a Matrix](Solutions/0329.Longest-Increasing-Path-in-a-Matrix.py) (!!!H Google) <br>
solution 1: 从每一个点开始做backtrack - next candidate valid的条件是matrix[next_i][next_j] > matrix[curr_i][curr_j].  - O(MN2^(MN)).  solution 2: 由于题目并不要求算出path, 所以可以用recurssion with memorization to memorize the LIP from (curr_i, curr_j) (top down dp). Time complexity : O(MN). solution 3: buttom up dp.
- [1057.Campus-Bikes.py](Solutions/1057.Campus-Bikes.py) (!!M) <br>
brutal force solution O(MNlog(MN)): find the distance of all combinations, and sort them.
. bucket sort solution O(MN): find the distance of all combinations, and put them into bucket based on their distance. 
In this way, the distances are represented by idx, which were sort by nature. <br>
- [1066. Campus Bikes II](Solutions/1066.Campus-Bikes-II.py) (!!M Google) <br>
backtracking with memorization, 由于必须把assigned_bike set放入到state中，所以是指数级别的复杂度, solution 2: backtrack + Dijkstra's <br>
Extention: __Campus Bikes III (minimize max) - Dijkstra's__
- [0464. Can I Win](Solutions/0464.Can-I-Win.py) (M)
dfs + memo, memo: (curr_choosable_numbers --> can_win_with_curr_choosable_numbers?)
- [0551. Student Attendance Record I](Solutions/0551.Student-Attendance-Record-I.py) (E Google) <br>
warm up for 552. Student Attendance Record II.
- [0552. Student Attendance Record II](Solutions/0552.Student-Attendance-Record-II.py) (!!!H Google) <br>
dfs + memo. solution 1: typical backtrack - O(3^N); solution 2: dp - O(n). dp[i] = how many ways for i. If we don't have "A" in the record, then we have below: dp[i] = dp[i-1] if choose ith ch to be "P". dp[i] = dp[i-2] if choose the last two ch to be "PL"
dp[i] = dp[i-3] if choose last three ch to be "PLL", note that cannot be "LLL". so dp[i] = dp[i-1] + dp[i-2] + dp[i-3] for the case there is not "A" in the record. Now we have the dp[i] for the case with out "A". Since we can add "A" anywhere, so the res = sum(dp[i-1] * dp[n-i]).
- [Longest snake in a matrix](Solutions/Google_longest-snake-in-a-matrix.py) (!!M Google) <br>
dfs + memo same as 329. Longest Increasing Path in a Matrix.  特别注意： 一般四个方向都可以走的情况不能用bottom up dp. 因为dp[i][j]需要用到dp[i-1][j], 而dp[i-1][j]也需要用到dp[i][j]，
所以会形成环，DP需要无后效性，基本上是有向无环图，也就是必须能够拓扑排序。正确解法: dfs + memo, same as 329. Longest Increasing Path in a Matrix. dfs with memorization to memorize the LIP from (curr_i, curr_j)
- [1223. Dice Roll Simulation](Solutions/1223.Dice-Roll-Simulation.py) (!!!M Google) <br>
solution 1: backtrack - O(6^N) in worst case. 不需要传入curr_comb, 只需要last_num和the repeat time of last_num. solution 2: backtrack + memo - O(6n^2). 套backtrack + memo的模板即可
- [Google_面经1](Solutions/Google_面经1.py) (!!!M Google) <br>
- [1444. Number of Ways of Cutting a Pizza](Solutions/1444.Number-of-Ways-of-Cutting-a-Pizza.py) (!!!H Google) <br>
dfs + memo. memo[(i, j, k)] returns the number of ways to cut pizza[i:n][j:m] into k pieces.
Step 1: In order to fast get how many apples are there in the down-right corner pizza[i:n][j:m] block,
construct suff_sum similar with 304. Range Sum Query 2D - Immutable. Step 2: dfs + memo.







# [Dynamic Programming/bottom up DP](Dynamic-Programming.py)
### [坐标型DP](/Dynamic-Programming.py)
- [0062. Unique Paths](Solutions/0062.Unique-Paths.py) (!!M) <br>
状态: f[i][j]=有多少种方式从左上角走到(i, j); 转移方程：f[i][j] = f[i][j-1]+f[i-1][j]
- [0063. Unique Paths II](Solutions/0063.Unique-Paths-II.py) (M) <br> 
转移方程：f[i][j] = 0 if it is obstacle else f[i][j-1]+f[i-1][j])
- [Google Unique Paths With Ladder](Solutions/0063.Unique-Paths-II.py) (M) <br> 
dp[i][j] = the number of unique paths to reach (i, j). dp[i][j] += dp[i-1][j] if grid[i][j] <= grid[i-1][j] + k; dp[i][j] += dp[i][j-1] if grid[i][j] <= grid[i][j-1] + k
- [0064. Minimum Path Sum](Solutions/0064.Minimum-Path-Sum.py) (M) <br> 
dp[i][j]=the minimum path sum to (i, j); dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]). DP works because we can pre compute two directions ... but we cannot pre-compute 4 directions or more .. in those cases Djikstra would be better
- [0120. Triangle](Solutions/0120.Triangle.py) (M) <br>
dp[i][j] = min(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1]), rolling array to reduce space to O(N)
- [0931. Minimum Falling Path Sum](Solutions/0931.Minimum-Falling-Path-Sum.py) (M) <br>
dp[i][j] = min(dp[i-1][j-k] + A[i][j], where k = -1,0,1)
- [1289. Minimum Falling Path Sum II](Solutions/1289.Minimum-Falling-Path-Sum-II.py) (!!H) <br>
similar with 265. Paint House II: 将上一行的fisrt_min和second_min提前计算好 - O(MN)
- [0174. Dungeon Game](Solutions/0174.Dungeon-Game.py) (!!H Google) <br>
find the max of mininum_sum in all the paths.这题不能像1102.Path-With-Maximum-Minimum-Value那样用Dijkstra's (mnlogn)因为这题不是四个方向都能走的，也就是说选择了一个方向就不能回到原来的位置了，所以只能dp -O(mn). 假设我们能到达(m, n)房间，我们需要的最小血量是dp[m][n] = 1 if A[m][n] >= 0 else 1- A[m][n], 这是我们的base case.
那我们就知道了我们到达(m-1, n)房间所需的最小血量是dp[m-1][n] = 到达(m, n)房间所需要的血量减去在(m-1, n)房间的损耗，
即dp[m-1][n] =max(dp[m][n] - A[m-1][n], 1); 到达(m, n-1)房间所需的最小血量是dp[m][n-1] = max(dp[m][n] - A[m][n-1], 1).
所以我们是从终点倒着往起点推。
- [0221. Maximal Square](Solutions/0221.Maximal-Square.py) (M) <br>
dp[i][j]=以(i, j)为右下角的最大正方形的边长; dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j]=1 
- [1277. Count Square Submatrices with All Ones](Solutions/1277.Count-Square-Submatrices-with-All-Ones.py) (M Google) <br>
DP. very similar with 221.Maximal-Square. dp[i][j] 表示以 (i, j) 结尾所组成的最大正方形的边长。dp[i][j] 也表示以 (i, j) 结尾能组成的正方形的个数。
- [0403. Frog Jump](Solutions/0403.Frog-Jump.py) (H) <br>
维护一个stonesDict的key is the stone in stones. value is the possible steps to reach the stone.
There could be multiple possible steps to reach the stone, so stonesDict[stone] = set(). 
状态转移方程为：1. 跳k-1到stone+k-1: stonesDict[stone + k - 1].add(k - 1); 2. 跳k到stone + k: stonesDict[stone + k].add(k); 3. 跳k + 1到stone + k + 1:stonesDict[stone + k + 1].add(k + 1); Return stonesDict[last stone] is not empty; this is bottom up method O(N^2), O(N^2)
- [1463. Cherry Pickup II](Solutions/1463.Cherry-Pickup-II.py) (!!!H Google) <br>
dp[i][j1][j2] = the max cherry when robot reached (i, j1) and (i, j2). 注意要判断dp[i-1][prev_j1][prev_j2] >= 0 表示(prev_j1, prev_j2)可以到达
- [0741. Cherry Pickup](Solutions/0741.Cherry-Pickup.py) (!!H Google) <br>
Go from (0, 0) -> (n-1, n-1) -> (0, 0) can be treated as two men go from (0, 0) -> (n-1, n-1) together, dp[x1][y1][x2] to represent the largest ans we can get when first guy (marked as A) at(x1, y2) and second guy(marked as B) at (x2, x1 + y1 - x2)




### [序列型DP](/Dynamic-Programming.py)
- [0978. Longest Turbulent Subarray](Solutions/0978.Longest-Turbulent-Subarray.py) (!!M) <br>
dp: keep track of the lens of current increasing subarray and lens of current decreasing subarray.
inc = dec + 1 if A[i]>A[i-1]; dec = inc + 1 if A[i]<A[i-1]
- [0256. Paint House](Solutions/0256.Paint-House.py) (E) <br>
dp[i][j] means the minimum cost to paint house i to be color j; dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
- [0265. Paint House II](Solutions/0265.Paint-House-II.py) (!!H) <br> 
dp[i][j]=minimum cost to paint the ith house the be color j; dp[i][j] = dp(min in the (i-1)th row) + costs[i][j]. In order to find dp(min in the (i-1)th row), we can find the position for the 1st and 2nd min in the i-1 th row first, then in the ith row calcuation, if j==1st_min_pos, then dp[i][j]=2nd_min + costs[i][j], else dp[i][j]=1st_min + costs[i][j]
- [0198. House Robber](Solutions/0198.House-Robber.py) (E) <br>
f[i]=the max profit when reaching ith house; f[i] = max(rob ith = f[i-2]+nums[i], not rob ith = f[i-1]) <br>
空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]
- [0213. House Robber II](Solutions/0213.House-Robber-II.py) (!!M) <br>
房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：1. 房子1没偷：问题变成了对房子2:N做House robber I的问题; 2. 房子N没偷：问题变成了对房子1:N-1做House robber I的问题
- [0337. House Robber III](Solutions/0337.House-Robber-III.py) (!!M) <br>
树状的house.递归： def with_without_rob(self, root): return a tuple, the 1st element in the tuple is the max profift with_rob_root， the 2nd element in the tuple is the max profit without_rob_root. 递归公式：with_rob_root = root.val + without_rob_left + without_rob_right; without_rob_root = max(with_rob_left, without_rob_left) + max(with_rob_right, without_rob_right)
- [0152. Maximum Product Subarray](Solutions/0152.Maximum-Product-Subarray.py) (!!M) <br>
最大值问题。maxDP[i]表示以i为结尾的subarray的最大的正数，minDP[i]表示以i为结尾的subarray的最小负数. 根据nums[i]的正负, 更新maxDP[i]和minDP[i]
- [0983. Minimum Cost For Tickets](Solutions/0983.Minimum-Cost-For-Tickets.py) (!!M) <br>
我们定义函数f(i)表示第i天的最低消费，那么
某天，如果你不必出行的话，等一等再购买火车票一定更优，如果你需要出行的话，那么就有三种选择：在通行期为 1 天、7 天、30 天中的火车票中选择一张购买。
f(i)=f(i−1)  if i not in days
else f(i)=min(f(i−1)+costs[0],f(i−7)+costs[1],f(i−30)+costs[2])


### [Buy and sell stock DP问题](/Dynamic-Programming.py)
#### 所有的buy and sell stock问题都可以分两种状态进行更新：hold and unhold: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益.
#### we update hold[i] and unhold[i] as we loop over the prices list.
- [0121. Best Time to Buy and Sell Stock](Solutions/0121.Best-Time-to-Buy-and-Sell-Stock.py) (E) <br>
Only one transaction is allowed.  Maintain a curr_min and a max_prof; max_prof = max(max_prof, price - curr_min)
- [0122. Best Time to Buy and Sell Stock II](Solutions/0122.Best-Time-to-Buy-and-Sell-Stock-II.py) (E) <br>
As many transaction as possible.  make a transaction every time price[i]>price[i-1]
- [0309. Best Time to Buy and Sell Stock with Cooldown](Solutions/0309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py) (M) <br>
Has to rest for one day before buy another stock.  **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益, return unhold[-1] <br> 
hold[i] = max(hold[i-1], unhold[**i-2**]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i]) 学会画state machine
- [0714. Best Time to Buy and Sell Stock with Transaction Fee](Solutions/0714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) (M) <br>
There is transaction fee when you sell. **分两个状态: hold and unhold**: hold[i]=第i天有股票在手状态下的最大收益； unhold[i]=第i天没有股票在手状态下的最大收益 <br>
hold[i] = max(hold[i-1], unhold[i-1]-prices[i]); unhold[i] = max(unhold[i-1], hold[i-1] + prices[i] **- fee**)
- [0123. Best Time to Buy and Sell Stock III](Solutions/0123.Best-Time-to-Buy-and-Sell-Stock-III.py) (H) <br>
Only two transactions are allowed.  Maintain buy1=the minimum money you can **owe** after the first buy, sell1=the maximum money you **earn** after the first sell, also, buy2, sell2, and update them together in a for loop, 算法只是把121中的算法重复两次而已.
- [0188. Best Time to Buy and Sell Stock IV](Solutions/0188.Best-Time-to-Buy-and-Sell-Stock-IV.py) (H) <br>
Only k transactions are allowed.   Maintain buy=[]* k, sell=[]* k, and update them together in a for loop. buy[i] = min(buy[i], price - sell[i - 1]), buy[i] = the minimum money you can own after the ith purchase; sell[i] = max(sell[i], price - buy[i]), sell[i] = the maximum money you can earn after the ith purchase.  Solve the memory overflow problem: if k>prices.length/2, then it is the same as 122.
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M) <br>
与714. Best Time to Buy and Sell Stock with Transaction Fee 很像，都有交换和不交换两种情况



###  [最长子序列问题](/Dynamic-Programming.py) 
##### (dp[i]都是定义为以i结尾的最长....)
- [0674. Longest Continuous Increasing Subsequence](Solutions/0674.Longest-Continuous-Increasing-Subsequence.py) (E) <br>
dp[i] = 以i结尾(包括i)的最长连续子序列; dp[i] = dp[i-1] + 1 if nums[i]>nums[i-1]; solution 2: 同向双指针（滑动窗口）
- [Google__similar with 674 Longest Continuous Increasing Subsequence](Solutions/Google__similar_with_0674.Longest-Continuous-Increasing-Subsequence.py) (E) <br>
- [0300. Longest Increasing Subsequence](Solutions/0300.Longest-Increasing-Subsequence.py) (!!M) <br> 
不需要连续，所以不是dp[i] = dp[i-1] + 1，而是所有的j之前的i都有可能, 所以转移方程是 dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]) <br>
dp + binary search (O(NlogN))的算法也很重要！dp[i] = the maintianed array with i as the possible increadsing numbers, dp should be an orderd array: if nums[i] > the last item in dp, then append nums[i] to dp, else then将sorted arr中最接近num的数用num取代, by using binary search. same as 35. Search Insert Position
- [0354. Russian Doll Envelopes](Solutions/0354.Russian-Doll-Envelopes.py) (!!H) <br>
solution 1 dp - O(N^2): Similiar with 300. LIS; sort the list first envelopes.sort(key = lambda x: (x[0], x[1])), here we not only compare nums[j]>nums[i], but instead both the width and height; TLE. Solution 2: sort the evelopes first (tricky in sorting order!!), then 用length来做300. LIS - O(nlogn)
- [0673. Number of Longest Increasing Subsequence](Solutions/0673.Number-of-Longest-Increasing-Subsequence.py) (!!M) <br>
 dp=以i为结尾的最大的长度; cnt=以i为结尾的最大的长度的个数; 在nums[j]>nums[i]的情况下：cnt[j]+=cnt[i] if dp[j]=dp[i]+1.    
- [1218. Longest Arithmetic Subsequence of Given Difference](Solutions/1218.Longest-Arithmetic-Subsequence-of-Given-Difference.py) (!!!M Google) <br>
dp, similar with. solution 1: O(N^2), dp[i] = the LAS ended with arr[i]. dp[j] = dp[i] + 1 for i < j and arr[j] - arr[i] == diff. O(N) use hashmap, like two sum problem. dp[arr[j]] = dp[arr[j] - diff] + 1 if arr[j] - diff in dp else 1.
- [1027. Longest Arithmetic Sequence.py](Solutions/1027.Longest-Arithmetic-Sequence.py) (!!M) <br>
dp[i] = {key:diff, val:lens of arithmetic sequence ended with i and diff as 公差}; dp[j][nums[j]-nums[i]] = dp[i][nums[j] - nums[i]] + 1
- [0873. Length of Longest Fibonacci Subsequence](Solutions/0873.Length-of-Longest-Fibonacci-Subsequence.py) (M) <br>
dp[i]=dictionary{key: last num of the fib; val: the lens of the fib ended with ith}, dp[j][nums[i]]=d[i][nums[j]-nums[i]]+1
- [0334. Increasing Triplet Subsequence](Solutions/0334.Increasing-Triplet-Subsequence.py) (M) <br>
Similiar with 300. LIS; dp[j] = max(dp[i] + 1 for i<j and nums[i]<nums[j]); if dp[j]>=3 return True；  how to solve it in O(N), O(1); min_1, min_2 and are the most min and the second min in the arr, if min_1 and min_2 are renewed twice already and there is a num>min_2 later, then return True.
- [1048. Longest String Chain](Solutions/1048.Longest-String-Chain.py) (!!M Google) <br>
dp = dict, key is word, val is the longest chain lens ended with word; prevWord = word[:i]+word[i+1:]; if prevWord in dp: dp[word] = max(dp[redesessor]+1)
- [0907. Sum of Subarray Minimums](Solutions/0907.Sum-of-Subarray-Minimums.py) (!!!M) <br>
我们其实关心的是以某个数字结尾时的子数组最小值之和，可以用一个一维数组 dp，其中 dp[i] 表示以数字 A[i] 结尾的所有子数组最小值之和， 遍历A, 更新 dp[i] = dp[idx] + A[i] * (i-idx)，其中idx是往左寻找第一个比当前A[i]小的数的idx，
最终的结果 res 就是将 dp 数组累加起来即可. 为了更快速得到往左寻找第一个比当前A[i]小的数的 idx, 我们可以提前算好存起来，怎样算：monostack. 这种预先计算好sums的思想非常重要，参看132. Palindrome Partitioning II.
- [0646. Maximum Length of Pair Chain](Solutions/0646.Maximum-Length-of-Pair-Chain.py) (!M Google) <br>
dp. step 1: sort the interval by end_time or start_time;
step 2: dp. dp[i] = the max lens ended with ith interval. dp[j] = max(dp[i] + 1 for i < j and intervals[i][1] < intervals[j][0]). O(N^2)
solution 2 greedy: 找到所有overlapped intervals. 用一个last_end指针记录上一个end; O(NlogN)
- [1235. Maximum Profit in Job Scheduling](Solutions/1235.Maximum-Profit-in-Job-Scheduling.py) (!!H Google) <br>
dp. similar with 646. Maximum Length of Pair Chain, we define dp as dp[i] = the max_prof for intervals __ended with__ ith interval; dp[j] = max(dp[i] + profit[j] for i < j if endTime[i] <= startTime[j]). O(N^2). solution 2: dp. 我们将dp定义为dp[i] = the max_prof for intervals __before (including)__ ith interval; solution 3: dp + binary search. 由于我们定义dp[i] = the max_prof for intervals before (including) ith interval, 所以dp是递增的，所以只需要在dp[:j]中选最后一个满足intervals[i][1] <= intervals[j][0]的i就可以了



### [区间型DP](/Dynamic-Programming.py) 
##### 状态定义为f[i][j]表示面对子区间[i, j]时的最佳性质
- [0005. Longest Palindromic Substring](Solutions/0005.Longest-Palindromic-Substring.py) (!!M) <br>
题目问substring, substring就需要是连续的，题目要求Return the longest substr: dp[i][j]=from i to j (including j), is it a palindr? if s[i]==s[j]: dp[i][j] = dp[i+1][j-1]; 注意初始化对角线和相邻的，因为计算dp[i][j]需要用到dp[i+1][j-1]，所以要先算i+1, 再算i，所以i 是倒序遍历
solution Solution 2: central spread.  从中间c往两边遍历i--, j++，遍历两次：一次是i=c, j=c开始遍历， 一次是i=c, j=c+1开始遍历。
- [0647. Palindromic Substrings](Solutions/0647.Palindromic-Substrings.py) (!!M) <br>
dp[i][j] = is s[i to j including i and j] a palindrome?
dp[i][j] = True if s[i]==s[j] and (dp[i+1][j-1] or lens <=2).
if it is True, then number of palindromic substring += 1
- [0516. Longest Palindromic Subsequence](Solutions/0516.Longest-Palindromic-Subsequence.py) (!!M) <br>
题目问subsequence, subsequence不需要连续，题目要求Return the longest length: dp[i][j]=longest palindr from i to j; dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j], dp[i][j-1]);注意初始化对角线，因为计算dp[i]需要用到dp[i+1]，所以要先算i+1, 再算i，所以i is from (j, 0)
- [0680. Valid Palindrome II](Solutions/0680.Valid-Palindrome-II.py) (E) <br>
warm up for next question.  two pointers: if s[i] != s[j]: return self.ispalin(s[i:j]) or self.ispalin(s[i+1:j+1])
- [1216. Valid Palindrome III](Solutions/1216.Valid-Palindrome-III.py) (H) <br>
find the Longest Palindromic Subsequence L, return lens - L <= k.
- [0476. Stone Game](Solutions/0476.Stone-Game.py) (!!M Lintcode) <br>
dp[i][j]表示合并i到j的石头需要的最小代价, including i and j.
转移函数：dp[i][j] = max(dp[i][k]+dp[k+1][j]+sums[i][j] for k in range(i, j)). 
即合并i－j的代价为合并左边部分的代价＋合并右边部分的代价＋合并左右部分的代价（即i－j所有元素的总和）。找到使dp[i][j]最小的k.
- [0312. Burst Balloons](Solutions/0312.Burst-Balloons.py) (!!H) <br>
solution 1: dp[i][j] = max coin we can get from i to j, __not including i, not including j__.  dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]* nums[k]* nums[j] for k in range(i+1, j)). solution 2: backtrack without memorizaiton - O(2^N). solution 3: 带memo的recursion; left = self.memoSearch(nums, i, k, memo); right=self.memoSearch(nums, k, j, memo); maxCoins = max(maxCoins, left + right + nums[i] * nums[k] * nums[j]). 
- [0374. Guess Number Higher or Lower](Solutions/0374.Guess-Number-Higher-or-Lower.py) (!!M Google) <br>
Binary search.
- [0375. Guess Number Higher or Lower II](Solutions/0375.Guess-Number-Higher-or-Lower-II.py) (!!M Google) <br>
DP. dp[i][j] = 数字在[i, j]范围内所需要的最小payment. dp[i][j] = mid + max(dp[i][mid-1], dp[mid+1][j]) for mid in range(i, j)
- [0471. Encode String with Shortest Length](Solutions/0471.Encode-String-with-Shortest-Length.py) (!!!H Google) <br>
solution dp. dp[i][j] is the encode of substring including index i to index j. dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j], potential_candidate) in terms of length.
potential_candidate = "k[repeating_pattern]",  where pattern is the repeating string in substring s[i:j+1] and k is the number of repeating times. 
initializaton: dp[i][j] = s[i:j+1] originally, return dp[0][n-1]



###  [划分型DP](/Dynamic-Programming.py) 
#### 状态定义为前j个的某种特性，__不包括 j__. 这个思想很重要，相当于给前面做了一层buffer layer!!
- [0139. Word Break](Solutions/0139.Word-Break.py) (!!M) <br>
solution 1: dp[i]=can partition until ith char?, not including i; dp[j]=true if (for i < j, there is dp[i]=True and s[i:j]is in wordDict). solution 2: bfs, solution 3: dfs + memorization (top-down dp)
- [0091. Decode Ways](Solutions/0091.Decode-Ways.py) (M) <br>
f[i]=number of decode ways until i (not including i); f[i]=f[i-1]+f[i-2] if int(s[i-2:i])<=26 else f[i-1]
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (!!M) <br>
f[j]=the least number of perfect square numbers which sum to i; f[j] = min(f[j-i^2]+1) for i^2<=j; Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5); solution 2: level order BFS.
Given a N-ary tree, where each node represents a __remainder__ of the number n subtracting a combination of square numbers, 
our task is to find a node in the tree, which should meet the conditions or remainder=0.
Time complexity: 比较复杂最后是 O(n^(h/2)), where h is the height of the N-ary tree, h is 0 to 4
- [0132. Palindrome Partitioning II](Solutions/0132.Palindrome-Partitioning-II.py) (!!H) <br>
子数组或者子字符串且求极值的题，基本就是 DP 没差了. f[j]=the minimum number of total palindrome till the jth character (not including j); f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome. O(N^3), 划分型的dp的状态一般都not include j, 这样就有一个buffer layer可以用。Solution 2: 优化为O(N^2), 用一个isPalin[i][j]记录s[i:j]是否是palindrome, 更新isPalin[i][j]的方法与leetcode 5 相同，这样就不用每次都用双指针去判断s[i:j]是不是palindrome. 这种预先计算好的思想非常重要，参看907. Sum of Subarray Minimums.  输出所有的可能的partition成palindrome的组合问题只能dfs+backtracking了- 131. Palindrome Partitioning
- [1043. Partition Array for Maximum Sum](Solutions/1043.Partition-Array-for-Maximum-Sum.py) (!!M) <br>
Suppose you are at position X of the array. What is the maximum possible sum to this point?
so we go back K-1 steps, we choose the maximum from the following combinations: dp_sum[X - (k-1)] + max(A[X-(k-2)] ..... A[X])* (k-1)



### [博弈型DP](/Dynamic-Programming.py)
- [0394. Coins in a Line](Solutions/0394.Coins-in-a-Line.py) (M Lintcode) <br>
Solution1 dp: f[i]=面对i个石子，先手是必胜吗; f[i]=True if f[i-1] or f[i-2] 有一个是False <br>
Solution 2: 至于prev, curr有关，所以可以空间优化成O(1)了; Solution 3 数学: 只要是3的倍数就一定输 return n % 3 != 0
- [0486. Predict the Winner](Solutions/0486.Predict-the-Winner.py) (M) <br>
f[i][j]=当石子还剩i到j时，先手最多能赢多少; f[i][j] = max(取左边A[i]-f[i+1][j], 取右边A[j]-f[i][j-1]), 注意f[i][j]与f[i+1][j]相关，所以i要从后往前遍历.
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
- [1025. Divisor Game](Solutions/1025.Divisor-Game.py) (E) <br>
dp[i] = can he/she win facing i



### [背包型DP](/Dynamic-Programming.py)
#### 1. 背包问题的特点：题目要求加起来满足什么条件往往是背包；2. 背包问题总重量一定要入状态！ 3. 如果list中的items不能重复利用，那么状态要定义为成二维：前i个item拼出m的个数/可能性/方法/性质; 4. buffer layer
- [0322. Coin Change](Solutions/0322.Coin-Change.py) (!!M) <br>
背包问题，重量一定要入状态。状态: f[X]=最少用多少枚硬币拼出X; 转移方程：f[X] = min(f[X-1]+1, f[X-2]+1, f[X-5]+1, f[X])
- [0092. Backpack](Solutions/0092.Backpack.py) (!!M Lintcode) <br>
__背包里的物品不能重复使用，所有状态定义为二维__ f[i][m]=能否用前i个物品拼出重量m; f[i][m] = f[i-1][m] (不放入，表示前i-1个物品就可以拼出m) or f[i-1][m-A[i-1]] (放入，表示前i-1个物品可以拼出m-A[i-1]); # 注意点1：这里要定义lens+1，这样就可以做一个buffer layer出来了; # 注意点2；这里循环i在外面，m在里面，千万别搞反了！！# 注意点3：由于buffer layer的存在，这里用nums[i-1]与m相比较
- [0563. Backpack-V](Solutions/0563.Backpack-V.py) (!!M Lintcode) <br>
__一个num不能取多次，所有状态定义为二维__ ，f[i][m]=前i个物品能拼出重量m有多少种方式。f[i][m] = 不放入 f[i-1][m] + 放入 f[i-1][m-A[i-1]] if m > nums[i]
- [1049. Last Stone Weight II](Solutions/1049.Last-Stone-Weight-II.py) (M)
找一组数使他们的和尽可能接近sum(nums)//2.
由于一个数只能用一次，所以我们使用二维dp: dp[i][m] = can we use first i nums to add up to m? 
dp[i][m] = True of dp[i-1][m] == True or dp[i-1][m-A[i]] == True
- [0518. Coin Change 2](Solutions/0518.Coin-Change-2.py) (M) <br>
与Combination Sum一模一样，只是题目不要求输出所有可能组合，只要求输出可能组合的数目，所以可以用DP解。DP解的for循环顺序很重要，由于(1,3)和(3,1)被认为是同一解，所以for coin in coins:是主循环，for num in range(1, amount + 1):是次循环。因为当coin遍历到coin=1的时候，dp[4]+=dp[3]此时的dp[3]=0所以dp[4]实际上加的是0；而当coin遍历到coin=3的时候，dp[4]+=dp[1]，此时dp[1]被更新过一次。所以真个过程dp[4]只被更新一次，不会重复更新。
- [0377. Combination Sum IV](Solutions/0377.Combination-Sum-IV.py) (M)<br>
self.dfs(nums, target - nums[i], 0, curr, res)  # (1, 3)和(3, 1)被认为是不同解，所以让i从0开始; solution 2: dp. 一个num能取多次，所以与322. coin change 相同。所以可以用一维数组，f[i]=how many ways to combine to number i; 背包问题一定要把总承重放到状态里！！ f[i]=f[i-A1]+f[i-A2]+f[i-A3].... <br> DP解的for循环顺序很重要， for m in range(target + 1): 是主循环，for num in nums:是次循环，这么写可以保证(1,3)可以进solution, (3,1)也可以进solution, 所以符合题意。
- [0125. Backpack II](Solutions/0125.Backpack-II.py) (!!M Lintcode) <br>
这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。用子问题定义状态：即f[i][j]表示前i件物品拼出重量j可以获得的最大价值。
f[i][j]=max{f[i-1][j] (不放入),f[i-1][j-A[i-1]]+V[i-1] (放入)}; return f[lens][M]
- [0089. k Sum](Solutions/0089.k-Sum.py) (M Lintcode) <br>
f[i][j][s]表示有多少种方法可以在前i个数中选出j个，使得它们的和是s; 情况一:（A[i-1]不选入）：需要在前n-1个数中选K个数，使得它们的和是Target: f[i][j][s] += f[i-1][j][s]; 情况二（A[i-1]选入）：需要在前i-1个数中选j-1个数，使得它们的和是Target-A[i-1]: f[i][j][s] += f[i-1][j-1][s-A[i-1]]
- [0416. Partition Equal Subset Sum](Solutions/0416.Partition-Equal-Subset-Sum.py) (M) <br>
背包问题：将A中的物品放入容量为target的背包中，问是否存在 __背包里的物品不能重复使用，所有状态定义为二维__ 。与0092一模一样。 f[i][t]=将前i个物品放入背包中，能否拼出t (背包问题重量一定要入状态); f[i][t]=True if 不放最后一个进背包: f[i-1][t]=True or 放最后一个进背包: f[i-1][t-A[i-1]]=True
- [1155. Number of Dice Rolls With Target Sum](Solutions/1155.Number-of-Dice-Rolls-With-Target-Sum.py) (M)
dp[i][m] = how many ways to add up to m using i dices. - 背包问题总承重要放入状态
dp[i][m] += sum(dp[i-1][m - all_possible_f])
- [0473. Matchsticks to Square](Solutions/0473.Matchsticks-to-Square.py) (!!M) <br>
backtrack: 698. Partition to 4 Equal Sum Subsets
- [0956. Tallest Billboard](Solutions/0956.Tallest-Billboard.py) (!!M) <br>
Given a list of numbers, multiply each number with 1 or 0 or -1, make the sum of all numbers to 0. 
Find a combination which has the largest sum of all positive numbers.


### [位操作型DP](/Dynamic-Programming.py)
- [0338. Counting Bits](Solutions/0338.Counting-Bits.py) (M) <br>
状态dp[i]=i的二进制中有多少个1; dp[i] = dp[i >> 1] + i % 2
- [0898. Bitwise ORs of Subarrays](Solutions/0898.Bitwise-ORs-of-Subarrays.py) (M)
simply just find all the possible. res is a set that stores all the possible combinations.
curr is a set that stores all the combinations ended with ith number as we loop over the list.


### [双序列型DP!!](/Dynamic-Programming.py) 
#### dp[i][j]定义为二维数组下标表示序列A前i个，序列B前j个的某个性质
- [1143. Longest Common Subsequence](Solutions/1143.Longest-Common-Subsequence.py) (!!M) <br>
f[i][j]为A前i个字符A[0..i)和B前j个字符[0..j)的最长公共子串的长度，注意不包括i和j，前面有一层buffer layer非常重要，就像sputtering那样重要！ f[i][j]=f[i-1][j-1] + 1 when A[i-1]=B[j-1], else f[i][j]=max(f[i-1][j], f[i][j-1])) # 注意有了buffer layer之后，dp中的i对应的是text中的i-1,所以判断条件是when A[i-1]=B[j-1]
- [0718. Maximum Length of Repeated Subarray](Solutions/0718.Maximum-Length-of-Repeated-Subarray.py) (!!M)
__两个arr/string common subarr/substring的问题都similar with 1143.Longest Common Subsequence__. since subarray has to be continuous, we define dp as
dp[i][j] = the max lens of repeated subarray ended with A[i] and B[j]
dp[i][j] = if A[i-1]==B[j-1]: dp[i-1][j-1] + 1; else: 0 cuz has ot be continuous.
solution 2: binary search - (m+n)mlogm.
- [583. Delete Operation for Two Strings](Solutions/0583.Delete-Operation-for-Two-Strings.py) (M) <br>
f[i][j] = the min number of steps needed to make word1[:i] and word[:j] the same; f[i][j]=f[i-1][j-1] when A[i-1]=B[j-1], else f[i][j]=min(f[i-1][j], f[i][j-1])) + 1
- [1092. Shortest Common Supersequence](Solutions/1092.Shortest-Common-Supersequence.py) (!!H) <br>
solution 1: naive backtrack - O(2^(M+N)); solution 2: recursion + memorization (bottom up dp) - O(MN); solution 3: top down dp - O(MN); step 1: construct_dp_table; step 2: get_result_by_reversely_traverse_dp_table
- [0161. One Edit Distance](Solutions/0161.One-Edit-Distance.py) (M) <br>
warm up problem for 72.  One pass solution using two pointers: if s[i] != t[j]: return s[i+1:] == t[j+1:] or s[i+1:] == t[j:] or s[i:] == t[j+1:]
- [0097. Interleaving String](Solutions/0097.Interleaving-String.py) (!!H) <br>
f[i][j]=s3的前[0..i+j)个字符能否由s1前i个字符[0..i)和s2前j个字符[0..j)交错形成; f[i][j]=True when (s3[i+j-1]=s1[i-1] 且 f[i-1][j]=True 即s3的前[0..i+j-1)个字符能否由s1前i-1个字符[0..i-1)和s2前j个字符[0..j)交错形成) or (s3[i+j-1]=s2[j-1] and f[i][j-1]=True)
- [0115. Distinct Subsequences](Solutions/0115.Distinct-Subsequences.py) (H) <br>
dp[i][j] = the number of discinct subeseq until ith char in s and jth char in t; if s[i]!=t[j], dp[i][j] = dp[i - 1][j]  eg: rab, ra; else: rabb, rab, dp[i][j] = dp[i-1][j] + dp[i-1][j-1], 品，细品！ 
- [0044. Wildcard Matching](Solutions/0044.Wildcard-Matching.py) (H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配； 画个图会很明了，详见九章算法动态规划双序列型DP。
情况一：B[j-1]不是"星": if (B[j-1]="?" or A[i-1]=B[j-1]): f[i][j] = f[i-1][j-1]  <br>
情况二：B[j-1]是"星"：可以让"星"表示0个字符，那就让A[0..i)去和B[0..j-1)匹配： f[i][j] = f[i][j-1]；也可以让"星"表示字符，A[i-1]肯定是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j]
- [0010. Regular Expression Matching](Solutions/0010.Regular-Expression-Matching.py) (!!H) <br>
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配; 情况一：B[j-1]不是"星": f[i][j] = f[i-1][j-1] if (B[j-1]="." or A[i-1]=B[j-1]); 情况二：B[j-1]是"星"：可以让"星"表示0个前面的字符，那就让A[0..i)去和B[0..j-2)匹配： f[i][j] = f[i][j-2]；也可以让"星"表示几个前面的字符，A[i-1]是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j] if (B[j-2]="." or B[j-2]=A[i-1])
- [0727. Minimum Window Subsequence](Solutions/0727.Minimum-Window-Subsequence.py) (!!H Google) <br>
solution 1: sliding window - O(MN) 这题subseq与上题substring不同，上题只需要freq都满足了就行，这题不仅如此，而且还是讲究顺序的，; solution 2: dp - dp[i][j] = the min window subsequence that ends with ith ch in t, and jth ch in s.
If t[i-1] == s[j-1]: dp[i][j] = dp[i-1][j-1] + 1; else: dp[i][j] = dp[i][j-1] + 1
- [1537. Get the Maximum Score](Solutions/1537.Get-the-Maximum-Score.py) (!!H) <br>
two pointers + dp: dp1[i] = max path sum ends with nums1[i-1]; dp2[j] = max path sum ends with nums2[j-1]  two pointers loop over nums1 and nums2 and update dp1 and dp2.
- [0072. Edit Distance/Levenshtein distance](Solutions/0072.Edit-Distance.py) (!!H) <br>
f[i][j]=A前i个字符[0..i)和B前j个字符[0..j)的最小编辑距离; f[i][j]=min{case 1. f[i-1][j]+1 (f[i-1][j]表示A[0..i-1)就可以拼成B[0..j)了，所以A[0..i)要拼成B[0..j)需要删掉A[0..i)的最后一个字母); case 2. f[i][j-1]+1 (B[0..j)需要删掉最后一个字母，即A[0..i)的后面需要增加一个字母); case 3. f[i-1][j-1]+1 (A[0..i)的后面需要replace一个字母); case 4. f[i-1][j-1] (if A[i-1]=B[j-1] 就不需要任何操作直接就是了)}
- [100320-Diff Between Two Strings](Solutions/Pramp__100320-Diff-Between-Two-Strings.py) (!!!H Google) <br>
__DP to find path__ This problem is easiest to attempt in two steps:
step 1: do a dp for 72. Edit Distance;
step 2: construct the answer using the dp list we constructed;
If source[i] == target[j] we write source[i] in the answer. If j is invalid or dp(i+1, j) <= dp(i, j+1) we write -source[i] in the answer.
Otherwise, we write +target[j].
- [1548. The Most Similar Path in a Graph](Solutions/1548.The-Most-Similar-Path-in-a-Graph.py) (!!!H Google) <br>
similar with 100320-Diff Between Two Strings - __DP to find path__
Step 1: build a DP table in order to find the minimum edit distance to targetPath; Step 2: we traverse __reversely the build DP table__ to find which path did we take 
in order to get the minimum edit distance. At last, we return res[::-1]. dp[i][u] = the min edit distance if we take i steps, with u as the last city visited; dp[i][u] = min(dp[i-1][v] for v in graph[u]) + 0 if names[u] == targetPath[i] else 1; then min(dp[m]) is our minimum edit distance overall. O(MN^2)



### [Other DP Problems](https://juejin.im/post/5d556b7ef265da03aa2568d5)
- [1105. Filling Bookcase Shelves](Solutions/1105.Filling-Bookcase-Shelves.py) (!!!M)
dp[i]: the min height to place the first i-1 books.
For dp[i+1], either place book i on a new shelve dp[i] = dp[i-1] + height[i-1],
or grab previous books together with book i and move to next level together: 
dp[i] = min(dp[j-1] + max(height[j-1] .. height[0])), where sum(width[j-1] + ... + sum(width[i]) <= shelve_width
- [0650. 2 Keys Keyboard](Solutions/0650.2-Keys-Keyboard.py) (!!M) <br>
递归调用即可，寻找第一个可以dividor that can divide n, return dividor + self.minSteps(n//dividor)
- [0651. 4 Keys Keyboard](Solutions/0651.4-Keys-Keyboard.py) (!!M) <br>
dp[j] = max number pressing j times.
dp[j] = max(dp[i] * (j-i-1)), eg: i = j - 3; dp[j] = dp[j-3]* 2, 因为把dp[j-3] ctr+V了一次; 
eg: i = j - 4, dp[j] = dp[j-4]* 3, 因为把dp[j-4] ctr+V了两次
- [0887. Super Egg Drop](Solutions/0887.Super-Egg-Drop.py) (!!H) <br>
solution 1 - O(KN^2): dp[i][j] 表示有i个鸡蛋，j层楼要测需要的最小操作数. dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]) for k in range(1, j)). solution 2 - O(KNlogN). 用binary search 找k， instead of linear search.
- [0688. Knight Probability in Chessboard](Solutions/0688.Knight-Probability-in-Chessboard.py) (!!M Google)
dp[i][j][k]表示在棋盘(i, j)位置上走完k步数还留在棋盘上的走法总和(注意是走法，不是步数). dp[i][j][k] += dp[next_i][next_j][k-1] for next_i and next_j in bound.
- [Similar with 688. Knight Probability in Chessboard](Solutions/Google_Similar-with-688.Knight-Probability-in-Chessboard.py) (!!!M Google) <br>
dp.  dp[i][j][k] = from (i, j) the number of ways you to end up at the original coordinate with k steps.
dp[i][j][k] = dp[i - 1][j][k - 1] + dp[i][j - 1][k - 1] + dp[i + 1][j][k - 1] + dp[i][j + 1][k - 1]
- [0467. Unique Substrings in Wraparound String](Solutions/0467.Unique-Substrings-in-Wraparound-String.py) (!!M)
题目可以转换为分别求出以每个字符(a-z)为结束字符的最长连续字符串就行了，
我们用一个数组记录下 以每个字符(a-z)为结束字符的最长连续字符串，最后求出数组的所有数字之和就是我们要的结果啦.
- [0837. New 21 Game](Solutions/0837.New-21-Game.py) (!!M Google) <br>
dp + sliding widown with fixed size.  The probability to get point K point is p(K) = p(K-1) / W + p(K-2) / W + p(K-3) / W + ... p(K-W) / W = (p(K-1) + p(K-2) + ... + p(K-W)) / W.  let wsum = p(K-1) + p(K-2) + ... + p(K-W), p(K) = wsum / W. dp is storing p(i) for i in [0 ... N]. We need to maintain the window by adding the new p(i), and getting rid of the old p(i-w)
- [0361. Bomb Enemy](Solutions/0361.Bomb-Enemy.py) (M)
brutal force: 上下左右四个方向去找能炸死多少人即可。 DP解法: 把(i, j)位置能炸死多少敌人提前计算好放入二维数组中， up[i][j]=在(i,j)位置能向上炸的敌人数目
- [0913. Cat and Mouse](Solutions/0913.Cat-and-Mouse.py) (H) <br>
dp + bfs

----------1335. Minimum Difficulty of a Job Schedule--------




# [Binary Search](/Binary-Search.py)
- [0704. Binary Search](Solutions/0704.Binary-Search.py) (!!E) <br>
九章模板: 1. while start + 1 < end; 2. mid = start + (end - start) // 2; 3. 循环内只写两个分支； 4. 往左逼find the first X; 5. 往右逼find the last X
- [0702. Search in a Sorted Array of Unknown Size](Solutions/0702.Search-in-a-Sorted-Array-of-Unknown-Size.py) (M) <br>
Find end point using "double method", same as dynamic array
- [0367. Valid Perfect Square](Solutions/0367.Valid-Perfect-Square.py) (E) <br>
same as sqrt(x)
- [0050. Pow(x, n)](Solutions/0050.Pow(x,n).py) (M) <br>
recursion solution: half = self.myPow(x, n//2); if n%2 == 0: res = half * half; else: res = half * half * x
- [0029. Divide Two Integers](Solutions/0029.Divide-Two-Integers.py) (M) <br>
eg: 10//3, 每次都右移几次3 << k, 相当于3x2x2x2...,直到3x2x2x2...>10, 然后取余数继续这个算法是O(logN)
- [0034. Find First and Last Position of Element in Sorted Array](Solutions/0034.Find-First-and-Last-Position-of-Element-in-Sorted-Array.py) (!!M) <br>
用两次二分分别找first pos of target and last pos of target. 想找first position of target，要保证两点：1. while循环里的判断要往左逼，也就是if nums[mid] **>=** target: end = mid； 2. 就把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉，因为start肯定是小于end的。<br>
Follow up: In a sorted array [1,3,4.......], search the elements that are in a certain range eg:[10, 100]. solution: 用两次二分分别找first position of 10 and last position of 100.  Then the elements between the two positions should be in range [10, 100].
- [1287. Element Appearing More Than 25% In Sorted Array](Solutions/1287.Element-Appearing-More-Than-25%-In-Sorted-Array.py) (!!E) <br>
想想如果我们需要求sorted arr 里 more than n//2 times的num, 只需要直接return arr[n//2]就可以了
同理我们可以求more than 25%的num.
step 1: 找出 n//4, 2n//4, 3n//4 位置处的num, 因为答案只可能存在于这三个位置上
step 2: 对这三个num分别做binary search求出first_pos and last_pos, 如果last_pos - first_pos >= n//4 就找到了
- [0035. Search Insert Position](Solutions/0035.Search-Insert-Position.py) (E) <br>
This is to implement bisect.bisect_left(nums, target), which returns the position of inserting target in order to keep nums sorted
- [0278. First Bad Version](Solutions/0278.First-Bad-Version.py) (E)
- [0153. Find Minimum in Rotated Sorted Array](Solutions/0153.Find-Minimum-in-Rotated-Sorted-Array.py) (!!M) <br>
解法一：nums[mid]可以与nums[0]比较；解法二：也可以与nums[-1]比较；解法三：也可以与nums[end]比较
- [0154. Find Minimum in Rotated Sorted Array II](Solutions/0154.Find-Minimum-in-Rotated-Sorted-Array-II.py) (!!H) <br>
与153类似，只是array里可能有duplicates，采用153的解法三，唯一不同的是：nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半，因为eg: nums=[2,2,2,2,2,1,2,2,2,2,2,2........], 由于不知道mid是1前面的2还是1后面的2，所以无法确定是drop前面还是drop后面，只能保险地把end往前挪一位，所以154这题in extreme case, 时间复杂度是O(N). 这题用nums[end]与nums[mid]比较能work的原因是end永远不可能出现在最小值的左边。
- [0039. Recover Rotated Sorted Array](Solutions/0039.Recover-Rotated-Sorted-Array.py) (M LintCode) <br>
154 相同方法binary search找到minPos, __注意如果有重复的元素就要跟nums[end]比较__, 然后三步反转法recover
- [0033. Search in Rotated Sorted Array](Solutions/0033.Search-in-Rotated-Sorted-Array.py) (M) 
画个图分几个区间讨论就可以了, 分target在左边区间和target在右边区间讨论
- [0081. Search in Rotated Sorted Array II](Solutions/0081.Search-in-Rotated-Sorted-Array-II.py) (M) 
If nums[0] = nums[-1], the binary search would be very complicated, so we pre-process the nums by remving the nums[-1] if it equals nums[0]. Then we can do LC 33 (分target在左边区间和target在右边区间) + LC 154 (nums[mid] == nums[end]: end -= 1, 注意不能drop掉一半)
- [0852. Peak Index in a Mountain Array](Solutions/0852.Peak-Index-in-a-Mountain-Array.py) (E) <br>
OOOXXX问题，找到第一个出现的X，X是the first position of 递减的序列 arr[mid] 与 arr[mid+1] 比较
- [1095. Find in Mountain Array](Solutions/1095.Find-in-Mountain-Array.py) (H) <br>
step 1: Binary find peak in the mountain - 852. Peak Index in a Mountain Array.
step 2: Binary find the target in strict increasing/left part.
step 3: Binary find the target in strict decreasing/right part.
- [0162. Find Peak Element](Solutions/0162.Find-Peak-Element.py) (M) <br>
OOXX问题，找到第一个出现的X，X是the first position of 递减的序列, mid 要与 mid-1 比较 也要与 mid+1 比较. 分四种情况：上升区间，下降区间，谷底，山顶
- [0390. Find Peak Element II](Solutions/0390.Find-Peak-Element-II.py) (!!H Lintocde) <br>
先二分找到中间某一行的最大值位置(i, j)，然后这个最大值的地方向上(i-1, j)和向下(i-1, j)分别比一下，如果(i, j)最大，那恭喜找到了peak, 如果向上更大，那就往上爬到(i-1,j), 此时i行及其以下的行都可以丢掉了，然后在j那一列查找最大值的位置(ii, j), 这时候在(ii, j)这个位置向左(ii, j-1)向右(ii, j+1)分别比一下，如果发现(ii, j)最大，那么恭喜找到peak了，如果发现(ii, j-1)更大，那就继续往(ii, j-1)爬一步，可以直接丢掉j-1列及其右边的部分了。这样的时间复杂度是T(N)=O(N 在第i行查找最大值)+T(N/2), using Master's theorem, then time complexity is O(N).
- [0436. Find Right Interval](Solutions/0436.Find-Right-Interval.py) (M) <br>
step 1: include the idx information into the interval;
step 2: then sort the intervals based on start time;
step 3: scan the interval and update res, by using binary search.
- [0981. Time Based Key-Value Store](Solutions/0981.Time-Based-Key-Value-Store.py) (M) <br>
- [0074. Search a 2D Matrix](Solutions/0074.Search-a-2D-Matrix.py) (M) <br>
Think it as a long 1D array with MxN element, then we can use binary search; row = mid // n, col = mid % n; O(log(MN))
- [0240. Search a 2D Matrix II](Solutions/0240.Search-a-2D-Matrix-II.py) (M) <br>
__从左下角出发往右上角搜索__, each comparism rule out a row (i-1=1) or rule out a col (j+=1). O(M+N).
Comparing with 74, we can see that in 74, the 2D matrix is strongly sorted, so the time is logM + logN <br>
in 240, the 2D matrix is less strongly sorted, so the time is M + N <br>
If the 2D matrix is not sorted at all, then the time is MN.
- [0668. Kth Smallest Number in Multiplication Table](Solutions/0668.Kth-Smallest-Number-in-Multiplication-Table.py) (!!H Google) <br>
helper函数定义为是否有k个数大于mid, helper函数利用sorted matrix的特性，可以达到O(m+n).
so overall O((m+n)log(mn))
- [1060. Missing Element in Sorted Array](Solutions/1060.Missing-Element-in-Sorted-Array.py) (!!!M Google) <br>
定义一个function missing(idx) to find the number of number missing before idx. so that we can compare missing(mid) with k. Google真的把binary search 玩出花了！
- [1428. Leftmost Column with at Least a One](Solutions/1428.Leftmost-Column-with-at-Least-a-One.py) (M) <br>
binary search on each row - O(mlogn)
- [0302. Smallest Rectangle Enclosing Black Pixels](Solutions/0302.Smallest-Rectangle-Enclosing-Black-Pixels.py) (!!H) <br>
solution 1: simple dfs visit every balck pixel, and update the max_i, max_j, min_i, min_j during dfs. - O(mn). solution 2: 我们需要知道Black出现的最大的i和最小的i, 所以我们可以求出每一行的第一个Black和最后一个Black的idx, 就是我们想求的最大的i和最小的i了，转换成了OOXX问题了. 这题可以用binary search的原因是有且只有一个Black的岛屿，所以每一行都是一个先上后下的mountain array. - O(mlogn+nlogm). 我们在某一行扫binary search的时候范围是start, end = 0, self.min_j 



### [二分答案](/Binary-Search.py)
##### 1. minimum of maximum / maximum of minimum 的问题; 2. minimum/maximum to satisfy some condition 的问题
- [0643. Maximum Average Subarray I](Solutions/0643.Maximum-Average-Subarray-I.py) (E) <br>
- [0644. Maximum Average Subarray II](Solutions/0644.Maximum-Average-Subarray-II.py) (!!H Google) <br>
binary search + prefix sum + best_time_to_buy_and_sell_stock (two pointers). 二分答案：初始化 left 为原数组的最小值，right 为原数组的最大值 - O(Nlog(max-min)). helper function比较难需要构造prefix_sum, 然后check if there is in a sum with at least K length that is larger than mid, which we can do in linear time by keeping a min_sum and use it for compare, similar with 121. Best Time to Buy and Sell Stock
- [0719. Find K-th Smallest Pair Distance](Solutions/0719.Find-K-th-Smallest-Pair-Distance.py) (!!H Google) <br>
binary search + sliding window 二分答案：sort the list, then it becomes [1,1,3,4,8,8,9]. let helper function return if there is more than k distance smaller than mid.
we use two pointers to go through the list to check if there is more than k distance smaller than mid. The algorithm of helper function is sliding window so it's only O(N)
- [1283. Find the Smallest Divisor Given a Threshold](Solutions/1283.Find-the-Smallest-Divisor-Given-a-Threshold.py) (M) <br>
minimum/maximum to satisfy some condition 的问题: helper function returns whether we can have sum(num//mid) <= threshold? start = 1, end = max(nums) + 1
- [0875. Koko Eating Bananas](Solutions/0875.Koko-Eating-Bananas.py) (M) <br>
minimum/maximum to satisfy some condition 的问题: If Koko can finish eating all the bananas (within H hours) with an eating speed of K, she can finish with a larger speed too. So it is a OOOXXX problem trying to find the first X. end is set to be max(piles). Every time find if it posible to eat all the bananas with speed mid. if yes, then drop the right part, if no, then drop the left.
- [0183. Wood Cut](Solutions/0183.Wood-Cut.py) (H Lintcode) <br>
minimum/maximum to satisfy some condition 的问题: If we can cut into pieces with lens, then we can also cut into prices with len - 1, So this is a OOOXXX problem, to find the last O.
- [0437. Copy Books](Solutions/0437.Copy-Books.py) (!!M Lintcode) <br>
minimum/maximum to satisfy some condition 的问题: OOOXXX problem, to find the first O. 二分法不难想，难想的是比较mid时的那个helper function, helper function return if k people can finish all the pages in the midTime.  Algorithm: greedy. 只有上一个人无法在mid时间内完成的情况下，我们才加一个人进来 
- [1011. Capacity To Ship Packages Within D Days](Solutions/1011.Capacity-To-Ship-Packages-Within-D-Days.py) (M) <br>
minimum/maximum to satisfy some condition 的问题: similar with copy books
- [1482. Minimum Number of Days to Make m Bouquets](Solutions/1482.Minimum-Number-of-Days-to-Make-m-Bouquets.py) (M) <br>
minimum/maximum to satisfy some condition 的问题: helper function returns can we have at least m bouquets after mid days?
- [1552. Magnetic Force Between Two Balls](Solutions/1552.Magnetic-Force-Between-Two-Balls.py) (!!M) <br>
minimum of maximum / maximum of minimum 的问题: the thinking process of helper function is the most difficult part.
- [0410. Split Array Largest Sum](Solutions/0410.Split-Array-Largest-Sum.py) (!!H) <br>
minimum of maximum / maximum of minimum 的问题: 把array分成K份，求min of max subarray sum. If we can divide nums so that the minimum subarray sum is mid, we can also divide nums so that the minimum subarray sum is larger than mid. So this is a OOXX problem.  The difficult part is to check if mid is valid.
We use greedy algorithm to do that, which is very similar with copy books.
- [1231. Divide Chocolate](Solutions/1231.Divide-Chocolate.py) (!!!H Google) <br>
minimum of maximum / maximum of minimum 的问题: 与上一题类似，把array分成K份，求max of min subarray sum. Divide the nums into K+1 subarrays, and make sure each subarray has a sum at least S. Find the max S. so it's a OOXXX problem finding the last O.
- [0774. Minimize Max Distance to Gas Station](Solutions/0774.Minimize-Max-Distance-to-Gas-Station.py) (!!H Google) <br>
minimum of maximum / maximum of minimum 的问题: If we can do it at D, then we can do it at larger than D. This is a OOXX problem to find the minimum D.
The difficult part is to find if is_valid to place K stations so that every adjacent station has distance smaller than D - using greedy. 注意这一题的start, end都是小数
- [0792. Number of Matching Subsequences](Solutions/0792.Number-of-Matching-Subsequences.py) (!!M Google) <br>
solution 1: compare each word with source string using two pointers. O(nmk), where n = len(s), m = len(words) and k = average lens of word in words. solution 2: use binary search in s, similar with 1055.  O(mklogn)
- [0524. Longest Word in Dictionary through Deleting](Solutions/0524.Longest-Word-in-Dictionary-through-Deleting.py) (!!M) <br>
sort the words by lens, and check the word one by one to see if there is a match. How to check if word matches s? use two pointers to traverse word and s, compare as they go.
solution 2: binary search on s. same as 792. Number of Matching Subsequences.
- [0392. Is Subsequence](Solutions/0392.Is-Subsequence.py) (!!E Google) <br>
solution 1: two pointers. solution 2: binary search.
- [1055. Shortest Way to Form String](Solutions/1055.Shortest-Way-to-Form-String.py) (!!M Google) <br>
solution 1: greedy + two pointers - O(st). solution 2: greedy + binary seach - O(tlog(s))
- [0941. Valid Mountain Array](Solutions/0941.Valid-Mountain-Array.py) (E Google) <br>
Binary search. 题目要求只要有arr[i]==arr[i-1]的情况就return False, 所以不能用binary search的
- [0911. Online Election](Solutions/0911.Online-Election.py) (!!M Google) <br>
Precomputed Answer + Binary Search.
Constructor: O(N). each query: O(logN). 我们将每一个时刻的winner放到self.res中，这种提前计算好的思想非常重要！






# [Sort](/Sort.py)
- [0912. Sort an Array](Solutions/0912.Sort-an-Array.py) (!!M Youtubed) <br>
quick sort: 先整体有序，再局部有序，需要helper function, helper function无返回值 - modify nums in place，先整体有序：选一个pivot，把arr按pivot的值分为左右两边；后局部有序：递归
merge sort: 用mid分成左右两部分，leftArr和righArr分别记录局部的有序数组，然后merge到arr数组，不需要helper function
- [0179. Largest Number](Solutions/0179.Largest-Number.py) (M) <br>
quick sort, self-define comparing two strings by: if s1 + s2 <= s2 + s1: return True else False
- [0969. Pancake Sorting](Solutions/0969.Pancake-Sorting.py) (M Pramp) <br>
for i in range(lens-1, -1, -1 ): Find maxIndex -> flip max to top -> flip max to bottom of the whole arr -> repeat
- [0280. Wiggle Sort](Solutions/0280.Wiggle-Sort.py) (M) <br>
O(N): 从左到右扫一遍，不满足条件的交换就好了。定义一个变量prevShouldLessThanCurr, in the for loop, prevShouldLessThanCurr = not prevShouldLessThanCurr every step, and based on prevShouldLessThanCurr is true or not, we swap nums[i-1] with nums[i] or not.
- [0324. Wiggle Sort II](Solutions/0324.Wiggle-Sort-II.py) (M) <br>
这题比Wiggle Sort I难在相邻的数不能相等，所以相邻交换法行不通，
我们可以sort the nums, then 把有序数组从中间分成两部分，然后从前半段的末尾取一个，在从后半的末尾取一个，这样保证了第一个数小于第二个数，然后从前半段取倒数第二个，从后半段取倒数第二个，这保证了第二个数大于第三个数，且第三个数小于第四个数，以此类推。O(nlogn), O(n)
- [Sort a nearly sorted (or K sorted) array](Solutions/Geeks__Sort-a-nearly-sorted-or-K-sorted-array.py) (Geeks) <br>
题目要求sort一个长程无序短(k)程有序的数组，solution: 用一个大小为k的heapq存储k个元素，然后i从k开始遍历nums, 遍历的过程中每次都更新nums的最左边: nums[target_idx] = heappop(hq)，同时更新hq: heappush(hq, nums[i]), 这么做成立的原因是i是从k开始遍历的，所以nums[i]一定是大于nums[0]的，而nums[0]>=heappop(hq), 所以nums[i]及其后面的数一定是大于heappop(hq)的，所以可以放心地把heappop(hq)放到target_idx的位置。时间复杂度是O(nlogk). 当k=1: O(0), 当k=n: O(nlogn), 当k=n时就degrade成了heap sort了

### [Quick sort - Partition and quick select](/Sort.py) 
- [0031. Partition Array](Solutions/0031.Partition-Array.py) (!!Lintcode) 
用quick select的模板，partition这个函数的作用是O(N)找到某个数k在一个无序数组中所在的位置，并按照这个数k将该数组分为左右两部分。
- [0905. Sort Array By Parity](Solutions/0905.Sort-Array-By-Parity.py) (E) <br>
solution 1: 同向双指针； solution 2: 反向双指针 - partition 好像两种方法都不能maintain the original order of numbers. 貌似同向双指针可以maintain the original order of numbers.
- [0144. Interleaving Positive and Negative Numbers](Solutions/0144.Interleaving-Positive-and-Negative-Numbers.py) (Lintcode) <br>
STEP 1: 反向双指针（或同向双指针）对[-1,-2,4,,5,-3,6]进行partition，负数在左边，正数在右边[-1, -2, -3, 4, 5, 6]; STEP 2: 再正负正负安插
- [0075. Sort Colors](Solutions/0075.Sort-Colors.py) (!!M) <br>
solution 1: 同向双指针: step 1: move all 0s to the left; step 2: move all 1s to the left of the rest of the arr; 优点：very easy to implement, don't need to memorize anything.
Solution 2: 经典的荷兰三色旗问题采用 Dijkstra's 3-way partitioning: while i <= gt: <br>
a[i] < pivot: exchange a[i] and a[lt] and i++, lt++; <br>
a[i] > pivot: exchange a[i] and a[gt] and gt--; <br>
a[i] = pivot: i++; <br>
QuickSort with 3-way partitioning is very fast because it is entropy optimal
- [0399. Nuts & Bolts Problem](Solutions/0399.Nuts&Bolts-Problem.py) (!!M Lintcode) <br>
核心在于：首先使用 nuts 中的某一个元素作为基准对 bolts 进行 partition 操作，随后将 bolts 中得到的基准元素作为基准对 nuts 进行 partition 操作
- [0215. Kth Largest Element in an Array](Solutions/0215.Kth-Largest-Element-in-an-Array.py) (!!!M Youtubed)  <br>
solution 1: quick select O(N) in average!!!!; solution 2: heap O(NlogK): heapq.heappush(numsHeap, num); heapq.heappop(numsHeap)
<br> 一个follow up: find the median in a un-sorted array.  solution: this is to find the Kth largest in an array, where K=len(arr)//2
- [0692. Top K Frequent Words](Solutions/0692.Top-K-Frequent-Words.py) (!!M) <br>
heapq solution: O(N + klogN); quick select solution: O(N + klogk)
- [0453. Minimum Moves to Equal Array Elements](Solutions/0453.Minimum-Moves-to-Equal-Array-Elements.py) (!!M)  <br>
给 n-1 个数字加1，效果等同于给那个未被选中的数字减1，
比如数组 [1，2，3]，给除去最大值的其他数字加1，变为 [2，3，3]，等价于最大的数减一变为 [1，2，2]，
那么问题也可能转化为，将所有数字都减小到最小值
- [0462. Minimum Moves to Equal Array Elements II](Solutions/0462.Minimum-Moves-to-Equal-Array-Elements-II.py) (!!M)  <br>
solution 1: find median by sorting; solution 2: find meddian by quick select(kth largest element) - O(N)
- [0296. Best Meeting Point](Solutions/0296.Best-Meeting-Point.py) (!!H)  <br>
It all about finding median, very similar with 462. Minimum Moves to Equal Array Elements II. step 1: find row_median; step 2: find col_median; step 3: the min total distance is sum of every house to (row_median, col_median). 注意千万不要错误的去求mean: Median minimizes the absolute distance of points. Mean minimizes the squared distance from points.


### [Merge sort](/Sort.py) 
- [0775. Global and Local Inversions](Solutions/0775.Global-and-Local-Inversions.py) (!!M) <br>
solution 1: If the number of global inversions is equal to the number of local inversions,  it means that all global inversions in permutations are local inversions. It also means that we can not find A[i] > A[j] with j > i + 1, cuz that will be globa not local. In other words, max(A[i]) < A[i+2].
Solution 2: mergesort: 这题其实是coursera Algorithms Sorting chapter的一个习题: counting inversions. When we're doing mergesort, original index of elements in left part (smaller side), i, must less than those in right part, j. So in the merging part of merge_sort, we can update cnt if left_arr[i] > right_arr[j]. Everthing is exactly the same as merge sort, except that before merge/conquer, we update cnt first.
- [0493. Reverse Pairs](Solutions/0493.Reverse-Pairs.py) (!!H) <br>
solution 2: merge sort. 其实merge sort才是这道题的正解！Count "important reverse pairs" while doing mergesort: When we're doing mergesort, original index of elements in left part (smaller side), i, must less than those in right part, j. So in addition to the while loop for do merge/conquer, we use an additonal while loop to compare nums[i] and 2* nums[j] to update cnt. - O(nlogn).
solution 1: segment tree. similar with 315. count of smaller number after itself. We sweep from left to right, and query range [2* num+1, max_num]. 与count number after itself相比，就只有一行代码不同. 
- [0315. Count of Smaller Numbers After Self](Solutions/0315.Count-of-Smaller-Numbers-After-Self.py) (!!H Google) <br>
Segment Tree solution: O(NlogN) time and O(N) space. 从右往左遍历add num into the tree one by one， at the same time update the cnt of smaller number after self. Follow up: how to solve Spare Segment Tree problem? - Merge sort. 正解是solution 2: merge sort O(nlogn)



### [Bucket Sort - use freq/dist/num as idx](/Sort.py) 
- [0451. Sort Characters By Frequency](Solutions/0451.Sort-Characters-By-Frequency.py) (!!M) <br>
solution 1: use hash map, and then convert to list, then sort, then conver to string - O(nlogn). solution 2: bucket sort: putting our chars in buckets/indexes based on their frequency - O(N).
- [0347. Top K Frequent Elements](Solutions/0347.Top-K-Frequent-Elements.py) (!!M) <br>
需要一个freqDict来记录每个数出现的freq， heapq, heapq中放入的是(freq, key)对; 按照freq来做heapq，这样就保证了可以筛选出most freqent k item; solution 2: quick select should implement; solution 3: bucket sort O(N) faster then solution 2, cuz solution 2 is O(N^2) in worst case. use the freq as index for the bucket.
- [Pramp__1218__Word-Count-Engine](Solutions/Pramp__1218__Word-Count-Engine.py) (!!M) <br>
use freq as idx to do bucket sort. 既然没做出来，真是耻辱呀！
- [0217. Contains Duplicate](Solutions/0217.Contains-Duplicate.py) (E) <br>
hash set to store the seen number, if seen again, return True. Warm up for 219
- [0219. Contains Duplicate II](Solutions/0219.Contains-Duplicate-II.py) (E) <br>
solution 1: dictionary to store the (num, pos) pairs. O(N), O(M), where N is the number of num in nums, M is the number of distinct num in nums; solution 2: sliding window: use a numSet to fix the sliding window to be k.  O(N), O(k), where k is the size of the window. Warm up for 220
- [0220. Contains Duplicate III](Solutions/0220.Contains-Duplicate-III.py) (!!!M) <br>
Solution 1: brutal force O(n^2); solution 2: Balanced BST O(nlogk); solution 3: bucket method: O(n). bucket sort利用的是分块的思想
The main idea is splitting elements in nums into different buckets in terms of the value of t (for each element, divide by (t+1) for integer division). 保持bucket的大小为t这样只要有两个数被分配到了同一个bucket, 那么就可以return True了
If the result is True, which means one of the following 3 cases hold: 1. Two elements in the same bucket; 2. One in the previous bucket; 3. One in the next bucket. If the case 2 or 3 holds, you need to check if their difference <= t.
- [1057.Campus-Bikes.py](Solutions/1057.Campus-Bikes.py) (!!!M) <br>
brutal force solution O(MNlog(MN)): find the distance of all combinations, and sort them.
. bucket sort solution O(MN): find the distance of all combinations, and put them into bucket based on their distance. 
In this way, the distances are represented by idx, which were sort by nature.
- [0275. H-Index II](Solutions/0275.H-Index-II.py) (!!M) <br>
The list is sorted, 疯狂暗示二分呀有木有！
find the first idx where citations[idx] >= N - idx, OOOXXX problem - O(logN)
- [0274. H-Index](Solutions/0274.H-Index.py) (!!M) <br>
Now the list is not sorted, what do we do? We can sort it and then do exactly the same as 275.  However, that takes nlogn. bucket sort: - O(N) garanteed.
step 1: 把citation num被引次数放入bucket中作为idx, 而idx上对应的值是cnt of how many papers were cited this much time.
step 2: bucket size 是 len(citations);
step 3: O(N) 遍历把相应的(被引次数, how many paper被引了那么多次) pair 放到相应的(idx, val)上, 这样一来high idx上就天然放着high 被引次数了, 就不需要sort了
- [0164. Maximum Gap](Solutions/0164.Maximum-Gap.py) (!!H) <br>
遇到这类问题肯定先想到的是要给数组排序，但是题目要求是要线性的时间和空间，那么只能用桶排序Bucket Sort 。
If we set the bucket size clever(relatively small), 
we can ensure that the max gap cannot be in same bucket.
Largest gap can not be smaller than (max-min)/lens + 1, so if we make the buckets smaller than this number, 
any gaps within the same bucket is not the amount we are looking for, 
so we are safe to look only for the inter-bucket gaps.
- [0791. Custom Sort String](Solutions/0791.Custom-Sort-String.py) (!!M Google) <br>
Bucket sort. use a bucket with bucket size n+1, store all the ch in t that also appear in s to the corresponding bucket_id, and those didn't appear in s to the last bucket_id.
O(M+N)


### [Cyclic Sort/把数当坐标用](/)
- [0448. Find All Numbers Disappeared in an Array](Solutions/0448.Find-All-Numbers-Disappeared-in-an-Array.py) (E) <br>
难就难在题目要求O(1) space. 做法是把数组里的数当坐标用，We use the sign of the index as the indicator. If one number never occur, 
we know the number corresponding to the idx will never be negative. eg: [4,3,1,3] -- > [-4,3,-1,-3], 2 is missing, so num[2-1] will never be changed to be negative. 1st pass: change numbers to be negative [4,3,1,3] --> [-4,3,-1,-3].  2nd pass: find those numbers that has not been changed negative, there is not num corrsponding to their idx.
- [0442. Find All Duplicates in an Array](Solutions/0442.Find-All-Duplicates-in-an-Array.py) (!!!M) <br>
难就难在题目要求O(1) space. 做法是把数组里的数当坐标用，We use the sign of the index as the indicator. If one number occurs twice, 
we know the second time occurance becasue we flip the sign each time.
- [0268. Missing Number](Solutions/0268.Missing-Number.py) (!!M) <br>
solution 1: 448类似的做法，我们通过nums[i] += 1来change all 0s to be positive number.  solution 2: bit manipulation 所有的idx and num都异或起来. solution 3: 题目确定只有一个missing number. add every num together and compare with n(n+1)/2. O(1).  Follow up: what is there are 2 missing numbers?  How can we solve within O(1). we can calculate the sum of the 2 missing numbers using solutino 3, and also prodct of the 2 missing number, then 用求根公式求出来就可以了
- [Pramp. Getting a Different Number](Solutions/Pramp.Getting-a-Different-Number.py) (failed) <br>
Use a list to record the appearance of idx.
- [0041. First Missing Positive](Solutions/0041.First-Missing-Positive.py) (!!H) <br>
1st pass: change all negtive numbers to be 1, so that there will be no negtive numbers;  2nd pass: change the positive numbers into negative; 3rd pass: find the first positive number, and the corresponding idx is missing
- [0287. Find the Duplicate Number](Solutions/0287.Find-the-Duplicate-Number.py) (!!M) <br>
142. linked list找环的题目，把这个数组的每一个数num看成这样一个linked list node: num的下标代表.val, num的值代表.next指向下一个node。那么如果存在重复的num，那就表示有两个不同node都指向了同一个公共，也就是成环的地点。这么想这个题目就和142一样了，具体实现过程中对p取一个nums[p]，就相当于取一个p.next



### [Sorted Array](/Sort.py) 
- [1051. Height Checker](Solutions/1051.Height-Checker.py) (E) <br>
just check 谁不在他该有的位置
- [0561. Array Partition I](Solutions/0561.Array-Partition-I.py) (E) <br>
sort the arr first, then the maximum sum of pairs is the sum of every other num
- [0004. Median of Two Sorted Arrays](Solutions/0004.Median-of-Two-Sorted-Arrays.py) (!!H) <br>
midIdx1, midIdx2 = len(nums1)//2, len(nums2)//2; midVal1, midVal2 = nums1[midIdx1], nums2[midIdx2]; when k is relatively large, then we can safely drop the first half that are surely smaller than the kth, the question is where is the first half that are surely smaller than the kth? by comparing midVal1 and midVal2, we can find it out, if midVal1 < midVal2, then all the vals in nums1[:midIdx1] are less than midVal2, also all of those vals are less than kth, we can safely drop all those vals



# [Greedy](/) <br>
这个视频讲贪心不错：https://www.bilibili.com/video/BV1hJ411v7w4
- [0455. Assign Cookies](Solutions/0455.Assign-Cookies.py) (!!E) <br>
greedily 尽量用最少的糖果去优先满足孩子孩子，所以需要先排序
- [0870. Advantage Shuffle](Solutions/0870.Advantage-Shuffle.py) (M) <br>
田忌赛马核心algorithm: 每次都给最大的b做匹配，如果最大的a可以匹配上最大的b，那就把最大的a分配给最大的b；如果不能匹配上，那就把最小的a分配给最大的b. 需要sort A and B.
- [0055. Jump Game](Solutions/0055.Jump-Game.py) (!!M) <br>
solution 1: dp - TLE. solution 2: greedy - O(N)
- [0045. Jump Game II](Solutions/0045.Jump-Game-II.py) (!!H) <br>
Greedy算法：第一步可以跳到比如位置10，也就是说0-10我们都可以一步跳到，那我们就在0-10这些位置中，选一个位置i跳第二步，看看第二步能跳到最远的地方是哪里，比如是最远的是从位置6跳到位置28，那么就说明两步可以跳到位置28，也就是说11-28我们可以通过两步跳到，那我们就继续在11-28这些位置中，选一个位置i跳第三步.........这个greedy的思想非常重要，要熟记！！ 
- [1024. Video Stitching](Solutions/1024.Video-Stitching.py) (!!M) <br>
每次都选结束时间最大的，比如选了[0, 4], 那就选开始时间在[0, 4]的Interval中选结束时间最大的, 比如选到了[2, 9],
接着就在开始时间为[4, 9]的interval中选结束时间最大的，比如[7, 15]....这样依次下去。。。
直到找到一个结束时间大于T的- 需要提前sort - O(nlogn).  solution 2: jump game - 无需sort - O(N).
先建立一个reacable list. reachable[idx]=start from idx, where can we reach.  然后就是jump game II了，求最少几步从0跳到T.
Jump Game II greedy的思想非常重要。
- [1326. Minimum Number of Taps to Open to Water a Garden](Solutions/1326.Minimum-Number-of-Taps-to-Open-to-Water-a-Garden.py) (!!H Twitter) <br>
We build a list reachable to store the max range it can be watered from each index. reachable[idx] = start from idx, where we can reach
Then it becomes Jump Game II, where we want to find the minimum steps to jump from 0 to n.
每跳一步就相当于开一个水龙头. 所以我们可以看到45. Jump Game II, 1024. Video Stitching和这题其实是一个题。
- [0763. Partition Labels](Solutions/0763.Partition-Labels.py) (!!M) <br>
step 1: use a hashmap to store the last time a ch appears. mapping[ch] = the last idx the ch appears; step 2: construct has_to_reach[idx] = starting from idx, where we have to reach. step 3: jump game II
- [0769. Max Chunks To Make Sorted](Solutions/0769.Max-Chunks-To-Make-Sorted.py) (!!M) <br>
similar with 45. Jump Game, define a curr_must_reach and next_must_reach. if next_must_reach == curr_must_reach, we can cut it.
- [0768. Max Chunks To Make Sorted II](Solutions/0768.Max-Chunks-To-Make-Sorted-II.py) (!!H) <br>
pre-calculation. left_max arr and right_min arr.
- [1306. Jump Game III](Solutions/1306.Jump-Game-III.py) (M) <br>
simple dfs/bfs, if can find arr[idx]==0, then return True.
- [0134. Gas Station](Solutions/0134.Gas-Station.py) (!!M) <br>
Every time a fail happens, we start reset the gas_left to 0, and reset the possible_station. 
The problem has an assumption: if sum of gas is more than sum of cost, then there must be a solution. 
And the question guaranteed that the solution is unique(The first one I found is the right one).
- [0135. Candy](Solutions/0135.Candy.py) (!!H) <br>
先给每个孩子分配一个糖果，然后做两次扫描，从左往右扫，遇到上升的child就把他的cnady+1; 接着从右往左扫，遇到上升的child就把他的cnady+1.
- [0406. Queue Reconstruction by Height](Solutions/0406.Queue-Reconstruction-by-Height.py) (!!M) <br>
Greedy: Since short people will not disturb/affect the relative order of taller people so we can start from tallest guy(s). Then for each person [i,j], we insert it into res based on j.
- [1029. Two City Scheduling](Solutions/1029.Two-City-Scheduling.py) (!!E) <br>
像这种interval的题一般都需要先排个序，排序标准很重要，排序标准：去city A比去city B多用多少钱，这样一来去排在前面的就是去city A能省下最多钱的人，让前N个人都去A就能省下最多的钱
- [0991. Broken Calculator](Solutions/0991.Broken-Calculator.py) (!!M) <br>
solution 1: bfs - O(2^(X-Y)) TLE. solution 2: greedy. 先将y除下来，除到y < x之后再减，除的过程中遇到y为奇数就加一
- [0397. Integer Replacement](Solutions/0397.Integer-Replacement.py) (!!M) <br>
similar with 991. Broken Calculator (bfs). backtrack with memo - O(n)
- [1553. Minimum Number of Days to Eat N Oranges](Solutions/1553.Minimum-Number-of-Days-to-Eat-N-Oranges.py) (!!H) <br>
solution 1: bfs - O(N), solution 2: backtrack with memo
- [1658. Minimum Operations to Reduce X to Zero](Solutions/1658.Minimum-Operations-to-Reduce-X-to-Zero.py) (!!M) <br>
这题是从两端找 the fewest number added to x. 
换个角度就是找 the longest subarry that sum up to sum(nums) - x.
由于nums are all positive, sliding window即可 - O(N)
- [1007. Minimum Domino Rotations For Equal Row](Solutions/1007.Minimum-Domino-Rotations-For-Equal-Row.py) (!!M) <br>
Try all possibilities from 1 to 6. If we can make number i in a whole row, it should satisfy that countA[i] + countB[i] - same[i] = n
- [0659. Split Array into Consecutive Subsequences](Solutions/0659.Split-Array-into-Consecutive-Subsequences.py) (!!!M Google) <br>
这道题我们遍历nums的时候只要当前的num被前面的顺子需要，就把num连上去，顺子连得越长越好，这就是greedy所在，使用两个 HashMap，第一个 HashMap 用来建立某个数字和其出现次数之间的映射 freq，
第二个用来建立某个数字被前面顺子所需要的次数之间的映射 need。
- [1296. Divide Array in Sets of K Consecutive Numbers](Solutions/1296.Divide-Array-in-Sets-of-K-Consecutive-Numbers.py) (!!!M Google) <br>
用以一个hashmap记录frequency. 由于必须固定长度为k, 所以我们每次都去连k个就可以了
- [0846. Hand of Straights](Solutions/0846.Hand-of-Straights.py) (!!!M Google) <br>
same as 1296. 用以一个hashmap记录frequency. 由于必须固定长度为W, 所以我们每次都去连W个就可以了
- [0670. Maximum Swap](Solutions/0670.Maximum-Swap.py) (!!M) <br>
solution 1: sort and compare - O(nlogn); solution 2: one pass from backward, 如果碰到一个小的，应该与后面已经遍历过的max_idx交换 - O(N)
- [1383. Maximum Performance of a Team](Solutions/1383.Maximum-Performance-of-a-Team.py) (!!!H) <br>
将workers按照efficiency降序排序，这样我们只需要从第k个worker开始，
取他的efficiency去乘以(他之前所有workers选k个能组成的最大的speed)，
这个因为他的efficiency一定是这k个worker里面最小的。
可以保持一个k size的heap来存(他之前所有workers), 如果size>k就把min_speed的worker踢出去
- [0857. Minimum Cost to Hire K Workers](Solutions/0857.Minimum-Cost-to-Hire-K-Workers.py) (!!!H Google) <br>
generally, a team cost is ∑wi = w/q * ∑qi where w/q is the maximum wage/quality ratio in that team. 我们发现与1383. Maximum Performance of a Team是类似的。
- [1642. Furthest Building You Can Reach](Solutions/1642.Furthest-Building-You-Can-Reach.py) (H) <br>
solution 1: backtrack; solution 2: memorization; solution 3: greedy heapq - O(nlog(n))
- [0321. Create Maximum Number](Solutions/0321.Create-Maximum-Number.py) (!!H) <br>
O(k^2): there're 3 steps: 1. iterate i from 0 to k; 2. find max number from nums1, nums2 by select i , k-i numbers - monostack; 3. merge the max_num1 and max_num2 into one number - two pointers. 非常牛叉的题目呀
- [0013. Roman to Integer](Solutions/0013.Roman-to-Integer.py) (!!E) <br>
use a distionary to store the roman to num pair, warm up for the following problem
- [0012. Integer to Roman](Solutions/0012.Integer-to-Roman.py) (!!!M) <br>
use a list of tuples to store (num, roman) pair, 注意list要逆序排列. Then find the num that is closest to num and num minus it and update res.
- [0420. Strong Password Checker](Solutions/0420.Strong-Password-Checker.py) (!!H Google) <br>
Greedy. 分三个区间讨论：1. n <= 5: return max(6 - n, missing_types), 用三个小Helper function to calculate three missing_types;2. 6 <= n <= 20: just need to return how many replacements are needed to avoid consecutive chars: number_of_replacements += num_of_consecutives // 3; 3. n > 20: step 1: calculate how many replacements are neededto avoid consecutive chars; step 2: calculate how many deletions can be used to save replacements - greedy.好难呀
- [0853. Car Fleet](Solutions/0853.Car-Fleet.py) (!!M) <br>
算法：我的位置比你小，需要的时间还比你少，那说明我可以追上你
- [1616. Split Two Strings to Make Palindrome](Solutions/1616.Split-Two-Strings-to-Make-Palindrome.py) (H) <br>
pre-calculation: O(N)






# [系列题](/)
### [Gradient Descent](/)
- [0069. Sqrt(x)](Solutions/0069.Sqrt(x).py) (!!E) <br>
gradient descent. 三种方法：1. Binary Search; 2. Newton's Method. x<sub>k+1</sub> = (x<sub>k</sub> + x/x<sub>k</sub>) / 2; O(logN) since the set converges quadratically.
solution 3: gradient descent: Gradient descent 核心算法: <br>
while alpha > eps: <br>
     prediction -= alpha * gradient, where gradient = d(cost_func)/dx, where cost_func = MSE; <br>
     alpha * = 0.2 <br>
return prediction <br>
- [1515. Best Position for a Service Centre](Solutions/1515.Best-Position-for-a-Service-Centre.py) (!!!H) <br>
the cost_func is actually defined as distance. 


### [Geometry](/)
- [0836. Rectangle Overlap](Solutions/0836.Rectangle-Overlap.py) (E) <br>
比较点的坐标即可
- [0223. Rectangle Area](Solutions/0223.Rectangle-Area.py) (M) <br>
分成是否overlap两种情况来计算, overlap = (min(C, G) - max(A, E)) * (min(H, D) - max(B, F))
- [0391. Perfect Rectangle](Solutions/0391.Perfect-Rectangle.py) (!!H) <br>
属于观察题目性质的题, In order to form a perfect rectangle, two condictions must be satisfied:
condition 1. for all the coordinates, there are 4 and only 4 coordinates that appear only once, others appear either twice or 4 times.  So we can use a set to store all the coordinates and cnt their appear times
condition 2. the sum of area of all the small rectangles should be the same as the whole big one (the area enclosed by the 4 coordinates in condition 1)
- [0963. Minimum Area Rectangle II](Solutions/0963.Minimum-Area-Rectangle-II.py) (!!M Google) <br>
如果两条对角线相等，且平分对方，则这两条对角线可以组成矩形. use a hashmap to map (对角线的长度, 对角线的中点坐标) to a list of (对角线连接的两点的坐标) - O(n^2), O(n^2)
- [Path with Circle Blocks](Solutions/Google__Path-with-Circle-Blocks.py) (!! M) <br>
Solution: Union-Find all the circles
- [1266. Minimum Time Visiting All Points](Solutions/1266.Minimum-Time-Visiting-All-Points.py) (E) <br>
- [1232. Check If It Is a Straight Line](Solutions/1232.Check-If-It-Is-a-Straight-Line.py) (E) <br>
y = k* x + b. 单独判断k不存在的情况
- [1453. Maximum Number of Darts Inside of a Circular Dartboard](Solutions/) (H) <br>
The intuition is that each potential answer has at least two points(darts) on the circle. O(n^3). Too hard for an interview.
- [1401. Circle and Rectangle Overlapping](Solutions/1401.Circle-and-Rectangle-Overlapping.py) (M) <br>
there are 9 cases in terms of repative pos of a circle and a rectangle
- [0593. Valid Square](Solutions/0593.Valid-Square.py) (M Google) <br>
Geometry. 看对角线吧 - 平分且相等且垂直
- [0939. Minimum Area Rectangle](Solutions/0939.Minimum-Area-Rectangle.py) (!!M Google) <br>
Geometry. O(N^2) - 我们choose two diagnol points to iterate, then check if other two diagonal points in p_set. 
- [0356. Line Reflection](Solutions/0356.Line-Reflection.py) (M) <br>
use a hashset to store all the points. loop through the points and check if (max_x + min_x - x, y)  in hashset
- [1610. Maximum Number of Visible Points](Solutions/1610.Maximum-Number-of-Visible-Points.py) (H) <br>
step 1: calculate all the angles with respect to the location; step 2: sort the angles; step 3: find the max_subarray size with diff_of_max_and_min <= angle, using sliding window




### [Robot Simulation!!!](/)
- [0657. Robot Return to Origin](Solutions/0657.Robot-Return-to-Origin.py) (E) <br>
Beacuase the way that the robot is "facing" is irrelevant, the solution is trivial.  Just count if the steps of going up equals the steps of going down; and the steps of going left equals the steps of going right.
- [0874. Walking Robot Simulation](Solutions/0874.Walking-Robot-Simulation.py) (!!E) <br>
首先定义facing directions: (1, 0) 代表facing up, (0, 1)代表facing right，(-1, 0)代表facing down, (0, -1)达标facing left, facing_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  注意顺序不能变. 如果是右转就是facing = (facing + 1) % 4, 新的facing direction 就是facing_directions[facing];  如果是左转就是facing = (facing - 1) % 4, 新的facing direction 就是facing_directions[facing].  
- [1041. Robot Bounded In Circle](Solutions/1041.Robot-Bounded-In-Circle.py) (!!M) <br>
The robot stays in the circle if (looking at the final vector!!!), it changes direction (ie. doesn't stay pointing north), or it moves 0
- [0489. Robot Room Cleaner](Solutions/0489.Robot-Room-Cleaner.py) (!!!H Google) <br>
遍历机器人的四个方向即可，唯一需要注意的是每次都需要调整机器人的朝向才能move一下，毕竟是机器人嘛. backtrack函数需要传入(curr_i, curr_j, curr_facing). 另外需要定义一个go_back function so that we can go back to the original position and facing for backtracking purpose.



### [Bit Manipulation](/)
- [0136. Single Number](Solutions/0136.Single-Number.py) (!!E) <br>
Bitwise XOR is the most important in bit manipulation. 要牢记xor的三条定律: If we take XOR of zero and some bit, it will return that bit: a⊕0=a; If we take XOR of two same bits, it will return 0: a⊕a=0; Commutative law for XOR: a⊕b⊕a=(a⊕a)⊕b=0⊕b=b. So we can XOR all bits together to find the unique number.
- [0137. Single Number II](Solutions/0137.Single-Number-II.py) (M) <br>
A general solution for dealing with numbers with n-repeating time is to deal with bit by bit, and then take the mod of n.
- [0260. Single Number III](Solutions/0260.Single-Number-III.py) (M) <br>
Use a bitmask to record the difference between two numbers (x and y) which were seen only once - 看不懂
- [0191. Number of 1 Bits](Solutions/0191.Number-of-1-Bits.py) (!!E) <br>
The way to iterate each bit in an integer is: while n > 0: n = n >> 1. get the last bit of n: last_bit = n & 1
- [0190. Reverse Bits](Solutions/0190.Reverse-Bits.py) (E) <br>
- [0371. Sum of Two Integers](Solutions/0371.Sum-of-Two-Integers.py) (!!M) <br>
- [0201. Bitwise AND of Numbers Range](Solutions/0201.Bitwise-AND-of-Numbers-Range.py) (M) <br>
只要写代码找到左边公共的部分即可
- [0318. Maximum Product of Word Lengths](Solutions/0318.Maximum-Product-of-Word-Lengths.py) (M) <br>
solution 1: sort and put larger lens in front. O(NlogN + N^2* L)
- [0393. UTF-8 Validation](Solutions/0393.UTF-8-Validation.py) (M) <br>
- [0089. Gray Code](Solutions/0089.Gray-Code.py) (M) <br>
找规律的题




### [Math](/)
- [1071. Greatest Common Divisor of Strings](Solutions/1071.Greatest-Common-Divisor-of-Strings.py) (!!!E) <br>
交叉相除法，又叫Euclidean algorithm: The central idea is that if y > x, the GCD of x and y is the GCD of x and y − x. For example, GCD(156, 36) = GCD((156 − 36) = 120, 36). By extension, this implies that the GCD of x and y is the GCD of x and y mod x, i.e., GCD(156, 36) = GCD((156 mod 36) = 12, 36) = GCD(12, 36 mod 12 = 0) = 12. 具体implement的时候用recursion就可以了
- [0780. Reaching Points](Solutions/0780.Reaching-Points.py) (!!H) <br>
work backwards: we compare tx and ty, whenever we found tx > ty, we update tx: tx -= ty. else we update ty: ty -= tx.  we update tx and ty all the way until we reach sx and sy.
O(max(tx, ty))
- [0343. Integer Break](Solutions/0343.Integer-Break.py) (M)
拆分乘积最大的两个原则：1. 当所有拆分出的数字相等时，乘积最大； 2：拆分成三份时，乘积最大
- [0829. Consecutive Numbers Sum](Solutions/0829.Consecutive-Numbers-Sum.py) (H) <br>
假设从x开始存在连续有k个加起来等于N, then x+(x+1)+...+(x+k-1) = N, ie: kx + k(k-1)/2 = N.
kx = N - k(k-1)/2. x = (N - k(k-1)/2) / k.  so the problem becomes: for k in range(1, N),
is there a number k, such that (N - k(k-1)/2) / k is an integer?
- [0043. Multiply Strings](Solutions/0043.Multiply-Strings.py) (M Google) <br>
Math. 3 * 456 = 456 + 456 + 456
- [0335. Self Crossing](Solutions/0335.Self-Crossing.py) (!!H Google) <br>
Math. there are 3 cases in total.
- [0326. Power of Three](Solutions/0326.Power-of-Three.py) (E) <br>
solution 1: recursion; solution 2: math: return abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10
- [1131. Maximum of Absolute Value Expression](Solutions/1131.Maximum-of-Absolute-Value-Expression.py) (M) <br>
根据正负符号分为4个situations. 对于每一个situation, 我们用121. Best time to buy stock problem: maintain 一个prev_min
- [0539. Minimum Time Difference](Solutions/0539.Minimum-Time-Difference.py) (M) <br>
sort之后相邻的进行比较即可，最后compare time_points[0] and time_points[-1]
- [1344. Angle Between Hands of a Clock](Solutions/1344.Angle-Between-Hands-of-a-Clock.py) (M) <br>




### [Rolling Hash/Rabin Karp]()
- [0128. Hash Function](Solutions/0128.Hash-Function.py) (E Lintcode) <br>
Rabin Karp Algorithm O(M+N)
- [0028. Implement strStr()](Solutions/0028.Implement-strStr().py) (!!E) <br>
Rabin Karp Algorithm O(M+N): Rolling hash 的核心就是用一个hash function把一个长度为m的string hash成一个整数，这样就可以避免O(m)的时间复杂度去比较两个string是否相等，而是去比较两个string的hash code 只用O(1)的就可以比较了。A good application of this strStr() problem is that it can be used as an API for solving the problem of check if T2 is subtree of T1 ,both are very large trees.
- [0187. Repeated DNA Sequences](Solutions/0187.Repeated-DNA-Sequences.py) (!!M) <br>
O(N) solution: Rabin Karp / Rolling hash. calculate the hash_code for each L = 10 window. use a hash_code_set to record the calculated hash_code, if the newly calculated hahs_code is in the hash_code_set, then that means we have repeated sequance.
- [1062. Longest Repeating Substring](Solutions/1062.Longest-Repeating-Substring.py) (!!!M Google) <br>
可以从lens-1开始逐个去试，takes O(N^2). 也可以用binary search去试. 如何快速判断是否存在two substring with length = L that equal? 
Using rolling hash to check if two substring have the same hash_code, using rolling hash, we realized O(1) string comparison;
So the overall time complexity is O(nlogn), where n is the lens of S
- [1044. Longest Duplicate Substring](Solutions/1044.Longest-Duplicate-Substring.py) (H) <br>
step 1: find the lens of longest duplicated substring using binary search - 1062. Longest Repeating Substring;
step 2: use the longest lens to find the substring - 187. Repeated DNA Sequences
- [1147. Longest Chunked Palindrome Decomposition](Solutions/1147.Longest-Chunked-Palindrome-Decomposition.py) (!!H) <br>
greedy algorithm: 双指针left and right, 一个从前往后遍历得到left_s，另一个从后往前遍历right_s，
if left_s == right_s: res += 1;
O(NL), N is lens of s, L is the average lens of equal string. Improve: instead of comparing left_s == right_s, we compare left_hash_code == right_hash_code.
- [1316. Distinct Echo Substrings](Solutions/1316.Distinct-Echo-Substrings.py) (H) <br>
先把整个string的hash_code计算出来存在一个数组里面hash_code[i] = the hash code for s[:i] 相当于prefix_hash_code这样后面计算substring s[i:j]的hash code就是O(1) 了
- [0214. Shortest Palindrome](Solutions/0214.Shortest-Palindrome.py) (!!H Google) <br>
The problem really is to find the longest palindrome starts with s[0].
rabin carp / rolling hash O(N). The algorithm is for string s, left_code = the hash_code scan from left to right,
right_code = the hash_code scan from right to left. if left_code == right_code, then s is a palindrome.
- [1312. Minimum Insertion Steps to Make a String Palindrome](Solutions/1312.Minimum-Insertion-Steps-to-Make-a-String-Palindrome.py) (!!H Google) <br>
dp 1143.Longest Common- Subsequence. 题目其实是求 n - (the longest palindromic subsequence in s); 也就是 to find the longest common subsequence between s and s[::-1]. which is same as 1143.Longest Common- Subsequence.
- [0616. Add Bold Tag in String](Solutions/0616.Add-Bold-Tag-in-String.py) (!!M) <br>
step 1: store the (start_idx, end_idx) for every appearance of substring in s.  Algorithm: 28. Implement strStr() Rabin Karp - O((M+N)* W), where N is len(s), M is avg lens of words in dict, and W is len(dict). step 2: now we have a list of (start, end) intervals, we merge interval so that we don't have overlaps anymore.  Algorithm: 56. merge intervals. step 3: add <b> and </b> pair to generate res




### [String Manipulation](/)
- [0833. Find And Replace in String](Solutions/0833.Find-And-Replace-in-String.py) (!!!M Google) <br>
String manipulation.
- [0722. Remove Comments](Solutions/0722.Remove-Comments.py) (!!M Google) <br>
String manipulation. manipulate string line by line.
- [0777. Swap Adjacent in LR String](Solutions/0777.Swap-Adjacent-in-LR-String.py) (!!M Google) <br>
观察之后可以发现每次replace "XL" to "LX"都是相当于把"L"向左移动。
所以"L"一直向左移动，并且不会跨越其他"L" or "R". 而"R"一直向右移动，并且不会跨越其他"R" or "L".
- [0271. Encode and Decode Strings](Solutions/0271.Encode-and-Decode-Strings.py) (!!M Google) <br>
quite smart. Encodes a list of strings to a single string. encode ["a$c@d", "31_;df"] as "5 a$c@d6 31_;df", where 5 is len("a$c@d") and 6 is len("31_;df").
- [0418. Sentence Screen Fitting](Solutions/0418.Sentence-Screen-Fitting.py) (!M Google) <br>
string. fit the sentence in line by line
- [0068. Text Justification](Solutions/0068.Text-Justification.py) (!!H Google) <br>
String manipulation. use curr_line = [] to record curr words in curr_line; use curr_width = 0 to record curr total number of chars in curr_line. Iterate the word in words, if too many words to fit in one line, we first justify that line and update res, then start over the curr_line = [] and curr_width = 0 for the next line. Lastly, we deal with the last line seperately.
- [0771. Jewels and Stones](Solutions/0771.Jewels-and-Stones.py) (E Google) <br>
Too easy to believe.
- [1592. Rearrange Spaces Between Words](Solutions/1592.Rearrange-Spaces-Between-Words.py) (E Google) <br>
Easy heasy!
- [0389. Find the Difference](Solutions/0389.Find-the-Difference.py) (E Google) <br>
Use two cnters, easy heasy!
- [0058. Length of Last Word](Solutions/0058.Length-of-Last-Word.py) (!!E Google) <br>
一定要熟悉句式：while j + 1 < len(s) and s[j+1].isalpha(): j += 1
- [100420-Sentence Reverse](Solutions/Pramp__100420-Sentence-Reverse.py) (!!M) <br>
O(N), O(1) solution - step 1: loop thru the given arr and inverse the whole array; step 2: reverse each word
- [0819. Most Common Word](Solutions/0819.Most-Common-Word.py) (E) <br>
String processing in pipline: step 1: pre-process: convert all letters in lower case and replace the punctuations with spaces cuz they are not valid words; step 2: count the freq of the words that are not banned
- [0008. String to Integer (atoi)](Solutions/0008.String-to-Integer-(atoi).py) (!!M) <br>
we only need to handle 3 cases: 1. discards all leading whitespaces - using python str.strip(char). 2. sign of the number - use 正负1来代表符号. 3. overflow
- [0273. Integer to English Words](Solutions/0273.Integer-to-English-Words.py) (!!H) <br>
construct 3 lists for the english expressions for numbers less_than_20, tens, thousands.
the main funciton handle the situation of num >= thousands.
use a helper funciton to calcuate cases when num <= hundreds.
- [0459. Repeated Substring Pattern](Solutions/0459.Repeated-Substring-Pattern.py) (E) <br>
step 1: find all possible divisible lens - O(n^0.5); step 2: try each possible divisible lens to see is it's a valid divide - O(n^1.5).
- [0929. Unique Email Addresses](Solutions/0929.Unique-Email-Addresses.py) (E) <br>





### [Array / Image Process](/)
- [0169. Majority Element](Solutions/0169.Majority-Element.py) (!!E) <br>
Boyer-Moore Voting Algorithm - IO(N), O(1)
- [0229. Majority Element II](Solutions/0229.Majority-Element-II.py) (M) <br>
Boyer-Moore Voting Algorithm
- [0048. Rotate Image](Solutions/0048.Rotate-Image.py) (!M) <br>
Step 1: reverse columns: swap( matrix[][i], matrix[][j] ); Step 2: transpose: swap( matrix[i][j], matrix[j][i] )
- [1329. Sort the Matrix Diagonally](Solutions/1329.Sort-the-Matrix-Diagonally.py) (M) <br>
just sort each diagonal - O(MNlog(min(M, N)))
- [0835. Image Overlap](Solutions/0835.Image-Overlap.py) (!!M) <br>
step 1: use a list to record the positions for A and B where 1s are located;
step 2: use a dictionary 来存 (左右移动步数，上下移动步数) --> 多少个1能通过这样的移动重合
O(N^4), O(N^2)
- [0989. Add to Array-Form of Integer](Solutions/0989.Add-to-Array-Form-of-Integer.py) (E Google) <br>
Array. 
- [0463. Island Perimeter](Solutions/0463.Island-Perimeter.py) (E Google) <br>
Array.  step 1: find the min_row, max_row, min_col, max_col for the island; step 2: update the res row by row, col by col
- [0840. Magic Squares In Grid](Solutions/0840.Magic-Squares-In-Grid.py) (!!!M Google) <br>
Array. 找规律就可以了
- [070820-Busiest Time in The Mall](Solutions/Pramp__070820-Busiest-Time-in-The-Mall.py) (M) <br>
居然没做出来呀，太菜了，真的需要练呀！！
- [0073. Set Matrix Zeroes](Solutions/0073.Set-Matrix-Zeroes.py) (M) <br>
solution 1: mark the rows and cols that need to be set to zero - O(mn), O(m+n); solution 2: use the first cell of every row and column as a flag.  This flag would determine whether a row or column has been set to zero. - O(mn), O(1)
- [0006. ZigZag Conversion](Solutions/0006.ZigZag-Conversion.py) (M) <br>
- [0605. Can Place Flowers](Solutions/0605.Can-Place-Flowers.py) (E) <br>
把arr进行预处理：把arr的头部和尾部各加上0
- [1630. Arithmetic Subarrays](Solutions/1630.Arithmetic-Subarrays.py) (E) <br>
- [0066. Plus One](Solutions/0066.Plus-One.py) (E) <br>




###  [Segment Tree](https://docs.google.com/document/d/17TreXs76VcuSkbqIz7UTaambKF81O9gdK8ruT5nFG1M/edit#)
##### build, update, query三个函数都是用递归(divide and conquer)的方式实现的
- [0201. Segment Tree Build](Solutions/0201.Segment-Tree-Build.py) (M Lintcode) <br>
Segment tree build takes O(N), where lens of the input arr
- [0439. Segment Tree Build II](Solutions/0439.Segment-Tree-Build-II.py) (M Lintcode) <br>
Segment tree build takes O(N), root.max need to be updated in this problem
- [0203. Segment Tree Modify](Solutions/0203.Segment-Tree-Modify.py) (M Lintcode) <br>
Segment tree update takes O(h) or O(logN)
- [0202. Segment Tree Query](Solutions/0202.Segment-Tree-Query.py) (M Lintcode) <br>
Segment tree query takes O(h) or O(logN). This problem is to query the max number in a range.
- [0247. Segment Tree Query II](Solutions/0247.Segment-Tree-Query-II.py) (M Lintcode) <br>
Segment tree query takes O(h) or O(logN). This problem is to query the count in a range.
- [0205. Interval Minimum Number](Solutions/0205.Interval-Minimum-Number.py) (!!M Lintcode) <br>
Maintain a self.min_num in building the SegmentTree. 
- [0751. John's business](Solutions/0751.John's-business.py) (!!M Lintcode) <br>
Solution 1: sliding window minimum - use a mono deque - O(n). similar with 239. Sliding Window Maximum.min_vals[i]表示以i结尾的window的minimum value, 特别注意sliding window maximum/minimum 都是以以i为dq window的最右端 构造 mono deque. solution 2: segment tree - O(nlogk). Maintain a self.min_num in building the SegmentTree.
- [0206. Interval Sum](Solutions/0206.Interval-Sum.py) (M Lintcode) <br>
Maintain a self.range_sum in buildign the SegmentTree
- [0207. Interval Sum II](Solutions/0207.Interval-Sum-II.py) (!!M Lintcode) <br>
Segment tree is good for 需要动态更新数组和query range sum的情况，O(logN) update and O(logN) range sum query
- [0303. Range Sum Query - Immutable](Solutions/0303.Range-Sum-Query-Immutable.py) (!!E) <br>
输入数组是immutable的，因此用不着segment tree, 用一个prefix_sum数组做cache就可以实现O(1) query 了
- [0307. Range Sum Query - Mutable](Solutions/0307.Range-Sum-Query-Mutable.py) (!!M) <br>
输入数组是mutable, 需要快速的update, 所以可以用segment tree来实现O(logn) update and O(logn) query.
- [0304. Range Sum Query 2D - Immutable](Solutions/0304.Range-Sum-Query-2D-Immutable.py) (!!M) <br>
a 2D version prefix sum. O(1) for query.
- [0308. Range Sum Query 2D - Mutable](Solutions/0308.Range-Sum-Query-2D-Mutable.py) (H) <br>
solution: segment tree. 代码裸长115行，我去NMLGB! 放弃这题算了
- [0699. Falling Squares](Solutions/0699.Falling-Squares.py) (!!H) <br>
solution 1: O(N^2). Every time a new square falls down, we check the previous square to see if there is any square beneath the current falling square. If we found that we have squares i intersect with us, which means my current square will go above to that square. Then we should update the max_h. solution 2: 因为每进来一个squre我们都需要query 在这个interval里的max_num, 所以我们segement tree to enable O(logN) query. - O(NlogN)
- [0248. Count of Smaller Number](Solutions/0248.Count-of-Smaller-Number.py) (M Lintcode) <br>
solution 1: binary search, need to sort the arr first which takes O(NlogN). This solution is better for an interview.
solution 2: Segment Tree, which takes O(N) to build the tree and O(logN) to query. To find how many numbers are less than num, 
is actually to find how many numbers are there in range [0, num-1], since the minimum number is 0 given by the description of the problem. 这样就相当于转化成了类似range_sum的问题了，since we add num into the tree one by one, each update takes O(logN), so the whole updating takes O(NlogN).
这题的self.start, self.end represent the num, not idx.  sel.cnt is how many numbers are there in range [start, end], and again start, end are not idx, they are actual vals.
- [0493. Reverse Pairs](Solutions/0493.Reverse-Pairs.py) (!!H) <br>
merge sort才是这道题的正解！Count "important reverse pairs" while doing mergesort: When we're doing mergesort, original index of elements in left part (smaller side), i, must less than those in right part, j.  So in addition to the while loop for do merge/conquer,我们在conquer那个while loop之前额外加一个 while loop to compare nums[i] and 2* nums[j] to update cnt. - O(nlogn)
- [0315. Count of Smaller Numbers After Self](Solutions/0315.Count-of-Smaller-Numbers-After-Self.py) (!!H) <br>
正解是solution 2: merge sort O(nlogn). 注意因为self.res是要更新没有个idx的cnt, 所以要把idx带在nums里面去sort nums. 在conquer 的 while loop之前，我们用一个while loop to compare nums[i] and nums[j] to update self.res
- [0327. Count of Range Sum](Solutions/0327.Count-of-Range-Sum.py) (!!H) <br>
Solution 1: prefix_sum + hashmap.  construct a prefix_sum. Then do the LC 0001. Two Sum problem. The presum_dict stores (presum --> how many times the presum occurs). O(NW), where N is len(nums) and W is the width of the range we want to query. 面试第一反应就应该是solution 1, 如果面试官说[lower, upper] range is very large much larger than N, 
then we might consider the following solution prefix_sum + merge_sort. solution 2: prefix_sum + merge_sort 在conquer 的 while loop之前，我们用一个while loop to compare lower <= (right[j] - left[i]) <= upper to update self.res. update self.res 的方法可以是暴力也可以是sliding window来实现






# Google top 200

- [0843. Guess the Word](Solutions/0843.Guess-the-Word.py) (!!!H Google) <br>
Repeatedly choose a word to guess, and then eliminate all words that do not have the same number of matches as the guessed word. 
In this way, the wordlist is narrowed down each time we do a guess.
How to choose a word: solution 1: random guess; 2. choose the guess word wisely (Heuristically). Soltion 2: Each time we guess, we choose the word that has the most common chars (overlaps) with other words in the candidates list. This is just a hueristic estimation, hard to prove why it works. But indeed it works much better than random guess.
- [1423. Maximum Points You Can Obtain from Cards](Solutions/1423.Maximum-Points-You-Can-Obtain-from-Cards.py) (!!!M Google) <br>
sliding window with fix size problem, the only difference is that some part of the window is at the beginning of the list and some are at the end. 我们可以转化为 find the minimum points you can get within window with fixed size: lens-k. 套用模板即可 Google真是滑窗控
- [0727. Minimum Window Subsequence](Solutions/0727.Minimum-Window-Subsequence.py) (!!!H) <br>
solution 1: sliding window - O(MN) 这题subseq与上题substring不同，上题只需要freq都满足了就行，这题不仅如此，而且还是讲究顺序的，; solution 2: dp. dp[i][j] = the min window subsequence that __ends with__ ith ch in t, and jth ch in s. If t[i-1] == s[j-1]: dp[i][j] = dp[i-1][j-1] + 1; else: dp[i][j] = dp[i][j-1] + 1
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
我们分账总得有一定顺序吧，用什么顺序呢？我们一个人一个人去balance, 这个人balance完之后就再也不用管他了。用backtrack的方法我们一个idx一个idx去balance,
backtrack结束条件: curr_balanced_idx == len(lst) - 1,
constraints for next_candidate: next_balanced_idx = curr_balanced_idx + 1,
arguments pass into backtrack function: curr_idx, curr_cnt,
time complexity is O(N* 2^N) cuz we need to to balance curr_idx one by one, so O(N),
and each balance process, we need to put or not-put next_idx to balance curr_idx, so O(2^N)
- [0471. Encode String with Shortest Length](Solutions/0471.Encode-String-with-Shortest-Length.py) (!!!H Google) <br>
solution dp. dp[i][j] is the encode of substring including index i to index j. dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j], potential_concadenation) in terms of length.
potential_concadenation = "k[repeating_pattern]",  where pattern is the repeating string in substring s[i:j+1] and k is the number of repeating times. 
initializaton: dp[i][j] = s[i:j+1] originally, return dp[0][n-1]
- [0715. Range Module](Solutions/0715.Range-Module.py) (!!!H) <br>
Store intervals in a 1D sorted array. Use bisect_left and bisect_right to locate where the incoming interval should be. addRange and removeRange use bisect to replace the exsited range, takes O(log(N)). queryRange can also use bisect to locate where the interval location is, [left, right]必须在某一个且同一个range内才return True - O(logN)
- [0846. Hand of Straights](Solutions/0846.Hand-of-Straights.py) (!!!M Google) <br>
same as 1296. 用以一个hashmap记录frequency. 由于必须固定长度为W, 所以我们每次都去连W个就可以了
- [0722. Remove Comments](Solutions/0722.Remove-Comments.py) (!!M Google) <br>
String manipulation. manipulate string line by line.
- [1060. Missing Element in Sorted Array](Solutions/1060.Missing-Element-in-Sorted-Array.py) (!!!M Google) <br>
定义一个function missing(idx) to find the number of number missing before idx. so that we can compare missing(mid) with k. Google真的把binary search 玩出花了！
- [1056. Confusing Number](Solutions/1056.Confusing-Number.py) (E) <br>
use a hashmap
- [1088. Confusing Number II](Solutions/1088.Confusing-Number-II.py) (!!H Google) <br>
Only 0, 1, 6, 8, 9 are the valid set of digits, do a backtracking to generate all the numbers containing this digits and check they are valid. backtrack结束条件: int(curr_comb) in range [1, N +1] and curr_comb is confusing nubmer; constraints on next_candidates: has to come from mapping, cannot have leading zero; arguments pass into function: curr_comb
time complexity: O(M* 5^M), where M is how many digits are there in str(N), which scales with ~logN, where log is 10-based.
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
solution 1: modify the input nums by changing the 0 one by one - O(nk); solution 2: do not change the input nums, just use a q to record if ith num has been changed - O(n); q 记录区间[i-k, i]内被反转了的idx, 遍历过程中把里i很远的idx都pop出来，保持窗口小于等于K, 此时len(q)就是位置i已经被翻转的次数，如果为奇数表示i已经从0翻到1或者从1翻到0了
- [0753. Cracking the Safe](Solutions/0753.Cracking-the-Safe.py) (!!!H) <br>
思路： dfs结束条件: len(covered) == n** k; constraints on next_candidates: greedily choose the last n-1 chars from curr_candidate, and next_candidate not in covered; arguments pass into dfs function: None
- [0308. Range Sum Query 2D - Mutable](Solutions/0308.Range-Sum-Query-2D-Mutable.py) (H) <br>
solution: segment tree. 代码裸长115行，我去NMLGB! 放弃这题算了
- [0085. Maximal Rectangle](Solutions/0085.Maximal-Rectangle.py) (!!!H Google) <br>
step 1: construct a heights list for each row; step 2: calculate the largestRectangularHistogram of each height using the same method in 84; Should think about dynamic programming solution also.
- [0690. Employee Importance](Solutions/0690.Employee-Importance.py) (!!E Google) <br>
simple dfs 可破, use a dictionary to map employee_id with employee, so that looking for employee by id takes O(1)
- [1146. Snapshot Array](Solutions/1146.Snapshot-Array.py) (!!!M Google) <br>
solution 1: sparse array. Since 题目说了 initially, each element equals 0.
we treated it as a sparse matrix: use a dictionary to store only the non-zero values.
- [1293. Shortest Path in a Grid with Obstacles Elimination](Solutions/1293.Shortest-Path-in-a-Grid-with-Obstacles-Elimination.py) (!!!H Google) <br>
bfs. q 里面需要放入当前用了多少eliminations. q.append((next_i, next_j, curr_elimination_cnt)). if we can get to (next_i, next_j) with less elimination, we should also visit, even if it is visited already
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
- [1277. Count Square Submatrices with All Ones](Solutions/1277.Count-Square-Submatrices-with-All-Ones.py) (M Google) <br>
DP. very similar with 221.Maximal-Square. dp[i][j] 表示以 (i, j) 结尾所组成的最大正方形的边长。dp[i][j] 也表示以 (i, j) 结尾能组成的正方形的个数。
- [1376. Time Needed to Inform All Employees](Solutions/1376.Time-Needed-to-Inform-All-Employees.py) (!!!M Google) <br> 
Same as Path Sum II except it's a N-arry tree.
- [1240. Tiling a Rectangle with the Fewest Squares](Solutions/1240.Tiling-a-Rectangle-with-the-Fewest-Squares.py) (!!!H Google) <br>
backtrack. The basic idea is to fill the entire block bottom up.  In every step, find the lowest unfilled square first, and select a square with different possible sizes to fill it.  What is the nodes in the graph? It is a height array (skyline) height_arr!!!!! 
The start_node is height_arr = [0, 0, 0...], the end_node is height_arr = [m, m, m...]. Pruning: 1. When the current cnt has exceeded the value of the current global optimal solution, then no need to move forward. 2. Try largest square possible first (improves time by a lot).
- [1504. Count Submatrices With All Ones](Solutions/1504.Count-Submatrices-With-All-Ones.py) (!!!M Google) <br>
Monostack. solution 1: dp. O(M^2N) 固定以up_row为长方形上边，然后去探寻不同下边的情况, 每次探寻一个下边，我们都计算一次从up_row到down_row可能有多少个valid_submatrices,
我们把这个计算转换成一维来计算，对于每一个up_row, 都构建一个一位数组arr.  arr[j] = 1 if from up_row to down_row, all values in column j are 1. 只要up_row到down_row有一个value is 0，
我们就设置arr[j] = 0, 表示不可能以up_row为上边以down_row为下边以j为右col构造valid submatrce. solution 2: 与84.Largest-Rectangle-in-Histogram, 85.Maximal-Rectangle很类似.
先构造histogram. 以j结尾的submatrices的个数等于heights[j] * (j - 向左找第一个height小于heights[j]的idx).
- [0729. My Calendar I](Solutions/0729.My-Calendar-I.py) (!!M Google) <br>
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
If two subtrees have the same string representation, then they are duplicated subtrees. serialize the binary tree using divide and conque.  use a hashmap to store the serialization_representation --> a list of the root_node, the whole algorith takes O(N)
- [0767. Reorganize String](Solutions/0767.Reorganize-String.py) (!!M Google) <br>
套task schedule的模板即可
- [1444. Number of Ways of Cutting a Pizza](Solutions/1444.Number-of-Ways-of-Cutting-a-Pizza.py) (!!!H Google) <br>
dfs + memo. memo[(i, j, k)] returns the number of ways to cut pizza[i:n][j:m] into k pieces.
Step 1: In order to fast get how many apples are there in the down-right corner pizza[i:n][j:m] block,
construct suff_sum similar with 304. Range Sum Query 2D - Immutable. Step 2: dfs + memo.
- [0777. Swap Adjacent in LR String](Solutions/0777.Swap-Adjacent-in-LR-String.py) (!!M Google) <br>
观察之后可以发现每次replace "XL" to "LX"都是相当于把"L"向左移动。
所以"L"一直向左移动，并且不会跨越其他"L" or "R". 而"R"一直向右移动，并且不会跨越其他"R" or "L".
- [0752. Open the Lock](Solutions/0752.Open-the-Lock.py) (!!M Google) <br>
题目蛮有意思的, 带层序遍历的bfs, If next_node is deadend, then we don't put it into q, find neighbor 函数比较有意思，这里第一次学到了yield;
- [0834. Sum of Distances in Tree](Solutions/0834.Sum-of-Distances-in-Tree.py) (!!H) <br> 
sums(Y) = sums(X) + cnt(X) - cnt(Y) = sums(X) + (N - cnt(Y) - cnt(Y) = sums(X) + N - 2* cnt(X).
cnt[X]可以通过dfs遍历一次算出来存到一个list里面，这样我们如果已知sums(0)的话，
那么其余的sums(X)都可以通过上述公式算出来了
- [1244. Design A Leaderboard](Solutions/1244.Design-A-Leaderboard.py) (M) <br>
use a dictionary for fast addscore and reset. use a heapq to find top K elements
- [0299. Bulls and Cows](Solutions/0299.Bulls-and-Cows.py) (!!!M Google) <br>
use a digit_to_cnt hashmap for digit. one pass to update A_cnt, another pass to update B_cnt.
- [0130. Surrounded Regions](Solutions/0130.Surrounded-Regions.py) (!!M) <br>
Solution 1: dfs/bfs: Step 1: Start from border, do a bfs for "O", mark all the "O" that can be reached from the border. We can either mark by putting them into a visited set, or just change it to some symbol "#". Step 2: 2nd pass, we change to "X" tha "O" that could not be visited from the border.  Solution 2: Union Find.  Step 1: Union all the "O" that are neighborign with each other. We do a weighted union, meaning when we union, we also choose to point to the one that is on the border. Step 2: 2nd pass, we change to "X" tha "O" that has a root not on border.  bfs只从border出发做bfs, 很中间的"O"就不用管了，而Union Find中间的也需要union, 所以bfs 比union find 更快。Solution 3: dfs interatively, only change one line in the bfs solution. Solution 4: dfs recurssively.
- [0394. Decode String](Solutions/0394.Decode-String.py) (!!M Google) <br>
定义一个numStack, 一个strStack 存nums和parenthesis. if it's a digit, should use a while loop to add the num in case there are multiple digits; if it's a ch, then put it into strStack; if it's a [, then put the num in numStack and re-initialize the tempNum and tempStr for calculation inside the []; if it's a ], then pop the resStack and signStack and update res.
- [1296. Divide Array in Sets of K Consecutive Numbers](Solutions/1296.Divide-Array-in-Sets-of-K-Consecutive-Numbers.py) (!!!M Google) <br>
用以一个hashmap记录frequency. 由于必须固定长度为k, 所以我们每次都去连k个就可以了
- [0165. Compare Version Numbers](Solutions/0165.Compare-Version-Numbers.py) (M Google) <br>
把每一段的num计算出来是最好的
- [1074. Number of Submatrices That Sum to Target](Solutions/1074.Number-of-Submatrices-That-Sum-to-Target.py) (H) <br>
也可以先把行处理好，让每一行里面保存上面所有行的和，接下来就是在每一行里面去求560问题了，注意一点不同的是需要遍历upRow和downRow的, 如果不遍历就是solution 3的错误写法举一个反例想明白solution 3为什么行不通，自然就会改成solution 2了O(MMN)
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
dp[i][j][k]表示在棋盘(i, j)位置上走完k步数还留在棋盘上的走法总和(注意是走法，不是步数). dp[i][j][k] += dp[prev_i][prev_j][k-1] for prev_i and prev_j in bound.
- [Similar with 688. Knight Probability in Chessboard](Solutions/Google_Similar-with-688.Knight-Probability-in-Chessboard.py) (!!!M Google) <br>
dp.  dp[i][j][k] = from (i, j) the number of ways you to end up at the original coordinate with k steps.
dp[i][j][k] = dp[i - 1][j][k - 1] + dp[i][j - 1][k - 1] + dp[i + 1][j][k - 1] + dp[i][j + 1][k - 1]
- [0840. Magic Squares In Grid](Solutions/0840.Magic-Squares-In-Grid.py) (!!!M Google) <br>
Array. 找规律就可以了
- [0992. Subarrays with K Different Integers](Solutions/0992.Subarrays-with-K-Different-Integers.py) (!!H) <br>
exactly(K) = atMost(K) - atMost(K-1). Helper function is exactly the same as 340. Longest Substring with At Most K Distinct Characters
- [1218. Longest Arithmetic Subsequence of Given Difference](Solutions/1218.Longest-Arithmetic-Subsequence-of-Given-Difference.py) (!!!M Google) <br>
dp, similar with. solution 1: O(N^2), dp[i] = the LAS ended with arr[i]. dp[j] = dp[i] + 1 for i < j and arr[j] - arr[i] == diff. O(N) use hashmap, like two sum problem. dp[arr[j]] = dp[arr[j] - diff] + 1 if arr[j] - diff in dp else 1.
- [0818. Race Car](Solutions/0818.Race-Car.py) (!!H) <br>
层序遍历的bfs. 这个graph的nodes比较特殊，nodes是(curr_pos, curr_speed). strong pruning that is 100 times faster: 我们是有条件的回退，只有在超过了target的情况下我们才回退
- [0174. Dungeon Game](Solutions/0174.Dungeon-Game.py) (!!H Google) <br>
find the max of mininum_sum in all the paths.这题不能像1102.Path-With-Maximum-Minimum-Value那样用Dijkstra's (mnlogn)因为这题不是四个方向都能走的，也就是说选择了一个方向就不能回到原来的位置了，所以只能dp -O(mn). 假设我们能到达(m, n)房间，我们需要的最小血量是dp[m][n] = 1 if A[m][n] >= 0 else 1- A[m][n], 这是我们的base case.
那我们就知道了我们到达(m-1, n)房间所需的最小血量是dp[m-1][n] = 到达(m, n)房间所需要的血量减去在(m-1, n)房间的损耗，
即dp[m-1][n] =max(dp[m][n] - A[m-1][n], 1); 到达(m, n-1)房间所需的最小血量是dp[m][n-1] = max(dp[m][n] - A[m][n-1], 1).
所以我们是从终点倒着往起点推。
- [0949. Largest Time for Given Digits](Solutions/0949.Largest-Time-for-Given-Digits.py) (!!M Google) <br>
backtrack. step 1: find all possible permutations - O(4!). step 2: update max_possible time that can be constructed from the permutations.
- [1219. Path with Maximum Gold](Solutions/1219.Path-with-Maximum-Gold.py) (!!M)<br>
尝试每一个pos出发backtrack所有可能的path比较哪一条path能得到最多的gold - O(4^N). 注意backtrack遍历得到的是每一条path的curr_sum, 而不是像普通dfs那样得遍历的是整个区域的. 对比这一题与200. Number of islands. 我们可以看到求path一定需要用backtrack. backtrack与dfs相比其实就是多了一步visited.remove(next_candidate). 这就导致dfs的时间复杂度是O(N), while backtrack的时间复杂度是O(4^N), where N is the number of cells in the matrix. 4 is the number of next_nodes in the for next_candidate in ...
- [0068. Text Justification](Solutions/0068.Text-Justification.py) (!!H Google) <br>
String manipulation. use curr_line = [] to record curr words in curr_line; use curr_width = 0 to record curr total number of chars in curr_line. Iterate the word in words, if too many words to fit in one line, we first justify that line and update res, then start over the curr_line = [] and curr_width = 0 for the next line. Lastly, we deal with the last line seperately.
- [0609. Find Duplicate File in System](Solutions/0609.Find-Duplicate-File-in-System.py) (!!M) <br>
build a content_to_dir dictionary where key is content in txt file, val is a list of dir holding the content eg: ["root/a/1.txt"];
需要用到string.split(char), string.index(substring). Super important follow up questions for big data.
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
- [0659. Split Array into Consecutive Subsequences](Solutions/0659.Split-Array-into-Consecutive-Subsequences.py) (!!!M Google) <br>
这道题我们遍历nums的时候只要当前的num被前面的顺子需要，就把num连上去，顺子连得越长越好，这就是greedy所在，使用两个 HashMap，第一个 HashMap 用来建立某个数字和其出现次数之间的映射 freq，
第二个用来建立某个数字被前面顺子所需要的次数之间的映射 need。
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
solution 1: backtrack - 第一步：把单买的方式也转换成specials; backtrack结束条件: the needs has been met: all(curr_bought[i] > needs[i] for i in range(len(needs)))
constraint on next_candidates: 题目要求You are not allowed to buy more items than you want, even if that would lower the overall price.
arguments pass into backtrack function: curr_bought, curr_cost solution 2: dfs + memorization
- [1237. Find Positive Integer Solution for a Given Equation](Solutions/1237.Find-Positive-Integer-Solution-for-a-Given-Equation.py) (E Google) <br>
反向双指针. 
- [0844. Backspace String Compare](Solutions/0844.Backspace-String-Compare.py) (!!!E) <br>
这种双指针处理比较双序列问题很常见。由于题目"#"可以删掉前面的ch, We can use a pointer traverse from __right to left__, and use a counter to count how many "#" we got so far. 一般要求用O(1) space解决。Google follow up: 加一个按键是类似caps lock，即按了之后所有的字母小写变大写，再按一下大写变小写。
思路：定义caps cnt，先扫一遍看多少个caps lock，比较s1.charAt(i) == s2.charAt(j) && caps1 == caps2
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
similar with 45. Jump Game, define a curr_must_reach and next_must_reach. if next_must_reach == curr_must_reach, we can cut it.
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
- [0698. Partition to K Equal Sum Subsets](Solutions/0698.Partition-to-K-Equal-Sum-Subsets.py) (!!!M) <br>
套backtrack模板即可，backtrack里面需要传入(curr_sum, curr_idx, curr_cnt).
结束条件是已有curr_cnt=k段满足条件了. 
Time complexity: we basically iterate over nums and for each element either use it or drop it, 
which is O(2^n). We are doing the same for each subset. Total subsets are k. 
So Time Complexity becomes O(k*(2^n))
- [0123. Best Time to Buy and Sell Stock III](Solutions/0123.Best-Time-to-Buy-and-Sell-Stock-III.py) (H) <br>
Only two transactions are allowed.  Maintain buy1=the minimum money you can **owe** after the first buy, sell1=the maximum money you **earn** after the first sell, also, buy2, sell2, and update them together in a for loop, 算法只是把121中的算法重复两次而已.
- [0188. Best Time to Buy and Sell Stock IV](Solutions/0188.Best-Time-to-Buy-and-Sell-Stock-IV.py) (H) <br>
Only k transactions are allowed.   Maintain buy=[]* k, sell=[]* k, and update them together in a for loop. buy[i] = min(buy[i], price - sell[i - 1]), buy[i] = the minimum money you can own after the ith purchase; sell[i] = max(sell[i], price - buy[i]), sell[i] = the maximum money you can earn after the ith purchase.  Solve the memory overflow problem: if k>prices.length/2, then it is the same as 122.
- [0801. Minimum Swaps To Make Sequences Increasing](Solutions/0801.Minimum-Swaps-To-Make-Sequences-Increasing.py) (M) <br>
与714. Best Time to Buy and Sell Stock with Transaction Fee 很像，都有交换和不交换两种情况
- [0226. Invert Binary Tree](Solutions/0226.Invert-Binary-Tree.py) (E) <br>
- [0017. Letter Combinations of a Phone Number](Solutions/0017.Letter-Combinations-of-a-Phone-Number.py) (!!M) <br>
经典的backtrack题，in dfs template, find solution: if currIdx == len(digits); for next_candidate in list_of_candidates: for ch in self.phone[digits[next_idx]];
- [0072. Edit Distance/Levenshtein distance](Solutions/0072.Edit-Distance.py) (!!H) <br>
f[i][j]=A前i个字符[0..i)和B前j个字符[0..j)的最小编辑距离; f[i][j]=min{case 1. f[i-1][j]+1 (f[i-1][j]表示A[0..i-1)就可以拼成B[0..j)了，所以A[0..i)要拼成B[0..j)需要删掉A[0..i)的最后一个字母); case 2. f[i][j-1]+1 (B[0..j)需要删掉最后一个字母，即A[0..i)的后面需要增加一个字母); case 3. f[i-1][j-1]+1 (A[0..i)的后面需要replace一个字母); case 4. f[i-1][j-1] (if A[i-1]=B[j-1] 就不需要任何操作直接就是了)}
- [1007. Minimum Domino Rotations For Equal Row](Solutions/1007.Minimum-Domino-Rotations-For-Equal-Row.py) (!!M) <br>
Try all possibilities from 1 to 6. If we can make number i in a whole row, it should satisfy that countA[i] + countB[i] - same[i] = n
- [0560. Subarray Sum Equals K](Solutions/0560.Subarray-Sum-Equals-K.py) (!!M Google) <br>
新建一个prefixSumDict = {0: 1}, key是prefixSum, val是how many times the prefixSum appears; if prefixSum - k in prefixSumDict: 等价于if prefixSum[j+1]-prefixSum[i] == k
- [0284. Peeking Iterator](Solutions/0284.Peeking-Iterator.py) (!!M) <br>
define a self.iterator, and a self.next_item to record the top item of the iterator, 相当于提前预支next_item.
- [0246. Strobogrammatic Number](Solutions/0246.Strobogrammatic-Number.py) (E) <br>
Two pointers. similar with 1056. Confusing Number.
- [0247. Strobogrammatic Number II](Solutions/0247.Strobogrammatic-Number-II.py) (!!M Google) <br>
Backtrack. find all combinations for n//2 lens, using backtrack.
- [0248. Strobogrammatic Number III](Solutions/0248.Strobogrammatic-Number-III.py) (H) <br>
解法：每次都按照一个lens做backtrack. 每次添加next_ch都在curr_comb前面和后面添加
backtrack end consition: if len(curr_comb) == lens, check if curr_comb in range(low, high)
constraints on next_candidates: next_comb = ch + curr_comb + mapping[ch], cannot have leading zero
arguments pass into backtrack function: curr_comb
- [0979. Distribute Coins in Binary Tree](Solutions/0979.Distribute-Coins-in-Binary-Tree.py) (!!M) <br> 
The algorithm is: one node by another, try to balance node from down to top.
helper function returns how many coins should the node receive from it's parent in order to balance itself.
用一个全局变量打擂台记录移动了多少个coins
- [0214. Shortest Palindrome](Solutions/0214.Shortest-Palindrome.py) (!!H Google) <br>
The problem really is to find the longest palindrome starts with s[0].
rabin carp / rolling hash O(N). The algorithm is for string s, left_code = the hash_code scan from left to right,
right_code = the hash_code scan from right to left. if left_code == right_code, then s is a palindrome.
- [0133. Clone Graph](Solutions/0133.Clone-Graph.py) (!!!M) <br>
用一个mapping 保存node-->node_copy. 然后一边dfs一边新建copied nodes 
- [0022. Generate Parentheses](Solutions/0022.Generate-Parentheses.py) (!!M)  <br>
Very similar with permutation problem. if leftCnt == n and rightCnt == n: self.res.append(curr) return; if leftCnt < rightCnt: return  # 这个判断尤为关键！
- [0132. Palindrome Partitioning II](Solutions/0132.Palindrome-Partitioning-II.py) (!!H) <br>
子数组或者子字符串且求极值的题，基本就是 DP 没差了. f[j]=the minimum number of total palindrome till the jth character (not including j); f[j]=min(f[i]+1) for i<j and s[i:j] is palindrome. O(N^3), 划分型的dp的状态一般都not include j, 这样就有一个buffer layer可以用。Solution 2: 优化为O(N^2), 用一个isPalin[i][j]记录s[i:j]是否是palindrome, 更新isPalin[i][j]的方法与leetcode 5 相同，这样就不用每次都用双指针去判断s[i:j]是不是palindrome. 这种预先计算好的思想非常重要，参看907. Sum of Subarray Minimums.  输出所有的可能的partition成palindrome的组合问题只能dfs+backtracking了- 131. Palindrome Partitioning
- [0041. First Missing Positive](Solutions/0041.First-Missing-Positive.py) (!!H) <br>
1st pass: change all negtive numbers to be 1, so that there will be no negtive numbers;  2nd pass: change the positive numbers into negative; 3rd pass: find the first positive number, and the corresponding idx is missing
- [0399. Evaluate Division](Solutions/0399.Evaluate-Division.py) (!!M) <br>
Solution 1: bfs 去做path compression; 注意这里构建图的时候采用hashmap构建邻接表 graph = collections.defaultdict(dict), in graph, key is node1, val is a dict of (key: node2, val: node1/node2), 然后每次query其实就是从单源节点出发寻求不带权值最短路径问题。  Soltution 2: DFS;
- [0048. Rotate Image](Solutions/0048.Rotate-Image.py) (!M) <br>
Step 1: 沿对角线swap; Step 2: 沿水平线swap
- [0050. Pow(x, n)](Solutions/0050.Pow(x,n).py) (M) <br>
recursion solution: half = self.myPow(x, n//2); if n%2 == 0: res = half * half; else: res = half * half * x
- [0036. Valid Sudoku](Solutions/0036.Valid-Sudoku.py) (M) <br>
use a row_dict to record each row, a col_dict to record each col; a block_dict to record each 3x3 block. block_id is (row // 3, col // 3)
- [0209. Minimum Size Subarray Sum](Solutions/0209.Minimum-Size-Subarray-Sum.py) (!!M) <br>
这题是第一种模板：find min subarray size for at least problem. 写法是while loop里让后面的指针逐渐远离前面的指针；
Can we solve in O(NlogN)? Yes, we can traverse the the list, say at i, we search the fisrt j that satisfy sum(nums[i:]>=s), so it is a OOXX probelm, which could be solved using binary search. Follow up: 如果有负数怎么办？那就不能用sliding window了, 只能用pre_sum / deque, 详见862.
- [0862. Shortest Subarray with Sum at Least K](Solutions/0862.Shorteast-Subarray-with-Sum-at-Least-K.py) (!!H) <br>
不能像209. Minimum Size Subarray Sum那样用sliding window因为209那题是positive numbers, 这题可以为负值。
这题的最优解是mono deque. O(N). 先构造一个presum list, 接下来方法与239类似的，
两个while循环，一个while loop do sliding window to update res, 从队首pop, 同时更新res, 
另一个while loop do monostack to maintain an increasing dq, 从队尾pop, 对deq进行清理。
- [0054. Spiral Matrix](Solutions/000054.Spiral-Matrix.py) (!!M) <br>
每一个转弯的点是dfs的node, dfs helper function 需要传入的参数有(min_row, max_row, min_col, max_col, curr_dir)
- [0095. Unique Binary Search Trees II](Solutions/0095.Unique-Binary-Search-Trees-II.py) (!!M) <br>
helper(start, end): return the trees from start to end.  Finally return helper(1, n). Time complexity: The main computations are to construct all possible trees with a given root, that is actually Catalan number Gn (超纲).
- [0096. Unique Binary Search Trees](Solutions/0096.Unique-Binary-Search-Trees.py) (!!M) <br>
solution 1: brutal force, same as 95, return len(helper(1, n)). If we defind dp[i] = how many trees possible in a range with width == i, then we have
dp[j] = sum for (dp[i] * dp[j - i - 1] for all i < j)
- [0131. Palindrome Partitioning](Solutions/0131.Palindrome-Partitioning.py) (!!!M) <br>
要求输出所有的可能组合，所以只能backtrack. O(L* 2^L), where L is the lens of string, 2 is two choices: 这这里分还是不分。  
如果题目只是要求输出所有可能组合的数目，那就dp - O(L^2)
- [0150. Evaluate Reverse Polish Notation](Solutions/0150.Evaluate-Reverse-Polish-Notation.py) (!!M) <br>
stack存num就可以了
- [0435. Non-overlapping Intervals](Solutions/0435.Non-overlapping-Intervals.py) (!!M) <br>
This is actually greedy algorithm: always pick the interval with the earliest end time. 
Step 1: sort the list based on the end time of the intervals, cuz we want to pick up the earliest end time.
step 2: maintain a min_end_time as we sweep over the intervals. each time, we compare the start time with the pointer.
if the current start time is larger than the pointer, then renew the pointer to be the new end time;
else then we will have to remove the current interval in order to to keep the end time as small as possible,  removed_cnt += 1
- [0430. Flatten a Multilevel Doubly Linked List](Solutions/0430.Flatten-a-Multilevel-Doubly-Linked-List.py) (!!M) <br>
递归即可，易错点是return head之前别忘了把head.child设置成None
- [0037. Sudoku Solver](Solutions/0037.Sudoku-Solver.py) (!!H) <br> 
use rows, cols, boxes dictionary to record the numbers in each row, each col and each small box, then do standard backtrack
- [0228. Summary Ranges](Solutions/0228.Summary-Ranges.py) (M) <br>
sliding window可解
- [0163. Missing Ranges](Solutions/0163.Missing-Ranges.py) (M) <br>
这题是上一题的延伸，跟sliding window没啥关系
- [0341. Flatten Nested List Iterator](Solutions/0341.Flatten-Nested-List-Iterator.py) (!!M) <br>
solution 1: 用一个辅助函数把nested_list flatten掉存到一个q中就可以了，用递归去flatten既可以了. Solution 2: use a q to partially flatten the list in hasnext function.
- [0136. Single Number](Solutions/0136.Single-Number.py) (!!E) <br>
Bitwise XOR is the most important in bit manipulation. 要牢记xor的三条定律: If we take XOR of zero and some bit, it will return that bit: a⊕0=a; If we take XOR of two same bits, it will return 0: a⊕a=0; Commutative law for XOR: a⊕b⊕a=(a⊕a)⊕b=0⊕b=b. So we can XOR all bits together to find the unique number.
- [0137. Single Number II](Solutions/0137.Single-Number-II.py) (M) <br>
A general solution for dealing with numbers with n-repeating time is to deal with bit by bit, and then take the mod of n.
- [0658. Find K Closest Elements](Solutions/0658.Find-K-Closest-Elements.py) (M) <br>
step 1: binary search to find the idx where x should be; step 2: put the closest k elements in a hq - O(klogk); step 3: output - O(klogk)
- [0159. Longest Substring with At Most Two Distinct Characters](Solutions/0159.Longest-Substring-with-At-Most-Two-Distinct-Characters.py) (M) <br>
Exactly the same as 340.
- [0904. Fruit Into Baskets](Solutions/0904.Fruit-Into-Baskets.py) (M) <br>
Exactly the same as 159.
- [0286. Walls and Gates](Solutions/0286.Walls-and-Gates.py) (M) <br>
求最小距离问题，必须用bfs. Step 1: append all the gates into the queue; Step 2: change all the EMPTY rooms to a value that equals the layer number, 必须层序遍历才可以保证每次都能变成最小距离
- [0622. Design Circular Queue](Solutions/0622.Design-Circular-Queue.py) (!!M) <br>
we can use a Singly-Linked List. 也可以用double-linked-list这把宰牛刀也非常快
enqueue: we append the value to the tail; dequeue: we remove node from head.
front: the head; rear: the tail; isempty: cnt=0; isFull: cnt = k
- [0403. Frog Jump](Solutions/0403.Frog-Jump.py) (H) <br>
维护一个stonesDict的key is the stone in stones. value is the possible steps to reach the stone.
There could be multiple possible steps to reach the stone, so stonesDict[stone] = set(). 
状态转移方程为：1. 跳k-1到stone+k-1: stonesDict[stone + k - 1].add(k - 1); 2. 跳k到stone + k: stonesDict[stone + k].add(k); 3. 跳k + 1到stone + k + 1:stonesDict[stone + k + 1].add(k + 1); Return stonesDict[last stone] is not empty; this is bottom up method O(N^2), O(N^2)
- [0279. Perfect Squares](Solutions/0279.Perfect-Squares.py) (!!M) <br>
f[j]=the least number of perfect square numbers which sum to i; f[j] = min(f[j-i^2]+1) for i^2<=j; Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5); solution 2: level order BFS.
Given a N-ary tree, where each node represents a __remainder__ of the number n subtracting a combination of square numbers, 
our task is to find a node in the tree, which should meet the conditions or remainder=0.
Time complexity: 比较复杂最后是 O(n^(h/2)), where h is the height of the N-ary tree, h is 0 to 4
- [0733. Flood Fill](Solutions/0733.Flood-Fill.py) (!!E) <br>
Solution 1: dfs recurssively, don't need a set to record visited nodes, cuz we can modify the matrix in place; Solution 2: bfs; Solution 3: dfs iteratively; Solution 4: Union Find; 
- [0849. Maximize Distance to Closest Person](Solutions/0849.Maximize-Distance-to-Closest-Person.py) (E) <br>
step 1: check what is the distace if he sits at two ends;
step 2: check what is the distance if he sits in the middle, two pinters: same method as 245. Shortest Word Distance III. warm up for next question.
- [0855. Exam Room](Solutions/0855.Exam-Room.py) (M) <br>
Use a sorted list to record the index of seats where people sit, so that we can save tons of space if the seats is sparse;
seat(): 1. find the biggest distance at the start, at the end and in the middle. 2. insert index of seat into the idx list. 3. return index.
leave(p): pop out p.
- [0134. Gas Station](Solutions/0134.Gas-Station.py) (!!M) <br>
Every time a fail happens, we start reset the gas_left to 0, and reset the possible_station. 
The problem has an assumption: if sum of gas is more than sum of cost, then there must be a solution. 
And the question guaranteed that the solution is unique(The first one I found is the right one).
- [0863. All Nodes Distance K in Binary Tree](Solutions/0863.All-Nodes-Distance-K-in-Binary-Tree.py) (M) <br>
step 1: use dfs, change a tree to a graph with adjacency list representation; 
step 2: start from target, use bfs/dfs to find the nodes with distance == K
- [1283. Find the Smallest Divisor Given a Threshold](Solutions/1283.Find-the-Smallest-Divisor-Given-a-Threshold.py) (M) <br>
minimum/maximum to satisfy some condition 的问题: helper function returns whether we can have sum(num//mid) <= threshold? start = 1, end = max(nums) + 1

## New

- [0169. Majority Element](Solutions/0169.Majority-Element.py) (!!E) <br>
Boyer-Moore Voting Algorithm - IO(N), O(1)
- [0229. Majority Element II](Solutions/0229.Majority-Element-II.py) (M) <br>
Boyer-Moore Voting Algorithm
- [1287. Element Appearing More Than 25% In Sorted Array](Solutions/1287.Element-Appearing-More-Than-25%-In-Sorted-Array.py) (!!E) <br>
想想如果我们需要求sorted arr 里 more than n//2 times的num, 只需要直接return arr[n//2]就可以了
同理我们可以求more than 25%的num.
step 1: 找出 n//4, 2n//4, 3n//4 位置处的num, 因为答案只可能存在于这三个位置上
step 2: 对这三个num分别做binary search求出first_pos and last_pos, 如果last_pos - first_pos >= n//4 就找到了
- [0853. Car Fleet](Solutions/0853.Car-Fleet.py) (!!M) <br>
算法：我的位置比你小，需要的时间还比你少，那说明我可以追上你
- [1483. Kth Ancestor of a Tree Node](Solutions/1483.Kth-Ancestor-of-a-Tree-Node.py) (H) <br>
just memo it. dfs + binary search, or binary lifting can realize O(logk) time for getKthAncester
- [1610. Maximum Number of Visible Points](Solutions/1610.Maximum-Number-of-Visible-Points.py) (H) <br>
step 1: calculate all the angles with respect to the location; step 2: sort the angles; step 3: find the max_subarray size with diff_of_max_and_min <= angle, using sliding window
- [1642. Furthest Building You Can Reach](Solutions/1642.Furthest-Building-You-Can-Reach.py) (H) <br>
solution 1: backtrack; solution 2: memorization; solution 3: greedy heapq - O(nlog(n))
- [0419. Battleships in a Board](Solutions/0419.Battleships-in-a-Board.py) (!!M) <br>
solution 1: unionfind. solutoin 2: O(1) space solution
whenever we meet a "X", we check if it is the top left corner of a battleship,
if it is cnt += 1
- [1101. The Earliest Moment When Everyone Become Friends](Solutions/1101.The-Earliest-Moment-When-Everyone-Become-Friends.py) (!!M) <br>
算法有点像MST, 首先sort by cost, 然后union one by one as we loop over the logs.
if uf.disjoint_cnt == 1, then that means all nodes are connected.
- [1329. Sort the Matrix Diagonally](Solutions/1329.Sort-the-Matrix-Diagonally.py) (M) <br>
just sort each diagonal - O(MNlog(min(M, N)))
- [817. Linked List Components](Solutions/0817.Linked-List-Components.py) (M) <br>
solution 1: 直接遍历linked list, 如果curr.val in nums_set and curr.next.val in nums_set, 那就disjoint_cnt -= 1. solution 2: union find
- [0397. Integer Replacement](Solutions/0397.Integer-Replacement.py) (!!M) <br>
similar with 991. Broken Calculator (bfs). backtrack with memo - O(n)
- [1553. Minimum Number of Days to Eat N Oranges](Solutions/1553.Minimum-Number-of-Days-to-Eat-N-Oranges.py) (!!H) <br>
solution 1: bfs - O(N), solution 2: backtrack with memo
- [1658. Minimum Operations to Reduce X to Zero](Solutions/1658.Minimum-Operations-to-Reduce-X-to-Zero.py) (!!M) <br>
这题是从两端找 the fewest number added to x. 
换个角度就是找 the longest subarry that sum up to sum(nums) - x.
由于nums are all positive, sliding window即可 - O(N)
- [1697. Checking Existence of Edge Length Limited Paths](Solutions/1697.Checking-Existence-of-Edge-Length-Limited-Paths.py) (H) <br>
loop over the queries, each query is a dijkstra's to find min_max problem. O(QVlogV), Q is how many queries are there, V is how many nodes are there.
- [1616. Split Two Strings to Make Palindrome](Solutions/1616.Split-Two-Strings-to-Make-Palindrome.py) (H) <br>
pre-calculation: O(N)
- [0913. Cat and Mouse](Solutions/0913.Cat-and-Mouse.py) (H) <br>
dp + bfs
- [1576. Replace All ?'s to Avoid Consecutive Repeating Characters](Solutions/1576.Replace-All-?-s-to-Avoid -Consecutive-Repeating-Characters.py) (E) <br>
just choose to replace "?" to be one of "abc"



### Jeff Jeff Erickson's Algorithms https://jeffe.cs.illinois.edu/teaching/algorithms/
