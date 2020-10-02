"""
846. Hand of Straights

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 
Constraints:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""




"""
用以一个hashmap记录frequency. 由于必须固定长度为W, 所以我们每次都去连W个就可以了
"""
class Solution:
    def isNStraightHand(self, nums: List[int], W: int) -> bool:
        nums.sort()
        
        freq = collections.Counter(nums)

        for num in nums:
            if freq[num] == 0: 
                continue

            for i in range(W):
                if freq[num + i] == 0:
                    return False
                freq[num + i] -= 1
            
        return True
       
        
        
"""
solution 2: use a heapq - O(NlogN + N/W * WlogN) = O(NlogN).
这个写法更好理解一些！我们每次都从从最小的num为起点，依次加连续的num.
用一个counter记录当前各个num的cnt, 如果cnt>0就需要add_back to heap.
"""
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        hq = []
        for num in counter:
            heappush(hq, num)
        
        while len(hq) > 0:
            add_back = []   # 对于例子[1,2,2,3,3,4], 我们需要将误pop出来的2和3重新加回到heap中
            
            smallest = heappop(hq)      # 从最小的num为起点，依次加W个连续的num
            counter[smallest] -= 1
            if counter[smallest] > 0:   # 如果还没用完，需要放入add_back list, 一会儿好加回到heap中
                add_back.append(smallest)
            for i in range(1, W):       # 依次加W个连续的num
                if len(hq) == 0 or smallest + i != heappop(hq): # 提前退出
                    return False
                counter[smallest + i] -= 1
                if counter[smallest + i] > 0:
                    add_back.append(smallest + i)
            
            for num in add_back:
                heappush(hq, num)
                
        return True
