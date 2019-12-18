We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

 

Example 1:

Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.
Example 2:

Input: [1,1,2]
Output: 3
Explanation: 
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.


"""https://www.cnblogs.com/grandyang/p/10982534.html
好讨厌位操作的题目！！"""
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res, curr = set(), set()
        for a in A:
            temp = {a}
            for b in curr:
                temp.add(a|b)
            curr = temp
            for num in curr:
                res.add(num)
        return len(res)
