1286. Iterator for Combination

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false



"""
use backtrack to find all the possible combinations, then put them in a deque so that we can output in lexicographical order.
"""
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = collections.deque()
        self._backtrack(characters, combinationLength, -1, "")
        
    # O(solution), ie: O(pick k from N, ie: C_N_k)
    def _backtrack(self, s, n, curr_idx, curr):
        if len(curr) == n:
            self.combinations.append(curr)
            return
        for next_idx in range(curr_idx + 1, len(s)):
            self._backtrack(s, n, next_idx, curr + s[next_idx])

    def next(self) -> str:
        if self.hasNext():
            return self.combinations.popleft()

    def hasNext(self) -> bool:
        return len(self.combinations) > 0

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
