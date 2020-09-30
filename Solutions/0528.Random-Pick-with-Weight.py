"""
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




"""
step 1: create a prefix sum arr
step 2: generate a rand_idx
step 3: binary search to find where the idx is in the prefix_sum arr
(should be noted that it works only if prefix sum is icreasing, meaning only if arr vals in the arr are positive)
"""
class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = [0 for _ in range(len(w) + 1)]
        for i in range(len(w)):
            self.pre_sum[i+1] = self.pre_sum[i] + w[i]

    def pickIndex(self) -> int:
        rand_num = random.randrange(self.pre_sum[-1])
        return self._binary_search(rand_num) - 1
    
    def _binary_search(self, num):
        """
        Return the idx to the right of the position of where the num should be in self.pre_sum
        eg: [1, 3] --> [0, 1, 4], if num = 0, return idx = 1; if num = 3, return idx = 2
        """
        start, end = 0, len(self.pre_sum) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.pre_sum[mid] <= num:    # 往右边逼近
                start = mid
            else:
                end = mid
        return start if self.pre_sum[start] > num else end
