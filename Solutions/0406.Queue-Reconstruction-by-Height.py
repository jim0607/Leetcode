406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


"""
Greedy: Since short people will not disturb/affect the relative order of taller people so we can start from tallest guy(s).
We first sort the list people, in the order of descending height. 
If multiple people are of the same height, sort them in ascending order of the number of people in front of them. 
Then for each person [i,j], we insert it into res based on j. This is inserting it into j can garantee j is the right
pos for i, and at the same time, does not disturb the relative order of previous peope, cuz previous people are taller.
We illustrate the above procedure with people_sorted, as i goes from 0 to 5, the empty list res changes as follows:
[[7,0]] (insert [7,0] at index 0)
[[7,0],[7,1]] (insert [7,1] at index 1)
[[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
[[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
[[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for height, pos in people:
            res.insert(pos, [height, pos])
        return res
