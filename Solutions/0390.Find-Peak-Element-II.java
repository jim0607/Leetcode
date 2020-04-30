Find Peak Element II 390
Question
There is an integer matrix which has the following features:
The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:
A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.
Example
Given a matrix:
[ [1 ,2 ,3 ,6 ,5], [16,41,23,22,6], [15,17,24,21,7], [14,18,19,20,10], [13,14,11,10,9] ]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])
Challenge
Solve it in O(n+m) time.
If you come up with an algorithm that you thought it is O(n log m) or O(m log n), can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?
Solution

class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> findPeakII(int[][] A) {
        // write your code here
        List<Integer> res = new ArrayList<Integer>();
        if(A == null || A.length == 0 || A[0].length == 0){
            return res;
        }
        //根据题意，第1行和最后一行都不可能是peak，所以从第2行和倒数第2行开始
        int low = 1;
        int high = A.length - 2;

        while(low <= high){
            int mid = low + (high - low) / 2;
            int col = findPeak(mid, A);
            if(A[mid][col] < A[mid - 1][col]){
                high = mid - 1;
            }else if(A[mid][col] < A[mid + 1][col]){
                low = mid + 1;
            }else{
                res.add(mid);
                res.add(col);
                break;
            }
        }

        return res;

    }

    private int findPeak(int row, int[][] A){
        int start = 0;
        int end = A[row].length - 1;

        while(start + 1 < end){
            int mid = start + (end - start) / 2;
            if(A[row][mid] > A[row][mid - 1] && A[row][mid] > A[row][mid + 1]){
                return mid;
            }else if(A[row][mid] < A[row][mid - 1]){
                end = mid;
            }else{
                start = mid;
            }
        }

        if(A[row][start] > A[row][end]){
            return start;
        }else{
            return end;
        }
    }
}
