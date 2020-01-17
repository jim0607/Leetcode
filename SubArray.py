前缀和prefixSum[i]: the sum of all the items before i
arr =          [1, 2, 3, 2]
prefixSum = [0, 1, 3, 6, 8]，构造prefixSum需要O(N)时间和O(N)空间
Remember: len(prefixSum) == len(arr) + 1
这样subArray的和就是sum(i~j包括i和j) = prefixSum[j+1] - prefixSum[i]，这样求任何一个subarray的和的时候只需要O(1)的时间复杂度就可以了.
如果不用prefixSum，那就用sum(arr[i:j+1])，sum(arr[i:j+1])的时间复杂度是O(N)。

一般的prefixSum[i]都是这样写的，而不是单独开一个数组出来存prefixSum:
for num in nums:
    prefixSum += num
    

subArr问题的模板（0560. Subarray Sum Equals K）： 一般都是 O(N), O(N)
一般都是prefixSum+hashmap来实现，prefixSum记录遍历到的那个地方之前所有的item加起来的和。
hashmap的key是prefixSum，val是prefixSum中出现的数字频率（0560. Subarray Sum Equals K, prefixSumMap = {0: 1}）
或者val是j/position (523. Continuous Subarray Sum, prefixSumMap = {0: -1} # key: prefixSum[j], val: j/position)
或者key是prefixSum[j]%K (974. Subarray Sums Divisible by K, prefixSum_f = {0: 1} # key: prefixSum[j]%K, val: 出现的frequency)

0560. Subarray Sum Equals K:  几乎所有的subArr的问题都是一样的模板，要背熟。
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumMap = {0: 1}   # 注意prefixSumMap需要初始化，就像solution 2中的prefixSum = [0]那样
        prefixSum, cnt = 0, 0

        for num in nums:
            prefixSum += num     # 这里的prefixSum 相当于 prefixSum[j]，一般的prefixSum[j]都是这样写的，而不是单独开一个数组出来寸prefixSum
            if prefixSum - k in prefixSumMap:     # 等价于 if prefixSum[j+1]-prefixSum[i] == k
                cnt += prefixSumMap[prefixSum - k]        
            
            # 将prefixSum 存入prefixSumMap中
            if prefixSum in prefixSumMap:
                prefixSumMap[prefixSum] += 1
            else:
                prefixSumMap[prefixSum] = 1
            
        return cnt
