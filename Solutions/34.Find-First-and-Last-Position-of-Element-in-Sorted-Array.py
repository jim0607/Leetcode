class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        if lens == 0:
            return [-1, -1]
        start, end = 0, lens-1
        first, last = 0, lens-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target <= nums[mid]:   # 这种判断条件是只要遇到相等的就把右半部分去掉，也就是尽量往左逼
                end = mid
            elif target > nums[mid]:
                start = mid
        # 由于上面的判断条件是尽量往左逼，所以逼出来的结果一定是第一个出现的target，此时便找到了first position of element
        if target == nums[end]:  
            first = end
        if target == nums[start]:  # 注意由于是想找first position of target，所以把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉。
            first = start
        
        start, end = 0, lens-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target < nums[mid]:   
                end = mid
            elif target >= nums[mid]: # 这种判断条件是只要遇到相等的就把左半部分去掉，也就是尽量往右逼
                start = mid
        print(start, end)
        # 由于上面的判断条件是尽量往右逼，所以逼出来的结果一定是最后一个出现的target
        if target == nums[start]:
            last = start
        if target == nums[end]:   # 注意由于是想找last position of target，所以把end放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，last可以被后面较大的end替换掉。
            last = end
            
        if target != nums[start] and target != nums[end]:
            return [-1, -1]
        return [first, last]
