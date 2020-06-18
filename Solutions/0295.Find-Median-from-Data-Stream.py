295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


"""
每次新增一个数的时候，先根据比 maxheap 中最后一个数 大还是小丢到对应的 heap 里。
丢完以后，再处理左右两边的平衡性:
如果左边太少了，就从右边拿出一个最小的丢到左边。
如果右边太少了，从左边拿出一个最大的丢到右边。
"""
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.leftHq = []        # use a maxheap to store the nums that are smaller than median
        self.rightHq = []       # use a minheap store the nums that are larger then median

    def addNum(self, num: int) -> None:
        if not self.leftHq:
            heapq.heappush(self.leftHq, -num)
            return
        
        if num <= -self.leftHq[0]:
            heapq.heappush(self.leftHq, -num)
        else:
            heapq.heappush(self.rightHq, num)
            
        if len(self.leftHq) < len(self.rightHq):      # we want to maintina the lens of leftHq equal or slightly larger to rightHq
            heapq.heappush(self.leftHq, -heapq.heappop(self.rightHq))
        elif len(self.leftHq) > len(self.rightHq) + 1:
            heapq.heappush(self.rightHq, -heapq.heappop(self.leftHq))

    def findMedian(self) -> float:
        if len(self.leftHq) > len(self.rightHq):
            return -self.leftHq[0]
        else:
            return (self.rightHq[0] - self.leftHq[0]) / 2


"""
Q1: If all integer numbers from the stream are between 0 and 100, how would you optimize it?
We can maintain an integer array of length 100 to store the count of each number along with a total count. 
Then, we can iterate over the array to find the middle value to get our median (where the totalCnt//2 lies). O(100)

Q2: If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
As 99% is between 0-100.  So the median (not mean) is definetely in the range 0-100. 
So can keep a counter for less_than_hundred and greater_than_hundred. Then do Q1. O(100)
"""


Google 真题：
Create a data structure to take in a stream of numbers and create a function that will give the average excluding the outliers (5% and 95%).
Solution: use 4 heapq, one maxHeap for left outliner, one maxHeap close to left, one minHeap colse to right, one minHeap for right outliner.
  []    (       []			      		  []     )    []
maxHeap1		   minHeap1		     maxHeap2     minHeap2
这题由于是求average, 所以不需要管中间的minHeap1与maxHeap2之间的关系，我们只需要用上题同样的方法来维护maxHeap1与minHeap1之间的关系，
以及maxHeap2与minHeap2之间的关系就可以了。好牛逼的题呀！

