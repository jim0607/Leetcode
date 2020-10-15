"""
1125. Smallest Sufficient Team

In a project, you have a list of required skills req_skills, and a list of people.  
The i-th person people[i] contains a list of skills that person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, 
there is at least one person in the team who has that skill.  
We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]

Constraints:

1 <= req_skills.length <= 16
1 <= people.length <= 60
1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
Elements of req_skills and people[i] are (respectively) distinct.
req_skills[i][j], people[i][j][k] are lowercase English letters.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
"""


"""
"The Set Cover Problem": find the min number of subsets to cover the entire set.
This famous "Set Cover Problem" is actually a NP Complete problem.
NP-complete problem: any of a class of computational problems for which no efficient solution algorithm has been found.
solution 1: backtrack - the subset problem 78. Subsets: find the subset that is valid.
O(m*2^n), where m = len(req_skills), n = len(people)
"""
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def backtrack(curr_comb, curr_skills):
            if set(curr_skills) == entire_set:
                if len(curr_comb) < self.min_lens:
                    self.min_lens = len(curr_comb)
                    self.res = list(curr_comb.copy())
                return
            
            if len(curr_comb) >= self.min_lens:      # strong pruning
                return
            
            for idx in range(len(people)):
                if idx not in curr_comb:        # 也相当于visited set用
                    curr_comb.add(idx)
                    for skill in people[idx]:
                        curr_skills.append(skill)
                    backtrack(curr_comb, curr_skills)
                    curr_comb.remove(idx)
                    for _ in range(len(people[idx])):
                        curr_skills.pop()
                

        entire_set = set(req_skills)
        self.res = []
        self.min_lens = sys.maxsize
        curr_comb = set()       # 也可以相当于visited set用
        backtrack(curr_comb, [])
        return self.res
        
        
        
"""
_preprocessing people list, Remove all skill sets that are subset of another skillset, 
by replacing the subset with an empty set. Then in the backtracking, strong pruning will be
do not continue of len(people[idx]) == 0.
O(m*2^n), where m = len(req_skills), n = len(people)
"""
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def backtrack(curr_comb, curr_skills):
            if set(curr_skills) == entire_set:
                if len(curr_comb) < self.min_lens:
                    self.min_lens = len(curr_comb)
                    self.res = list(curr_comb.copy())
                return
            
            if len(curr_comb) >= self.min_lens:      # strong pruning
                return
            
            for idx in range(len(people)):
                if idx in curr_comb:        # 也相当于visited set用
                    continue
                if len(people[idx]) == 0:   # 在之前的_preprocessing中已经把被包含的subsets设置为空了
                    continue                # strong pruning
                curr_comb.add(idx)
                for skill in people[idx]:
                    curr_skills.append(skill)
                backtrack(curr_comb, curr_skills)
                curr_comb.remove(idx)
                for _ in range(len(people[idx])):
                    curr_skills.pop()
                

        entire_set = set(req_skills)
        people = self._preprocessing(people)
        self.res = []
        self.min_lens = sys.maxsize
        curr_comb = set()       # 也可以相当于visited set用
        backtrack(curr_comb, [])
        return self.res
    
    
    def _preprocessing(self, people):
        for i in range(len(people)):
            people[i] = set(people[i])
        
        # Remove all skill sets that are subset of another skillset, by replacing the subset 
        # with an empty set. We do this rather than completely removing, so that indexes aren't 
        # disrupted, especially we need to return a list of idx.
        for i, i_skills in enumerate(people):
            for j, j_skills in enumerate(people):
                if i != j and i_skills.issubset(j_skills):
                    people[i] = set()
                    
        return people
