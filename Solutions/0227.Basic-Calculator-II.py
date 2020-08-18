227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.


"""
用一个opt_st存所有的operator, 一个num_st存所有的num.
1. 如果ch.isdigit()就while loop得到num, 紧接着判断这个num前面的operator是不是"*/", 如果是就不需要等，可以马上计算。
2. 如果not ch.isdigit()那ch就是operator, 就把operator放进opt_st里。
这样处理之后到最后opt_st里面装的全是"+-", 我们要左往右计算最后的res.
"""
class Solution:
    def calculate(self, s: str) -> int:
        opt_st = []
        num_st = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ord(s[i]) - ord("0")
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = 10 * num + ord(s[i + 1]) - ord("0")
                    i += 1
                
                # 判断这个num前面的operator是不是"*/", 如果是就不需要等，可以马上计算
                if len(opt_st) > 0 and opt_st[-1] == "*":
                    opt_st.pop()
                    num_st.append(num_st.pop() * num)   # 计算完了之后要append到num_st中
                elif len(opt_st) > 0 and opt_st[-1] == "/":
                    opt_st.pop()
                    num_st.append(int(num_st.pop() / num))
                    
                else:       # 需要将num存入num_st中
                    num_st.append(num)
                    
            # 如果not ch.isdigit()就把operator放进opt_st里
            elif s[i] in ["+", "-", "*", "/"]:
                opt_st.append(s[i])
                
            i += 1

        # 到最后opt_st里面装的全是"+-", 我们要左往右计算最后的res
        res = num_st[0]
        for i in range(len(opt_st)):
            if opt_st[i] == "+":
                res += num_st[i+1]
            else:
                res -= num_st[i+1]
                
        return res


"""
solution 2: 上述方法的变种，我们可以不用opt_st, 只用一个num_st存所有的num.
1. 如果ch.isdigit()就while loop得到num, 紧接着判断这个num前面的operator, 并进行马上计算。
2. 如果not ch.isdigit()那ch就是operator, 就把operator放进opt_st里。
这样处理之后到最后opt_st里面装的全是"+", 我们要左往右计算最后的res.
"""
class Solution:
    def calculate(self, s: str) -> int:
        prev_sign = "+"
        num_st = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ord(s[i]) - ord("0")
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = 10 * num + ord(s[i + 1]) - ord("0")
                    i += 1
                
                # 紧接着判断这个num前面的operator, 并进行马上计算
                if prev_sign == "*":
                    num_st.append(num_st.pop() * num)   # 计算完了之后要append到num_st中
                elif prev_sign == "/":
                    num_st.append(int(num_st.pop() / num))
                elif prev_sign == "+":
                    num_st.append(num)  
                elif prev_sign == "-":
                    num_st.append(-num)
                    
            # 如果not ch.isdigit()就把operator放进opt_st里
            elif s[i] in ["+", "-", "*", "/"]:
                prev_sign = s[i]
                
            i += 1

        # 到最后opt_st里面装的全是"+", 我们要左往右计算最后的res
        return sum(num_st)
    
    
    

"""
solution 3: 不用stack, 用三根指针prevNum, prevSign, currNum
"""
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        prevNum, prevSign = 0, "+"
        currNum, currSign = 0, "+"
        i = 0
        while i < len(s):
            if s[i].isdigit():
                currNum = ord(s[i]) - ord("0")
                while i+1 < len(s) and s[i+1].isdigit():
                    currNum = currNum * 10 + ord(s[i+1]) - ord("0")
                    i += 1
                
                if prevSign == "+":
                    res += prevNum
                    prevNum = currNum
                elif prevSign == "-":
                    res += prevNum
                    prevNum = -currNum
                elif prevSign == "*":       # do not update res, combine preVal & curVal and keep loop
                    prevNum *= currNum
                elif prevSign == "/":
                    prevNum = int(prevNum / currNum) 
                    
            elif s[i] in ["+", "-", "*", "/"]:
                prevSign = s[i]
                     
            i += 1
                
        return res + prevNum
    
    
Google 06/2020 真题  
第四轮：实现一个calculator，语法是 (operator node0 node1...),  op只能是加法或者是乘法, node可以是数字或者另一个(operator node0 ....)。
比如(+ 9 1) = 10,
(+ 2 (* 1 (+ 1 2)) 3) = 2 + (1*3) + 3 = 8
(+ 2 3 3) 2 + 3 + 3 = 8

followup是node 还可以是 if(a b c) 如果a！=0 是b 反之是c。要自己设计输入和testcase。
思路就是recursive的找（），类似蠡口幺零九六。
public static int calculate(String str) {
   if(str == null) return 0;
   Stack<String> opStack = new Stack<>();
   Stack<String> numStack = new Stack<>();
   int index = 0;
   int num = 0;
   while(index < str.length()) {
       if(str.charAt(index) == '(') {
           numStack.push("(");
           index++;
       } else if (str.charAt(index) == '+' || str.charAt(index) == '*') {
           opStack.push(str.charAt(index) + "");
           index++;
       } else if (str.charAt(index) >= '0' && str.charAt(index) <= '9') {
           while(index < str.length() && str.charAt(index) >= '0' && str.charAt(index) <= '9') {
               num = 10 * num + str.charAt(index) + 0 - '0';
               index++;
           }
           numStack.push(num + "");
           num = 0;
       } else if (str.charAt(index) == ')') {
           String operator = opStack.pop();
           int num1 = Integer.parseInt(numStack.pop());
           int num2 = Integer.parseInt(numStack.pop());
           int res = operate(operator, num1, num2);
           while(!numStack.peek().equals("(")) {
               res = operate(operator, res, Integer.parseInt(numStack.pop()));
           }
           numStack.pop();
           numStack.push(res + "");
           index++;
       } else {
           index++;
       }
   }
   return Integer.parseInt(numStack.pop());
}

public static int calculateFollowUp(String str) {
   if(str == null) return 0;
   Stack<String> opStack = new Stack<>();
   Stack<String> numStack = new Stack<>();
   int index = 0;
   int num = 0;
   while(index < str.length()) {
       if(str.charAt(index) == '(') {
           numStack.push("(");
           index++;
       } else if (str.charAt(index) == '+' || str.charAt(index) == '*') {
           opStack.push(str.charAt(index) + "");
           index++;
       } else if (str.charAt(index) == 'i') {
           opStack.push("if");
           index++;
           index++;
       } else if (str.charAt(index) >= '0' && str.charAt(index) <= '9') {
           while(index < str.length() && str.charAt(index) >= '0' && str.charAt(index) <= '9') {
               num = 10 * num + str.charAt(index) + 0 - '0';
               index++;
           }
           numStack.push(num + "");
           num = 0;
       } else if (str.charAt(index) == ')') {
           String operator = opStack.pop();
           int res = 0;
           if(operator.equals("if")) {
               int num1 = Integer.parseInt(numStack.pop());
               int num2 = Integer.parseInt(numStack.pop());
               int num3 = Integer.parseInt(numStack.pop());
               if(num3 != 0) {
                   res = num2;
               } else {
                   res = num1;
               }
           } else {
               int num1 = Integer.parseInt(numStack.pop());
               int num2 = Integer.parseInt(numStack.pop());
               res = operate(operator, num1, num2);
               while(!numStack.peek().equals("(")) {
                   res = operate(operator, res, Integer.parseInt(numStack.pop()));
               }
           }
           numStack.pop();
           numStack.push(res + "");
           index++;
       } else {
           index++;
       }
   }
   return Integer.parseInt(numStack.pop());
}

