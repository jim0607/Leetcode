93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]



"""
Grandyang: 根据目前刷了这么多题，得出了两个经验，一是只要遇到字符串的子序列或配准问题首先考虑动态规划DP，二是只要遇到需要求出所有可能情况首先考虑用递归。
这道题并非是求字符串的子序列或配准问题，更符合第二种情况，所以我们要用递归来解。我们用k来表示当前已经分出的段数，
如果k = 4，四段已经形成，若这时字符串刚好为空，则将当前分好的结果保存。
则对于每一段，我们分别用一位，两位，三位来尝试，分别判断其合不合法，如果合法，则调用递归继续分剩下的字符串，最终和求出所有合法组合.
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(substr, intervals, path):
            if intervals == 4:
                if not substr:
                    res.append(path[:-1])
                return
            
            if intervals > 4:
                return
            
            # choose next interval, the lens of next interval could be 1-3, so there are three cases
            for i in range(1, 4):
                if i <= len(substr):    # the digits we cohose should no more than the lens of s
                    if i == 1:          # choose one digit for the next interval
                        dfs(substr[i:], intervals + 1, path + substr[:i] + ".")
                        
                    elif i == 2 and substr[0] != "0":      # choose two digits, the first one should not be "0" cuz "01" is not valid interval
                        dfs(substr[i:], intervals + 1, path + substr[:i] + ".",)
                        
                    elif i == 3 and substr[0] != "0" and int(substr[:3]) <= 255:  # choose three digits, the first one should not be "0" and should be less than 256
                        dfs(substr[i:], intervals + 1, path + substr[:i] + ".")
                        
        res = []
        dfs(s, 0, "")
        
        return res