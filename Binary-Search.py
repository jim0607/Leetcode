1. 比O(N)更好的算法一定是O(logN)，O(logN)一定是二分法。如果面试官不满意O(N)的时间复杂度，那么一定是考二分法。

2. 使用递归和非递归的权衡，问面试官即可，一般能不递归就不递归。

3. 通用的二分法模板：
  while start < end:
    mid = start + (end-start) // 2
    if 
  
  
4. 理解二分法的三个境界：
    1. 熟记背诵模板
    2. OOXX的思考方法解决first X或者last O的问题，注意要画图可以帮助理解好问题，有时候空想是想不出来的。
      eg: sqrt(x); search a 2D matrix; search insertion position; First bad version; Wood count; Search in a big sorted array, Recover rotated array; Find minimum in Rotate sorted Array II, maximum number in mountain
    3. Half half是二分法本质，每次去掉没有答案的那一半，保留有答案的那一半。
      eg: Find peak element; Search in rotated sorted array
