"""
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, just return any of them.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


"""
Idea is to put every remainder into the hash table as a key, and the position where the remainder appears as val.
如果remainder重复出现了，就说明找到循环的部分了，循环的部分就是从dict[remainder]到最后的部分
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if numerator * denominator < 0:
            res += "-"
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        # 整型数INT的取值范围是-2147483648～2147483647，对于c# and java, -2147483648取绝对值就会超出范围
        # 需要转换成long type, 然后再取绝对值，但是python不用担心，python已经提前handle好了
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        res += "."
        remain = numerator % denominator
        
        remain_to_res = collections.defaultdict(int)    # key is remainder, val is where the remainder appears
        decimal = ""          # string decimal is the decimal part of res
        pos = 0               # pos 记录remainder出现的位置
        while remain != 0:
            if remain in remain_to_res:     # now we find the recurrent remainder
                recur_pos = remain_to_res[remain]
                decimal = decimal[:recur_pos] +"(" + decimal[recur_pos:] + ")"
                break
            
            remain_to_res[remain] = pos
            
            # 下面是模拟除法的过程：
            remain *= 10                            # remainder不够除数除的，所以先在后面添零
            decimal += str(remain // denominator)   # 然后再除除数，得到的商作为res保存
            remain %= denominator                   # 得到余数，如果余数为零就停止整个除法运算
            
            pos += 1
            
        return res + decimal
