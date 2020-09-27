"""
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



"""
核心algorithm: 每次都给最大的b做匹配，如果最大的a可以匹配上最大的b，
那就把最大的a分配给最大的b；如果不能匹配上，那就把最小的a分配给最大的b
"""
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()            # sort A so that 我们可以选择分配最快马或最慢马
        B = [(num, idx) for idx, num in enumerate(B)]   # 把idx带上，这样我们才能在正确的位置上更新res
        B.sort()            # sort b so that 我们可以每次都给最大的b做匹配

        res = [0 for _ in range(len(B))]
        left, right = 0, len(A) - 1     # idx points at A 中最慢的马和最快的马
        for i in range(len(B) - 1, -1, -1):
            top_b, top_b_idx = B[i]         # 每次都给最大的b做匹配
            if top_b >= A[right]:           # 反正我A中最快的马都干不过你top_b, 那就干脆把最慢的马分配给你，
                res[top_b_idx] = A[left]    # 这样可以留着我A最快的马去干你别的马
                left += 1       
            else:
                res[top_b_idx] = A[right]
                right -= 1
        return res


"""
核心algorithm是每次都给最大的b做匹配，我们其实也可以用最大堆存储b, 这样每次pop出来的就都是最大的b了
"""
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()            # step 1: sort A so that 我们可以选择分配最快马或最慢马
        
        hq = []             # step 2: 以b来维护一个最大堆，每次都pop出最大的b来分配
        for idx, b in enumerate(B):
            heappush(hq, (-b, idx))
        
        # step 3: 核心algorithm, 每次都给最大的b做匹配，如果最大的a可以匹配上最大的b，
        # 那就把最大的a分配给最大的b；如果不能匹配上，那就把最小的a分配给最大的b
        res = [0 for _ in range(len(B))]
        left, right = 0, len(A) - 1     # idx points at A 中最慢的马和最快的马
        while len(hq) > 0:
            top_b, top_b_idx = heappop(hq)
            top_b = -top_b
            if top_b >= A[right]:           # 反正我A中最快的马都干不过你top_b, 那就干脆把最慢的马分配给你，
                res[top_b_idx] = A[left]    # 这样可以留着我A最快的马去干你别的马
                left += 1       
            else:
                res[top_b_idx] = A[right]
                right -= 1
        return res



"""
Greedy algorithm: sort A and B first, and then assign num_a to num_b so that num_a is larger than num_b and num_a as small as possible.
For each num_a a in sortedA, we will either beat that num_b (put a into assigned[b] map), or throw it out (put a into not_assigned list). 
"""

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)     # sort A and B so that we can do greedy: 
        sortedB = sorted(B)     # always assign num_b the num_a that is just larger than num_b, and as small as possible in A
        
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
