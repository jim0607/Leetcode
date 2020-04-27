Union find是一种用来解决集合查询合并的数据结构
支持O(1) find and O(1) union
本质上是一个hash map表示数据之间的对应关系。
操作：
find(A), 找点A所在集合的最上层的点
union(A, D), 合并点A和点D所在的集合
