Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
Let's take the following BST as an example, it may help you understand the problem better:

 
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.
The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.


https://www.cnblogs.com/grandyang/p/9615871.html
这道题给了一个二叉搜索树，让我们将其转化为双向链表。并且题目中给了一个带图的例子，帮助理解。题目本身并不难理解，仔细观察下给的示例图。
首先，转化成双向链表的每个结点都有 left 和 right 指针指向左右两个结点，不管其原来是否是叶结点还是根结点，转换后统统没有区别。
其次，这是个循环双向链表，即首尾结点是相连的，原先的二叉搜索树中的最左结点和最右结点，现在也互相连接起来了。
最后，返回的结点不再是原二叉搜索树的根结点 root 了，而是最左结点，即最小值结点。
好，发现了上述规律后，来考虑如何破题。根据博主多年经验，跟二叉搜索树有关的题，肯定要利用其性质，即左<根<右，即左子结点值小于根结点值小于右子结点值。
而且十有八九都得用中序遍历来解，因为中序遍历的顺序就是左根右啊，跟性质吻合。观察到原二叉搜索树中结点4连接着结点2和结点5，而在双向链表中，连接的是结点3和结点5，这就是为啥要用中序遍历了，因为只有中序遍历，结点3之后才会遍历到结点4，这时候可以将结点3和结点4串起来。
决定了用中序遍历之后，就要考虑是迭代还是递归的写法，博主建议写递归的，一般写起来都比较简洁，而且递归是解树类问题的神器啊，十有八九都是用递归，一定要熟练掌握。
再写中序遍历之前，其实还有难点，因为需要把相邻的结点连接起来，所以需要知道上一个遍历到的结点是什么，所以用一个变量 pre，来记录上一个遍历到的结点。
还需要一个变量 head，来记录最左结点，这样的话，在递归函数中，先判空，之后对左子结点调用递归，这样会先一直递归到最左结点，此时如果 head 为空的话，说明当前就是最左结点，赋值给 head 和 pre，对于之后的遍历到的结点，那么可以和 pre 相互连接上，然后 pre 赋值为当前结点 node，再对右子结点调用递归即可，参见代码如下：

"""https://www.cnblogs.com/grandyang/p/9615871.html
这道题给了一个二叉搜索树，让我们将其转化为双向链表。并且题目中给了一个带图的例子，帮助理解。题目本身并不难理解，仔细观察下给的示例图。
首先，转化成双向链表的每个结点都有 left 和 right 指针指向左右两个结点，不管其原来是否是叶结点还是根结点，转换后统统没有区别。
其次，这是个循环双向链表，即首尾结点是相连的，原先的二叉搜索树中的最左结点和最右结点，现在也互相连接起来了。
最后，返回的结点不再是原二叉搜索树的根结点 root 了，而是最左结点，即最小值结点。
好，发现了上述规律后，来考虑如何破题。根据博主多年经验，跟二叉搜索树有关的题，肯定要利用其性质，即左<根<右，即左子结点值小于根结点值小于右子结点值。
而且十有八九都得用中序遍历来解，因为中序遍历的顺序就是左根右啊，跟性质吻合。观察到原二叉搜索树中结点4连接着结点2和结点5，而在双向链表中，连接的是结点3和结点5，这就是为啥要用中序遍历了，因为只有中序遍历，结点3之后才会遍历到结点4，这时候可以将结点3和结点4串起来。
决定了用中序遍历之后，就要考虑是迭代还是递归的写法，博主建议写递归的，一般写起来都比较简洁，而且递归是解树类问题的神器啊，十有八九都是用递归，一定要熟练掌握。
再写中序遍历之前，其实还有难点，因为需要把相邻的结点连接起来，所以需要知道上一个遍历到的结点是什么，所以用一个变量 last，来记录上一个遍历到的结点。
还需要一个变量 first，来记录最左结点，这样的话，在递归函数中，先判空，之后对左子结点调用递归，这样会先一直递归到最左结点，此时如果 first 为空的话，说明当前就是最左结点，赋值给 first，对于之后的遍历到的结点，那么可以和 last 相互连接上，然后 last 赋值为当前结点 node，再对右子结点调用递归即可，参见代码如下：
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # the smallest (first) and the largest (last) nodes
        global first, last
        first, last = None, None
        self.inOrder(root)
        # close DLL
        last.right = first
        first.left = last
        return first
        
    def inOrder(self, node):
        """
        Performs standard inorder traversal: left -> node -> right
        and links all nodes into DLL
        """
        global last, first
        if not node:
            return
        # 1. left
        self.inOrder(node.left)  # 对左子结点调用递归，这样会先一直递归到最左结点
        # 2. node 
        if not first:
            # 此时如果 first 为空的话，说明当前就是最左结点，赋值给 first
            first = node
            last = node
        else:
            # keep the smallest node to close DLL later on
            last.right = node        
            node.left = last
        last = node  # 可能意思是连接上之后往前遍历吧
        # 3. right
        self.inOrder(node.right)
        
        
"""解法二：divide and conquer, somehow don't know how to make it work..........."""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        return self.helper(root)
       
    # 1. 递归的定义：return 以root为根节点的BST的DLL(的head)    
    def helper(self, root):
        """
        return DLL of a BST
        """
        # 2. 递归的出口
        if not root:
            return
        
        # 3. 递归的拆解：divide
        leftDLL_head = self.helper(root.left)
        rightDLL_head = self.helper(root.right)
        
        # 递归的拆解：conquer
        if leftDLL_head:
            # the last node on the left is the leftDLL_head.left
            last_left = leftDLL_head.left
            # 左边是3-4-5，右边是7-8-9，先把3-4-5-root连起来
            last_left.right = root
            root.left = last_left.right
            
        if rightDLL_head:
            last_right = rightDLL_head.left
            # 再把root-7-8-9连起来
            rightDLL_head.left = root
            root.right = rightDLL_head

        # 再把3-9连起来形成环
        if leftDLL_head and last_right:
            leftDLL_head.right = last_right
            last_right.left = leftDLL_head
        
        return leftDLL_head






