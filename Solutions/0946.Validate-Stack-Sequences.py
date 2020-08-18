946. Validate Stack Sequences

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.


Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.



"""
pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
[]              empty:   append(1)
[1]             1 != 4:  append(2)
[1, 2]          2 != 4:  append(3)
[1, 2, 3]       3 != 4:  append(4)
[1, 2, 3, 4]    4 == 4:  pop from st [1, 2, 3], i+=1, i = 1
[1, 2, 3]       3 != 5:  append(5)
[1, 2, 3, 5]    5 == 5:  pop from st [1, 2, 3], i+=1, i = 2
[1, 2, 3]       3 == 3:  pop from st [1, 2], i+=1, i = 3
[1, 2]          2 == 2:  pop from st [1], i = 4
[1]             1 == 1:  pop from st [], i = 5
return st is empty
"""
"""
使用一个栈st来模拟push和pop的过程，用一个指针在popped list里面跑，如果popped[i]==st[-1]那就一直pop, 最后判断st能不能pop为空
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i = 0
        for num in pushed:
            st.append(num)
            while len(st) > 0 and st[-1] == popped[i]:
                st.pop()
                i += 1
        return len(st) == 0
