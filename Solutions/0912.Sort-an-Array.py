# solution 2: quick sort
"""
另一个采用分而治之策略的排序算法是快速排序，其优势是不需要额外的存储空间，这一点比归并排序强。
快速排序的思路是依据一个“中值”数据项来把数据表分为两半：小于中值的一半和大于中值的一半，然后每部分分别进行快速排序
输入list, i, j; 输出：list中以list[i]为pivot分为左右两边，左边小于pivot，右边大于；输出分边之后pivot所在的位置。
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self._quickSort_(nums, 0, len(nums) - 1)
        return nums
    
    def _partition_(self, arr: List[int], i: int, j: int) -> int:
        """
        return the pivot position where on the left, the values are less than the pivot, on the right, the values are larger
        """
        # we choose arr[i] as the pivot value
        pivot = arr[i]

        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]

        arr[i] = pivot
        
        return i

    def _quickSort_(self, arr: List[int], start, end):
        """
        sort the arr based on the partition position, using recursion, no return
        """
        if start >= end:
            return
        pivotPos = self._partition_(arr, start, end)
        self._quickSort_(arr, start, pivotPos - 1)
        self._quickSort_(arr, pivotPos + 1, end)
        
        
# solution 1: merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self._mergeSort_(nums)

    def _mergeSort_(self, arr):
        """
        use divide and conquer to sort an arr, no the arr
        """
        lens = len(arr)
        if lens <= 1:
            return arr  # if return None, then leftArr = self._mergeSort_(arr[:mid]) could be a typeErrot: object of type "NoneType has no len()"
        # divide
        mid = lens // 2
        # this leftArr, rightArr is neccessary for the merge part, and that is why
        # merge sort takes O(N) space
        leftArr = self._mergeSort_(arr[:mid])
        rightArr = self._mergeSort_(arr[mid:])

        # conquer/merge
        i, j, k = 0, 0, 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
            
        return arr
