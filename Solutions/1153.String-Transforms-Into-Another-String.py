1153. String Transforms Into Another String

Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.


"""
Map each character in str1 to what it needs to be in str2. If any of these mappings collide (e.g. str1 = "aa", str2 = "bc", "a" needs to become both "b" and "c"),
we immediately return False since the transformation is impossible.
Next, we check the number of unique characters in str2. If all 26 characters are represented, there are no characters available to use for temporary conversions, 
and the transformation is impossible. The only exception to this is if str1 is equal to str2, so we handle this case at the start of the function.
"""

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        lens = len(str1)
        if str1 == str2:
            return True
        
        mapping = collections.defaultdict()
        for i, ch in enumerate(str1):
            if ch not in mapping:
                mapping[ch] = str2[i]
            else:
                if mapping[ch] != str2[i]:
                    return False
                
        return len(set(str2)) < 26
