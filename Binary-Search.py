1. 比O(N)更好的算法一定是O(logN)，O(logN)一定是二分法。如果面试官不满意O(N)的时间复杂度，那么一定是考二分法。
另外，如果题目说了是排序数组，那就是在疯狂暗示使用二分法。

2. 使用递归和非递归的权衡，问面试官即可，一般能不递归就不递归。

3. 通用的二分法模板：九章算法
	start, end = 0, lens-1
	while start + 1 < end:   
		mid = start + (end - start) // 2 #防止溢出，尤其是在left和right都很大的情况下
		# 循环内只写两个分支，一个分支排除中位数，另一个分支不排除中位数，循环中不单独对中位数作判断,这一点很重要，
		# 希望读者结合具体练习仔细体会，每次循环开始的时候都单独做一次判断，在统计意义上看，二分时候的中位数恰好是目标元素的概率并不高，
		# 并且即使要这么做，也不是普适性的，不能解决绝大部分的问题。
    		if nums[mid] >= target:  # 注意这个模板是在遇到相等的就去掉右边的，所以是一个劲的往左逼近。
			end = mid
		else:
			start = mid
	# 二分法的本质是夹逼法：在每一轮循环中排除一半以上的元素，于是在对数级别的时间复杂度内，就可以把区间“夹逼” 只剩下 1 个数，
	# 而这个数是不是我们要找的数，单独判断就可以了。
	if nums[start] == target:
		return start
	if nums[end] == target:   # 注意这里的顺序，先判断start还是先判断end，取决于是想找first position of X还是last position of x，把start放在前面return可以保证return到的是first position of X.比如[1,2,3,3,3,3,4,5]，一直往左逼就可以找到first position of 3
		return end
	return -1
  
4. 理解二分法的三个境界：
    1. 熟记背诵模板
    2. OOXX的思考方法解决找数组当中first X或者last O的问题，注意要画图可以帮助理解好问题，有时候空想是想不出来的。
    3. Half half是二分法本质，每次去掉没有答案的那一半，保留有答案的那一半。
				

		
二分法——二分答案   eg: sqrt(x), Koko Eating Bananas, Wood Cut
Binary Search on Result
往往没有给你一个数组让你二分
同样是找到满足某个条件的最大或者最小值
模板：
start, end = 0, max	# 1. 找到可行解范围
while start + 1 < end:   
    mid = start + (end - start) // 2 
    if check(mid): 
	start = mid
    else:
	end = mid
