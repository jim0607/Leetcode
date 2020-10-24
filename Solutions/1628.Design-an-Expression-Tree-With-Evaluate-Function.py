"""
1628. Design an Expression Tree With Evaluate Function

Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. 
For example, the postfix tokens of the expression 4*(5-(2+7)) are represented in the array postfix = ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. 
The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. 
You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. 
Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, 
is your design able to support additional operators without making changes to your existing evaluate implementation?

Example 1:

Input: s = ["3","4","+","2","*","7","/"]
Output: 2
Explanation: this expression evaluates to the above binary tree with expression ((3+4)*2)/7) = 14/7 = 2.
Example 2:

Input: s = ["4","5","7","2","+","-","*"]
Output: -16
Explanation: this expression evaluates to the above binary tree with expression 4*(5-(2+7)) = 4*(-4) = -16.
Example 3:

Input: s = ["4","2","+","3","5","1","-","*","+"]
Output: 18
Example 4:

Input: s = ["100","200","+","2","/","5","*","7","+"]
Output: 757
 
Constraints:

1 <= s.length < 100
s.length is odd.
s consists of numbers and the characters '+', '-', '*', and '/'.
If s[i] is a number, its integer representation is no more than 105.
It is guaranteed that s is a valid expression.
The absolute value of the result and intermediate values will not exceed 109.
It is guaranteed that no expression will include division by zero.
"""

"""
With careful obervation, we'll see the operator tree node cannot be leaf, and the number tree node can only be leaf. 
With that, we can easily implement:
In building a tree, we can use a stack to store the operator tree nodes.
In evaluate the result, we just do divide and conquer.
"""
import abc 
from abc import ABC, abstractmethod 

class Node(ABC):
   
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

    
class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        
        if self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        if self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        if self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        if self.val == "/":
            return self.left.evaluate() // self.right.evaluate()
        

class TreeBuilder(object):
    def buildTree(self, s: List[str]) -> 'Node':
        s.reverse()                 # ['/', '7', '*', '2', '+', '4', '3']
        root = TreeNode(s[0])
        st = [root]
        for ch in s[1:]:
            node = TreeNode(ch)
            while len(st) > 0 and st[-1].left and st[-1].right:   # 找到第一个空着的operator node去append
                st.pop()
            if len(st) > 0 and not st[-1].right:    # we append right node first cuz the given list is post order traversal
                st[-1].right = node
            elif len(st) > 0 and not st[-1].left:
                st[-1].left = node
            
            if ch in "+-*/":   # we only append opt node into st, cuz number nodes can only be leaf, and opt node cannot be leaf
                st.append(node)

        return root
                
            
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        
