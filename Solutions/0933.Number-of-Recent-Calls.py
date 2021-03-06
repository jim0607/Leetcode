"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

 

Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
"""

class RecentCounter:

    def __init__(self):
        self.window = deque()

    def ping(self, t: int) -> int:
        while len(self.window) > 0 and t > self.window[0] + 3000:
            self.window.popleft()
        self.window.append(t)
        return len(self.window)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)




public class RecentCounter {
    Queue <int> q = new Queue <int> ();
    
    public RecentCounter() {

    }
    
    public int Ping(int t) {
        q.Enqueue(t);
        while (t - q.Peek()> 3000) {
            q.Dequeue();
        }
        return q.Count();       // Count is a method that gets the number of elements contained in the Queue.
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.Ping(t);
 */
