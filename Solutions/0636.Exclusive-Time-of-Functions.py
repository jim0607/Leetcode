636. Exclusive Time of Functions

On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

Example 1:

Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.



"""
函数开启了就压入栈，结束了就出栈，不会有函数被漏掉。这样的我们可以遍历每个log。
use a stack to store the id of start funciton, and a prev_time to keep track of the prev_time.
if type is "start", then we should update the res[st[-1]], and st.append(id), and update pre_time;
if type is "start", then we should update the res[st[-1]], and st.pop(), and update pre_time.
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        st = []         # store the time
        prev_time = 0
        for log in logs:
            id, type, time = log.split(":")
            id, time = int(id), int(time)
            
            # if type is "start", then we should update the res[st[-1]]
            # and st.append(id), update pre_time
            if type == "start":
                if len(st) > 0:
                    res[st[-1]] += time - prev_time
                st.append(id)
                prev_time = time
                
            # if type is "start", then we should update the res[st[-1]]
            # and st.pop(), update pre_time
            elif type == "end":
                res[st[-1]] += time - prev_time + 1
                st.pop()
                prev_time = time + 1
                    
        return res
