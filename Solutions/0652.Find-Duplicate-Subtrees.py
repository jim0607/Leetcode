"""
652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""



"""
use a hashmap to store the serialization_representation --> a list of the root_node, the whole algorith takes O(N)
"""
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def serialize(root):
            if not root:
                return "#"
            
            left_serialization = serialize(root.left)
            right_serialization = serialize(root.right)
            
            root_serialization = str(root.val) + "," + left_serialization + "," + right_serialization   # 注意这里如果直接相加就不对, 必须要加逗号将root, left, right分隔开来，不然就从string representation就不能唯一得到subtree了
            
            mapping[root_serialization].append(root)    # put the root_serialization into the hashmap
            
            return root_serialization
            
        
        mapping = defaultdict(list)     # serialization_of_root --> root
        serialize(root)
        return [lst[0] for lst in mapping.values() if len(lst) > 1]



"""
solution 3: similar with solution 2 postOrder traversal with memorization.   Note that in-order traversal never works for serialization!
"""
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        memo = set()
        res = []
        already_added = set()
        
        def postOrder(root):
            """
            return a str constrcucted by a tree
            """
            if not root:
                return "#"
            
            left = postOrder(root.left)
            right = postOrder(root.right)
            
            rootStr = left + right + str(root.val)  # don't know why preOrder and inOrder doesn't work
            
            if rootStr in memo:
                if rootStr not in already_added:
                    already_added.add(rootStr)
                    res.append(root)
            else:
                memo.add(rootStr)
                
            return rootStr

        postOrder(root)
        
        return res
        
  

"""
solution 1: serialize the every subtree using bfs, and put (string presentation of subtree --> subtree node) into a hashmap.
Since serialization takes O(N), so the overall algorithm takes O(N^2)
"""
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []

        mapping = collections.defaultdict(list) # key is string representation of sub-root, val is the a list of sub-root
        self.dfs(root, mapping)                 # dfs to serialize the tree and update mapping
        return [mapping[key][0] for key, lst in mapping.items() if len(lst) > 1]
        
    def dfs(self, root, mapping):
        if not root:
            return []

        serialized = self.serialize(root)  # this takes O(N), so overall algorithm O(N^2)
        mapping[serialized].append(root)
            
        self.dfs(root.left, mapping)
        self.dfs(root.right, mapping)
        
    # 下面的serialize函数与297. Serialize and Deserialize Binary Tree是一模一样的
    def serialize(self, root):
        res = []
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            level = []
            lens = len(q)
            for _ in range(lens):
                curr_node = q.popleft()
                if curr_node:
                    level.append(str(curr_node.val))
                    q.append(curr_node.left)
                    q.append(curr_node.right)
                else:
                    level.append("#")       # we use "#" to represent None
            res += level

        return ",".join(res)
