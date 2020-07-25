514. Freedom Trail

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
Example:


 
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.


"""
dfs+memo的关键是memo的定义，跟dp的关键是状态的定义是一样的。
这题的定义为memo[(curr_ring, curr_idx)] = steps needed if from (curr_ring, curr_idx)
then memo[(curr_ring, curr_idx)] = min(memo[(curr_ring, curr_idx)], steps + 1 + dfs(next_ring, curr_idx + 1, memo))
"""
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def dfs(curr_ring, curr_idx, memo):
            if curr_idx == len(key):
                return 0
            
            if (curr_ring, curr_idx) in memo:
                return memo[(curr_ring, curr_idx)]  # memo stores the steps needed if from (curr_ring, curr_idx)
            
            memo[(curr_ring, curr_idx)] = float("inf")
            for i, ch in enumerate(curr_ring):
                if ch == key[curr_idx]:
                    next_ring = curr_ring[i:] + curr_ring[:i]
                    steps = min(i, len(curr_ring) - i)
                    memo[(curr_ring, curr_idx)] = min(memo[(curr_ring, curr_idx)], steps + 1 + dfs(next_ring, curr_idx + 1, memo))
                    
            return memo[(curr_ring, curr_idx)]
        
        return dfs(ring, 0, {})
        
""" 
也可以用dp解: dp[curr_idx in ring][curr_idx in key] = steps needed if from (curr_idx in ring, curr_idx in key)
从curr_idx in ring转换到next_ring需要多转几道弯，没有直接把curr_ring放到状态中方便，
这就是dfs+memo的优势所在，而且面试过程中还能体现自己递归不错！所以难一点的题优先dfs+memo比较好
"""
