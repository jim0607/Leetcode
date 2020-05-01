Quick sort: 先整体有序，在局部有序的算法
先任意找一个值作为pivot，然后partition：把小于pivot的值放在pivot的左边，大于pivot的值放到右边，返回pivot的位置。
这样整个数组就变得“有序”了: 左边都大于pivot，右边都小于pivot。
然后再对左右两边分别递归进行局部有序就可以了。

Merge sort: 先局部有序，在整体有序的算法
先将数组根据mid的位置分为左右两边，然后分别排序，得到左右两边都排好序的数组。
最后merge：把左右两边排好序的数组的元素进行比较，完成最后的排序。


                   Quick sort                              vs.                             Merge Sort

Time:     N*logN in average, N^2 worst case:                                          N*logN in best and worst case
          every time choose the minimum or maximum
          as povit value, eg:(1,2,3,4,5,6,7,8), then the
          time complexity is N^2
          
Space:    O(1)                                   O(N) because need to merge leftArr and rightArr into one array

Stable:   No                                     Yes, meaning for example: [3,2,1,3,4], there are two 3s in the unsorted arr
                                                 after merge sort, the number 3 on the left will still be on the left, while
                                                 the 3 on the right will still on he riht in the sorted arr [1,2,3,3,4]
                                                         
                                                         
                                                        
python 内置的sort()函数是结合了merge sort 和 insertion sort 的一种排序， 叫Timsort
https://www.cnblogs.com/clement-jiao/p/9243066.html
  
  
  
912. Sort an Array

# solution 2: quick sort
"""另一个采用分而治之策略的排序算法是快速排序，其优势是不需要额外的存储空间，这一点比归并排序强。
Quick sort: 先整体有序，再局部有序的算法
先任意找一个值作为pivot，然后partition：把小于pivot的值放在pivot的左边，大于pivot的值放到右边，返回pivot的位置。这样整个数组就变得“有序”了: 左边都大于pivot，右边都小于pivot。然后再对左右两边分别递归进行局部有序就可以了。
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self._quickSort_(nums, 0, len(nums) - 1)
        return nums
    
    # 输入list, i, j; 输出：list中以list[i]为pivot分为左右两边，左边小于pivot，右边大于；输出分边之
    # 后pivot所在的位置。这就是先整体有序，再局部有序。
  
    # _partition_的模板要牢记！！
    def _partition_(self, arr, i, j):
	
        pivot = arr[i]

        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]

        arr[i] = pivot		# 返回pivot点到数组里面！
        
        return i

    def _quickSort_(self, arr, start, end):	
        if start >= end:
            return

        pivotPos = self._partition_(arr, start, end)
        self._quickSort_(arr, start, pivotPos - 1)
        self._quickSort_(arr, pivotPos + 1, end)



 
Merge sort: 先局部有序，再整体有序的算法
先将数组根据mid的位置分为左右两边，然后分别排序，得到左右两边都排好序的数组。
最后merge：把左右两边排好序的数组的元素进行比较，完成最后的排序。

# solution 1: merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self._mergeSort_(nums)

    def _mergeSort_(self, arr):		
        lens = len(arr)
        if lens <= 1:
            return arr
  
        # divide
        mid = lens // 2
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

