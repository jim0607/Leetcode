751. John's business

There are n cities on an axis, numbers from 0 ~ n - 1. John intends to do business in these n cities, He is interested in Armani's shipment. Each city has a price for these goods prices [i]. For city x, John can buy the goods from the city numbered from x - k to x + k, and sell them to city x. We want to know how much John can earn at most in each city?

Example
Example1

Input: prices = [1, 3, 2, 1, 5] and k = 2
Output: [0, 2, 1, 0, 4]
Explanation:
i = 0, John can go to the city 0 ~ 2. He can not make money because the prices in city 1 and city 2 are both higher than the price in city 0, that is, ans[0] = 0;
i = 1, John can go to the city 0~3. He can buy from city 0 or city 3 to earn the largest price difference. That is, ans[1] = 2.
i = 2, John can go to the city 0~4. Obviously, he can earn the largest price difference by buying from city 3. That is, ans[2] = 1.
i = 3, John can go to the city 1~4. He can not make money cause city 3 has the lowest price. That is, ans[3] = 0.
i = 4, John can go to the city 2~4. He can earn the largest price difference by buying from city 3. That is, ans[4] = 4.
Example2

Input: prices = [1, 1, 1, 1, 1] and k = 1
Output: [0, 0, 0, 0, 0]
Explanation:
All cities are the same price, so John can not make money, that is, all ans are 0.


class SegmentTree:

    def __init__(self, start, end, min_num):
        self.start = start
        self.end = end
        self.min_num = min_num
        self.left = None
        self.right = None

    def build(self, start, end, arr):
        if start > end:
            return None

        root = SegmentTree(start, end, arr[start])
        if start == end:
            return root

        mid = start + (end - start) // 2
        root.left = self.build(start, mid, arr)
        root.right = self.build(mid + 1, end, arr)
        root.min_num = min(root.left.min_num, root.right.min_num)

        return root

    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return float("inf")

        if start <= root.start and end >= root.end:
            return root.min_num

        return min(self.query(root.left, start, end), self.query(root.right, start, end))


class Solution:
    def business(self, prices, k):
        segment_tree = SegmentTree(0, len(prices) - 1, float("inf"))
        root = segment_tree.build(0, len(prices) - 1, prices)
        res = []
        for i, price in enumerate(prices):
            start = i - k if i - k >= 0 else 0
            end = i + k if i + k <= len(prices) - 1 else len(prices) - 1
            profit = price - segment_tree.query(root, start, end)
            res.append(profit)

        return res
