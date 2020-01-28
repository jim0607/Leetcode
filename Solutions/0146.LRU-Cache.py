#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (29.50%)
# Likes:    4425
# Dislikes: 189
# Total Accepted:    421.7K
# Total Submissions: 1.4M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#
"""solution 1: use a queue to store the time-linear data and a dictionary to store the cache number
a cache实际上就是一个hashmap/dictionary"""
# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.q = collections.deque()    # 保存key，最recently used放在最后面，最least used放在最前面。
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.q.remove(key)      # O(N)
            self.q.append(key)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = value
            self.q.append(key)
            if len(self.q) > self.capacity:
                leastUsedKey = self.q.popleft()
                del self.cache[leastUsedKey]
        else:
            self.cache[key] = value
            self.q.remove(key)      # O(N)
            self.q.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

