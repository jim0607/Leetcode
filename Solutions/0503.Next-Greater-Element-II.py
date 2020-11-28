503. Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.



"""
double the nums, then iterate the nums and maintain a mono decreasing stack.
if the item is less or equal than st[-1], just append.
else we pop st, and the curr item is the next greater of the popped item.
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums     # 处理circle的问题，一般都需要先把arr double一下
        
        st = []     # st store the (num, idx) pair so that we can easily update res
        res = [-1 for _ in range(len(nums2))]
        for i, num in enumerate(nums2):
            while len(st) > 0 and st[-1][0] < num:
                res[st.pop()[1]] = num
            st.append((num, i))
            
        return res[:len(nums)]


"""
solution 2: should also know the soution that don't need to double the nums. 
方法是for idx in range(2* lens): 对长度lens取模，i = idx % lens 
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1 for _ in range(n)]
        st = []
        for i in range(2 * n):
            while len(st) > 0 and st[-1][0] < nums[i % n]:
                res[st.pop()[1]] = nums[i % n]
            st.append((nums[i % n], i % n))
        return res
    

"""
Double the nums first, then do the same thing as 496.
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        res = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1]  # 注意这里不是res.append(),否则res就需要return reverse of res了
                
            stack.append(nums[i])

        return res[:len(nums)//2]
        
        
"""
Same idea except don't need to create a new nums
"""      
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        res = [0 for _ in range(lens)]
        stack = []
        for i in range(2*lens-1, -1, -1):
            while stack and nums[i%lens] >= stack[-1]:
                stack.pop()
            if not stack:
                res[i%lens] = -1
            else:
                res[i%lens] = stack[-1]
                
            stack.append(nums[i%lens])

        return res
