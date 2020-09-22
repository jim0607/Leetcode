"""
451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""



"""
solution 2: Bucket sort - O(N)
Firstly, observe that because all of the characters came out of a String of length n, the maximum frequency for any one character is n. 
This means that once we've determined all the letter frequencies using a HashMap, we can sort them in O(n) time using Bucket Sort. 
Recall that for our previous approaches, we used comparison-based sorts, which have a cost of O(nlogn).
Recall that Bucket Sort is the sorting algorithm where items are placed at Array indexes based on their values (the indexes are called "buckets"). 
For this problem, we can put our chars in buckets/indexes based on their frequency, we'll have a List of characters at each index.
While we could simply make our bucket Array length n, we're best to just look for the maximum value (frequency) in the HashMap. 
That way, we only use as much space as we need, and won't need to iterate over lots of empty buckets.

Bucket sort的本质是让idx含信息，把信息压缩到idx里，变相用空间换时间了。
In order to use bucket sort:
step 1: 确定把什么放进bucket里做idx, 什么做idx对应的val, 这一题是把freq当做idx来放入bucket中, idx对应的val是a list of chars having the same freqency;
step 2: 确定bucket size, 这一题是use max_freq as our bucket size;
step 3: O(N) 遍历把相应的(freq, ch) pair 放到相应的(idx, ch)上, 这样一来high freq的ch就天然的放在bucket数组后面了, 就不需要sort了
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return s
        
        freq = collections.defaultdict(int)
        for ch in s:
            freq[ch] += 1
            
        max_freq = max(freq.values())   # we use max_freq as our bucket size, in order to use bucket sort, the first step is to 确定bucket size
            
        bucket = [[] for _ in range(max_freq + 1)]
        for ch, cnt in freq.items():
            bucket[cnt].append(ch)      # 把freq当做idx来放入bucket中，这样一来high freq的ch就天然的放在bucket数组后面了, 就不需要sort了
        
        res = ""
        for i in range(len(bucket) - 1, -1, -1):     # 这里的index i就是freq
            for ch in bucket[i]:
                res += ch * i
            
        return res


"""
也可以idx is frequency, values 直接就是string了
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s or len(s) <= 2:
            return s
        
        counter = collections.Counter(s)
        
        max_cnt = max(cnt for cnt in counter.values())
        freq_to_str = ["" for _ in range(max_cnt + 1)]    # idx is freq, values is str
        for ch, cnt in counter.items():
            freq_to_str[cnt] += ch * cnt
        
        res = ""
        for i in range(len(freq_to_str) - 1, -1, -1):
            res += freq_to_str[i]
        return res 
    
    


"""
solution 1: use hash map, and then convert to list, then sort, then conver to string - O(nlogn)
"""
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.defaultdict(int)
        for ch in s:
            freq[ch] += 1
            
        lst = []
        for ch, cnt in freq.items():
            lst.append((cnt, ch))
            
        lst.sort(key = lambda x: (-x[0], x[1]))
        
        res = ""
        for ch, cnt in lst:
            res += ch * cnt
            
        return res
