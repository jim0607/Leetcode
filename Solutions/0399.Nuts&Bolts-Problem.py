"""
399. Nuts & Bolts Problem

Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts.

Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller. We will give you a compare function to compare nut with bolt.

Using the function we give you, you are supposed to sort nuts or bolts, so that they can map in order.

Example
Given nuts = ['ab','bc','dd','gg'], bolts = ['AB','GG', 'DD', 'BC'].

Your code should find the matching of bolts and nuts.

According to the function, one of the possible return:

nuts = ['ab','bc','dd','gg'], bolts = ['AB','BC','DD','GG'].

If we give you another compare function, the possible return is the following:

nuts = ['ab','bc','dd','gg'], bolts = ['BC','AA','DD','GG'].

So you must use the compare function that we give to do the sorting.

The order of the nuts or bolts does not matter. You just need to find the matching bolt for each nut.
"""





"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""

"""
螺帽螺母问题脱胎于排序问题，这里的特别之处在于需要通过两个array进行对应的排序。
这就需要利用一个array中的元素对另一个array进行partition，并反过来重复这一个过程，最终让两个array都满足comparator所定义的相同顺序。

这里要注意的是partition的变式，因为pivot并非来源当前array，只能通过一方元素作为基准，对另一个array进行partition。

核心在于：首先使用 nuts 中的某一个元素作为基准对 bolts 进行 partition 操作，随后将 bolts 中得到的基准元素作为基准对 nuts 进行 partition 操作。
"""
"""
将nuts和botls用quick sort排序成一一对应关系。
首先以bolts的左边界元素作为基准，对nuts进行排序。在nuts中寻找该bolt对应的nut，找到之后将该nut交换到其左边界，
然后以该nut为pivot进行quick sort，因为compare只能比较nut和bult，所以还是以之前的bolt作为基准，将比该bolt小的nut交换到前部，
将比该bolt大的nut交换到后部，最后将pivot填入到相遇的位置，并返回该位置。
与1类似，以1返回的位置的nut为基准，对bolt进行排序。最后将比该nut小的bolt放到前部，将比该nut大的bolt放到后部，将与该nut对应的bolt放到相遇位置。
这样就有1对nut和bolt一一对应，并且在数组中该nut之前的部分都是比它小的，之后的部分都是比它大的，bolt也是一样。
然后再重复1-2，递归地对前半部和后半部分进行quick sort。
"""

class Solution:
    def sortNutsAndBolts(self, nuts, bolts, compare):
        self.quick_sort(nuts, bolts, 0, len(nuts) - 1, compare.cmp)
        
    def quick_sort(self, nuts, bolts, start, end, cmp):
        if start >= end:
            return
        
        left, right = start, end
        idx = self.partition(bolts, left, right, nuts[(left + right) // 2], cmp)      # the pivot val for bolts is: nuts[(start+end)//2]
        self.partition(nuts, left, right, bolts[idx], cmp)            # the pivot val for nuts is: bolts[index] 
        
        self.quick_sort(nuts, bolts, start, idx - 1, cmp)
        self.quick_sort(nuts, bolts, idx + 1, end, cmp)
        
    def partition(self, arr, start, end, pivot, cmp):
        # step 1: 暂时把等于pivot的螺丝移到最前面去, 这是为了保证bolts和nuts进行的是同样的partition
        for i in range(start, end + 1):
            if cmp(arr[i], pivot) == 0 or cmp(pivot, arr[i]) == 0:
                arr[i], arr[start] = arr[start], arr[i]
                break
                
        # step 2: partition the rest of the arr
        left, right = start + 1, end  
        while left <= right:
            while left <= right and (cmp(arr[left], pivot) == -1 or cmp(pivot, arr[left]) == 1):
                left += 1
            while left <= right and (cmp(arr[right], pivot) == 1 or cmp(pivot, arr[right]) == -1):
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
        # step 3: 在partition之前暂时把等于pivot的螺丝移到最前面去了，现在把它移回它该有的位置
        # Now [start + 1,right] < pivot & [left, end] > pivot, Swap arr[start], arr[right] makes [start, right - 1] < pivot & [left, end] > pivot.
        arr[start], arr[right] = arr[right], arr[start]

        return right
