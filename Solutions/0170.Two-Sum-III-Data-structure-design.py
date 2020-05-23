170. Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numsDict = collections.defaultdict(lambda: 0) # val is num val, key is how namy times the val was added, initilized as 0

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.numsDict[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key, val in self.numsDict.items():
            if value - key in self.numsDict:
                if value - key != key:
                    return True
                else:
                    if self.numsDict[key] > 1:
                        return True
                    
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
