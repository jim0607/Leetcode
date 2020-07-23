433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
 

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
 

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3




class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        lens = len(start)
        if len(end) != lens:
            return -1
        
        bank_set = set()
        for gene in bank:
            if len(gene) == lens:
                bank_set.add(gene)
        if end not in bank_set:
            return -1
        
        q = collections.deque()
        visited = set()
        q.append(start)
        visited.add(start)
        step = -1
        while q:            # O(4LN), L is lens, N is len(bank_set)
            step += 1
            lens_q = len(q)
            for _ in range(lens_q):
                curr = q.popleft()
                if curr == end:
                    return step
                for next in self._possible_mutations(curr, bank_set):
                    if next in visited:
                        continue
                    q.append(next)
                    visited.add(next)
                    
        return -1
    
    def _possible_mutations(self, curr, bank_set):      # O(4L)
        possible_mutations = []
        for i, ch in enumerate(curr):
            for replace_ch in "ACTG":
                if replace_ch == ch:
                    continue
                next_possible = curr[:i] + replace_ch + curr[i+1:]
                if next_possible in bank_set:
                    possible_mutations.append(next_possible)
        return possible_mutations
        
        
        
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        lens = len(start)
        if len(end) != lens:
            return -1
        
        bank_set = set()
        for gene in bank:
            if len(gene) == lens:
                bank_set.add(gene)
        if end not in bank_set:
            return -1
        
        q_src, q_des = collections.deque(), collections.deque()
        visited_src, visited_des = set(), set()
        q_src.append(start)
        q_des.append(end)
        visited_src.add(start)
        visited_des.add(end)
        
        step = 0
        while q_src and q_des:
            if visited_src & visited_des:
                return step
            
            self._bfs(q_src, visited_src, bank_set)       # src走一步
            step += 1
            
            if visited_src & visited_des:                 # 走一步判断一下visited_src & visited_des
                return step
            
            self._bfs(q_des, visited_des, bank_set)       # des走一步
            step += 1        
            
        return -1
    
    def _bfs(self, q, visited, bank_set):  # 双端bfs中每个bfs就走一步，走完一步之后去比对visited_src & visited_des
        lens_q = len(q)
        for _ in range(lens_q):
            curr = q.popleft()
            for next in self._possible_mutations(curr, bank_set):
                if next in visited:
                    continue
                q.append(next)
                visited.add(next)
        return q, visited
    
    def _possible_mutations(self, curr, bank_set):      # O(4L)
        possible_mutations = []
        for i, ch in enumerate(curr):
            for replace_ch in "ACTG":
                if replace_ch == ch:
                    continue
                next_possible = curr[:i] + replace_ch + curr[i+1:]
                if next_possible in bank_set:
                    possible_mutations.append(next_possible)
        return possible_mutations
