"""
683. K Empty Slots

There are N slots in a river. An array P is given where each index denotes the time at which the stone at that position will appear. 
I have to come up with an algorithm to find the earliest time at which there will be K contiguous empty slots. For E.G.

N = 5
P = [2,5,1,4,3]
K = 2
Initially: [0,0,0,0,0] 
All the slots are empty.

Now at:
Time t = 1, second stone will appear --> [0,1,0,0,0]
Time t = 2, fifth stone will appear --> [0,1,**0,0**,1]
Time t = 3, first stone will appear --> [1,1,0,0,1]
Time t = 4, fourth stone will appear --> [1,1,0,1,1]
Time t = 5, third stone will appear --> [1,1,1,1,1]
So the answer for above case is 2, because at time 2 there are (k = 2) continuous empty slots.
"""



"""
The idea is to use an array days[] to record each position's flower's blooming day. 
That means days[i] is the blooming day of the flower in position i+1. 
We just need to find a subarray days[left, left+1,..., left+k-1, right] which satisfies: for any i = left+1,..., left+k-1, we have days[left] < days[i] and days[right] < days[i].
So the problem is to find a fixed sized window, where any num in the window [i, i+k], are smaller than days[i-1] and also smaller than days[i+k+1].
"""
class Solution:
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        days = [0 for _ in range(len(flowers))]
        for i, flower in enumerate(flowers):
            days[flower - 1] = i + 1
            
        left, right = 0, k + 1          # maintain一个fixed size k+2 的window
        res = float("inf")
        for i, day in enumerate(days):
            if right >= len(days):
                break
                
            if day < days[left] or day <= days[right]: # 如果在window内有比left or right更早开花的，那就说明这个window不valid, 需要更新left and right.
                if i == right:                         # 如果在window内有比left or right更早开花的，那就说明这个window不valid, unless i == right
                    res = min(res, max(days[left], days[right]))
                left = i                  # 更新left and right
                right = left + k + 1

        return res if res != float("inf") else -1
