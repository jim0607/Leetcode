384. Shuffle an Array

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();


"""
randrange(): Python offers a function that can generate random numbers from a specified range and 
also allowing rooms for steps to be included, called randrange() in random module. 
Syntax: random.randrange(start(opt),stop,step(opt)), will return random numbers in range [start, stop), with step step.
# step 1: generate a random idx after i;
# step 2: swap the num in i with random idx after i, then we have got the random num for ith pos;
# step 3: keep going forward until we generate all the random num based on random idx;
"""

from random import randrange

class Solution:

    def __init__(self, nums: List[int]):
        self.reset_arr = nums.copy()        # has to be a deep copy
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.reset_arr.copy()    # has to be a deep copy
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        lens = len(self.arr)
        for i in range(lens):
            random_idx = randrange(i, lens)     # O(1)
            self.arr[i], self.arr[random_idx] = self.arr[random_idx], self.arr[i]
            
        return self.arr

"""
Google follow up: 写test方案证明shuffle符合要求。
那就跑N次，假设N很大，然后跑完之后在每个位置上出现的数字的概率是不是都在[1/lens - margin, 1/lens + margin]内, margin很小比如1e-8
"""
def check_random_shuffle(self, nums, N, margin):
    cnt_dict = collections.defaultdict(lambda: collections.defaultdict(int))        # 记录在某个idx上出翔某个数的次数
    for i in range(N):
        self.shuffle(nums)
        for idx in range(lens):
            cnt_dict[idx][nums[idx]] += 1

    for idx, dict in cnt_dict.items():
        if len(dict) == lens:           # 如果有的数从来不能出现在一个idx上，那说明不是random的
            return False
        for num, cnt in dict.items():
            if not (1 / lens - margin <= cnt / N <= 1/ lens + margin):      # 如果有的数出现的概率偏高或偏低就说明不是random的
                return False
    
    return True
