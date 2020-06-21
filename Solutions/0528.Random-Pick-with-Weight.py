528. Random Pick with Weight

The explaination of the example is shity. Let's take this for example:
the input is an arr [2, 4, 1, 5], we want to randomly pick an idx based on the val of the idx.
idx:         0      1       2       3
val:         2      4       1       5     sum = 12, so the probability of out put the idx is:
probability:2/12   4/12    1/12    5/12

prefix sum + binary search
take this for example:
idx:         0      1       2       3
val:         2      4       1       5    
prefixsum:   2      6       7       12
if we randomly pick an idx, say 9, since 9 is within 7 to 12, so the output idx is idx 3
if we randomly pick an idx, say 4, since 4 is within 2 to 6, so the output idx is 1

"""
step 1: create a prefix sum arr
step 2: generate a rand_idx
step 3: binary search to find where the idx is in the prefix_sum arr
(should be noted that it works only if prefix sum is icreasing, meaning only if arr vals in the arr are positive)
"""
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [w[0]] * len(w)
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i]
            
        print(self.prefix_sum)

    def pickIndex(self) -> int:
        rand_idx = random.randrange(self.prefix_sum[-1])
        start, end = 0, len(self.prefix_sum) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.prefix_sum[mid] <= rand_idx:   # 因为等于的话需要输出后面的idx所以只能往右边逼近
                start = mid
            else:
                end = mid
            
        return start if self.prefix_sum[start] > rand_idx else end  # 等于的话需要输出后面的idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
