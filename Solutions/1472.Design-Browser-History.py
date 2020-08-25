1472. Design Browser History

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. 
Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. 
Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
 

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.


"""
soution 1: simple: one list store the browse history, one pointer point at where we are at the list.
"""
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.idx + 1]
        self.history.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        back_idx = max(self.idx - steps, 0)
        self.idx = back_idx
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        forward_idx = min(self.idx + steps, len(self.history) - 1)
        self.idx = forward_idx
        return self.history[self.idx]


"""
solution 2: two stacks.
"""
class BrowserHistory:

    def __init__(self, homepage: str):
        self.forw_memo = []     # forw_memo stores the future url
        self.back_memo = []     # back_memo stores the previous url
        self.curr_url = homepage

    def visit(self, url: str) -> None:
        self.back_memo.append(self.curr_url)
        self.curr_url = url
        self.forw_memo = []      # clear forw_memo
        
    def back(self, steps: int) -> str:
        while self.back_memo and steps >= 1:
            self.forw_memo.append(self.curr_url)
            pop_url = self.back_memo.pop()
            self.curr_url = pop_url
            steps -= 1
        
        return self.curr_url

    def forward(self, steps: int) -> str:
        while self.forw_memo and steps >= 1:
            self.back_memo.append(self.curr_url)
            pop_url = self.forw_memo.pop()
            self.curr_url = pop_url
            steps -= 1
            
        return self.curr_url           
