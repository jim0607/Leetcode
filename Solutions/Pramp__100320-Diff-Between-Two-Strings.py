"""
Diff Between Two Strings

Given two strings of uppercase letters source and target, list (in string form) a sequence of edits to convert from source to target that uses the least edits possible.

For example, with strings source = "ABCDEFG", and target = "ABDFFGH" we might return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"

More formally, for each character C in source, we will either write the token C, which does not count as an edit; or write the token -C, which counts as an edit.

Additionally, between any token that we write, we may write +D where D is any letter, which counts as an edit.

At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign, the letters should spell out target (when ignoring plus-signs.)

In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible), and ignoring subtraction-tokens, 
spells out A, B, D, F, +F, G, +H which represents the string target.

If there are multiple answers, use the answer that favors removing from the source first.
"""




"""
source = "ABCDEFG", and target = "ABDFFGH"

This problem is easiest to attempt in two steps:
step 1: do a dp for 72. Edit Distance
step 2: construct the answer using the dp list we constructed
If source[i] == target[j] we write source[i] in the answer. If j is invalid or dp(i+1, j) <= dp(i, j+1) we write -source[i] in the answer.
Otherwise, we write +target[j].
"""
def diffBetweenTwoStrings(s, t):

    # step 1: do a dp for 72. Edit Distance
    m, n = len(s), len(t)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # if we choose to insert a ch to s, then dp[i][j] = 1 + dp[i][j-1]
                # if we choose to delete a ch from s, then dp[i][j] = 1 + dp[i-1][j]
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    # step 2: construct the answer using the dp list we constructed
    res = []
    i, j = m - 1, n - 1         # 注意要逆序遍历找path!!!!!!!
    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            res.append(s[i])
            i -= 1
            j -= 1
        else:
            if dp[i+1][j] <= dp[i][j+1]:  # need to insert a ch to s
                res.append("+" + t[j])
                j -= 1
            else:                         # need to delete a ch from s
                res.append("-" + s[i])
                i -= 1

    # 注意出了while循环之后要判断i, j
    while i >= 0:
        res.append("-" + s[i])
        i -= 1
    while j >= 0:
        res.append("+" + t[j])
        j -= 1

    return res[::-1]


source = "ABCDEFG"
target = "ABDFFGH"
diff = diffBetweenTwoStrings(source, target)
print(diff)
