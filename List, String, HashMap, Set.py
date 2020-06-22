List

1. for i in range(start, end, t)中，这个i一定是包含start, 不包含end, t可正可负
t 属于 [start, end), 如果start=end, 那么i是不存在的，也就是说不会进入for循环中。

2. 将arr变成string: "".join(arr) 时间复杂度是O(N)
case 1: 如果arr中的element是string, eg: ["1", "2", "3"], 则用 "".join(arr) 输出 "123"
case 2: 如果arr中的element是int, eg: [1, 2, 3], 则用 "".join(map(str, arr)) 输出 "123". 
      map(str, arr) is to map every element in an array into string type
      
      最大的int:  import sys
                  max = sys.maxsize
                  min = -sys.maxsize - 1
      
3. 将string变成arr: arr = list(string), 时间复杂度是O(N)
      
4. Somehow these two are different: [collections.defaultdict(lambda: 1) for _ in range(lens)] and [collections.defaultdict(lambda: 1)] * lens
   don't know why....., I guess it is safe to always define any array in this way: [someDataStructure for _ in range(lens)]
   初始化创建2D array: dp = [[None] * len_col for _ in range(len_row)]
   length of 2D array: len_row = len(dp), len_col = len(dp[0])
   初始化创建3D array: dp = [[[0 for _ in range(target + 1)] for _ in range(k +  1)] for _ in range(lens + 1)]
      
5. array支持相加: eg: [1, 2] + [3, 4] = [1, 2, 3, 4]
                     [1, 2].append([3, 4]) = [[1, 2], [3, 4]]
      
6. 反转list: arr = arr[::-1]
      
7. Tuple is immutable while list is mutable.
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, 
whereas lists use square brackets.
eg of immutable: tuple1 = (10, 20, "ch1", "ch2"), tuple1[0] = 3 is not valid because we cannot change the value in a tuple.
      
8. Sort
list.sort(key=..., reverse=...)
A = [1, 3, 2, 4], A.sort() -> A = [1, 2, 3, 4]
A = [1, 3, 2, 5], A.sort(reverse = True) -> A = [4, 3, 2, 1]
B = sorted(A)  ->  B = [1, 2, 3, 4]
A = [[5, 4], [6, 7], [6, 4], [2, 6]]
A.sort(key = lambda x: x[0]) -> A = [[2, 6], [5, 4], [6, 7], [6, 4]]
A.sort(key = lambda x: (x[0], x[1])) -> A = [[2, 6], [5, 4], [6, 4], [6, 7]]  
      
9. ArrayList or Dynamic Array 不需要提前定义list的大小，根据存储数据的多少而增加大小。
实现方法：倍增思想：比如一开始给10个位置，往里面存数据，存满之后需要存第11个数据的时候，重新开一个大小为10*2的位置，把之前的十个数据复制进去
然后把原来的大小为10的数组delete掉......依次这样下去，每次数组的大小都翻倍，这就是Double的思想。
Double思想的应用: 用二分法search in a big sorted array的时候，确定end的位置就可以这样确定。
      
10. list del, remove, pop 的区别！
https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
      
      

String
      
1. Python不支持string中元素的修改, eg: s = "ab", s[1] = "c" is not a valid operation

2. string支持相加, eg: "ab" + "cd" = "abcd"
      
3. 判断一个字符ch是不是数字字符比如"8": ch.isdigit(); 如果return true, 则说明ch是数字字符, 提取数字: int(ch) = 8 或者 ord(ch)-ord("0")=8
   判断一个字符ch是不是字母字符比如"8": ch.isalpha(); 如果return true, 则说明ch是字母字符.
      
      
Hash Map
      
In python, hash map is dictionary
1. ways to iterate over hash map:
      1. for key in dict.keys():
      2. for val in dict.values():
      3. for key, val in dict.items():
      
2. defaultdict means that if a key doesn't exsit in a dictionary, then instead of error being thrown, a new entry is created.
   dictNums = collections.defaultdict()
   如果想声明dict里面的val是int：dictNums = collections.defaultdict(int)
   如果想将默认的int值设置为1,可以使用lambda表达式: dictNums = collections.defaultdict(lambda: 1), eg: 1027. Longest Arithmetic Sequence
   edges = collections.defaultdict(list) means that value of the dictionary is a list
      
3. delete a key, val pair in a dict: del dictNums[key]
      
将list作为key放入dict会报错: unhashable type 'list'   
Reason: Dictionary keys must be immutable types and list is a mutable type. 
Solution: Cast list to a tuple. eg: 305. Number of Islands II
      
4. instead of using a cntDict, we can use the defulat Counter in Python
   from collections import Counter
   s = "suggest"
   sCnt = Counter(s)
   print(sCnt)
   --> Counter({'s': 3, 'u': 1, 'g': 2, 'e': 1, 't': 1, 'i': 1, 'o': 1, 'n': 1})
      
      
  
OrderedDict
      
The OrderedDict is a subclass of dict object in Python. 
The only difference between OrderedDict and dict is that, in OrderedDict, it maintains the orders of keys as inserted. 
The OrderedDict is a standard library class, which is located in the collections module.
ordict = collections.defaultdict()

可以把OrderedDict当做是更强大的deque
1. OrderedDict可以先进先出: OrderedDict.popitem(last=True)
2. OrderedDict可以O(1) delete: del OrderedDict(key)
3. 支持move to end: OrderedDict.move_to_end(key)
      
      

Set
Set is a hash table except it caitains only keys, not key-val pairs.
1. Set的特点是集合中的元素是唯一的，不能有重复元素
      
2. A set is a hash table, so "if item in set" has O(1) complexity
      
3. Add item to set: set.add(item), 如果item already in set, 就加不进去，但不会报错。
   Remove from set: set.remove(item)
      
4. create a set: 
      1. numSet = set(), numSet.add(1), numSet.add(2)
      2. letterSet = {"a", "e", "i", "o", "u"} 
      3. nums = [1, 2, 3, 4, 5], numsSet = set(nums)
      4. 不能numsSet = {}来create a set, 因为这是在create a dictionary
      
5. 'set' does not support indexing, so numSet[0] is wrong sytax.
      
6. 我去才发现定义visited = set(3) 是错的，只能一步步按4.1中那样定义！79. Word Search
      
7. sort a set 只能用sorted(setA). eg: for pos in sorted(positionSet):  218. The Skyline Problem
      
8. 遍历set的方法 eg: 710. Random Pick with Blacklist
   1. for num in self.unreachable_set:
   2. for i, num in enumerate(self.unreachable_set):
      
      

      
zip:
zip(*iterables)
Make an iterator that aggregates elements from each of the iterables.
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. 
The iterator stops when the shortest input iterable is exhausted. 

a = "abc"
b = "cba"
print(zip(a, b))
for ch in zip(a, b):
    print(type(ch))
    print(ch)

Output:
<class 'tuple'>
('a', 'c')
<class 'tuple'>
('b', 'b')
<class 'tuple'>
('c', 'a')
      
      
      
In python, we don't need to worry aobut get mod for negative vals because python already taken care of that: (-3) % 4 = 1, the mod always return a positive val
