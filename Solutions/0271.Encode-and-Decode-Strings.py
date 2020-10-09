"""
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:

The string may contain any possible characters out of 256 valid ascii characters. 
Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. 
Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. 
You should implement your own encode/decode algorithm.
"""



class Codec:
    def encode(self, strs: [str]) -> str:
        """
        Encodes a list of strings to a single string.
        encode ["a$c@d", "31_*df"] as "5 a$c@d6 31_*df",
        where 5 is len("a$c@d") and 6 is len("31_*df").
        """
        res = ""
        for s in strs:
            res += str(len(s))
            res += " "  # place a space ' ' before each string when encoding,
            res += s    # to seperate 6 and 31 in the above example
        return res
            
    def decode(self, s: str) -> [str]:
        """
        Decodes a single string to a list of strings.
        Decode "5 a$c@d6 31_*df" to be ["a$c@d", "31_*df"]
        """
        res = []
        next_len = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                next_len = 10*next_len + int(s[i])
                i += 1
            else:       # else then s[i] must be a " "
                res.append(s[i + 1: i + 1 + next_len])
                i += 1 + next_len
                next_len = 0
                
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
