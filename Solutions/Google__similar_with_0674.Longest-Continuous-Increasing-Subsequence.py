"""
Given a string str and a string t where t represents a custom alphabetical order of lowercase letters, 
find the length of the longest sorted substring in s. 
t: [a-z] permuation
s: lower case string, 
	Input: s = "pierywq", t = "qwertyuiopasdfghjklzxcvbnm"

Output: "ery"
	             i
	p i e r y w q
	             J
	Solution 1: sliding window
	Solution 2: dp[i] = the longest lens ended with s[i].
	 Dp[i] = 1 if hashmap[s[i]] < hashmap[s[i-1]] else dp[i-1] + 1
Returtn max(dp)
---> O(1) space 
"""
