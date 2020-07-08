621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 题目真他妈难理解
        # eg: AAA, n = 2
        # 每个A之间至少要隔n=2个，所以是A - - A - - A 总共 7 个任务
        # eg: AAAABBBCCD, n = 3
        # 先把频率最高的隔开3:   A - - - A - - - A - - - A
        # 然后把频率次高的插入:  A B - - A B - - A B - - A B
        # 继续把频率次高的插入:  A B C - A B C - A B - - A B
        # 继续把频率次高的插入:  A B C D A B C - A B - - A B
        # 于是总的任务数就是上图的
        # I have to be concerned about tasks with higher frequencies. This makes it a perfect candidate for a Priority Queue, or a Max-Heap.
        
        freqDict = collections.Counter(tasks)
            
        hq = []
        for task, freq in freqDict.items():
            heapq.heappush(hq, (-freq, task))   # get the most frequent items to heap top, by using negative freq, 维护一个最大堆
            
        res = 0
        while hq:
            addBack = []
            
            # 先预设有n + 1个座位，eg: n = 3， 那就先预设四个座位: _ _ _ _
            # 每进一次循环代表占领一个座位的位置，让高频的去占领那4个座位
            # 同时将高频的那四个的freq分别减1
            for _ in range(n + 1):
                res += 1  
                
                if hq:      # 遍历一遍hq的所有元素，这些元素分别freq分别减1
                    freq, task = heapq.heappop(hq)
                    freq *= -1
                    freq -= 1
                    if freq > 0:  # if more than one char remains, then should add the char back to heap
                        addBack.append((freq, task))

                if not hq and not addBack:  # if not heap, and no additon to heap, 需要提前出来！
                    return res
                
            # add back to heap
            for freq, task in addBack:
                heapq.heappush(hq, (-freq, task))
                    
        return res
