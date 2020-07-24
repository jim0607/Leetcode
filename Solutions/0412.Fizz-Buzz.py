412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = ["" for _ in range(n)]
        for i in range(1, n+1):
            if i % 3 == 0:
                res[i-1] += "Fizz"
            if i % 5 == 0:
                res[i-1] += "Buzz"
            if i % 3 != 0 and i % 5 != 0:
                res[i-1] += str(i)
        return res
    
"""
How to do it without for-loop: recursion
"""