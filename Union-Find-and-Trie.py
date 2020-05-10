Union find是一种用来解决集合查询合并的数据结构, 又叫 Disjoint Se
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
        
    def add(self, x):     # 有时候需要add 一个数组到graph里面，这时候就在__init__里面完成就可以了。
        """
        add x into the graph
        """
        self.father[x] = x
        
    def find(self, x):    # 用递归实现
        """
        find the root of x, by using path compression, which flattened the path
        """
        if self.father[x] == x:
            return x
            
        self.father[x] = self.find(self.father[x])    # Path compression, speeding up future operations for not only this element, but also all the father elements.
        
        return self.father[x]
  
    def union(self, a, b):
        """
        union a and b
        """
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b      # 注意这里顺序没关系，但是千万不要写成了root_b = self.father[root_a], 这样赋值顺序完全不对。



  
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
  
Path compression:
Path compression is a way of flattening the structure of the tree whenever Find is used on it. 
Since each element visited on the way to a root is part of the same set, all of these visited elements can be reattached directly to the root. 
The resulting tree is much flatter, speeding up future operations not only on these elements, but also on those referencing them.
  
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
  
  
一定要会默写 Implement a Trie:
  
# Before implement a trie, we should firstly define a trieNode class.  
# This is similar with tree, before implement a tree, we should firstly define a treeNode class
# a treeNode class has 3 properties: treeNode.left, treeNode.right, treeNode.val
# a trieNode class has 2 preperties: trieNode.child, trieNode.isEnd
class TrieNode:     
    def __init__(self):
        """
        A TrieNode has two properties:
        1. child, which represents the children of the TrieNode, all the children are stored in a dictionary
        2. isEnd, which represents whether or not the TrieNode is the end of a word
        """
        
        # use a defaultdict to represent a TrieNode, there could be multiple key-value pairs in a TrieNode
        # key is one of the children' char, value is TrieNode corresponding to the char
  
        self.child = collections.defaultdict(TrieNode)    
        self.isEnd = False        # return True if the self node is the end of the Trie


class Trie:
    def __init__(self):
        self.root = TrieNode()       # at the beginning, we should create a dummy root as a new TrieNode 

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for char in word:           # O(m), where m is the word length
            currNode = currNode.child[char]   # 把 char 放入 curr.child dictionary 中作为 众多 key 中的一个, 然后 currNode 往下遍历, 
                                              # 记住往下遍历 node 都是 currNode = currNode.child[char]
            
        currNode.isEnd = True        # 不要忘了标记 最后一个 node 为 isEnd

    def search(self, word: str) -> bool:
        """
        Return whether or not the word is in the trie.
        """
        currNode = self.root
        for char in word:             # O(m), where m is the word length
            if char not in currNode.child:
                return False
            
            currNode = currNode.child[char]
            
        return currNode.isEnd

    def startsWith(self, prefix: str) -> bool:      # exactly the same as search mehotd except for the reaturn
        """
        Return whether there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for char in prefix:     # O(m), where m is the prefix length
            if char not in currNode.child:
                return False
            currNode = currNode.child[char]
            
        return True
  
  
  
  
  
  
  
  
  
  
  
  
