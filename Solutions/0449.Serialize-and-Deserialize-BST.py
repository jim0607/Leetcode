449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        res = ""
        q = collections.deque()
        q.append(root)
        while q:
            currNode = q.popleft()
            if currNode:
                res += str(currNode.val) + ","
                q.append(currNode.left)
                q.append(currNode.right)
            else:
                res += "None,"
                
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        vals = data.split(",")
        idx = 0
        root = TreeNode(int(vals[idx]))
        idx += 1
        q = collections.deque()
        q.append(root)
        while q and idx < len(vals):
            currNode = q.popleft()
            if vals[idx] != "None":
                currNode.left = TreeNode(int(vals[idx]))
                q.append(currNode.left)
            idx += 1
            if vals[idx] != "None":
                currNode.right = TreeNode(int(vals[idx]))
                q.append(currNode.right)
            idx += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
