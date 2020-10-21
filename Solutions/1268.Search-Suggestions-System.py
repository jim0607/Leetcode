"""
1268. Search Suggestions System

Given an array of strings products and a string searchWord. We want to design a system that suggests 
at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with the searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
"""

    
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.words = []     # self.words store a list of words that pass curr node.
        

class Trie:
    
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self._insert(word)
            
    def _insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
            curr.words.append(word)
        
    def search(self, word):     # returns a list of words that include the input word.
        curr = self.root
        res = []
        for ch in word:
            if ch not in curr.child:
                return res
            curr = curr.child[ch]
        res += curr.words
        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)           # 把所有的products放入到Trie
        res = [[] for _ in range(len(searchWord))]
        for i in range(len(searchWord)):
            search_res = trie.search(searchWord[:i+1])
            if len(search_res) == 0:    # 如果这个已经找不到start_with这个substring的了，后面的substring更找不到
                break
            search_res.sort()       # 取lexicographically前三个输出
            res[i] += search_res[:3]
        return res 
    
    
    
    
"""
In TrieNode, there should be self.child, self.is_end, self.word;
In Trie, there should be a method to insert a word into the trie; there should also be 
a method to search for all the possible autocomplete words of a given input string;
这个search mehtod分三步，第一步是遍历Trie找到需要search的input_str在trie中所在的node, 第二步是从这个node出发，
找到其所有能到达的endNode, 显然是backtrack来做，第三步是对所有能达到的endNode.word排个序，取前三作为输出。
"""
class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        self.word = ""
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):   
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
            
        curr.is_end = True
        curr.word = word
        
    def search(self, input_str):
        res = []
        curr = self.root
        for ch in input_str:
            if ch not in curr.child:
                return res
            curr = curr.child[ch]
            
        self.backtrack(curr, res)
        
        return sorted(res)[:3]
    
    def backtrack(self, curr, res):     # O(depends on the number of solutions)
        if curr.is_end:
            res.append(curr.word)
        for next in curr.child.values():
            self.backtrack(next, res)
            

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:    # O(sum of all lens of product in products)
            trie.insert(product)
            
        input_str = ""
        res = []
        for ch in searchWord:
            input_str += ch
            res.append(trie.search(input_str))
            
        return res
