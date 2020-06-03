244. Shortest Word Distance II

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


"""
"""
如果题目要求multiple query with unlimited time, 那么一定考察的是precomputation!! precomputation记录结果一般都需要一个hash map!! 
这个思想非常重要！！这个题用dictionary记录每个word在words中的位置，这样如果这次需要query a and b, 下次需要query c and d, 
我们都可以很快找到他们的位置。"""

class WordDistance:
    # 注意constructors中的参数在instantiate这个class之后是不会变的，会变的只是shortest mehods中的arguments: word1 and word2. 
    # 所以这题是不断改变word1 and word2进行multiple query的问题
    def __init__(self, words: List[str]):   
        self.posDict = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.posDict[word].append(i)    # should be noted that the list is sorted
        
    # 注意可能会有重复的query，比如第一次query a and b, 第三次又需要query a and b
    # 这时候为了为了避免重复计算，我们可以直接用memo/cache保存query a and b 的结果
    # 这个思想非常重要！！这个思想成立的前提是memory不值钱！
    def shortest(self, word1: str, word2: str) -> int:
        """
        直接去self.posDict里面去找就可以了，如果len(posDict[word1])=1 and len(posDict[word])=1e10, then we use binary search: O(MlogN). if the lengths are similar, we use one pass O(M+N)
        """
        cache = collections.defaultdict(int)   # use a cache to store the alreay calculated resuts
        if (word1, word2) in cache:
            return cache[(word1, word2)]
        if (word2, word1) in cache:
            return cache[(word2, word2)]
        
        i, j = 0, 0
        minDist = abs(self.posDict[word1][0] - self.posDict[word2][0])
        while i < len(self.posDict[word1]) and j < len(self.posDict[word2]):
            if self.posDict[word1][i] > self.posDict[word2][j]:
                j += 1
            else:
                i += 1
            if i < len(self.posDict[word1]) and j < len(self.posDict[word2]):
                minDist = min(minDist, abs(self.posDict[word1][i] - self.posDict[word2][j]))
        
        cache[(word1, word2)] = minDist
        return minDist
            

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)



Follow up 1: 
你都用两个额外空间去存结果以达到加速的目的了（一个是dictinoary存放每个word在words中的位置，另一个是cache/memo记录已经query过的a and b的结果）
可是面试官还不开心，他还希望调用 query method 能更快一些，怎么办？
那咱们就采用最极端的方法：把所有words里可能的word1 and word2组合的结果都算出来存到cache中，这样所有的query 就都是O(1)了
这个方法的前提是words list是不会变的，如果重新instantiate一个class把constrcutor里的words list变了那之前的所有结果就都白算了。
