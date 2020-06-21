710. Random Pick with Blacklist

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:
Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]



"""
很显然solution只允许O(N) space, and less then O(N) time, and also call math.random function only once at one pick
solution 3: 建立一个tricky的一一映射。
既然数字总共有N个，那么减去黑名单中数字的个数，就是最多能随机出来的个数。比如N=6，黑名单中有两个数{2, 4}，那么我们最多只能随机出四个随机数0,1,3,5，
但是我们如果直接randrange(4)的话会得到0,1,2,3, 我们发现有两个问题，一是黑名单中的2可以随机到，二是数字5没法随机到。
那么我们想，能不能随机到0,1,3就返回其本身，而当随机到2到时候，我们返回的是5，***我们需要建立这样的映射把2映射到5***，这就是使用HashMap的动机啦。
我们首先将超过N - blacklist.size()的数字(即通过randrange随机不到的数字)放入一个HashSet，这里就把{4, 5}放进去了，
然后我们遍历blacklist中的数字，如果在HashSet中的话，就将其删除，这样HashSet中就只有{5}了，这时候的hashSet中存的就是需要建立映射的数字，
而用什么数字建立，当然是用黑名单中的数字了，遍历黑名单中的数字，如果小于N - blacklist.size()的话，说明是有可能随机到的，
我们和HashSet中的数字建立映射，这个时候我们就把2和5建立映射了。从而实现在pick函数中的移魂换影大法了.
pick method 中先随机个数字，如果有映射，则返回映射值，否则返回原数字.
O(N) initialize, O(1) to call pick method, each pick method only call math.random once.
"""

import random

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.could_random_get = N - len(blacklist)    
        self.unreachable_set = set()        # 保存本应random_get到但是could not random_get的数的一一映射
        self.unreachable_dict = collections.defaultdict(int)  # 保存blacklist中的数与could not random_get的数的一一映射
        
        # 找到本应random_get到但是could not random_get的数的一一映射
        for i in range(self.could_random_get, N):
            self.unreachable_set.add(i)
        for black_num in blacklist:
            if black_num in self.unreachable_set:
                self.unreachable_set.remove(black_num)   # now we have unreachable_set with number could not random_get and needs to be 映射到unreachable_dict中
        
        # 建立blacklist中的数(可以random_get到的数)与本应random_get到但是could not random_get的数的一一映射
        i = 0
        for num in self.unreachable_set:  
            while blacklist[i] >= self.could_random_get:    # blacklist[i]如果自己都random_get不到的话，那用它去映射的数肯定也得不到呀
                i += 1
            self.unreachable_dict[blacklist[i]] = num
            i += 1
        
    def pick(self) -> int:
        rand_num = random.randrange(self.could_random_get)
        return rand_num if rand_num not in self.unreachable_dict else self.unreachable_dict[rand_num]



"""
solution 1: 用black_set每次都做判断 (Time Limit Exceeded cuz need to call math.random multipule times in pick method) 
"""

import random

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.black_set = set(blacklist)

    def pick(self) -> int:
        if len(self.black_set) == self.N:
            return -1
        
        while True:
            rand_idx = random.randrange(self.N)
            if rand_idx not in self.black_set:
                return rand_idx


"""
solution 2: use a white list (Memory Limit Exceeded cuz used two sets, the two sets could be very large)
"""

import random

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.black_set = set(blacklist)
        self.white_list = []
        for i in range(self.N):
            if i not in self.black_set:
                self.white_list.append(i)

    def pick(self) -> int:
        if len(self.white_list) == 0:
            return -1

        rand_idx = random.randrange(len(self.white_list))
        return self.white_list[rand_idx]
