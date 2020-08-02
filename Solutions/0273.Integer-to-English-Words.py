273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"



"""
construct 3 lists for the english expressions for numbers less_than_20, tens, thousands.
the main funciton handle the situation of num >= thousands.
use a helper funciton to calcuate cases when num <= hundreds.
"""
class Solution:
    
    def __init__(self):
        self.less_than_20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
                             "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self._helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
        
        return res.strip()   # str.strip(ch) remove the ch in the front and tail of a string
    
    def _helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self._helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self._helper(num % 100)
