1028. Recover a Tree From Preorder Traversal

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

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



"""
use a dict to store the node_val and node_depth. dict[depth]=list of nodes.
Then construct the tree using dfs
"""
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # step 1: construct the dict
        depth_to_nodes = collections.defaultdict(list)
        i = 0
        prev_depth, curr_depth = 0, 0
        while i < len(S):
            j = i
            while j < len(S) and S[j] == "-":
                j += 1
            curr_depth = j - i
            
            k = j
            while k < len(S) and S[k].isdigit():
                k += 1
            val = int(S[j:k])
            
            depth_to_nodes[depth].append(val)
            i = k

        # step 2: do dfs to construct the tree
        return self._dfs(0, depth_to_nodes)
        
    def _dfs(self, depth, depth_to_nodes):
        if depth not in depth_to_nodes or not depth_to_nodes[depth]:
            return None
        
        root = TreeNode(depth_to_nodes[depth].pop(0))   # 可以换成deque这样popleft更快
        root.left = self._dfs(depth+1, depth_to_nodes)
        root.right = self._dfs(depth+1, depth_to_nodes)
        
        return root
    
""" 
上述解法过不了case "1-2--3-5--6--7", 错误把6当做2的right node了
这是因为node 6所在的位置信息没有放到depth_to_nodes里面去
"""


"""
since we need the position information of node 6, and disctionary doesnot maitain the position order.
we choose to use a list to store (level, node) information, the pos at the list stores the information
of porisiton order.
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
        if not nodes or depth > nodes[0][0]:  # 这里是解决问题的题眼，depth是当前depth的信息，nodes[0][0]试下一个node的depth信息
            return None                       # eg: "1-2--3-5--6--7", 遍历到node 3时，发现下一个node 5的depth更小了，这说明node 5不适合放在3的下面
                                              # 也就是1-->2-->3这个dfs path不能继续了(即2不能再放right node了), 所以就要return None
        root = TreeNode(nodes.popleft()[1])
        root.left = self._dfs(depth+1, nodes)
        root.right = self._dfs(depth+1, nodes)
        
        return root
