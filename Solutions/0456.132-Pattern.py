456. 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].



"""
solution: 从右往左，维护一个单调递减栈，while loop是为了保证选出一个最接近num的two, 这样num作为three, 下一个进来的num就更容易小于two了！
"""
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        two = -float("inf")
        st = []
        for num in nums[::-1]:
            if num < two:       # 进来一个num就把他当做是one用, 如果小于two的话那就return True
                return True     # 如果大于two, 那就当three用，用while loop里找比他小但尽量大的two
            
            # 这个while loop是为了保证选出一个最接近num的two, 这样num作为three, 下一个进来的num就更容易小于two了
            while len(st) > 0 and num > st[-1]:
                two = st.pop()      # 让two尽可能大同时不超过three
                
            st.append(num)
                
        return False
