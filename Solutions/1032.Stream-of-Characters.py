1032. Stream of Characters

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist




"""
If we really think about it, this is a suffix problem: 
each time we query, we go back to the previous queried letters and check if they can form a word.
Construct a Trie takes O(∑w_i) where w_i is the the lens of word in words.
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = []
        self.root = TrieNode()
        for word in words:
            self._insert(word)
            
    def _insert(self, word):        # 定义为protected, 只允许这个类和其子类访问
        curr = self.root
        for ch in word[::-1]:       # suffix problem, insert the chars in a reversed way
            curr = curr.child[ch]
        curr.is_end = True

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        curr = self.root
        for ch in self.letters[::-1]: # 注意letters这里也要reverse来遍历, 这里的reverse会导致query的时间复杂度非常高，尤其在query很频繁的情况下
            if curr.is_end:
                return True
            if ch not in curr.child:  
                return False
            curr = curr.child[ch]
            
        return curr.is_end
       
       
"""
上面的解法非常staight forward, 但是query的时间复杂度非常高，尤其在query很频繁的情况下，所以第二次再提交的时候就TLE了
一个小小的改进可以是，如果letters长度超过了the max_lens of word for word in words, 那就不用看max_lens之前的了。
所以我们可以Maintain a fixed window for letter. so that the time complexity is the max_lens of word for word in words
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.last_k = collections.deque()    # maintain a deque with size k for letters in query
        self.k = max(len(word) for word in words)
        
        for word in words:
            self._insert(word[::-1])
            
    def _insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
        curr.is_end = True        

    def query(self, letter: str) -> bool:
        self.last_k.appendleft(letter)      
        if len(self.last_k) > self.k:   # maintain a window size of k, this is why we can limit 
            self.last_k.pop()           # the time complesity of query to be O(max lens of word for word in words)
        
        curr = self.root
        for ch in self.last_k:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
            if curr.is_end:
                return True
        return curr.is_end
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
