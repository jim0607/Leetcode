做Linked List的题目一定要懂reference
node其实是一个reference/pointer，
一个Linked List Node在内存地址中占用8个字节的位置，其中的4个字节存储了一个数也就是node.val; 另外4个字节存储了一个指针也就是node.next，这个指针的值是下一个Linked List Node在内存中的存储位置。
所以node.val和node.next是存在物理内存中的，而node本身只是一个局部变量。
所以如果我们去修改局部变量的话（如操作 node = someNode）, 根本不会改变原来node原来的连接关系。
  ------------      ------------      ------------
  |  1  |  --|-->   |  2 |   --|-->   |  3 |   --|-->  None
  ------------      ------------      ------------
   ^  ^                ^
   |  |                |
   |  |                |
 Head Node1          Node2

操作 Node1 = Node2 做
一个Linked List Node在内存地址中占用8个字节的位置，其中的4个字节存储了一个数也就是node.val; 另外4个字节存储了一个指针也就是node.next，这个指针的值是下一个Linked List Node在内存中的存储位置。
