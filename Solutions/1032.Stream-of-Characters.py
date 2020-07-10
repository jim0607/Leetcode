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
Query takes O(L) where L is the word in the trie, so it is really constant time for query.
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
        for ch in self.letters[::-1]:       # 注意letters这里也要reverse来遍历
            if curr.is_end:
                return True
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
            
        return curr.is_end
