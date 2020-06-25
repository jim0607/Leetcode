381. Insert Delete GetRandom O(1) - Duplicates allowed

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();


"""
这题是之前那道 Insert Delete GetRandom O(1) 的拓展，与其不同的是，之前那道题不能有重复数字，而这道题可以有，
那么就不能像之前那道题那样建立每个数字和其坐标的映射了，但是我们可以建立数字和其所有出现位置的集合set之间的映射，
虽然写法略有不同，但是思路和之前那题完全一样。
对于 insert 函数，我们在数组 nums 末尾加入 val，然后将val所在 nums 中的位置idx加入 dict[val] set中。
remove 函数是这题的难点，我们首先看 HashMap 中有没有 val，或者有val但是对应的idx set 为空，则直接返回 false。
然后跟380是一样的。我们取出 nums 的尾元素和眼删除的元素调换位置，
如果dict[val]有多个元素，那我们就pop set中的一个元素，当然要记录其对应的idx然后把idx的位置填上last_num, 还要更新last_num在pos_dict中的新位置。
"""
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos_dict = collections.defaultdict(set)
        self.arr = []
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        not_included = True
        if val in self.pos_dict:
            not_included = False
        
        self.arr.append(val)
        self.pos_dict[val].add(self.size)
        self.size += 1
        
        return not_included

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.pos_dict or not self.pos_dict[val]:  # 注意要判断self.pos_dict[val]的set为空，不然下面的pop会报错
            return False
        
        last_num = self.arr[-1]
        need_delete_idx = self.pos_dict[val].pop()      # set.pop() removes a random element from the set

        self.arr[need_delete_idx] = last_num
        self.arr.pop()
        
        # 现在last_num从最尾部挪到了need_delete_idx处，所以last_num对应的位置是need_delete_idx了
        # 所以要加把need_delete_idx到pos_dict[last_num]的set里，**** 同时要把last_num之前的idx(尾部)从set中移除出去 ****
        self.pos_dict[last_num].add(need_delete_idx)    
        self.pos_dict[last_num].remove(self.size - 1)      
        
        self.size -= 1
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        rand_idx = random.randrange(0, self.size)
        return self.arr[rand_idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
