[LintCode] 590 Connecting Graph II
Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b.
2. query(a), Returns the number of connected component nodes which include node a.


Example
5 // n = 5
query(1) return 1
connect(1, 2)
query(1) return 2
connect(2, 4)
query(1) return 3
connect(1, 4)
query(1) return 3


思路
implement一下Union Find weighted + compression。对于每一个node我们要存一下和他连通的个数并且在每次union的时候更新。


Code
public class ConnectingGraph2 {

    private int[] id;
    private int[] sz;
    
    public int find(int i) {
        while (i != id[i]) {
            id[i] = id[id[i]];
            i = id[i];
        }
        return i;
    }
    
    public int getSize(int a) {
        return sz[a];
    }
    
    public ConnectingGraph2(int n) {      // 这里是在做initialization for id and size
        // initialize your data structure here.
        
        id = new int[n + 1];
        sz = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            id[i] = i;
            sz[i] = 1;
        }
    }

    public void connect(int a, int b) {
        // Write your code here
        
        int i = find(a);
        int j = find(b);
        if (i != j) {
            id[i] = j;
            sz[j] += sz[i];
        }
        
    }
        
    public int query(int a) {
        // Write your code here
        
        return getSize(find(a));
    }
}
