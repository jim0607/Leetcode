好好学C#，因为学会了C#就等于学会了JAVA了


List basics:
1. 新建一个list: int[] dp = new int[n];     // n为size
2. 最大值：a = int.MaxValue; 注意在C#中, int.MaxValue + 1 会变成 int.MinValue
3. 取两数最小值: minVal = Math.Min(a, b);
4. 取list中的最大值: maxVal = someList.Max();
    
    
    
运算符：
逻辑与：&&


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
 - 新建一个Queue: Queue <int> q = new Queue <int> ();
 - q.Equeue(val) (相当于q.append(val));  q.Dequeu() (相当于q.pop());   q.Count() (相当于len(q))
     
     
