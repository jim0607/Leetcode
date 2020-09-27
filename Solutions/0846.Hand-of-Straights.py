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
similar solution as 659. Split Array into Consecutive Subsequences - O(NlogN + N*W)
"""
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        
        counter = collections.Counter(hand)
        need = collections.defaultdict(int)
        curr_lens = 0
        for num in hand:
            if counter[num] == 0:
                continue
            counter[num] -= 1
            
            if need[num] > 0:
                need[num] -= 1
                curr_lens += 1
                if curr_lens == W:
                    curr_lens = 0
                else:
                    need[num + 1] += 1
            
            elif need[num] == 0:
                for i in range(1, W):
                    if counter[num + i] == 0:
                        return False
                    counter[num + i] -= 1
                curr_lens = 0
                
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
