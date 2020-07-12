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
class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:

    def __init__(self):
        self.levels = []
        prev = None
        
        # Because the number of calls is <50000, and 2^16>60000, which is enough to handle all calls.
        # Otherwise we need to consider the situation new level need to be added when level not being enough.
        for _ in range(16):
            node = Node(float("-inf"))  # initialize each level head as -inf
            self.levels.append(node)
            if prev:
                prev.down = node
            prev = node
            
    def _find_just_smaller(self, target):
        """
        helper function to find the largest node that is smaller than search target in all levels
        """
        res = []
        node = self.levels[0]
        while node:
            while node.next and node.next.val < target:
                node = node.next
            res.append(node)
            node = node.down        
        return res

    def search(self, target: int) -> bool:
        last = self._find_just_smaller(target)[-1]
        return last.next and last.next.val == target

    def add(self, num: int) -> None:
        res = self._find_just_smaller(num)
        prev = None
        for i in range(len(res)-1, -1, -1):  # If you add a node in a level, all levels after that also need to be added
            node = Node(num)
            node.next = res[i].next
            node.down = prev        # "down" pointer must target to their next level counterpart
            res[i].next = node
            prev = node
            
            # The purpose of coin toss is to ensure that each node at current level will be 
            # duplicated to its upper level with a probability of 0.5, 
            # so the number of nodes at the upper level is roughly half of the current level.
            # So in the extreme case, SkipList is equivalent to a balanced binary search tree.
            # that is why add, erase and search can be O(logn)
            rand = random.randrange(0, 10)  
            if rand >= 5:
                break

    def erase(self, num: int) -> bool:
        """
        locate where the node is, then remove the node
        """
        found = False
        res = self._find_just_smaller(num)
        for i in range(len(res)):
            if res[i].next and res[i].next.val == num:
                res[i].next = res[i].next.next      # remove the node
                found = True
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
