6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I




"""
Instead of convert into:
P     I    N
A   L S  I G
Y A   H R
P     I

we convert it into this:
P A Y P
    A
  L
I S H I
    R
  I
N G

and then we can get our res
"""
class Solution:
    def convert(self, s: str, n: int) -> str:
        if not s:
            return s
        if n == 1 or n == len(s):
            return s
        
        # step 1: construct a zigzag matrix
        zigzag = []
        curr_row = []
        row = 0
        for ch in s:
            if row % (n - 1) == 0:
                curr_row.append(ch)
                if len(curr_row) == n:
                    zigzag.append(curr_row)
                    curr_row = []
                    row += 1
            else:
                pos = n - 1 - row % (n - 1)     # position where the only one ch should be places
                curr_row = [" "] * pos + [ch] + [" "] * (n - 1 - pos)
                zigzag.append(curr_row)
                curr_row = []
                row += 1
        if curr_row:        # 处理最后一行
            curr_row += [" "] * (n - len(curr_row))
            zigzag.append(curr_row)

        # step 2: return the res
        res = ""
        for j in range(len(zigzag[0])):
            for i in range(len(zigzag)):
                res += zigzag[i][j] if zigzag[i][j] != " " else ""
        return res
