用java刷题吧，因为面试需要用java写code，再结合C#里学到的OOP的知识就可以应付面试了。
而且java真的比python快好多呀！


List basics:
0. 要声明data type, 要声明data type, 要声明data type: int firstMinCostPos = -1; int secondMinCostPos = -1;
1. 新建一个list: int[] dp = new int[n];  /* n为size */   或者   int arr[] = {12,23,44,56,78};
2. 最大值：a = Integer.MAX_VALUE;  Note that in Java, Integer.MAX_VALUE + 1 == Integer.MIN_VALUE; Integer.MIN_VALUE - 1 = Integer.MAX_VALUE;
3. 取两数最小值: minVal = Math.min(a, b); java 中Math.min 方法只能比较两个值，超过两个会报错。
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
4. dpMap.containsKey(someKey)
5. dpMap.size();




String:
1. In java, '' and "" are different. 'a' is a char, "b" is a string. 
   if ('a' == "b") 会报错, Should always take care of that.
    
    
    
运算符：
&& : Conditional And, Same as &, but if the operand on the left returns false, it returns false without evaluating the operand on the right.
|| : Conditional Or, Same as |, but if the operand on the left returns true, it returns true without evaluating the operand on theright.

    
    

定义一个新的class的方法：
// eg: 定义一个class DLLNode, 带有四个properties
public class DLLNode {
    public int key;       // 四个 property 要提前列出来
    public int val;
    public DLLNode prev;
    public DLLNode next;

    public DLLNode(int key, int value) {    // 相当于 def __init__(key, value)
        this.key = key;                     // 相当于self.key = key
        this.val = value;
        this.prev = null;
        this.next = null;
    }
}


Dictionary:
 - 新建一个Dictionary, key是int, value是一个DLLNode: Dictionary<int, DLLNode> dict = new Dictionary<int, DLLNode>();
 - check if key is in a dicitonary: dict.ContainsKey(key)
 - size of dictionary: dict.Count() (相当于len(dict))
 - remove a (key, value) pair in dictionary: dict.Remove(key);


Queue:
 - 新建一个Queue: Queue<int> q = new Queue<int>();
 - q.Equeue(val) (相当于q.append(val));  q.Dequeu() (相当于q.pop());   q.Count() (相当于len(q))
     
