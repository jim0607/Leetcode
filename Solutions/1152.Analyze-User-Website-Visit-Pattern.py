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
        # step 1: sort the user and websites based on timestamp
        data = zip(timestamp, username, website)
        data = sorted(data)
        
        # step 2: map username and the websites they visited
        user_to_web = collections.defaultdict(list)
        for time, user, web in data:
            user_to_web[user].append(web)
            
        # step 3: find all the possible 3-sequence and record their appear times
        counter = collections.defaultdict(int)
        for webs in user_to_web.values():
            seqs = set()    # 一个user不能拥有重复的seq, 所以这里必须用一个set
            self._find_seqs(webs, -1, [], seqs)
            for seq in seqs:
                counter[seq] += 1
            
        # step 4: get the 3-sequence with the max_cnt
        max_cnt = max(cnt for cnt in counter.values())
        res = []
        for seq, cnt in counter.items():
            if cnt == max_cnt:
                res.append(seq)
        
        # step 5: sortlexicographically smallest such 3-sequence
        res.sort(key = lambda x: (len(x), x))
        return res[0]
    
    
    def _find_seqs(self, webs, curr_idx, curr, seqs):
        if len(curr) == 3:
            seqs.add(tuple(curr.copy()))
            return seqs
        
        for next_idx in range(curr_idx + 1, len(webs)):
            curr.append(webs[next_idx])
            self._find_seqs(webs, next_idx, curr, seqs)
            curr.pop()
