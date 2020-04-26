415. Add Strings

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1 = "123", num2 = "432"
        lens1, lens2 = len(num1), len(num2)
        if lens1 == 0:
            return num2
        if lens2 == 0:
            return num1
        
        carryBit = 0
        res = []
        i, j = lens1 - 1, lens2 - 1
        while i >= 0 and j >= 0:
            tempSum = carryBit + int(num1[i]) + int(num2[j])
            if tempSum >= 10:
                carryBit = 1
                res.append(tempSum % 10)
            else:
                carryBit = 0
                res.append(tempSum)
                
            i -= 1
            j -= 1
                
        while i >= 0:
            tempSum = carryBit + int(num1[i])
            if tempSum >= 10:
                carryBit = 1
                res.append(tempSum % 10)
            else:
                carryBit = 0
                res.append(tempSum)
                
            i -= 1
            
        while j >= 0:
            tempSum = carryBit + int(num2[j])
            if tempSum >= 10:
                carryBit = 1
                res.append(tempSum % 10)
            else:
                carryBit = 0
                res.append(tempSum)
                
            j -= 1
        
        if carryBit:
            res.append(carryBit)

        return "".join(map(str, res[::-1]))
