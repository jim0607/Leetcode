692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

"""
heapq solution: O(N + klogN)
"""
"""
from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqDict = collections.Counter(words)
        hq = []
        for word, freq in freqDict.items():
            hq.append((-freq, word))
            
        heapify(hq)         # O(N)
        
        res = []
        for _ in range(k):  # O(klogN)
            res.append(heappop(hq)[1])
            
        return res


"""
quick select solution: O(N + klogk)
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqDict = collections.Counter(words)   # O(N)
        freqList = []
        for word, freq in freqDict.items():     # O(N)
            freqList.append((-freq, word))
        
        self.partition(freqList, 0, len(freqList) - 1, k)   # O(N)

        res = []
        for freq, word in sorted(freqList[:k], key = lambda x: (x[0], x[1])):   # O(klogk)
            res.append(word)
            
        return res
            
    def partition(self, freqList, start, end, k):
        """
        put all high freq (low -freq) word on the left of the freqList and all low freq word on the right of the freqList, no return
        """
        if start >= end:    # 模板注意点1
            return 
        
        left, right = start, end
        pivot = freqList[(left+right)//2]
        while left <= right:    # 模板注意点2
            while left <= right and freqList[left][0] < pivot[0] or (freqList[left][0] == pivot[0] and freqList[left][1] < pivot[1]): # 模板注意点3
                left += 1
            while left <= right and freqList[right][0] > pivot[0] or (freqList[right][0] == pivot[0] and freqList[right][1] > pivot[1]):
                right -= 1
            if left <= right:
                freqList[left], freqList[right] = freqList[right], freqList[left]
                left += 1
                right -= 1
                
        if k >= left:       # 模板注意点3
            self.partition(freqList, left, end, k)
        elif k <= right:    # 模板注意点4
            self.partition(freqList, start, right, k)
