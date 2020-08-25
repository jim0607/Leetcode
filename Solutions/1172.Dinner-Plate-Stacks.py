1172. Dinner Plate Stacks

You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.
Example:

Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.
 

Constraints:

1 <= capacity <= 20000
1 <= val <= 20000
0 <= index <= 100000
At most 200000 calls will be made to push, pop, and popAtStack.


"""
use a deque to store all the stacks - two cases TLE
"""
class DinnerPlates:

    def __init__(self, capacity: int):
        self.dq = collections.deque()
        for _ in range(100001):
            self.dq.append([None])

        self.capacity = capacity + 1

    def push(self, val: int) -> None:
        temp = []
        while len(self.dq[0]) == self.capacity:
            temp.append(self.dq.popleft())
        self.dq[0].append(val)
        while temp:
            self.dq.appendleft(temp.pop())            

    def pop(self) -> int:
        temp = []
        while self.dq and len(self.dq[-1]) == 1:
            temp.append(self.dq.pop())
        popped_item = self.dq[-1].pop() if self.dq else -1
        while temp:
            self.dq.append(temp.pop())
        return popped_item

    def popAtStack(self, index: int) -> int:        
        return -1 if len(self.dq[index]) == 1 else self.dq[index].pop()


"""
上述答案TLE的原因是我们提前定义了一个很大的数组村所有的stacks，这样很耗时间，我们可以动态更新数组的size. 并且记录最左边的非满数组和最右边的非空数组，
这样push和pop就更快了，
use a stack to store all the stacks.  
Use a heapq to store all the leftmost available-to-push stack, by storing their idx.
"""
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.available_to_push = []   # min heap to store the idx of available-to-push stack

    def push(self, val: int) -> None:       # O(logn)
        # step 1: pop out all the left stacks that are not avaliable to push, 
        # so that after the while loop, we will know the leftmost stack that is available to push
        while len(self.available_to_push) > 0 and self.available_to_push[0] < len(self.stack) and len(self.stack[self.available_to_push[0]]) == self.capacity:
            heappop(self.available_to_push)
            
        # if the q is empty, meaning there are no more available stacks
        if len(self.available_to_push) == 0:        
            heappush(self.available_to_push, len(self.stack))
        if self.available_to_push[0] == len(self.stack):
            self.stack.append([])
            
        # finally, we can push our val into the leftmost available stack
        self.stack[self.available_to_push[0]].append(val)

    def pop(self) -> int:       # O(1)
        # step 1: pop out all the empty stacks on the right, cuz they are not available to pop
        while len(self.stack) > 0 and len(self.stack[-1]) == 0:
            self.stack.pop()
            
        return self.popAtStack(len(self.stack) - 1)

    def popAtStack(self, index: int) -> int:        # O(logn)
        # check if it is available to pop
        if 0 <= index < len(self.stack) and len(self.stack[index]) > 0:
            heappush(self.available_to_push, index)     # add this index to the available-to-push heap
            return self.stack[index].pop()
        return -1
        

"""
Solution 3: use a stack to store all the stacks.  
Use a heapq to store all the leftmost available-to-push stack, by storing their idx.
Use another heapq to store all the rightmost available-to-pop stack, by storing the -idx.
"""
