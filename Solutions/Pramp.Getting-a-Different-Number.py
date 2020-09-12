"""
Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4 
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ MAX_INT
0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT
[output] integer
"""




"""
arr = [0, 2, 1, 3]

init:
sort the arr
[0,1,2,3]
loop the arr:
  the first number != idx
O(nlogn)
O(1)
O(n)

[0, 2, 1, 3]   # sum = 0 to len(arr)-1 - 6
sum(arr) - 6: 6-6= 0, nothing is missing is [0 to 3], res = 4

[0, 6, 1, 3]  # sum from 0 to  - 6
sum(arr) = 10   # 10-6 = 4 means we are 

max = max(arr), max-len(arr) = 2
4 -2 = 2

there could be more than one number missing

thinking aobut ueing bit manipulation.

bool = [False _ len(arr)] n  4
loop arr:
    bool[arr[i]] = True
find the first False in bool

0 5 1 3 10
"""




def get_different_number(arr):
  n = len(arr)
  b = [False for _ in range(n)]
  for num in arr:
    if num > len(b) - 1:
      continue
    b[num] = True
  for i in range(len(b)):
    if not b[i]:
      return i
  return len(arr)
  
  
