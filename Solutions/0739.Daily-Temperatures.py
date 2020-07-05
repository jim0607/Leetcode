739. Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


"""
维护一个单调递减栈即可
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st = []
        res = [0] * len(T)
        for i, temp in enumerate(T):
            while st and st[-1][0] < temp:    # 注意一般先写这个while loop把该pop出来的都pop出来，然后再去处理append.
                top = st.pop()
                res[top[1]] = i - top[1]
                
            if not st or st[-1][0] >= temp:
                st.append((temp, i))
                
        return res
