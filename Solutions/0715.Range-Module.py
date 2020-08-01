715. Range Module

A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)



class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        sub_track = []
        if start % 2 == 0:      # If the index is even, it means that left is outside a range (or between two ranges)
            sub_track.append(left)
        if end % 2 == 0:
            sub_track.append(right)
            
        self.track[start:end] = sub_track

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        sub_track = []
        if start % 2 == 1:      # If the index is odd, it means that left is inside a range
            sub_track.append(left)
        if end % 2 == 1:
            sub_track.append(right)
            
        self.track[start:end] = sub_track

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)       # 注意这里要用bisect_right
        end = bisect.bisect_left(self.track, right)
        if start % 2 == 1 and end % 2 == 1 and start == end:     # [left, right]必须在某一个且同一个range内才return True
            return True
        return False


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
