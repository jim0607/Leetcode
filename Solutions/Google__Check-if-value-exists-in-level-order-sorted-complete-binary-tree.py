"""
Check if value exists in level-order sorted complete binary tree

Given a level-order sorted complete binary tree, the task is to check whether a key exists in it or not. 
A complete binary tree has every level except possibly the last, completely filled, with all nodes as far left as possible.

Examples:

             7
          /     \
         10      15
       /   \    /  \
      17   20  30  35
     / \   /     
    40 41 50     
    
Input: Node = 3
Output: No

Input: Node = 7
Output: Yes

Input: Node = 30
Output: Yes

https://www.geeksforgeeks.org/check-if-value-exists-in-level-order-sorted-complete-binary-tree/
"""

"""
step 1: find the level of the num by going check the left path;
step 2: binary search on the located level. This is the hard part because unlike the conventional binary search, the nodes of this level cannot be accessed directly. 
However, the path from the root to every node in this level can be encoded using the binary logic. 
For example, consider the 3rd level in the sample tree. It can contain up to 2^3 = 8 nodes. 
These nodes can be reached from the root node by going left, left, left; or by going left, left, right; and so on. 
If the left is denoted by 0 and the right by 1 then the possible ways to reach nodes in this level can be encoded as arr = [000, 001, 010, 011, 100, 101, 110, 111].
However, this array doesn’t need to be created, binary search can be applied by recursively selecting the middle index 
and simply generating the l-bit gray code of this index.
Time complexity is O((logN)^2).
"""

def main(root, val):
    if val < root.val:
        return False
    if val == root.val:
        return True

    level = find_level(root, val)

    return binary_search_in_level(root, level, val)


def find_level(root, val):
    """
    Find the level for val by always going left - O(logN)
    """
    level = 1
    while root.left:
        if val < root.left.val:
            return level
        root = root.left
        level += 1
    return level


def binary_search_in_level(root, level, val):
    """
    Binary search in the located level - O((logN)^2)
    """
    start, end = 0, 2 ** level - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        gray_code = get_graycode(level, mid)
        node = get_node_from_graycode(root, gray_code)
        if node.val == val:
            return True
        elif node.val > val:
            end = mid
        else:
            start = mid
    start_gray_code = get_graycode(level, start)
    end_gray_code = get_graycode(level, end)
    start_node = get_node_from_graycode(root, start_gray_code)
    end_node = get_node_from_graycode(root, end_gray_code)
    return True if start_node.val == val or end_node.val == val else False


def get_graycode(level, mid):
    """
    Get the kth gray code.
    eg: if level == 3, gray codes are [000,001,010,011,100,101,110,111].
    we need to return the gray code at mid idx: 011.
    It should be noted that mid actually equals the gray code i.e. 011 = 3,
    so we are actually returning the 二进制码 of mid
    space: O(level), time: O(level) = O(logN)
    """
    # The way to iterate each bit in an integer is: while n > 0: n = n >> 1. 
    # get the last bit of n: last_bit = n & 1
    gray_code = [0 for _ in range(level)]
    for i in range(level - 1, -1, -1):    # 需要generate的gray_code长度为level
        gray_code[i] = mid & 1
        mid = mid >> 1
    return gray_code

def get_node_from_graycode(root, gray_code):
    """
    Get the node at the located level using the gray_code.
    0 means take the left path, 1 means take the right path
    eg: 011 means the path is node = root.left.right.right
    O(len(gray_code)) = O(level) = O(logN)
    """
    for num in gray_code:
        if num == 0:
            root = root.left
        elif num == 1:
            root = root.right
    return root
