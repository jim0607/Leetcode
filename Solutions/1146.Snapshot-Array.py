"""
1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  
Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 
Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""



"""
solution 1: easy hashmap solution - o(L) TLE: every time we snap, you make a copy of the list, 
for which the time complexity is O(L) - L being the length of the list.
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0 for _ in range(length)]
        self.snap_cnt = 0
        self.mapping = defaultdict(list)

    def set(self, index: int, val: int) -> None:   
        self.arr[index] = val

    def snap(self) -> int:        # O(L)
        self.mapping[self.snap_cnt] = self.arr.copy()   # 注意has to be a copy - O(L)
        self.snap_cnt += 1
        return self.snap_cnt - 1
    
    def get(self, index: int, snap_id: int) -> int:      # O(1)
        return self.mapping[snap_id][index]
        
        
        
"""
solution 2: sparse array.
Since 题目说了 initially, each element equals 0.
we treated it as a sparse matrix: use a dictionary to store only the non-zero values.
Now, every time we snap, you make a copy of the dictionary.
This operation is O(N) - N being the length of dict items, 
N could be much less then L if it is a sparse matrix.
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.idx_to_val = defaultdict(int)
        self.snapshots = []     # stores the idx_to_val dictionary at each time

    def set(self, index: int, val: int) -> None:
        self.idx_to_val[index] = val

    def snap(self) -> int:
        self.snapshots.append(self.idx_to_val.copy())   # now it is O(N), which is << O(L) if sparse
        return len(self.snapshots) - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]
        
        
"""
solution 3: binary search - 没看太明白
"""
class SnapshotArray(object):
    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        if self.A[index][-1][0] == self.snap_id: # if set(0, 4), set(0, 5), then delete previous to save space
            self.A[index].pop()
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]
