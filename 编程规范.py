1. 每次用arr[i]之前都要保证0 <= i < lens

2. 第一行往往用来判断特殊情况(coner/edge case). eg:
   if not matrix or not matrix[0]:
      return False

3. Google要求运算符两边都要有空格

4. 先写主函数，然后再写需要调用的子函数，这样即使子函数写不完，面试官也可以知道主体算法是否可行

5. 一个好习惯是定义全局变量. eg: EMPTY = 0, FULL = 1, OCCUPPIED = 1.
   这样在后面的程序中就不用再用0, 1, 2了，直接用EMPTY, FULL, 这样可以增加程序的可读性。
   也可以在主函数中定义全局变量self.EMPTY = 0
   在调用的时候都是用self.EMPTY
   
6. 养成命名有意义的好习惯，不要用dp, dic, q, deq, hq 之类的名字了，用minCnts, freqDict, minEndTimes 等等名字。
