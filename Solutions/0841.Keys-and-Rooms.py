841. Keys and Rooms

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.



"""
solution 1: dfs - 用global variable的写法 不推荐
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(curr_room):
            if len(visited) == lens:
                self.valid = True
                return
            
            for next_room in rooms[curr_room]:
                if next_room in visited:
                    continue
                visited.add(next_room)      # 注意visited.add(next_room)与dfs(next_room)的先后顺序不能变！
                dfs(next_room)
                
        lens = len(rooms)
        visited = set()
        visited.add(0)
        
        self.valid = False
        
        dfs(0)
        
        return self.valid
        
        
        
"""
solution 1: dfs - 不用global variable的写法，直接返回 - O(N)
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(curr_room):
            if len(visited) == lens:
                return True
            
            for next_room in rooms[curr_room]:
                if next_room in visited:
                    continue
                visited.add(next_room)      # 注意visited.add(next_room)与dfs(next_room)的先后顺序不能变！
                if dfs(next_room):
                    return True
                
            return False
        
        lens = len(rooms)
        visited = set()
        visited.add(0)
        
        self.valid = False
        
        return dfs(0)
        

"""
这题不能用union find来解，因为其实这个题是有向的图，eg: [[1],[],[0,3],[]], 2号房间有0号房间的钥匙所以2号可以从2号房间去到0号房间，
但是并不意味着从0号房间可以去到2号房间。可是union find把两个node连在一起代表的是双向联通的，所以如果用union find 例子会输出True.
"""
"""
Follow up 1: 如果要求访问所有房间的最短路径，那就用BFS
Follow up 2: 如果要求输出所有的path, 那就用backtracking. 普通dfs是O(n)时间复杂度因为有visited的判断，而backtracking的时间复杂度跟solution个数有关，往往是指数级别的。
"""
