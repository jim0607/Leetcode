658. Find K Closest Elements

Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


    
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hq = []
        for num in arr:
            hq.append((abs(num - x), num))
        
        heapify(hq)
        
        res = []
        for _ in range(k):      # KlogN
            res.append(heappop(hq)[1])
            
        return sorted(res)      # KlogK
    
    
"""
solution 2: 由于这题给的arr是已经sorted的，我们可以binary search寻找x在num中的位置-O(logN)，
然后从那个位置出发向两边寻找最接近x的值 - O(k).  总的时间复杂度是O(k+N). 比heapq要好一些，因为
heapq没有用到arr already soted的特性
"""
    
    

import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]
        
        # step 1: binary search to find the idx where x should be
        lens = len(arr)
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid
        
        idx = start if arr[start] <= x else end
    
        # step 2: put the closest k elements in a hq - O(klogk)
        hq = []
        i, j = idx, idx + 1
        while i >= 0 and j < lens:
            if x - arr[i] <= arr[j] - x:
                heapq.heappush(hq, (arr[i], i))
                i -= 1
            else:
                heapq.heappush(hq, (arr[j], j))
                j += 1
            if j - i >= k + 1:
                break
    
        if j - i < k + 1:
            while i >= 0:
                heapq.heappush(hq, (arr[i], i))
                i -= 1
                if j - i >= k + 1:
                    break
            while j < lens:
                heapq.heappush(hq, (arr[j], j))
                j += 1
                if j - i >= k + 1:
                    break
        
        # step 3: output - O(klogk)
        res = []
        while k > 0:
            res.append(heapq.heappop(hq)[0])
            k -= 1
        
        return res
