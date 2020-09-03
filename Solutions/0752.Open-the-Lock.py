752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.



"""
find neighbors: 4*4 where 4 is the number of digits in target
bfs all combinations: 10^4. So total complexity is O(4*4*10^4 + N) where N is number of deadends
space: O(10^4 + N)
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)
        if "0000" in deadset:
            return -1
        
        q = collections.deque()
        visited = set()
        q.append("0000")
        visited.add("0000")     # 其实在初始化的时候也可以把deadends都add进去
        
        steps = -1
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_node = q.popleft()
                if curr_node == target:
                    return steps
                for next_node in self._get_next(curr_node):
                    if next_node in deadset or next_node in visited:  # If next_node is deadend, then we don't put it into q
                        continue
                    q.append(next_node)
                    visited.add(next_node)
        
        return -1
    
    def _get_next(self, curr_node):
        for i in range(len(curr_node)):     # 注意neighbor不止两个，而是每个digit都可能有两个
            curr_num = int(curr_node[i])
            for delta in [-1, 1]:
                next_num = (curr_num + delta) % 10
                next_node = curr_node[:i] + str(next_num) + curr_node[i+1:]
                yield next_node
