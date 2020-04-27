[LintCode] 589 Connecting Graph
Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b.
2. query(a, b), check if two nodes are connected


Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true


思路
这题就是implement一下Union Find。


public class ConnectingGraph { 
    
    private int[] id;
    
    public int find(int i) {
        while (i != id[i]) {
            id[i] = id[id[i]];
            i = id[i];
        }
        return i;
    }

    public ConnectingGraph(int n) {
        // initialize your data structure here.
        
        id = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            id[i] = i;
        }
    }

    public void connect(int a, int b) {
        // Write your code here
        
        int i = find(a);
        int j = find(b);
        id[i] = j;
    }
        
    public boolean query(int a, int b) {
        // Write your code here
        
        return find(a) == find(b);
    }
}
