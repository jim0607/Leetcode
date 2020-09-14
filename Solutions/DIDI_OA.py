def findK(A, B):
    if not A or not B or len(A) <= 1 or len(B) <= 1:
        return 0

    preA, preB = [0 for _ in range(len(A) + 1)], [0 for _ in range(len(B) + 1)]
    for i in range(len(A)):
        preA[i+1] = preA[i] + A[i]
        preB[i+1] = preB[i] + B[i]

    cnt = 0
    for i in range(1, len(preA) - 1):
        if preA[i] == preA[-1] - preA[i] == preB[i] == preB[-1] - preB[i]:
            cnt += 1
    return cnt


print(findK([4,-1,0,3], [-2,5,0,3]))            # 2
print(findK([2,-2,-3,3], [0,0,4,-4]))           # 1
print(findK([4,-1,0,3], [-2,6,0,4]))            # 0
print(findK([3,2,6], [4,1,6]))                  # 0
print(findK([1,4,2,-2,5], [7,-2,-2,2,5]))       # 2





# condition 1: every node should have in_degree == 1 and out_degree == 1
# condition 2: from node 1, we can visit all N nodes

import collections

def detect_cycle(A, B):
    if not A or not B or len(A) == 0 or len(B) == 0:
        return False
    if len(A) == 1 == len(B) and A[0] == B[0]:
        return False

    graph = collections.defaultdict(list)
    in_degrees = collections.defaultdict(int)
    for i in range(len(A)):
        if A[i] in graph:   # check out_degree, we assume one node can only have out_degree == 1
            return False    # 试一下[1,2,3,4], [2,3,1,4]如果return True, 就说明这里的check是不对的，需要删掉这个check，如果return False, 就说明这里的check是对的
        graph[A[i]].append(B[i])
    for i in range(len(A)):
        if B[i] in in_degrees:   # check in_degree
            return False    # 同上用[1,2,3,4], [2,3,1,4]试一下
        in_degrees[B[i]] += 1

    visited = set()
    dfs(1, graph, visited)
    return len(visited) == len(A)

def dfs(curr_node, graph, visited):
    for next_node in graph[curr_node]:
        if next_node in visited:
            continue
        visited.add(next_node)
        dfs(next_node, graph, visited)

print(detect_cycle([1,3,2,4], [4,1,3,2]))            # True
print(detect_cycle([1,2,3,2], [2,3,1,4]))            # True/False, test case to check if in_degree and out_degree should be checked
print(detect_cycle([], []))            # True/False, test case to check empty graph
print(detect_cycle([1], [1]))            # True/False, test case to check graph that has only one node
print(detect_cycle([1,2,3,4], [2,1,4,3]))            # False
print(detect_cycle([3,1,2], [2,3,1]))                # True
print(detect_cycle([1,2,1], [2,3,3]))                # False
print(detect_cycle([1,2,3,4], [2,1,4,4]))            # False
print(detect_cycle([1,2,2,3,3], [2,3,3,4,5]))            # False




"""
Maximum sum of two elements whose digit sum is equal
Last Updated: 27-03-2020
Given an array arr[] of N positive elements, the task is to find a pair in the array such that the digit sum of elements in the pair 
are equal and their sum is maximum. Print -1 if it is not possible to find the pair else print the maximum sum.

Examples:

Input: arr[] = {55, 23, 32, 46, 88}
Output: 101
(23, 32) with digit sum 5 and (55, 46)
with digit sum 10 are the only pairs
with equal digit sum. The pair with maximum
sum is (55, 46) i.e. 55 + 46 = 101

Input: arr[] = {18, 19, 23, 15}
Output: -1
Since there are no two elements
whose digit sums are equal.
"""

import collections

def get_digit(num):
    ans = 0
    while num > 0:
        ans += num % 10
        num //= 10
    return ans

def find_max_sum(arr):
    if len(arr) <= 1:
        return -1

    mapping = collections.defaultdict(int)  # (digit_sum of a number-->the number)
    res = -1
    for i in range(len(arr)):
        digit = get_digit(arr[i])
        if digit in mapping:
            res = max(res, mapping[digit] + arr[i])
        mapping[digit] = max(mapping[digit], arr[i])
    return res


print(find_max_sum([55, 23, 32, 46, 88]))




"""
Min Deletions to Make Frequency of Each Letter Unique

Description:
Given a string s consisting of n lowercase letters, you have to delete the minimum number of characters from s so that every letter in s appears 
a unique number of times. We only care about the occurrences of letters that appear at least once in result.
Example 1:
Input: "eeeeffff"
Output: 1
Explanation:
We can delete one occurence of 'e' or one occurence of 'f'. Then one letter will occur four times and the other three times.
Example 2:
Input: "aabbffddeaee"
Output: 6
Explanation:
For example, we can delete all occurences of 'e' and 'f' and one occurence of 'd' to obtain the word "aabbda".
Note that both 'e' and 'f' will occur zero times in the new word, but that's fine, since we only care about the letter that appear at least once.
Example 3:
Input: "llll"
Output: 0
Explanation:
There is no need to delete any character.
Example 4:
Input: "example"
Output: 4
"""

# solution: priority queue
"""
abbbcccddddeeeeefffffff
we use a counter:
1: a
3: bbb
3: ccc
4: dddd
4: eeee
7: fffffff
we put [1, 3, 3, 4, 4, 7] into a heapq.
meaning there is one ch appears 1 time, one ch appears 3 times, another ch appear 3 times
one ch appears 4 times, another ch appears 4 times, one ch appears 7 times.
we maintain a max heap, so that each time we pop, we get the max_f, max_f = pop()
if max_f != top(), that means there is only one ch having this max_f, great, the max_f ch should be reserved, no deletion needed.
if max_f == top(), that means there is more than one ch having this max_f, then we should delete this ch by doing
heappush(max_f-1) and deletion_cnt += 1
In the end, we return deletion_cnt.

Complexity of counting of the characters is O(N)
Complexity of counting of the characters to remove is O(Log(D)) but not bigger than size of the alphabet, in our case not bigger than O(Log(26))
Where N is length of given string and D is number of characters to remove
Thus general complexity is O(N)
"""

import collections
import _heapq

def min_deletion(s):
    counter = collections.Counter(s)
    hq = []
    for freq in counter.values():
        _heapq.heappush(hq, -freq)
    cnt = 0
    while len(hq) > 0:
        max_f = -_heapq.heappop(hq)
        if len(hq) == 0:
            return cnt
        if max_f == -hq[0]:
            cnt += 1
            if max_f - 1 > 0:
                _heapq.heappush(hq, -(max_f - 1))
    return cnt

print(min_deletion("eeeeffff"))             # 1
print(min_deletion("aabbffddeaee"))         # 6
print(min_deletion("llll"))                 # 0
print(min_deletion("example"))              # 4
