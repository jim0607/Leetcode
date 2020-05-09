Union find是一种用来解决集合查询合并的数据结构
Union-Find 算法（中文称并查集算法）是解决动态连通性（Dynamic Conectivity）问题的一种算法
支持O(1) find and O(1) union
本质上是一个hash map表示数据之间的对应关系。
操作：
find(A), 找到点A所在的集合
union(A, D), 合并点A和点D所在的集合

要会用两行多列的方式画出并查集
  1 2 3 4 5
  2 2 2 4 4
表示有5个点1,2,3,4,5; 1,2,3分别指向2; 4,5分别指向4
  
  
  
union-find 模板: 遇到题目直接套用这个模板就可以了

Python version:

class UnionFind:
    def __init__(self):
        self.father = {}  # 用dictionary来实现可以更快查询
        self.cnt = 0      # cnt is the total number of all 集合in the graph
        
    def add(self, x):
        """
        add x into the graph
        """
        self.father[x] = x
        self.cnt += 1
        
    def find(self, x):    # 用递归实现
        if self.father[x] == x:
            return x
            
        self.father[x] = self.find(self.father[x])
        
        return self.father[x]
  
    def union(self, a, b):
        """
        union a and b
        """
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1

  
  
  
  
  
  
实现find(A): 路径压缩方法：
step 1: 遍历找到老大哥
step 2: 把沿路的每个点直接指向老大哥
这样以后每个点找老大哥都可以用O(1)
int find(int x) {
    if (father[x] == x) {
        return x;
    }
    father[x] = find(father[x]);    # 这里采用了路径压缩，把沿路每个点都指向老大哥。注意正因如此这个递归是不会stack over flow的，因为不会形成长链。
    return father[x];

知识点：递归算法的stack overflow是指在递归的时候会分配1M的栈空间，用来存储递归过程中的数，知道达到递归结束条件就FILO依次输出各个数，
        如果存储的数很多了还没找到递归结束条件的话，就会stack overflow
  
实现union(A, B): 
找到A和B的root, 然后root_a指向root_b即可
public void union(int a, int b) {     
    root_a = find(a);
    root_b = find(b);
    if (root_a != root_b) {
        father[root_a] = root_b;    // 注意这里谁是谁的father都没关系，目的只是连起来。
    }
}
并查集的原生操作：
  - 查询两个元素是否在同一个集合内 589
  - 合并两个元素所在的集合
  
并查集的派生操作：
  - 查询某个元素所在集合的元素个数 590
  - 查询图中集合的个数 591
  

  
Java template:
  
public class UnionFind {
    private int[] father = null;
  
    public int find(int x) {
        if (father[x] == x) {
            return x;
        }
        father[x] = find(father[x]);
        return father[x];

    public void union(int a, int b) {
        root_a = find(a);
        root_b = find(b);
        if (root_a != root_b) {
            father[root_a] = root_b;
        }
    }
}

  
  
  
  
Trie (Prefix Tree)
考点：
1. 实现Trie (一定要会默写)
2. 利用Trie的前缀特性直接解题
3. 矩阵类里面，字符串里面一个一个字符，深度优先dfs遍历的问题，优势在于可以快速找到满足前缀的字符串
  
Trie实现的功能：leetcode 208 is a good tutorial for Trie
  - insert (word): insert a word into the trie
  - search (word): return whether a word is in the trie
  - startWith (prefix): Returns if there is any word in the trie that starts with the given prefix
  
什么问题想到需要用Trie:
  - 非常适合查找处理前缀相关的问题
  - 一个字母一个字母遍历的问题
  - 需要节约空间，比hashmap更节约空间
  
  
工业界的Trie的应用：在search的时候有一个术语叫 Type head. 就是当输入一半内容的时候，后面直接自动联想填充进去 auto completion，
  这里就用到了Trie的startWith的功能
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
