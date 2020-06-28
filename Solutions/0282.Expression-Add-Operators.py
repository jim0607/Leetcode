282. Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []


"""
还是用递归来解题，我们需要两个变量curr_res, curr_num，一个用于计算当前所有运算加一起的值，另一个用来记录当前的数。
对于加和减，curr_num就是即将要加上的数和即将要减去的数的负值，而对于乘来说稍有些复杂，此时的curr_num应该是上一次的变化的curr_num乘以即将要乘上的数，
有点不好理解，那我们来举个例子，比如 2+3*2，即将要运算到乘以2的时候，上次循环的 curr_res = 5, curr_num = 3, 
而如果我们要算这个乘2的时候，新的变化值curr_num应为 3*2=6，而我们要把之前的curr_num (+3)操作的结果去掉，再加上新的curr_num，即 (5-3)+6=8；
如果非要找一个类似的题，可能跟combination sum II 比较像吧
backtrack parameters:
curr_idx: the curr_idx of the path we have gone through;
curr_num: the curr number we are operating now;
curr_res: the curr_res we have collected so far;
path: the curr path we have gone through
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        res = []
        def backtrack(curr_idx, curr_num, curr_res, path):
            if curr_res == target and curr_idx == len(num):
                res.append(path)
                return
            
            if curr_idx >= len(num):        # 提前退出
                return
            
            for next_idx in range(curr_idx + 1, len(num) + 1):
                next_num = int(num[curr_idx:next_idx])                  # "121" 可以输出1+2+1, 也可以是12+1, 所以下一个数可能比较长
                if next_idx > curr_idx + 1 and num[curr_idx] == "0":    # 00不能作为一个数的开头，eg: "00+0" is not valid, "00+0" is valid.
                    continue
                    
                if not path:        # 这里check path not none 是为了避免以operator开头的输出 eg: "+1"
                    backtrack(next_idx, next_num, next_num, num[curr_idx:next_idx])
                else:
                    backtrack(next_idx, next_num, curr_res + next_num, path + "+" + num[curr_idx:next_idx])
                    backtrack(next_idx, -next_num, curr_res - next_num, path + "-" + num[curr_idx:next_idx])
                    backtrack(next_idx, curr_num * next_num, curr_res - curr_num + curr_num * next_num, path + "*" + num[curr_idx:next_idx])
                    
        backtrack(0, 0, 0, "")
        
        return res
