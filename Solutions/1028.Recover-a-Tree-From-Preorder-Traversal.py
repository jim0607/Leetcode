1028. Recover a Tree From Preorder Traversal

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  
(If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

Example 1:
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
 
Example 2:
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]


class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        # step 1: put (depth, node_val) in a list
        lst = []
        i = 0
        while i < len(s):
            depth = 0
            while i < len(s) and s[i] == "-":
                i += 1
                depth += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = 10 * num + int(s[i])
                i += 1
            lst.append((depth, num))
            
        # step 2: construct the tree using the lst
        def construct(depth, lst):
            """
            Return the root of the constructed tree
            """
            if len(lst) == 0 or depth > lst[0][0]:   # 这里是解决问题的题眼，depth是当前depth的信息，nodes[0][0]是下一个node的depth信息
                return None                          # eg: "1-2--3-5--6--7", 遍历到node 3时，发现下一个node 5的depth更小了，这说明node 5不适合放在3的下面
                                                     # 也就是1-->2-->3这个dfs path不能继续了(即2不能再放right node了), 所以就要return None
            depth, val = lst.pop(0)   
            root = TreeNode(val)
            
            root.left = construct(depth + 1, lst)
            root.right = construct(depth + 1, lst)
            
            return root
            
        return construct(0, lst)
    
""" 
注意不能用dictionary 来存， dictionary解法过不了case "1-2--3-5--6--7", 错误把6当做2的right node了
这是因为node 6所在的位置信息没有放到depth_to_nodes里面去
since we need the position information of node 6, and dictionary doesnot maitain the position order. dictionary存入Key之后会被自动打乱顺序。
"""

"""
用deque会更快一些！
"""
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # step 1: construct the nodes
        nodes = collections.deque()     # use a deque so that popleft is faster
        i = 0
        while i < len(S):
            j = i
            while j < len(S) and S[j] == "-":
                j += 1
            depth = j - i
            
            k = j
            while k < len(S) and S[k].isdigit():
                k += 1
            val = int(S[j:k])
            
            nodes.append((depth, val))
            i = k

        # step 2: do dfs to construct the tree
        return self._dfs(0, nodes)
        
    def _dfs(self, depth, nodes):
        if not nodes or depth > nodes[0][0]:  # 这里是解决问题的题眼，depth是当前depth的信息，nodes[0][0]是下一个node的depth信息
            return None                       # eg: "1-2--3-5--6--7", 遍历到node 3时，发现下一个node 5的depth更小了，这说明node 5不适合放在3的下面
                                              # 也就是1-->2-->3这个dfs path不能继续了(即2不能再放right node了), 所以就要return None
        root = TreeNode(nodes.popleft()[1])
        root.left = self._dfs(depth+1, nodes)
        root.right = self._dfs(depth+1, nodes)
        
        return root
