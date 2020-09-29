"""
223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
"""


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        total = (C - A) * (D - B) + (G - E) * (H - F)
        if not self.isRectangleOverlap([A,B,C,D], [E,F,G,H]):
            return total
        
        overlap = (min(C, G) - max(A, E)) * (min(H, D) - max(B, F))
        return total - overlap
        
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[0] >= rec1[2] or rec2[2] <= rec1[0] or rec2[3] <= rec1[1] or rec2[1] >= rec1[3]:
            return False
        return True
