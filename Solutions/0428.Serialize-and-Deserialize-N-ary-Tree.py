428. Serialize and Deserialize N-ary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree



as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.



For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

You do not necessarily need to follow the above suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.


"""
solution 1: level order bfs.  This is very similar with serialize and deserialze a binary tree, except we need to do 
some trick to mark the end of a level. in binary tree, we know after visit left and right of a node, we can move to another node,
but in Nary tree, we don't know when to finish visiting a node cuz there could be multiple children for a node.
The trick is, when we do bfs to serialze, we append "*" into a q when we finish traversal the node's children, and also append "#" to res to mark the output string.
In deserialize, while res[idx] != "#" 就说明还要继续给curr_node添加child，因为res[idx] == "#"意味着要换node append child了
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)          # q 里面永远放node
        
        while q:
            lens = len(q)
            level = []
            for _ in range(lens):
                curr_node = q.popleft()
                if curr_node != "*":
                    level.append(str(curr_node.val))
                    for child in curr_node.children:
                        q.append(child)
                    q.append("*")           # use "*" to represnet the end of a level, meaning we should switch to another parent
                else:
                    level.append("#")       # use "#" to represent should switch to another parent in the represented string
             
            res += level
            
        return ",".join(res)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
    
        res = data.split(",")
        idx = 0
        root = Node(int(res[idx]), [])
        idx += 1      
        q = collections.deque()
        q.append(root)          # q 里面永远放node
        
        while q and idx < len(res):
            curr_node = q.popleft()
            while idx < len(res) and res[idx] != "#":   # while res[idx] != "#" 就说明还要继续给curr_node添加child，因为res[idx] == "#"意味着要换node append child了
                child = Node(int(res[idx]), [])
                curr_node.children.append(child)        # should append a TreeNode in it, cuz we are bulding a tree
                q.append(child)
                idx += 1
                
            idx += 1        # +1 跳过当前的 "#" 
            
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
