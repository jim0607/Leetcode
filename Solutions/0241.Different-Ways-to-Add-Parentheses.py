"""
241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        if s.isdigit():
            return [int(s)]
        
        results = []
        for i, ch in enumerate(s):
            if ch in "+-*":
                left_results = self.diffWaysToCompute(s[:i])
                right_results = self.diffWaysToCompute(s[i+1:])
                
                for left_res in left_results:
                    for right_res in right_results:
                        results.append(self.calculate(left_res, right_res, ch))
                        
        return results
    
    def calculate(self, num1, num2, opt):
        if opt == "*":
            return num1 * num2
        elif opt == "+":
            return num1 + num2
        elif opt == "-":
            return num1 - num2







class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:         
    
        def helper(s):
            """
            return all the different ways to add parentheses for input
            """
            if s.isdigit():
                return [int(s)]

            allResults = []
            for i in range(len(s)):
                if s[i] in "+-*":
                    leftResults = helper(s[:i])
                    rightResults = helper(s[i+1:])

                    for leftRes in leftResults:
                        for rightRes in rightResults:
                            allRes = operate(leftRes, s[i], rightRes)
                            allResults.append(allRes)

            return allResults
        
        def operate(num1, op, num2):
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
            if op == "*":
                return num1 * num2
            
                
        return helper(input)

    
    
"""
optimization: recursion with memorization
"""

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:         
    
        def helper(s, memo):
            """
            return all the different results to add parentheses for input
            """
            if s.isdigit():
                return [int(s)]
            
            if s in memo:
                return memo[s]

            allResults = []
            for i in range(len(s)):
                if s[i] in "+-*":
                    leftResults = helper(s[:i], memo)
                    rightResults = helper(s[i+1:], memo)

                    for leftRes in leftResults:
                        for rightRes in rightResults:
                            allRes = operate(leftRes, s[i], rightRes)
                            allResults.append(allRes)
                            
            memo[s] = allResults

            return allResults
        
        def operate(num1, op, num2):
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
            if op == "*":
                return num1 * num2
            
                
        return helper(input, {})
