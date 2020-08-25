353. Design Snake Game

Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)



"""
这个答案很简明，但是没有考虑到蛇太长转太多弯会咬到自己的情况。
"""
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.n = width      # width 宽度是列数而不是行数
        self.m = height
        self.food = food
        self.food_id = 0
        self.pos = [0, 0]
        self.lens = 0
        self.moves = {"U": (-1, 0), "D": (+1, 0), "L": (0, -1), "R": (0, +1)}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        self.pos[0] += self.moves[direction][0]
        self.pos[1] += self.moves[direction][1]
        print(self.pos)
        if 0 <= self.pos[0] < self.m and 0 <= self.pos[1] < self.n:
            if self.food_id < len(self.food) and self.pos == self.food[self.food_id]:
                self.food_id += 1
                self.lens += 1
                print(self.lens)
            return self.lens
        else:
            return -1


"""
为了考虑到蛇太长转太多弯会咬到自己的情况，我们需要记录蛇的尾巴的位置，所以需要用一个deque.
Each time we eat a food, we update the head pos as new head pos, and update the tail pos as stay the same pos, 
if not eating a food, then update the head pos as new head pos, and update the tail pos by simply popping it out of the deque. 
"""
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.pos = collections.deque()  # pos is a queue for which snake's head is on the left of the q
        self.pos.append([0, 0])         # and the snake's tail is on the right of the q 
        self.food_id = 0                # idx in food list to get the position of food
        self.food = food
        self.n = width
        self.m = height

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        new_head = self.pos[0].copy()   # list assignment一定要copy不然会出错，在这里debug了一个小时！！！!!!!!!!!!
        if direction == "U":
            new_head[0] -= 1
        elif direction == "D":
            new_head[0] += 1
        elif direction == "L":
            new_head[1] -= 1
        elif direction == "R":
            new_head[1] += 1

        if not (0 <= new_head[0] < self.m and 0 <= new_head[1] < self.n):   # 如果蛇撞到边界
            return -1
        if new_head in self.pos and new_head != self.pos[-1]:   # 如果蛇吃到自己身体
            return -1
        
        # 如果这次move吃到了food, 那就把头往前挪一步, 且food_id往前挪一步
        if self.food_id < len(self.food) and new_head == self.food[self.food_id]:
            self.pos.appendleft(new_head)
            self.food_id += 1

        # 如果这次move没有吃到了food, 那就把头往前挪一步，且把尾巴pop出来
        else:     
            self.pos.appendleft(new_head)
            self.pos.pop()

        return len(self.pos) - 1
