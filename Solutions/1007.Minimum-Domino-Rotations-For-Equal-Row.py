1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.


"""
让max_freq不动，去rotate freq比较小的
"""
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        freq_A = collections.Counter(A)
        freq_B = collections.Counter(B)
        max_freq_A, max_freq_B = 1, 1
        max_freq_num_A, max_freq_num_B = A[0], B[0]
        for num, freq in freq_A.items():
            if freq > max_freq_A:
                max_freq_A = freq
                max_freq_num_A = num
        for num, freq in freq_B.items():
            if freq > max_freq_B:   
                max_freq_B = freq
                max_freq_num_B = num
            
        if max_freq_A >= max_freq_B:
            return len(A) - max_freq_A if self._swap(A, B, max_freq_num_A) else -1
        else:
            return len(B) - max_freq_B if self._swap(B, A, max_freq_num_B) else -1
        
    def _swap(self, a, b, stay_put):
        for i in range(len(a)):
            if a[i] == stay_put:
                continue
            if b[i] != stay_put:
                return False
        return True
