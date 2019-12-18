In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.



"""由于状态不可用数组进行传递【在递归当中会受到改变，不能准确定位当前状态】，故在此处用Int的位表示状态（1表示用过,0表示未用过） 在目前状态取胜的条件为（在此步取得胜利，或下一手会取得失败）,假如status保存已经访问过的状态是为了避免进行重复计算"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger>desiredTotal:
            return True
        if sum(range(maxChoosableInteger+1))< desiredTotal:
            return False
        
        def win(max_num,total,visited,status):
            if status.get(visited):
                return status.get(visited)
            for i in range(1,max_num+1):
                tmp=1<<i
                if visited&tmp==0:                  
                    if i>=total or not win(max_num,total-i,visited|tmp,status):
                        status[visited]=True
                        return True
            status[visited]=False
            return False
        status={}
        return win(maxChoosableInteger, desiredTotal,0,status)
