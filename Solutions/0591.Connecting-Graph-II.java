591. Connecting Graph II

Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), an edge to connect node a and node b
query(), Returns the number of connected component in the graph
Have you met this question in a real interview?  
Example
Example 1:

Input:
ConnectingGraph3(5)
query()
connect(1, 2)
query()
connect(2, 4)
query()
connect(1, 4)
query()

Output:[5,4,3,3]

Example 2:

Input:
ConnectingGraph3(6)
query()
query()
query()
query()
query()


Output:
[6,6,6,6,6]



public class ConnectingGraph3 {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: nothing
     */
     
    private int[] father = null;
    private int cnt;
    
    private int find(int x) {
        if (father[x] == x) {
            return x;
        }
        father[x] = find(father[x]);
        return father[x];
    }
    
    public ConnectingGraph3(int n) {
        // initialize your data structure here.
        father = new int[n + 1];
        cnt = n;
        for (int i = 1; i < n + 1; i++) {
            father[i] = i;
        }
    }
    
    public void connect(int a, int b) {
        // write your code here
        int root_a = find(a);
        int root_b = find(b);
        if (root_a != root_b) {
            father[root_a] = root_b;
            cnt--;
        }
    }

    /**
     * @return: An integer
     */
    public int query() {
        // write your code here
        return cnt;
    }
}
