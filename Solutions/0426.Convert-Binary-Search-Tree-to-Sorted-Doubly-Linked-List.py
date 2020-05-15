Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
Let's take the following BST as an example, it may help you understand the problem better:

 
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.
The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

"""solution 1: recursion"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        self.head, self.curr = None, None   # 定义两个全局变量head和curr，head记录最小的节点，curr一直往后遍历到最大的节点
        self.inOrder(root)
        
        # 将最小节点和最大节点hook up起来，完成闭环
        self.head.left = self.curr
        self.curr.right = self.head
        
        return self.head
    
    def inOrder(self, root):
        """in order traversal the tree without return, update the DLL"""
        if not root:
            return
        
        # 中序遍历，先遍历左边
        self.inOrder(root.left)
        
        # 中序遍历，遍历中间，在这里update DLL
        if not self.head:
            # 此时如果 first 为空的话，说明当前就是最左结点，赋值给 first
            self.head = root
            self.curr = root
            
        else:
            # curr 代表相邻两个节点中靠前的节点，root代表靠后的节点，将两个节点hook up起来即可
            self.curr.right = root
            root.left = self.curr
            self.curr = root    # curr 往前遍历
        
        # 中序遍历，遍历右边
        self.inOrder(root.right)
        
        
"""解法二：divide and conquer, somehow don't know how to make it work..........."""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root
        
        if not root.left:
            root.right.left = root
            return root
            
        if not root.right:
            root.left.right = root
            return root.left
        
        leftDLLHead = self.treeToDoublyList(root.left)
        rightDLLHead = self.treeToDoublyList(root.right)
        
        if leftDLLHead:
            leftDLLTail = leftDLLHead.left
            if leftDLLTail:
                leftDLLTail.right = root
                root.left = leftDLLTail
        
        if rightDLLHead:
            rightDLLTail = rightDLLHead.left
            rightDLLHead.left = root
            root.right = rightDLLHead
            
        if leftDLLHead and rightDLLHead:
            leftDLLHead.left = rightDLLTail
            rightDLLTail.right = leftDLLHead
        
        return leftDLLHead
