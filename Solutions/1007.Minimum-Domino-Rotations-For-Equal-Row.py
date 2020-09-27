"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

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



"""
Try all possibilities from 1 to 6.
If we can make number i in a whole row,
it should satisfy that countA[i] + countB[i] - same[i] = n

Take example of
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]

countA[2] = 4, as A[0] = A[2] = A[4] = A[5] = 2
countB[2] = 3, as B[1] = B[3] = B[5] = 2
same[2] = 1, as A[5] = B[5] = 2

We have countA[2] + countB[2] - same[2] = 6,
so we can make 2 in a whole row.
"""
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        counter_A, counter_B = collections.Counter(A), collections.Counter(B)
        
        counter_same = collections.Counter()    # record the same num for A and B that appears at the same position,
        for a, b in zip(A, B):                  # so counter_same[num] means how many positions A[i] == num == B[i]
            if a == b:
                counter_same[a] += 1
        
        for num in range(1, 7):
            if counter_A[num] + counter_B[num] - counter_same[num] == len(A):
                return min(counter_A[num], counter_B[num]) - counter_same[num]
        return -1
