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
          
Space:    O(1)                                           O(N) because need to merge leftArr and rightArr into one array

Stabel:   No                                             Yes, meaning for example: [3,2,1,3,4], after merge sort, the number 3
                                                         on the left will still be on the left in the sorted arr [1,2,3,3,4]
                                                         
                                                         
                                                        
python 内置的sort()函数是结合了merge sort 和 insertion sort 的一种排序， 叫Timsort
https://www.cnblogs.com/clement-jiao/p/9243066.html
