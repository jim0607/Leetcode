1. 比O(N)更好的算法一定是O(logN)，O(logN)一定是二分法。如果面试官不满意O(N)的时间复杂度，那么一定是考二分法。另外，如果题目说了是排序数组，那就是在疯狂暗示使用二分法。

2. 使用递归和非递归的权衡，问面试官即可，一般能不递归就不递归。

3. 通用的二分法模板：九章算法
	start, end = 0, lens-1
	while start + 1 < end:   # 在退出循环的时候，一定有 left == right 成立，此时返回 left 或者 right 都可以
		mid = start + (end-start) // 2 #防止溢出，尤其是在left和right都很大的情况下
		# 循环内只写两个分支，一个分支排除中位数，另一个分支不排除中位数，循环中不单独对中位数作判断,这一点很重要，希望读者结合具体练习仔细体会，每次循环开始的时候都单独做一次判断，在统计意义上看，二分时候的中位数恰好是目标元素的概率并不高，并且即使要这么做，也不是普适性的，不能解决绝大部分的问题。
    		if nums[mid] >= target:  # 注意这个模板是在遇到相等的就去掉右边的，所以是一个劲的往左逼近。
			end = mid
		else:
			start = mid
	# 二分法的本质是夹逼法：在每一轮循环中排除一半以上的元素，于是在对数级别的时间复杂度内，就可以把区间“夹逼” 只剩下 1 个数，而这个数是不是我们要找的数，单独判断就可以了。
	if nums[start] == target:
		return start
	if nums[end] == target:
		return end
	return -1
  
4. 理解二分法的三个境界：
    1. 熟记背诵模板
    2. OOXX的思考方法解决找数组当中first X或者last O的问题，注意要画图可以帮助理解好问题，有时候空想是想不出来的。
      eg: 34（经典）153 (经典), 154, 1095, 658, 4, search a 2D matrix; Wood count; Search in a big sorted array, Recover rotated array; Find minimum in Rotate sorted Array II, maximum number in mountain
    3. Half half是二分法本质，每次去掉没有答案的那一半，保留有答案的那一半。
      eg: Find peak element; Search in rotated sorted array, 300
				
