"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


How one could improve the time complexity? The first idea is to use a heap, 
since in a maximum heap heap[0] is always the largest element. Though to add an element in a heap of size k costs log(k), 
that means O(Nlog(k)) time complexity for the solution.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lens = len(nums)
        if lens <= k:
            return [max(nums)]
        
        hq = []
        res = []
        for i in range(lens):
            if i < k - 1:
                heapq.heappush(hq, (-nums[i], i))
                continue
                
            heapq.heappush(hq, (-nums[i], i))
            if len(hq) > k:
                hq.remove((-nums[i - k], i - k))       # O(k) for remove, so O(kN) oeverall
                heapq.heapify(hq)       # 上一步做的remove操作并没有maitian原有的heapq的顺序，需要再heapiy一次

            res.append(-hq[0][0])
            
        return res


Could we figure out O(N) solution?

"""
Let's use a deque (double-ended queue), the structure which pops from / pushes to either side with the same O(1) performance.
It's more handy to store in the deque indexes instead of elements since both are used during an array parsing.
The algorithm is quite straigthforward:
Process the first k elements separately to initiate the deque.
Iterate over the array. At each step :
Clean the deque :
1. Keep only the indexes of elements from the current sliding window.
2. Remove indexes of all elements smaller than the current one, 
since they will not be the maximum ones. eg: [1,2,7,3,5,4], k = 3, because of 7, 1 and 2 will never be in res
Append the current element to the deque.
Append deque[0] to the output.
Return the output array.
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # step 1: put the first window into the dq, maintain dq a decreasing order
        # whenever we find the coming num is larger than dq[-1], we pop out cuz they WON'T be used anymore
        dq = deque()
        for i, num in enumerate(nums[:k]):
            # below code is the 模板 of mono stack
            while len(dq) > 0 and dq[-1][0] <= num:
                dq.pop()  # pop out the nums that are garanteed won't be used anymore
            dq.append((num, i))

        # step 2: do the following windows
        res = [dq[0][0]]  # since we are maintaining a decreasing st, dq[0] is the max_num in the window
        for i in range(k, len(nums)):
            # remove items that are outside the window, make sure the window size no larger than k
            # 注意这里必须比较idx来得到距离，而不能去比较len(dq) < k!!!
            # 这是因为len(dq) CANNOT represent window size. 这就是为什么需要在dq里存idx
            while len(dq) > 0 and i - dq[0][1] >= k:
                dq.popleft()  # this is why we need to use a dq - to enable fast pop from left 

            # below code is the 模板 of mono stack
            while len(dq) > 0 and dq[-1][0] <= nums[i]:
                dq.pop()
            dq.append((nums[i], i))

            res.append(dq[0][0])        # 更新res
            
        return res

"""
我们回头看看这题其实就是mono st多了一步保持窗口大小的步骤，而这个保持窗口大小的步骤需要从前面pop, 这就是为什么不直接用st, 而是用dq的原因
"""


"""
另一种写法
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Process the first k elements separately to initiate the deque
        deq = collections.deque()
        maxVal, maxIdx = nums[0], 0
        for i in range(k):
            self.clean_deq(deq, i, k, nums)
            deq.append(i)
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxIdx = i
        res.append(maxVal)
        
        for i in range(k, lens):
            self.clean_deq(deq, i, k, nums)
            deq.append(i)
            res.append(nums[deq[0]])
            
        return res
    
    def clean_deq(self, deq, i, k, nums):
        
        # 1. remov indexes of elements not from sliding window, Keep only the indexes of elements from the current sliding window.
        if deq and deq[0] == i - k:
            deq.popleft()
            
        # 2. Remove indexes of all elements smaller than the current one, since they will not be the maximum ones. 
        # eg: [1,2,7,3,5,4], k = 3, because of 7, 1 and 2 will never be in res
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()
          
        """ 为什么从前面开始pop就不行呢？  因为line 87: res.append(nums[deq[0]])我们要保证最左边的元素是最大的，耳聪右边pop是办不到的。
        while deq and nums[deq[0]] <= nums[i]:
            deq.popleft()
        """
