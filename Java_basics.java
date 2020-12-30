**** 不要用java刷算法，可以用java刷OOD, 需要知道java的特性做OOP ****


List basics:
0. 要声明data type, 要声明data type, 要声明data type: int firstMinCostPos = -1; int secondMinCostPos = -1;
1. 新建一个list: int[] dp = new int[n];  /* n为size */   或者   int arr[] = {12,23,44,56,78};
2. 最大值：a = Integer.MAX_VALUE;  Note that in Java, Integer.MAX_VALUE + 1 == Integer.MIN_VALUE; Integer.MIN_VALUE - 1 = Integer.MAX_VALUE;
3. 取两数最小值: minVal = Math.min(a, b); java 中Math.min 方法只能比较两个值，超过两个会报错。可以用Math.min(a, Math.min(b, c))比较三个数。
4. 取list中的最大值: maxVal = someList.max(); ??
5. 取list的长度: someList.length, 相当于python中的len(someList)
6. a good exmaple
        int m = matrix.length, n = m > 0 ? matrix[0].length : 0;       // 注意点: 1. 声明data type is int; 2. m 与 n之间用 , 隔开
        int[][] dp = new int[m][n];                                    // 3. 声明 data type in the 2D array is int
        for (int i = 0; i < m; i++) {                                  // 4. 声明 data type of i is int
            for (int j = 0; j < n; j++) {
            }
        } 
7. for each loop in Java:
   for (int coin : coins) {          // 相当于python中的for coin in coins
   }
8. Java中写dp[-1]会报错"Index -1 out of bound",
9. listA.add(item); listA.add(pos, item) 不行，// 注意heights.add(-1) 是不行的，在java中arr的size是不能改变的。 
10. return minLens == Integer.MAX_VALUE ? 0 : minLens;
        


Set:
1. Set is an interface which extends Collection. It is an unordered collection of objects in which duplicate values cannot be stored. 
   Basically, Set is implemented by HashSet, LinkedHashSet or TreeSet (sorted representation).
2. 新建一个 set: Set setA = new HashSet();  Set<Integer> setB = new HashSet<Interger>();
   setA.add(element);  setA.remove(element);  setA.size(); 
   setA.contains(element);
    



HashMap:
1. 新建一个HashMap: HashMap<Integer, Set<Integer>> dpMap = new HashMap<>();  // key is integer, val is a set
2. 加入一个(key, val) pair 进入HashMap: dpMap.put(key, val);
    for (int stone : stones) {
        dpMap.put(stone, new HashSet<Integer>());
    }
3. 从HashMap中提取出某个key对应的val: dpMap.get(key);   在python中可以直接用dpMap[key]
4. 判断一个someKey是否在map里面：dpMap.containsKey(someKey)
5. Get val from a key: map.get(someKey)
6. dpMap.size();




String:
1. In java, '' and "" are different. 'a' is a char, "b" is a string. 
   if ('a' == "b") 会报错, Should always take care of that.
2. lens = s.length()   // 注意与 list 不同
3. char ch1 = s.charAt(idx)
    
    
   
Stack:
private Stack<TreeNode> st = new Stack<TreeNode>();  // create a new stack as a golbal variable in the class, elements in the stack are TreeNode  
st.push(item); st.pop(); st.getSize(); st.isEmpty(); st.peek();        
           
           

           
运算符：
&& : Conditional And, Same as &, but if the operand on the left returns false, it returns false without evaluating the operand on the right.
|| : Conditional Or, Same as |, but if the operand on the left returns true, it returns true without evaluating the operand on theright.
divide: int 6 / 4 returns 1; double 6 / 4 returns 1.5; 





条件判断：
if () {
} else if () {
} else {
}

Another easy format: if (lens == 0) return 0;


print:
System.out.println(Arrays.toString(dp));
