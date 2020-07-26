531. Lonely Pixel I

Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.



"""
one pass to store number of "B" in col_cnt and row_cnt;
another pass to find where col_cnt == 1 or row_cnt == 1
"""
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        col_cnt = collections.defaultdict(int)
        row_cnt = collections.defaultdict(int)
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        cnt = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    if row_cnt[i] == 1 and col_cnt[j] == 1:
                        cnt += 1
        return cnt
