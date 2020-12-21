"""
1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
"""



"""
solution 1: use list to store the non-zero items
O(M + N + m + n) where M is how many items in nums, m is how many non-zero items in nums.
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        for i, num in enumerate(nums):
            if num != 0:        # only store the non-zero items 
                self.nums.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        nums1 = self.nums       # O(M)
        nums2 = vec.nums        # O(N)

        res = 0
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):    # O(m + n)
            if nums1[i][0] < nums2[j][0]:
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                j += 1
            else:
                res += nums1[i][1] * nums2[j][1]
                i += 1
                j += 1
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


"""
solution 2: use dictionary to store the non-zero items
O(M + N + min(m, n)) where M is how many items in nums, m is how many non-zero items in nums.
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_num = defaultdict(int)    # idx_of_non-zero_num --> non_zero_num
        for i, num in enumerate(nums):
            if num != 0:        # only store the non-zero items 
                self.idx_num[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        idx_num1 = self.idx_num       # O(M)
        idx_num2 = vec.idx_num        # O(N)

        if len(idx_num1) > len(idx_num2):   # this check is for if only one matrix is sparse - O(min(m, n))
            idx_num1, idx_num2 = idx_num2, idx_num1

        res = 0
        for idx1, num1 in idx_num1.items():   # O(min(m, n))
            if idx1 in idx_num2:
                res += num1 * idx_num2[idx1]
        return res
