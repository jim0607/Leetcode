431. Encode N-ary Tree to Binary Tree

Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See following example).

For example, you may encode the following 3-ary tree to a binary tree in this way:

Input: root = [1,null,3,2,4,null,5,6]
Note that the above is just an example which might or might not work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.



"""
The left child of a binary node is the subtree encoding all the children of the corresponding n-ary node.
The right child of a binary node is a chain of the binary root nodes encoding each sibling of the n-ary node.
Step 1). Link all siblings together, like a singly-linked list.
Step 2). Link the head of the obtained list of siblings with its parent node.
The solution explained it quite well.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

"""
把n-ary tree encode成一个binary tree:
n-ary的第一个child作为binary tree的左节点，后面同一层所有的child(又叫sibling)作为这个左节点的右子树。
          1                                  1
       /  |  \                              /   
      3   2   4          ----->            3    
     / \  |    \                          /  \
    5   6 7     8                        5    2 
                                          \    \
                                           6    4
                                            \
                                             7
                                              \
                                               8
"""
class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, n_root: 'Node') -> TreeNode:
        if not n_root:
            return None
        
        b_root = TreeNode(n_root.val)
        if not n_root.children:
            return b_root
        
        q = collections.deque()
        q.append((n_root, b_root))                      # append的是n_treeNode对应的b_TreeNode pair
        while q:
            n_curr, b_curr = q.popleft()
            b_child_head, b_child_prev = None, None
            for n_child in n_curr.children:
                b_child_new = TreeNode(n_child.val)       # 注意要create a TreeNode
                
                if not b_child_prev:
                    b_child_prev = b_child_new
                    b_child_head = b_child_new
                else:
                    b_child_prev.right = b_child_new    # hook up all siblings together, like a linked list
                    b_child_prev = b_child_new
                    
                q.append((n_child, b_child_new))          # append的是n_treeNode对应的b_TreeNode pair
                
            b_curr.left = b_child_head                  # hook up the head of the linked list with it's parent
            
        return b_root
            
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, b_root: TreeNode) -> 'Node':
        if not b_root:
            return None
        
        n_root = Node(b_root.val, [])                   # should set the default value to [] rather than None
        if not b_root.left and not b_root.right:
            return n_root
        
        q = collections.deque()
        q.append((b_root, n_root))
        while q:
            b_curr, n_curr = q.popleft()
            sibling = b_curr.left
            while sibling:
                n_child_new = Node(sibling.val, [])
                n_curr.children.append(n_child_new)     
                q.append((sibling, n_child_new))        # append的是b_TreeNode对应的n_treeNode pair
                sibling = sibling.right                 # go all hte way right to find all the siblings
                
        return n_root
        
        
        
"""
Solution 2: dfs
"""
class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, n_root: 'Node') -> TreeNode:
        if not n_root:
            return None
        
        b_root = TreeNode(n_root.val)
        if not n_root.children:
            return b_root
        
        b_root.left = self.encode(n_root.children[0])      # the left of b_root is the fisrt child of n_root, 注意在这里容易忘掉去递归调用encode函数
        b_curr = b_root.left
        for n_child in n_root.children[1:]:
            b_curr.right = self.encode(n_child)
            b_curr = b_curr.right
            
        return b_root
	
    # Decodes your binary tree to an n-ary tree.
    def decode(self, b_root: TreeNode) -> 'Node':
        if not b_root:
            return None
        
        n_root = Node(b_root.val, [])
        if not b_root.left and not b_root.right:
            return n_root
        
        node = b_root.left
        while node:
            n_root.children.append(self.decode(node))
            node = node.right
            
        return n_root
