"""
913. Cat and Mouse

A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  
For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in three ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (i.e., the players are in the same position as a previous turn, a
nd it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return

1 if the mouse wins the game,
2 if the cat wins the game, or
0 if the game is a draw.

Example 1:
Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Example 2:
Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1
"""


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
		
		# dp[mouse_loc][cat_loc][which_one_moves_first]
        # third index 0 mouse moves first
        # third index 1 cat moves first
        dp = [[[None,None] for j in range(n)] for i in range(n)]
        
		# same structure as dp to count the neighboring moves that makes current player lose
        # if count down goes to 0, then we can decide current move to be a lose for certain
        cd = [[[len(graph[i]),len(graph[j])] for j in range(n)] for i in range(n)]
        
        
        q = deque()
        
        # if a mouse arrives at hole, win for mouse
        for cat_index in range(1,n):
            dp[0][cat_index][0] = 'M'
            q.append((0,cat_index,0))
            dp[0][cat_index][1] = 'M'
            q.append((0,cat_index,1))
        
        # if a cat catches a mouse, win for cat
        for index in range(1,n):
            dp[index][index][0] = 'C'
            q.append((index,index,0))
            dp[index][index][1] = 'C'
            q.append((index,index,1))
        
        # cat can't go in at hole, regard it as lose for cat
        for mouse_index in range(1,n):
            dp[mouse_index][0][0] = 'M'
            q.append((mouse_index,0,0))
            dp[mouse_index][0][1] = 'M'
            q.append((mouse_index,0,1))
        
        
        while q:
            #print(q)
            mouse_loc,cat_loc,move = q.popleft()
            cur_move = 'mouse' if move == 0 else 'cat'
            
            # if previous move is mouse and current state is a win for mouse
            if cur_move == 'cat' and dp[mouse_loc][cat_loc][move] == 'M':
                for mouse_prev in graph[mouse_loc]:
                    if dp[mouse_prev][cat_loc][0] == None:
                        dp[mouse_prev][cat_loc][0] = 'M'
                        q.append((mouse_prev,cat_loc,0))
            
            # if previous move is mouse and current state is a lose for mouse
            elif cur_move == 'cat' and dp[mouse_loc][cat_loc][move] == 'C':
                for mouse_prev in graph[mouse_loc]:
                    cd[mouse_prev][cat_loc][0] -=1
                    if cd[mouse_prev][cat_loc][0] == 0 and dp[mouse_prev][cat_loc][0] == None:
                        dp[mouse_prev][cat_loc][0] = 'C'
                        q.append((mouse_prev,cat_loc,0))
            
            # if previous move is cat and current state is a win for cat
            elif cur_move == 'mouse' and dp[mouse_loc][cat_loc][move] == 'C':
                for cat_prev in graph[cat_loc]:
                    if dp[mouse_loc][cat_prev][1] == None:
                        dp[mouse_loc][cat_prev][1] = 'C'
                        q.append((mouse_loc,cat_prev, 1))
            
            # if previous move is car and current state is a lose for cat
            elif cur_move == 'mouse' and dp[mouse_loc][cat_loc][move] == 'M':
                for cat_prev in graph[cat_loc]:
                    cd[mouse_loc][cat_prev][1] -=1
                    if cd[mouse_loc][cat_prev][1] == 0 and dp[mouse_loc][cat_prev][1] == None:
                        dp[mouse_loc][cat_prev][1] = 'M'
                        q.append((mouse_loc,cat_prev,1))
                        
        
        if dp[1][2][0] == 'C':
            return 2
        elif dp[1][2][0] == 'M':
            return 1
        elif dp[1][2][0] == None:
            return 0
