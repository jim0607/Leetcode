"""
632. Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
"""


    
"""
这种关注diff的题其实变相的是在关注max_val和min_val, 我们往往可以通过一个hq来快速获取max_val， 
另一个hq来快速获取min_val。
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        maxhq, minhq = [], []
        for i in range(len(nums)):      # 每个lst中取一个数
            heappush(minhq, (nums[i][0], i, 0))
            heappush(maxhq, (-nums[i][0], i, 0))
             
        res = [-float("inf"), float("inf")]
        while minhq and maxhq:
            min_val, lst_idx, num_idx = heappop(minhq)
            max_val = -maxhq[0][0]
            maxhq.remove((-min_val, lst_idx, num_idx))  # remove takes O(m)
            if max_val - min_val < res[1] - res[0]:
                res = [min_val, max_val]
            
            if num_idx == len(nums[lst_idx]) - 1:   # 这个lst提供的number不能再增加了，
                return res                          # 其他lst提供的number又都比他大，所以差距只能越来越大
            
            # 将当前lst中的num_dix+1加入到hq中，保证每个lst中取一个数
            heappush(minhq, (nums[lst_idx][num_idx+1], lst_idx, num_idx+1))
            heappush(maxhq, (-nums[lst_idx][num_idx+1], lst_idx, num_idx+1))
    
    

"""
上面解法maxhq.remove((-min_val, lst_idx, num_idx))  # remove takes O(m). 
所以时间复杂度是O(mn). 我们其实可以不需要maxhq来更新max_val. 这样时间复杂度就变成了O(nlogm)
heapq solution: O(m+nlogm) where m is len(nums), n is len(lst)
hq stores (the item in the lst, the lst_idx of where lst is in the nums, the num_idx where the num is in the lst)
whenver a min_val is popped, we compare the max_val-min_val with the previous diff. 
Then we push (nums[lst_idx][num_idx+1], lst_idx, num_idx+1) into the heapq and update max_val in the heapq
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minhq = []
        for i in range(len(nums)):      # 每个lst中取一个数
            heappush(minhq, (nums[i][0], i, 0))
             
        res = [-float("inf"), float("inf")]
        max_val = max(t[0] for t in minhq)
        while minhq:
            min_val, lst_idx, num_idx = heappop(minhq)
            if max_val - min_val < res[1] - res[0]:
                res = [min_val, max_val]
            
            if num_idx == len(nums[lst_idx]) - 1:   # 这个lst提供的number不能再增加了，
                return res                          # 其他lst提供的number又都比他大，所以差距只能越来越大
            
            # 将当前lst中的num_dix+1加入到hq中，保证每个lst中取一个数
            heappush(minhq, (nums[lst_idx][num_idx+1], lst_idx, num_idx+1))
            max_val = max(max_val, nums[lst_idx][num_idx+1])    # 更新max_val
            
"""
那么你可能要问了，为什么不像更新max_val那样更新min_val呢？我也想呀，
可是我们需要知道min_val所对应的lst_idx and num_idx,
这样我们才能决定指针的下一个指向谁，这就是为什么lst_idx and num_idx要进去hq的原因
"""
            
