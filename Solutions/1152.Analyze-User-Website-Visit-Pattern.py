1152. Analyze User Website Visit Pattern

We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.



class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        packed_tuple = zip(timestamp, username, website)
        packed_tuple = sorted(packed_tuple)
        
        user_to_web = collections.defaultdict(list)
        for time, user, web in packed_tuple:
            user_to_web[user].append(web)
            
        counter = collections.defaultdict(int)
        for webs in user_to_web.values():
            self.seqs = set()
            self._find_sequences(webs, -1, [])
            for seq in self.seqs:
                counter[seq] += 1
        
        res = []
        max_cnt = max(cnt for cnt in counter.values())
        for seq, cnt in counter.items():
            if cnt == max_cnt:
                res.append(seq)
        res.sort(key = lambda x: (len(x), x))
        return res[0]
    
    def _find_sequences(self, webs, curr_idx, curr_seq):
        if len(curr_seq) == 3:
            self.seqs.add(tuple(curr_seq.copy()))
            return

        for idx in range(curr_idx + 1, len(webs)):
            curr_seq.append(webs[idx])
            self._find_sequences(webs, idx, curr_seq)
            curr_seq.pop()
