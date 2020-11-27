"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

    
    
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.window_sum += val
        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()
        return self.window_sum / len(self.window)

    

// use deque, or double-ended queue
// in C#, Queue class is by default a deque, with two methods:
// 1. enqueue, meaning push to the back of the queue; 2. dequeue, meaning pop from the front of the queue
// O(1) in time cuz enqueue and dequeue is O(1); O(N) in space where N is the size
public class MovingAverage {
    int size, windowSum = 0, count = 0;
    Queue <int> q = new Queue <int> ();

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        this.size = size;   // 可能相当于python里面的self.size = size
    }
    
    public double Next(int val) {
        ++count;
        // calculate the new sum by shifting the window
        q.Enqueue(val);
        int tail = count > size ? q.Dequeue() : 0;
        windowSum = windowSum - tail + val;
        
        return windowSum * 1.0 / Math.Min(size, count);    // 注意C#里面所有的class以及其methods开头都是大写的，比如Math, Math.Min, Queue, Enqueue, Dequeu
    }
}
