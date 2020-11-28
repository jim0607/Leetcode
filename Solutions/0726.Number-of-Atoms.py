"""
726. Number of Atoms

Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, 
then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. 
If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), 
followed by its count (if that count is more than 1), followed by the second name (in sorted order), 
followed by its count (if that count is more than 1), and so on.

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Example 4:

Input: formula = "Be32"
Output: "Be32"
"""



"""
与394.Decode String非常类似
"""
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        mapping = collections.defaultdict(int)      # chemical element --> cnt
        st = [1]        # 记录nums of 每一层需要repeat的次数
        num = 0         # 记录curr num we get, eg: num = 23
        ten = 0         # how many tens we need to multiply, we need this because we are 反向遍历 eg: 234 = 34 + 2*(10**2)
        lower_ch = ""   # the lower case of chemical element
        for ch in formula[::-1]:     # 反向遍历，这样只要遇到upper case的ch就可以加到dictionary了
            if ch.isdigit():
                num += int(ch) * (10**ten)
                ten += 1
                
            # 遇到")" 说明更加深入一层，则把这一层需要repeat的次数放入st
            elif ch == ")":
                repeat = st[-1] if num == 0 else st[-1] * num   # ")"后没有跟着num就默认repeat一次
                st.append(repeat)
                num, ten = 0, 0         # 注意要讲num, ten清空
                
            # 遇到lower case ch 则记录lower_ch，这就是从后往前遍历的好处
            elif ch.islower():
                lower_ch = ch
                
            # 遇到upper case ch 说明遇到了一个完整的chemical element, 将其记录到hashmap中
            elif ch.isupper(): 
                repeat = st[-1] if num == 0 else st[-1] * num   # upper case ch 后面没有跟着num就默认repeat一次
                mapping[ch + lower_ch] += repeat
                lower_ch = ""           # 注意要将lower_ch清空
                num, ten = 0, 0         # 将num, ten清空

            # 遇到"(" 说明需要出了这一层, 则把这一层需要repeat的次数pop出st
            elif ch == "(":
                st.pop()
                
        res = ""
        for element, cnt in sorted(mapping.items()):
            res += element if cnt == 1 else element + str(cnt)
        return res
    
    
"""
另一种写法
"""
class Solution:
    def countOfAtoms(self, s: str) -> str:
        cnter = defaultdict(int)
        
        num_st = [1]
        num, ten = 1, 1
        element = ""
        i = len(s) - 1
        reapeat = 0
        while i >= 0:
            if s[i].isdigit():
                num = ord(s[i]) - ord("0")
                while i - 1 >= 0 and s[i-1].isdigit():
                    num += (ord(s[i-1]) - ord("0")) * (10 ** ten)
                    i -= 1
                ten = 1
            
            elif s[i].islower():
                element = s[i]
            elif s[i].isupper():
                element = s[i] + element
                cnter[element] += num_st[-1] * num    
                num = 1
                element = ""

            elif s[i] == ")":
                num_st.append(num * num_st[-1])
                num = 1
            elif s[i] == "(":
                num_st.pop()
                
            i -= 1
            
        res = ""
        for element, cnt in sorted(cnter.items()):
            res += element if cnt == 1 else element + str(cnt)
        return res
