996. Number of Squareful Arrays

Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].


Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
 

Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9



"""
本质还是求permutation. 只是多了一个条件就是nums[cur_idx] +nums[next_idx]必须是square number.
"""
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:       
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(nums):
                res.append(curr_comb.copy())
                return
            for next_idx in range(len(nums)):
                if next_idx in visited:
                    continue
                if next_idx > 0 and nums[next_idx] == nums[next_idx-1] and next_idx - 1 not in visited:
                    continue
                if curr_idx != -1 and not is_square(nums[curr_idx] + nums[next_idx]):
                    continue
                visited.add(next_idx)
                curr_comb.append(nums[next_idx])
                backtrack(next_idx, curr_comb)
                curr_comb.pop()
                visited.remove(next_idx)
            
        def is_square(num):       # this takes O(1), we can also use binary search which takes O(logn)
            return int(num**0.5) == num**0.5
        
        
        nums.sort()     # 去重第一步
        res = []
        visited = set()
        backtrack(-1, [])
        return len(res)




"""
solution 1: brutal backtracking - find all permutations (O(n!)) and then check how many of them are squareful (O(n*n!))
"""
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        # construct squareful nums
        self.square_nums = []
        i = 0
        while i**2 <= 2*10**9:      # 0 <= A[i] <= 1e9
            self.square_nums.append(i**2)
            i += 1
        
        A.sort()        # 去重第一步
        res = []
        visited = set()
        self._backtrack(A, [], res, visited)
        
        cnt = 0
        for arr in res:         # O((N*logT)*N!)
            if self._is_squareful(arr):
                cnt += 1
        return cnt
    
    def _backtrack(self, A, curr, res, visited):    # O(N!)
        if len(curr) == len(A):
            res.append(curr.copy())
            return
        
        for idx in range(len(A)):
            if idx in visited:
                continue
            if (idx > 0 and A[idx] == A[idx-1]) and idx - 1 not in visited:   # 去重
                continue
            visited.add(idx)
            curr.append(A[idx])
            self._backtrack(A, curr, res, visited)
            curr.pop()
            visited.remove(idx)
            
    def _is_squareful(self, arr):
        """ check if an arr is squareful - O(N*logT), where T is lens of self.square_num """
        for i in range(1, len(arr)):
            if not self._is_square(arr[i] + arr[i-1]):
                return False
        return True
    
    def _is_square(self, target):
        """ use binary search to check if a target number is a sqaure number """
        start, end = 0, len(self.square_nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target > self.square_nums[mid]:
                start = mid
            else:
                end = mid
        if target == self.square_nums[start] or target == self.square_nums[end]:
            return True
        return False
        
        
        
        
"""
backtracking with constraints solution: O(number of possible solutions).
需要判断A[i]+A[i-1]合不合格，所以需要把prev_idx传入backtrack function signature
"""
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        # step 1: construct squareful nums
        self.square_nums = []
        i = 0
        while i**2 <= 10**2:      # 0 <= A[i] <= 1e2
            self.square_nums.append(i**2)
            i += 1
        
        # step 2: do backtrack to find valid permutations
        A.sort()        # 去重第一步
        res = []
        visited = set()
        self._backtrack(A, -1, [],  res, visited)   # 需要判断A[i]+A[i-1]合不合格，所以需要把prev_idx传入backtrack function signature
        return len(res)
    
    def _backtrack(self, A, prev_idx, curr_path, res, visited):    # O(number of possible solutions)
        if len(curr_path) == len(A):
            res.append(curr_path.copy())
            return
        
        for idx in range(len(A)):
            if idx in visited:
                continue
            if (idx > 0 and A[idx] == A[idx-1]) and idx - 1 not in visited:   # 去重
                continue
            if prev_idx != -1 and not self._is_square(A[idx] + A[prev_idx]):  # check if next_idx is valid
                continue
            visited.add(idx)
            curr_path.append(A[idx])
            self._backtrack(A, idx, curr_path, res, visited)
            curr_path.pop()
            visited.remove(idx)
    
    def _is_square(self, target):
        """ use binary search to check if a target number is a sqaure number """
        start, end = 0, len(self.square_nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target > self.square_nums[mid]:
                start = mid
            else:
                end = mid
        if target == self.square_nums[start] or target == self.square_nums[end]:
            return True
        return False
    
    """ 下面这个方法check square number 更快！"""
    def _is_square(self, target):
        sqrt = int(math.sqrt(target))
        return sqrt * sqrt == target
