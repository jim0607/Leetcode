"""
818. Race Car

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.

Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
"""




"""
solution 1: 层序遍历的bfs. 这个graph的nodes比较特殊，nodes是(curr_pos, curr_speed)
"""
class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque()
        visited = set()
        q.append((0, +1))
        visited.add((0, +1))
        
        steps = -1
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(len(q)):
                curr_pos, curr_speed = q.popleft()
                if curr_pos == target:
                    return steps
                
                # do next level
                if (curr_pos + curr_speed, curr_speed * 2) not in visited:
                    q.append((curr_pos + curr_speed, curr_speed * 2))
                    visited.add((curr_pos + curr_speed, curr_speed * 2))
                if curr_speed > 0:
                    if (curr_pos, -1) not in visited:
                        q.append((curr_pos, -1))
                        visited.add((curr_pos, -1))
                if curr_speed < 0:
                    if (curr_pos, +1) not in visited:
                        q.append((curr_pos, +1))
                        visited.add((curr_pos, +1))
                        
                        
                        
"""
solution 2: 层序遍历的bfs with strong pruning that is 100 times faster: 我们是有条件的回退，
只有在超过了target的情况下我们才回退, 不然的话每次都往回退一下会产生很多没用的分支
"""
class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque()
        visited = set()
        q.append((0, +1))
        visited.add((0, +1))
        
        steps = -1
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(len(q)):
                curr_pos, curr_speed = q.popleft()
                if curr_pos == target:
                    return steps
                
                # do next level
                if (curr_pos + curr_speed, curr_speed * 2) not in visited:
                    q.append((curr_pos + curr_speed, curr_speed * 2))
                    visited.add((curr_pos + curr_speed, curr_speed * 2))
                if curr_speed > 0:
                    if curr_pos + curr_speed > target and (curr_pos, -1) not in visited:    # strong pruning here
                        q.append((curr_pos, -1))            # 我们是有条件的回退，只有在超过了target的情况下我们才回退
                        visited.add((curr_pos, -1))
                if curr_speed < 0:
                    if curr_pos + curr_speed < target and (curr_pos, +1) not in visited:
                        q.append((curr_pos, +1))
                        visited.add((curr_pos, +1))
