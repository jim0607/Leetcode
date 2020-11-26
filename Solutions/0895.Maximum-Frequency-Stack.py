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

class FreqStack:

    def __init__(self):
        self.num_freq = defaultdict(int)    # num --> freq
        self.freq_nums = defaultdict(list)  # freq --> a stack of nums of that freq
        self.max_freq = 0

    def push(self, num: int) -> None:
        self.num_freq[num] += 1                     # update num_freq
        freq = self.num_freq[num]
        # It should be noted that since we don't delete the freq-1 in mapping (we did that in LC 460. LFU), 
        # cuz we want to know the position of x in freq-1 lsit 
        self.freq_nums[freq].append(num)            # update freq_nums
        self.max_freq = max(self.max_freq, freq)    # update max_freq
        
    def pop(self) -> int:
        num = self.freq_nums[self.max_freq].pop()   # update freq_nums
        if len(self.freq_nums[self.max_freq]) == 0:
            self.max_freq -= 1                      # update max_freq (注意这里不太好想)
        self.num_freq[num] -= 1                     # update num_freq
        
        return num
