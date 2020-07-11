308. Range Sum Query 2D - Mutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10



class SegmentTreeNode:
    
    def __init__(self, u, d, l, r):
        self.sum = 0      
        self.u = u         
        self.d = d         
        self.l = l          
        self.r = r          
        self.upleftChild = None   
        self.uprightChild = None
        self.downleftChild = None
        self.downrightChild = None

        
class SegmentTree:
    
    def __init__(self, u, d, l, r, nums):    
        self.root = self.build(u, d, l, r, nums)   

    def build(self, u, d, l, r, nums): 
        if l > r or u > d:   
            return None

        node = SegmentTreeNode(u, d, l, r)
        if l == r and u == d:    #leaf
            node.sum = nums[u][l]
        else:                   # when l < r:
            midRow = (u + d) // 2
            midCol = (l + r) // 2
            node.upleftChild = self.build(u, midRow, l, midCol, nums)
            node.uprightChild = self.build(u, midRow, midCol+1, r, nums)
            node.downleftChild = self.build(midRow+1, d, l, midCol, nums)
            node.downrightChild = self.build(midRow+1, d, midCol+1, r, nums)

            node.sum += node.upleftChild.sum if node.upleftChild else 0
            node.sum += node.uprightChild.sum if node.uprightChild else 0
            node.sum += node.downleftChild.sum if node.downleftChild else 0
            node.sum += node.downrightChild.sum if node.downrightChild else 0
        return node

    def update(self, node, row, col, val):
        if node.l == node.r and node.u == node.d:  #reach leaf
            node.sum = val
            return

        midCol = (node.r + node.l) // 2
        midRow = (node.u + node.d) // 2

        if row <= midRow and col <= midCol:
            self.update(node.upleftChild, row, col, val)  
        elif row <= midRow and col > midCol:
            self.update(node.uprightChild, row, col, val)
        elif row > midRow and col <= midCol:
            self.update(node.downleftChild, row, col, val) 
        else:
            self.update(node.downrightChild, row, col, val) 
        # update the changes after recursive :
        node.sum = 0   #reset first!
        node.sum += node.upleftChild.sum if node.upleftChild else 0
        node.sum += node.uprightChild.sum if node.uprightChild else 0
        node.sum += node.downleftChild.sum if node.downleftChild else 0
        node.sum += node.downrightChild.sum if node.downrightChild else 0

    # 9 cases total...
    def querySum(self, node, u, d, l, r):
        if not node:
            return 0
        if node.u == u and node.d == d and node.l == l and node.r == r:   
            return node.sum

        midCol = (node.r + node.l) // 2
        midRow = (node.u + node.d) // 2

        if r <= midCol: 
            if d <= midRow:         
                return self.querySum(node.upleftChild, u, d, l, r)  
            elif u >= midRow + 1:   
                return self.querySum(node.downleftChild, u, d, l, r)
            else:                                        
                return self.querySum(node.upleftChild, u, midRow, l, r) + \
            self.querySum(node.downleftChild, midRow+1, d, l, r)  
        elif l >= midCol + 1:   
            if d <= midRow:         
                return self.querySum(node.uprightChild, u, d, l, r) 
            elif u >= midRow + 1:   
                return self.querySum(node.downrightChild, u, d, l, r) 
            else:                                            
                return self.querySum(node.uprightChild, u, midRow, l, r) + \
            self.querySum(node.downrightChild, midRow+1, d, l, r)  
        else:          
            if d <= midRow:        
                return self.querySum(node.upleftChild, u, d, l, midCol) + \
            self.querySum(node.uprightChild, u, d, midCol+1, r)  
            elif u >= midRow + 1:  
                return self.querySum(node.downleftChild, u, d, l, midCol) + \
            self.querySum(node.downrightChild, u, d, midCol+1, r)
            else:                   
                return self.querySum(node.upleftChild, u, midRow, l, midCol) + \
            self.querySum(node.downleftChild, midRow+1, d, l, midCol) + \
            self.querySum(node.uprightChild, u, midRow, midCol+1, r) + \
            self.querySum(node.downrightChild, midRow+1, d, midCol+1, r)


class NumMatrix(object):
    
    def __init__(self, matrix):
        if not matrix or not matrix[0]:  #special
            return
        self.segmentTree = SegmentTree(0, len(matrix)-1, 0, len(matrix[0])-1, matrix)

    def update(self, row, col, val):
        self.segmentTree.update(self.segmentTree.root, row, col, val)

    def sumRegion(self, row1, col1, row2, col2):
        return self.segmentTree.querySum(self.segmentTree.root, row1, row2, col1, col2)
