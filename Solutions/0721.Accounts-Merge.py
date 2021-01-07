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


"""
union find: if email in a list, connect them.
In this way, we build a graph, then we map each disjoint_component into one name.
Step 1: use a dictionary to store email_to_name map. Step 2: iterate the edges to connect them. 
Step 3: use the email_to_name map and the graph to generage a new list where each name corresponding to a disjoint_component
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)    # 初始化uf图 by using vertex in accounts
        
        # connect the edges in the uf图
        email_to_name = collections.defaultdict(str)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                uf.union(account[1], email)
                email_to_name[email] = name
                
        # 接下来的部分是得到图里面连到一起的emails. 这里没有想出来
        # 建立root_email to emails dictionary as we go over uf.father.
        root_to_email = collections.defaultdict(list)
        for email in uf.father:
            root = uf.find(email)
            root_to_email[root].append(email)
            
        # 最后输出结果
        res = []
        for root, emails in root_to_email.items():
            account = []
            account.append(email_to_name[root])
            account += sorted(emails)
            res.append(account)
        return res
    
    
class UnionFind:
    
    def __init__(self, accounts):
        self.father = collections.defaultdict(str)
        
        for account in accounts:
            for email in account[1:]:
                self.father[email] = email
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
