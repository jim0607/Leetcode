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
        insert_pos = 0
        res_idx = 0
        if not self.idx:
            res_idx = 0
        else:
            dist, res_idx = self.idx[0], 0
            for a, b in zip(self.idx, self.idx[1:]):    # 如果zip的长度不相等就取短的那个来pair
                if (b - a) // 2 > dist:
                    dist, res_idx = (b - a) // 2, (b + a) // 2
            if self.idx[0] > dist:                   # check 开头
                dist, res_idx = self.idx[0], 0
            if self.N - 1 - self.idx[-1] > dist:     # check 末尾
                dist, res_idx = self.N - 1 - self.idx[-1], self.N - 1

            # maintain a sorted list using binary search
            start, end = 0, len(self.idx) - 1
            while start + 1 < end:
                mid = start + (end - start) // 2
                if self.idx[mid] >= res_idx:
                    end = mid
                else:
                    start = mid
            if self.idx[start] >= res_idx:
                insert_pos = start
            elif self.idx[end] >= res_idx:
                insert_pos = end
            else:
                insert_pos = end + 1

        self.idx.insert(insert_pos, res_idx)

        return res_idx

    def leave(self, p: int) -> None:
        self.idx.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
# leetcode submit region end(Prohibit modification and deletion)
