"""
1381. Design a Stack With Increment Operation

Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, 
just increment all the elements in the stack.
 
Example 1:
Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.
 
Constraints:
1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.
"""


""" O(k) solution """
class CustomStack:

    def __init__(self, max_size: int):
        self.st = []
        self.max_size = max_size

    def push(self, x: int) -> None:
        if len(self.st) < self.max_size:
            self.st.append(x)

    def pop(self) -> int:
        if len(self.st) == 0:
            return -1
        return self.st.pop()

    def increment(self, k: int, val: int) -> None:      # O(k)
        for i in range(k):
            if i >= len(self.st):
                break
            self.st[i] += val


"""
Use an additional array to record the increment value - O(1)
inc[i] means for all elements st[0] ~ st[i], we should plus inc[i] when popped from the stack.
When we pop, we should set inc[i-1] += inc[i], so that we can accumulate the increment inc[i]
for the bottom elements and the following pops.
"""
class CustomStack:

    def __init__(self, max_size: int):
        self.st = []        # simulate the stack
        self.inc = []       # inc[i] = by how much should st[:i] increase
        self.max_size = max_size

    def push(self, x: int) -> None:
        if len(self.st) < self.max_size:
            self.st.append(x)
            self.inc.append(0)      # inc and st has the same lens

    def pop(self) -> int:
        if len(self.st) == 0:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]        # save the inc[-1] information to inc[-2] so that we don't lose it
        return self.inc.pop() + self.st.pop()   # pop st[-1] plus how many st[-1] should increase

    def increment(self, k: int, val: int) -> None:      # O(1)
        idx = min(k, len(self.inc)) - 1    
        if idx >= 0:
            self.inc[idx] += val
