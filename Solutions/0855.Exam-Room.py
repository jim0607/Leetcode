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

Time Complexity:
O(N) for seat() and leave()
"""
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.idx = []

    def seat(self) -> int:
        if len(self.idx) == 0:
            self.idx.append(0)
            return 0
        
        if len(self.idx) == 1:
            if self.idx[0] >= self.N // 2:
                self.idx.insert(0, 0)
                return 0
            else:
                self.idx.append(self.N - 1)
                return self.N - 1
        
        # below is the same as 849. Maximize Distance to Closest Person
        # step 1: check two ends; step 2: check middle
        max_dist = 0
        should_seat_pos = 0
        if self.idx[0] > max_dist:      # check both ends
            max_dist = self.idx[0]
            should_seat = 0
            should_seat_pos = -1
        if self.N - 1 - self.idx[-1] > max_dist:
            max_dist = self.idx[0]
            should_seat = self.N - 1
            should_seat_pos = self.idx[-1]
            
        for i in range(len(self.idx) - 1):      # check middle
            if (self.idx[i+1] - self.idx[i]) // 2 > max_dist:
                max_dist = (self.idx[i+1] - self.idx[i]) // 2
                should_seat_pos = i
                should_seat = (self.idx[i] + self.idx[i+1]) // 2
                
        self.idx.insert(should_seat_pos + 1, should_seat)
        return should_seat

    def leave(self, p: int) -> None:
        self.idx.remove(p)
