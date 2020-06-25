870. Advantage Shuffle

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]



"""
Greedy algorithm: sort A and B first, and then assign num_a to num_b so that num_a is larger than num_b and num_a as small as possible.
For each num_a a in sortedA, we will either beat that num_b (put a into assigned[b] map), or throw it out (put a into not_assigned list). 
"""

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)     # sort A and B so that we can do greedy: always assign num_b the num_a that is just larger than num_b, and as small as possible in A
        sortedB = sorted(B)
        
        # eg: Input: A = [12,24,8,32], B = [13,25,32,11] Output: [24,32,8,12]
        assigned = collections.defaultdict(list)    # assigned[b]=[the num_a in A that is assgiend to num_b], eg: assgiend[13] = [24]
        for b in sortedB:     
            assigned[b] = []
            
        not_assigned = []       # store the num_a in A that are not assigned, eg: not_assigned = [8]
        
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                not_assigned.append(a)
                
        res = []
        for b in B:     # 这里不能用sortedB, 因为我们的res要保证输出的顺序
            if assigned[b]:
                res.append(assigned[b].pop())
            else:
                res.append(not_assigned.pop())
                
        return res
