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
"""
why this case should return False?
"abcdefghijklmnopqrstuvwxyz"
"bcdefghijklmnopqrstuvwxyza"
You can choose to change a -> b. So now the str1 becomes :
"abcdefghijklmnopqrstuvwxyz" -> "bbcdefghijklmnopqrstuvwxyz"
Now you are stuck. If you try to change b -> c, your first character will also change. The order of transformation matters.
or you can change z -> a, then the str1 will become: "abcdefghijklmnopqrstuvwxya", now you are stuck cuz there are two "a" in the string.

but in this case:
"abcdefghijklmnopqrstuvwxy"
"bcdefghijklmnopqrstuvwxyz"
there are only 25 different letters. we can change y -> z. then str becomes "abcdefghijklmnopqrstuvwxz"
then change x -> y....and so on....until change a -> b, and get "bcdefghijklmnopqrstuvwxyz"

The point is we cannot have all 26 different letters in str2. We need to have at least on letter to use as a buffer.
"""

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        mapping = collections.defaultdict(str)
        for i, ch in enumerate(str1):
            if ch not in mapping:
                mapping[ch] = str2[i]
            else:
                if mapping[ch] != str2[i]:
                    return False
                
        return len(set(str2)) < 26 or str1 == str2
       
       
       
"""
follow up: 若transform可行，判断是否需要用到中介字符，即判断有向图是否有环。
eg 1: abcd, bcde
d->e, c->d, b->c, a->b. 这样mapping dictionary作为adjacency matrix表示的图是无环，不需要用到中介字符。
eg 2: abcd, bcda
d->a, c->d, b->c, a->b. 我们会发现mapping dictionary作为adjacency matrix表示的图是有环的。
这时候我们就需要用到中介字符，否则就不可行了。
使用中介字符f, transition过程为 d->f: abcf, c->d: abdf, b->c: acdf, a->b: bcdf, f->a: bcda
"""
