321. Create Maximum Number

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]



"""
To create the max number from num1 and nums2 with k elements, 
we assume the final result combined by i numbers (denotes as left) from num1 
and j numbers (denotes as right) from nums2, where i+j==k.
Obviously, left and right must be the maximum possible number in num1 and num2 respectively. 
i.e. num1 = [6,5,7,1] and i == 2, then left must be [7,1].
The final result is the maximum possible merge of all left and right.

So there're 3 steps:
1. iterate i from 0 to k;
2. find max number from nums1, nums2 by select i , k-i numbers - monostack;
3. merge the max_num1 and max_num2 into one number - two pointers

helper function _find_inorder_max find the max number in nums in order and with lens.
helper function _merge merge the max_num1 and max_num2 into one number.
"""
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = [0 for _ in range(k)]
        for i in range(0, k+1):
            j = k - i           # i is the lens in nums1 and j is the lens in nums2
            if i > m or j > n:
                continue
            
            # step 1: find in order max possible number from nums1 with lens = i  
            # in order max possible number in nums2 with lens = j
            max_num1 = self._find_inorder_max(nums1, i)
            max_num2 = self._find_inorder_max(nums2, j)
            
            # step 2: merge the max_num1 and max_num2 into one number
            merged = self._merge(max_num1, max_num2)
            
            res = max(res, merged)
            
        return res
    
    def _find_inorder_max(self, nums, lens):
        """
        To find the max number in nums in order and with lens,
        we use a decreasing mono-stack to store the max digit in the front - O(N)
        """
        st = []
        for i, num in enumerate(nums):
            # 如果num > st[-1]就把st[-1] pop出来用num替换掉，注意还要保证有足够的num来组成长度为lens的数
            while st and num > st[-1] and len(st) + (len(nums) - i) >= lens + 1:
                st.pop()
            st.append(num)
            
        return st[:lens]
    
    def _merge(self, num1, num2):
        """
        方法是两根指针跑，谁大就先放谁进去 - O(K)
        """
        res = []
        i, j = 0, 0
        while i < len(num1) and j < len(num2):
            if num1[i] > num2[j]:
                res.append(num1[i])
                i += 1
            elif num1[i] < num2[j]:
                res.append(num2[j])
                j += 1
                
            # num1[i] == num2[j] 的情况比较复杂需要比较后面的第一个不相同的数. 
            # eg: [6,7], [6,0,4]要保证输出的是[6,7,6,0,4]而不是[6,6,7,0,4]
            else:      
                p, q = i, j     # 用两个指针去寻找第一个后面不相同的数
                while p < len(num1) and q < len(num2) and num1[p] == num2[q]: 
                    p += 1
                    q += 1
                if p == len(num1):
                    res.append(num2[j])
                    j += 1
                elif q == len(num2):
                    res.append(num1[i])
                    i += 1
                else:
                    if num1[p] > num2[q]:
                        res.append(num1[i])
                        i += 1
                    else:
                        res.append(num2[j])
                        j += 1
     
        while i <len(num1):
            res.append(num1[i])
            i += 1
        while j < len(num2):
            res.append(num2[j])
            j += 1
        
        return res
