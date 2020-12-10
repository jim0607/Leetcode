"""
1079. Letter Tile Possibilities

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  
Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(curr_comb):
            res.append(str(curr_comb.copy()))
            for next_idx in range(len(tiles)):
                if next_idx in visited:
                    continue
                if next_idx > 0 and tiles[next_idx] == tiles[next_idx-1] and next_idx-1 not in visited:
                    continue
                visited.add(next_idx)
                curr_comb.append(tiles[next_idx])
                backtrack(curr_comb)
                curr_comb.pop()
                visited.remove(next_idx)                    
                    
        tiles = sorted(tiles)     # 去重第一步sort, string只能用sorted
        res = []
        visited = set()
        backtrack([])
        return len(res) - 1
            

    


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()         # 用set去重, 也可以用47. Permutations II中的方法去重
        visited = set()
        self._backtrack(tiles, "", res, visited)
        return len(res) - 1
    
    def _backtrack(self, tiles, curr_str, res, visited):
        res.add(curr_str)
        for idx in range(len(tiles)):
            if idx in visited:
                continue
            visited.add(idx)
            self._backtrack(tiles, curr_str + tiles[idx], res, visited)
            visited.remove(idx)
            
"""
用47. Permutations II中的方法去重, 需要先sort!!!!!!!!
"""    
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)    # 用47. Permutations II中的方法去重, 需要先sort!!!!!!!!
        res = []         
        visited = set()
        self._backtrack(tiles, "", res, visited)
        return len(res) - 1
    
    def _backtrack(self, tiles, curr_str, res, visited):
        res.append(curr_str)
        for idx in range(len(tiles)):
            # 如果nums[i]这个数与它前一个数是一样的但是前一个数并没有放进去，那就不要把这个数放进去了，因为我们是优先放前面的那个数
            if (idx > 0 and tiles[idx] == tiles[idx-1]) and idx-1 not in visited:
                continue
            if idx in visited:
                continue
            visited.add(idx)
            self._backtrack(tiles, curr_str + tiles[idx], res, visited)
            visited.remove(idx)
