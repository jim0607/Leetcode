737. Sentence Similarity II

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].


"""
Different from Sentence SImilarity I, similarity relation is transitive. 
Two words are similar if they are the same, or are in the same connected component of this graph.  
So we can use union find to connect all the similar words. 
Using path compression, the time complexity is almost O(1) for find method and union mehtod. 
So the overall complexity is ~O(N) where N is the lens of words1.
"""
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        uf = UnionFind(pairs)
        
        for i in range(len(words1)):
            if not uf.connected(words1[i], words2[i]):
                return False
            
        return True
    
    
class UnionFind:
    
    def __init__(self, pairs):
        self.father = collections.defaultdict(str)
        for u, v in pairs:
            if u not in self.father:    # 注意将word add到图中之前要判断其是否已经在图中了，
                self.father[u] = u      # 不然重复加入x的时候会改变father的值，而导致father出错！！
            if v not in self.father:
                self.father[v] = v
                
            self.union(u, v)
            
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
