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
        self._backtrack(characters, combinationLength, "", -1, 0)       

    # O(solution), ie: O(pick k from N, ie: C_N_k)
    def _backtrack(self, chars, lens, curr_chars, curr_idx, curr_lens):
        if curr_lens == lens:
            self.combinations.append(curr_chars)
            return
        
        for next_idx in range(curr_idx + 1, len(chars)):
            self._backtrack(chars, lens, curr_chars + chars[next_idx], next_idx, curr_lens + 1)

    def next(self) -> str:
        if self.hasNext():
            return self.combinations.popleft()
        return -1

    def hasNext(self) -> bool:
        return len(self.combinations) > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
