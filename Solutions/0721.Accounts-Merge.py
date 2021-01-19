"""
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
         ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)    # 建一个uf图

        # step 1: map email to name for fast access name from email
        email_to_name = defaultdict(str)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                
        # step 2: 接下来把uf图里面连到一起的email放到一起去. 这里没有想出来
        root_to_emails = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            root_to_emails[root].append(email)
            
        # step 3: 输出结果
        res = []
        for root, emails in root_to_emails.items():
            name = email_to_name[root]
            account = [name]
            account += sorted(emails)
            res.append(account)
        return res
    
    
class UnionFind:
    
    def __init__(self, accounts):
        self.father = defaultdict(str)
        for account in accounts:
            for email in account[1:]:
                self.add(email)
                self.union(email, account[1])   # 将同一个acount下的email都连接起来
                    
    def add(self, x):
        if x not in self.father:
            self.father[x] = x
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
