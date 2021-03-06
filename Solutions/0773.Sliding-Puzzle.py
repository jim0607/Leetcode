"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. 
If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
"""



"""
最短路径问题一般都用bfs: 从单源节点出发到终节点的最短路径问题。
这题的起点是给定的board, 终点是最终想生成的board.
所以node就是某一个board, node的neighbors就是通过一次交换可以生成的board.
Time Complexity: O(R∗C∗(R∗C)!), where R,C are the number of rows and columns in board.
There are O((R∗C)!) possible board states.
"""
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        destination = [[1,2,3],[4,5,0]]
        m, n = len(board), len(board[0])
        q = collections.deque()
        visited = set()
        q.append(board)
        visited.add(tuple([board[i][j] for i in range(m) for j in range(n)]))   # list is mutable, so it's not hashable, we need to convert the board into tuples
        # print(visited)
        steps = -1
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_node = q.popleft()
                if curr_node == destination:
                    return steps
                for next_node in self._get_next(curr_node):
                    if tuple([next_node[i][j] for i in range(m) for j in range(n)]) not in visited:
                        q.append(next_node)
                        visited.add(tuple([next_node[i][j] for i in range(m) for j in range(n)]))
        return -1
                        
    def _get_next(self, board):
        m, n = len(board), len(board[0])
        next_board = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:    # 0 可以与相邻的数交换位置
                    if i - 1 >= 0:      # 与上面的数字调换位置
                        board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
                        next_board.append([[board[i][j] for j in range(n)] for i in range(m)])  # has to be a deep copy for 2D case
                        board[i-1][j], board[i][j] = board[i][j], board[i-1][j]     # 再换回来，以免改变了原有的borad
                    if i + 1 < m:       # 与下面的数字调换位置
                        board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
                        next_board.append([[board[i][j] for j in range(n)] for i in range(m)])  
                        board[i+1][j], board[i][j] = board[i][j], board[i+1][j]        
                    if j - 1 >= 0:      # 与左边的数字调换位置
                        board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
                        next_board.append([[board[i][j] for j in range(n)] for i in range(m)])  
                        board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
                    if j + 1 < n:       # 与右边的数字调换位置
                        board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
                        next_board.append([[board[i][j] for j in range(n)] for i in range(m)])  
                        board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        return next_board
