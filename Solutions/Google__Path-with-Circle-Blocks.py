Google 新题

There is a square. bottom left is (0.0, 0.0), top right is (1.0, 1.0).

There are a number of circular blockages in the square. We know the centers as well as the radii of the circles. 

Return whether we can go from bottom left to top right.


"""
Solution: Union-Find all the circles
O(N^2)
"""
"""

class UnionFind:

    def __init__(self):
        self.father = collections.defaultdict()

    def add(self, x):
        self.father[x] = x

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connected(self, a, b):
        return self.father[a] == self.father[b]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b


class Solution:

    def __init__(self, circles):        # connect all the circles that are overlapping with each other
        self.uf = UnionFind()
        for circle in circles:
            self.uf.add(circle)

        for i in range(len(circles) - 1):
            for j in range(i + 1, len(circles)):
                if self.circle_overlap(circles[i], circles[j]):
                    self.uf.father[circle[i]] = circle[j]

    def can_pass(self, circles):
        for i in range(len(circles) - 1):
            for j in range(i + 1, len(circles)):
                if self.uf.connected(circles[i], circles[j]):
                    if ( self.touching_left(circles[i]) and self.touching_right(circles[j]) ) \
                        or ( self.touching_left(circles[i]) and self.touching_down(circles[j]) ) \
                        or ( self.touching_up(circles[i]) and self.touching_down(circles[j]) ) \
                        or ( self.touching_up(circles[i]) and self.touching_right(circles[j]) ) \
                        or (self.touching_left(circles[j]) and self.touching_right(circles[i])) \
                        or (self.touching_left(circles[j]) and self.touching_down(circles[i])) \
                        or (self.touching_up(circles[j]) and self.touching_down(circles[i])) \
                        or (self.touching_up(circles[j]) and self.touching_right(circles[i])):
                        return False
        return True

    def circle_overlap(self, c1, c2):   # return whether two circles overlap or not
        return c1.radii + c2.radii >= ( (c1.x - c2.x) ^ 2 + (c1.y - c2.y) ^ 2 ) ^ 0.5

    def touching_left(self, c):         # return whether a circle is touching the left bound
        return abs(c.x) <= c.radii

    def touching_right(self, c):         # return whether a circle is touching the left bound
        return abs(c.x - 1) <= c.radii

    def touching_down(self, c):         # return whether a circle is touching the left bound
        return abs(c.y) <= c.radii

    def touching_up(self, c):         # return whether a circle is touching the left bound
        return abs(c.y - 1) <= c.radii
