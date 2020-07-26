981. Time Based Key-Value Store

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]


"""
Since we need to return the largest timestamp_prev, it's a OOOXXX problem.
"""
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = collections.defaultdict(list)   # a list of tuple: (timestamp, val)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        since curr timestamp is always larger than prev as time is passing by, we can just append,
        otherwise, we use binary insert the timestamp into the mapping[key] list - O(logN)
        """
        self.mapping[key].append((timestamp, value))
           
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping or self.mapping[key] == [] or timestamp < self.mapping[key][0][0]:
            return ""
        
        start, end = 0, len(self.mapping[key]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.mapping[key][mid][0] <= timestamp:
                start = mid
            else:
                end = mid
        return self.mapping[key][end][1] if self.mapping[key][end][0] <= timestamp else self.mapping[key][start][1]        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
