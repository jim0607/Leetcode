1206. Design Skiplist

Design a Skiplist without using any built-in libraries.

A Skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists are just simple linked lists.

For example: we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it. The Skiplist works this way:


Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add , erase and search can be faster than O(n). It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

To be specific, your design should include these functions:

bool search(int target) : Return whether the target exists in the Skiplist or not.
void add(int num): Insert a value into the SkipList. 
bool erase(int num): Remove a value in the Skiplist. If num does not exist in the Skiplist, do nothing and return false. If there exists multiple num values, removing any one of them is fine.
See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

 

Example:

Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // return false.
skiplist.add(4);
skiplist.search(1);   // return true.
skiplist.erase(0);    // return false, 0 is not in skiplist.
skiplist.erase(1);    // return true.
skiplist.search(1);   // return false, 1 has already been erased.
 

Constraints:

0 <= num, target <= 20000
At most 50000 calls will be made to search, add, and erase.


"""
Each node has 2 pointers: "next" targets to the next node in the same level, "down" targets the "next" level node.
"""
class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:

    def __init__(self):
        self.levels = []
        
        # Because the number of calls is <50000, and 2^16>60000, which is enough to handle all calls.
        # Otherwise we need to consider the situation new level need to be added when level not being enough.
        vertical = None
        for _ in range(16):
            head = ListNode(float("-inf"))  # 新建一些dummyhead放到每一层的头部
            self.levels.append(head)        # 处理each level - horizontal
            if vertical:                        # 处理verticals
                vertical.down = head
            vertical = head
            
    def _find_smaller(self, target):
        """
        helper function to find the largest node that is smaller than search target in EACH levels
        and store them in a list, return the list
        """
        res = []
        
        curr = self.levels[0]
        while curr:
            while curr.next and curr.next.val < target:
                curr = curr.next
            res.append(curr)    # on each level, just append the largest node that is smaller than target
            
            curr = curr.down
            
        return res

    def search(self, target: int) -> bool:
        last = self._find_smaller(target)[-1]   # last is just smaller node on the last level
        if last.next and last.next.val == target:
            return True
        return False

    def add(self, num: int) -> None:
        smaller = self._find_smaller(num) # the idea is to insert a new_node at the right place, we find the right place at each level first
        vertical = None
        for node in smaller[::-1]:      # If we add a node in a level, all levels after that also need to be added, so loop reversely
            new_node = ListNode(num)    # the idea is to insert a new_node at the right place, we create a new node first
            
            # firstly, insert the new_node to the level - horizontal
            new_node.next = node.next
            node.next = new_node
            
            # then, point the new_node.down to it's corresponding down node - vertical
            new_node.down = vertical
            vertical = node
            
            # we don't insert the new_node to every level, we only inser the new_node to some levesl on the bottom
            # how to we decide which levels to insert? we use coin toss
            # The purpose of coin toss is to ensure that each node at current level will be 
            # duplicated to its upper level with a probability of 0.5, 
            # so the number of nodes at the upper level is roughly half of the current level.
            # So in the extreme case, SkipList is equivalent to a balanced binary search tree.
            # that is why add, erase and search can be O(logn)
            rand = random.randrange(0, 10)
            if rand >= 5:   # half of the possibility that we stop inserting the new_node to any upper levels
                break

    def erase(self, num: int) -> bool:
        smaller = self._find_smaller(num)
        found = False
        for node in smaller[::-1]:
            if node.next and node.next.val == num:
                node.next = node.next.next  # remove the node
                found = True
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
