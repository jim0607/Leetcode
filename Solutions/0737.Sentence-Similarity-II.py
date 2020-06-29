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
class UnionFind:
    
    def __init__(self):
        self.father = collections.defaultdict()
        
    def add(self, x):
        if x not in self.father:   # 注意这里要加一句判断，不然重复加入x的时候会改变father的值
            self.father[x] = x
        
    def find(self, x):
        """
        Find the father of node x
        """
        if self.father[x] == x:
            return x
        
        self.father[x] = self.find(self.father[x])
        
        return self.father[x]
        
    def connected(self, a, b):
        """
        Check if node a and node b are connected
        """
        return self.find(a) == self.find(b)        
        
    def union(self, a, b):
        """
        Union node a and node b
        """
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
        
        
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if not pairs:
            return words1 == words2
        
        lens1, lens2 = len(words1), len(words2)
        if lens1 != lens2:
            return False
        
        uf = UnionFind()
        for pair in pairs:
            uf.add(pair[0])
            uf.add(pair[1])
            uf.union(pair[0], pair[1])
        
        for i in range(lens1):
            if words1[i] not in uf.father and words2[i] not in uf.father:
                if words1[i] != words2[i]:
                    return False
            elif words1[i] in uf.father and words2[i] not in uf.father:
                return False
            elif words1[i] not in uf.father and words2[i] in uf.father:
                return False
            elif words1[i] in uf.father and words2[i] in uf.father:
                if not uf.connected(words1[i], words2[i]):
                    return False
                
        return True
