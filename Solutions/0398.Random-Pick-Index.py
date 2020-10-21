"""
398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""


"""
reservoir sampling: 特点是来一个算一下，因此适用于data stream.
算法：
来第一个num: 选第一个num的概率为1/1；
来第二个num: 选第二个num的概率为1/2; 选第一个num的概率为(1-1/2)*1/1 = 1/2
来第三个num: 选第三个num的概率为1/3; 选第一个num的概率为(1-1/3)*1/2 = 1/3; 选第一个num的概率为(1-1/3)*1/2 = 1/3;
来第四个num: 选第四个num的概率为1/4; 选第一个num的概率为(1-1/4)*1/3 = 1/4; 选第二个num的概率为(1-1/4)*1/3 = 1/4; 选第三个num的概率为(1-1/4)*1/3 = 1/4;
来第m个num: 选第m个num的概率为1/m; 选第一个num的概率为(1-1/m)*1/(m-1) = 1/m..........
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        m = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                m += 1
                random_idx = random.randrange(m)
                if random_idx == 0:     # 这里不一定random_idx == 0, 我们用random_idx等于啥都行，我们需要的只是等于某一个数的概率是1/m
                    res = i
        return res



"""
O(N) time O(N) space using random.choice(seq): Return a random element from the non-empty sequence seq.
"""
from random import choice

class Solution:

    def __init__(self, nums: List[int]):
        self.pos_dict = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.pos_dict[num].append(i)

    def pick(self, target: int) -> int:
        print(self.pos_dict)
        return choice(self.pos_dict[target])
    
或者这样写也是一样的：
from random import randrange

class Solution:

    def __init__(self, nums: List[int]):
        self.pos_dict = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.pos_dict[num].append(i)

    def pick(self, target: int) -> int:
        random_idx = randrange(len(self.pos_dict[target]))
        return self.pos_dict[target][random_idx]
