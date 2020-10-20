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
Maintain left_hq as a max heap, right_hq as a min heap
每次新增一个数的时候，先根据比 maxheap 中最后一个数 大还是小丢到对应的 heap 里。
丢完以后，再处理左右两边的平衡性:
如果左边太少了，就从右边拿出一个最小的丢到左边。
如果右边太少了，从左边拿出一个最大的丢到右边。
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_hq = []  # left_hq is a max heap, stores the nums smaller than median
        self.right_hq = [] # right_hq is a min heap, stores the nums larger than median

    def addNum(self, num: int) -> None:     # O(logN)
        if len(self.left_hq) == 0 or num <= -self.left_hq[0]:
            heappush(self.left_hq, -num)
        else:
            heappush(self.right_hq, num) 
        
        # we want to maintain the lens of leftHq equal or slightly larger to rightHq
        if len(self.left_hq) < len(self.right_hq):
            heappush(self.left_hq, -heappop(self.right_hq))
        elif len(self.right_hq) < len(self.left_hq) - 1:
            heappush(self.right_hq, -heappop(self.left_hq))

    def findMedian(self) -> float:      # O(1)
        if len(self.left_hq) == len(self.right_hq):
            return (-self.left_hq[0] + self.right_hq[0]) / 2
        else:
            return -self.left_hq[0]
         
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
这题由于是求average, 所以不需要管中间的minHeap1与maxHeap2之间的关系，
我们只需要用上题同样的方法来维护maxHeap1与minHeap1之间的关系，以及maxHeap2与minHeap2之间的关系就可以了。好牛逼的题呀！
如果新来的数很小，小于minHeap1[0], 那就放到maxheap1中同时更新maxHeap1与minHeap1的长度关系(5%的关系)。
如果新来的数很大，大于maxHeap2[0], 那就放到minHeap2中同时更新maxHeap2与minHeap2的长度关系(95%的关系)。
otherwise, 就把新来的数放到minHeap1 和 maxHeap2中。事实上minHeap1与maxHeap2存的数是一样的，只是为了取min和max方便所有用两个heap. 

