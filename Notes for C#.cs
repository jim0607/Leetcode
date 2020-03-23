1. 定义一个新的class的方法：
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


2. Dictionary:
 - 新建一个Dictionary, key是int, value是一个DLLNode: Dictionary<int, DLLNode> dict = new Dictionary<int, DLLNode>();
 - check if key is in a dicitonary: dict.ContainsKey(key)
 - size of dictionary: dict.Count() (相当于len(dict))
 - remove a (key, value) pair in dictionary: dict.Remove(key);
 
 
 3. Queue:
 - 新建一个Queue: Queue <int> q = new Queue <int> ();
 - q.Equeue(val) (相当于q.append(val));  q.Dequeu() (相当于q.pop());   q.Count() (相当于len(q))
