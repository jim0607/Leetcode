"""
1597. Build Binary Expression Tree From Infix Expression

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. 
Each node of a binary expression tree has either zero or two children. 
Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) 
correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents is (A o B), 
where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, 
and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.

Example 1:

Input: s = "2-3/(5*2)+1"
Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. 
The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s:

The third tree below however is not valid. Although it produces the same result and is equivalent to the above trees, 
its inorder traversal doesn't produce s and its operands are not in the same order as s.

Example 2:

Input: s = "3*4-2*5"
Output: [-,*,*,3,4,2,5]
Explanation: The tree above is the only valid tree whose inorder traversal produces s.
Example 3:

Input: s = "1+2+3+4+5"
Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.
 
Constraints:

1 <= s.length <= 105
s consists of digits and the characters '+', '-', '*', '/', '(', and ')'.
Operands in s are exactly 1 digit.
It is guaranteed that s is a valid expression.
"""



"""
Divide and conquer - O(NlogN) in best case, O(N^2) in worst case.
"""
class Solution:
    def expTree(self, s: str) -> 'Node':
        def build_tree(start, end):
            """
            build the tree using in order traversal, return the root of the built tree
            """
            if start == end:
                return Node(arr[start])

            pm_idx = find_first_idx_ouside_prth(start, end, "+-")     # find the first "+-" outside prth - O(N)           
            if pm_idx != -1:            # 如果括号外有"+-", 优先把括号外的"+-"作为root
                root = Node(arr[pm_idx])
                root.left = build_tree(start, pm_idx - 1)
                root.right = build_tree(pm_idx + 1, end)
                return root
            
            td_idx = find_first_idx_ouside_prth(start, end, "*/")     # find the first "*/" outside prth
            if td_idx != -1:          # 如果括号外没有"+-", 把括号外的"*/"作为root
                root = Node(arr[td_idx])
                root.left = build_tree(start, td_idx - 1)
                root.right = build_tree(td_idx + 1, end)
                return root
            
            # 如果括号外没有"+-*/", 就说明只剩下括号里面的运算了，eg: "(5*3+4)", 就处理括号里面了
            return build_tree(start + 1, end - 1)

        def find_first_idx_ouside_prth(start, end, opt):
            """
            find the first appearance of the ch in s that is outsie parentheses
            """
            open_cnt = 0        # 记录当前open_parentheses的个数
            for i in range(start, end + 1):
                if arr[i] in opt and open_cnt == 0:
                    return i
                if arr[i] == "(":
                    open_cnt += 1
                elif arr[i] == ")":
                    open_cnt -= 1
            return -1 
    
    
        # firstly, "2-100/(23-3)+1" --> ['2', '-', '100', '/', '(', '23', '-', '3', ')', '+', '1']
        arr = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ord(s[i]) - ord("0")
                while i + 1 < len(s) and s[i+1].isdigit():
                    num = 10 * num + ord(s[i+1]) - ord("0")
                    i += 1
                arr.append(str(num))
            else:
                arr.append(s[i])
            i += 1
            
        # secondly, use recurssive way to build the tree
        return build_tree(0, len(arr) - 1)
