"""
1345. Jump Game IV

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
"""



"""
求最小步数用bfs: O(N). 解决TLE的办法：
pruning 1: eg. [100,-23,404,23,23,23,23,23,23,23,3,404] 如果有连续的数字出现，如中间的23，
那就可以删掉，只留下首尾两个就可以了，变成[100,-23,404,23,23,3,404];
pruning 2: idx逆序排列，这样较大的idx能提前遍历到;
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        num_to_idx = collections.defaultdict(list)
        for i, num in enumerate(arr):
            num_to_idx[num].append(i)
            
        # pruning 1: [100,-23,404,23,23,23,23,23,23,23,3,404] --> [100,-23,404,23,23,3,404]
        for num, lst in num_to_idx.items():
            if len(lst) > 2:
                modified = []
                for i in range(len(lst)):
                    if i > 0 and i < len(lst) - 1 and lst[i-1] + 1 == lst[i] == lst[i+1] - 1:
                        continue
                    modified.append(lst[i])
                num_to_idx[num] = modified

        q = collections.deque()
        visited = set()
        q.append(0)
        visited.add(0)
        steps = -1
        while len(q) > 0:
            lens = len(q)
            steps += 1
            for _ in range(lens):
                curr_idx = q.popleft()
                if curr_idx == len(arr) - 1:
                    return steps
                
                if curr_idx - 1 >= 0:
                    if curr_idx - 1 not in visited:
                        q.append(curr_idx - 1)
                        visited.add(curr_idx - 1)
                if curr_idx + 1 < len(arr):
                    if curr_idx + 1 not in visited:
                        q.append(curr_idx + 1)
                        visited.add(curr_idx + 1)
                for next_idx in num_to_idx[arr[curr_idx]][::-1]:  # pruning 2: idx逆序排列，这样较大的idx能提前遍历到
                    if next_idx not in visited:
                        q.append(next_idx)
                        visited.add(next_idx)
        return -1
