"""
359. Logger Rate Limiter

Design a logger system that receive stream of messages along with its timestamps, 
each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_time = defaultdict(int)    # msg --> time

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.msg_time or timestamp >= 10 + self.msg_time[message]:
            self.msg_time[message] = timestamp
            return True
        return False
    

"""
When applying the dctionary solution, since we are not removing the outdated messages (messages printed more than 10 seconds ago), 
the space complexity can grow linearly with the number of messages.

To prevent this, we need to actively find the obsolete messages and remove them from the dictionary. 
We can do this by using OrderedDict in python. Starting from the left-most element of the dictionary, 
we remove that element, if its time was before timestamp-10, 
then we can just throw it out and remove the next message from the dictionary. 
But if it was not, it means that we are done cleaning the obsolete messages 
and we return the removed message to its original place as the left-most message in the OrderedDict.
"""
class Logger:

    def __init__(self):
        # use ordered dict to maintain time ordered, odered dict is an enhanced deque
        # because each time we put a new key --> val pair in ordered dict, we put it at the end of the Double Linked List
        self.msg_time = OrderedDict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # step 1: check if we should print the incoming msg
        should_print = False
        if message not in self.msg_time or timestamp >= 10 + self.msg_time[message]:
            self.msg_time[message] = timestamp      # 将新的key → val pair添加到末尾
            should_print = True

        # step 2: remove the outdated msg
        while len(self.msg_time) > 0:
            msg, time = self.msg_time.popitem(last=False)
            if timestamp <= 10 + time:
                self.msg_time[msg] = time
                self.msg_time.move_to_end(msg, last=False)  # move back to the beginning
                break
                
        return should_print


""" 
Google followup: input在K长度内无序的，但是时间t+K之后的输入一定出现在t之后。比如K是5，
[4, foo], [1, foo], [0, bar], [6, bar] => 在[4, foo], [1, foo], [0, bar]内是无序的，但是[6, bar]一定出现在[0, bar]之后，因为6>0+5.
也就是短程无序，长程有序。这时候该怎么print输出呢？
用一个heapq, heapq里面存(timestamp, message), 用一个deque里面也存(timestamp, message)
当发现下一个时间大于当前最小时间+K，就pop出当前的最小的放入到deque里面去, 这样deque里面存的就是长短程都有序的了


本质就是Sort a nearly sorted (or K sorted) array： 时间复杂度是nlogk
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Examples:

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
"""


def sort_k(nums, k):
    hq = []
    for i in range(k):
        heappush(hq, nums[i])

    idx = 0
    for i in range(k, len(nums)):
        nums[idx] = heappop(hq)     # idx放入的永远是目前最小的那个数,
        idx += 1                    # 这是因为nums是k程有序的，所以最小值永远在[idx, idx+k]范围内，所以只需要保证hq size为k就可以了
        heappush(hq, nums[i])

    while len(hq) > 0:
        nums[idx] = heappop(hq)
        idx += 1

if __name__ == "__main__":
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    sort_k(arr, k)
    print(arr)
