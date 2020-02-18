1. for i in range(start, end, t)中，这个i一定是包含start, 不包含end, t可正可负
t 属于 [start, end), 如果start=end, 那么i是不存在的，也就是说不会进入for循环中。

2. 将arr变成string: "".join(arr) 时间复杂度是O(N)
case 1: 如果arr中的element是string, eg: ["1", "2", "3"], 则用 "".join(arr) 输出 "123"
case 2: 如果arr中的element是int, eg: [1, 2, 3], 则用 "".join(map(str, arr)) 输出 "123". map(str, arr) is to map every element in an array into string type
      
3. 将string变成arr: arr = list(string), 时间复杂度是O(N)
      
4. 初始化创建
      
