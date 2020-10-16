"""
895. Maximum Frequency Stack

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
 

Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""

"""
It should be noted that since we don't 
"""
class FreqStack:

    def __init__(self):
        self.freq = collections.defaultdict(int)        # key is num, val is freq of the num
        self.mapping = collections.defaultdict(list)    # key is freq, val is a stack of num of that freq
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1                       # update freq of x
        f = self.freq[x]
        # It should be noted that since we don't delete the f-1 in mapping (we did that in LC 460. LFU), cuz we want to know the position of x in f-1 lsit 
        self.mapping[f].append(x)               # update mapping. 
        self.max_freq = max(f, self.max_freq)   # update max_freq if neccessary

    def pop(self) -> int:
        x = self.mapping[self.max_freq].pop()   # update mapping
        self.freq[x] -= 1                       # update freq of x
        if not self.mapping[self.max_freq]:     # update max_freq if neccessary
            self.max_freq -= 1
        
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
