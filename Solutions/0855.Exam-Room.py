# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1
# . 
# 
#  When a student enters the room, they must sit in the seat that maximizes the 
# distance to the closest person. If there are multiple such seats, they sit in th
# e seat with the lowest number. (Also, if no one is in the room, then the student
#  sits at seat number 0.) 
# 
#  Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() re
# turning an int representing what seat the student sat in, and ExamRoom.leave(int
#  p) representing that the student in seat number p now leaves the room. It is gu
# aranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[]
# ,[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 10^9 
#  ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
#  all test cases. 
#  Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
#  in seat number p. 
#  
#  Related Topics Ordered Map


# leetcode submit region begin(Prohibit modification and deletion)



"""
Very straight forward idea.
Use a sorted list to record the index of seats where people sit, so that we can save tons of space if the seats is sparse

seat():
1. find the biggest distance at the start, at the end and in the middle.
2. insert index of seat into the idx list
3. return index

leave(p): pop out p

O(M) for seat() and leave(), where M is how many person are sitting there.
"""
class ExamRoom:

    def __init__(self, N: int):
        self.idx_arr = []       # store the idx where people sit
        self.N = N

    def seat(self) -> int:      # O(M), where M is how many person are sitting there
        if len(self.idx_arr) == 0:
            self.idx_arr.append(0)
            return 0

        max_dist = 0
        sit_pos = 0
        if self.idx_arr[0] > max_dist:                  # step 1: check left end
            max_dist = self.idx_arr[0]
            sit_pos = 0
            
        for i in range(1, len(self.idx_arr)):           # step 2: check mid
            if (self.idx_arr[i] - self.idx_arr[i-1]) // 2 > max_dist:
                max_dist = (self.idx_arr[i] - self.idx_arr[i-1]) // 2
                sit_pos = (self.idx_arr[i] + self.idx_arr[i-1]) // 2
                
        if self.N - self.idx_arr[-1] - 1 > max_dist:    # step 3: check right part
            max_dist = self.N - self.idx_arr[-1] - 1
            sit_pos = self.N - 1

        insert_idx = bisect.bisect_right(self.idx_arr, sit_pos)
        self.idx_arr.insert(insert_idx, sit_pos)
        return sit_pos

    def leave(self, p: int) -> None:        # O(M)
        self.idx_arr.remove(p)
        
        
        
"""
O(N) solution - TLE
"""
class ExamRoom:

    def __init__(self, N: int):
        self.arr = [0 for _ in range(N)]

    def seat(self) -> int:      # O(N)
        if 1 not in self.arr:
            self.arr[0] = 1
            return 0

        # step 1: check left
        max_dist = 0
        sit_pos = -1
        left = 0
        while left <= len(self.arr) and self.arr[left] == 0:
            left += 1
        if left > max_dist:
            max_dist = left
            sit_pos = 0
        
        # step 2: check middle
        prev, curr = 0, 0
        for i in range(1, len(self.arr)):
            if self.arr[i] == 1:
                prev, curr = curr, i
                if (curr - prev) // 2 > max_dist:
                    max_dist = (curr - prev) // 2
                    sit_pos = prev + (curr - prev) // 2
                 
        # step 3: check right
        right = len(self.arr) - 1
        while right >= 0 and self.arr[right] == 0:
            right -= 1
        if len(self.arr) - 1 - right > max_dist:
            max_dist = len(self.arr) - 1 - right
            sit_pos = len(self.arr) - 1
                    
        self.arr[sit_pos] = 1
        return sit_pos

    def leave(self, p: int) -> None:
        self.arr[p] = 0
