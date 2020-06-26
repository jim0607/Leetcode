class Heapq:

    def _swim(self, arr, k):
        """
        Move the smaller number up by exchange arr[k] with arr[k//2] until arr[k//2]<=arr[k] - O(logN)
        """
        while k > 0 and arr[(k - 1) // 2] > arr[k]:
            arr[(k - 1) // 2], arr[k] = arr[k], arr[(k - 1) // 2]   # Exchange arr[k] with arr[k//2] - swim up
            k = (k - 1) // 2

    def _sink(self, arr, k):
        """
        Move the larger number down by exchange min(arr[2*k], arr[2*k+1]) with arr[k] - O(logN)
        """
        while 2 * k + 1 < len(arr):
            j = 2 * k + 1
            if j + 1 < len(arr) and arr[j] > arr[j + 1]:     # find the min of arr[2*k] and arr[2*k+1]
                j += 1
            if arr[k] <= arr[j]:
                break
            arr[k], arr[j] = arr[j], arr[k]    # Exchange arr[k] with min(arr[2*k], arr[2*k+1]) - sink down
            k = j

    def heappush(self, arr, num):
        """
        Push a num into the heapq - O(logN)
        Step 1: add the num at the end of the arr
        Step 2: swim up to find a proper location for the new added num
        """
        arr.append(num)
        self._swim(arr, len(arr) - 1)

    def heappop(self, arr):
        """
        Pop the min num out of the heapq - O(logN)
        Step 1: exchange the min num (arr[0]) with the last num (arr[-1])
        Step 2: pop the new arr[-1] out of the arr
        Step 3: sink down to find a proper location for the new arr[0]
        """
        if not arr:
            raise IndexError()

        min_num = arr[0]
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
        self._sink(arr, 0)

        return min_num

    def heapify(self, arr):
        """
        Heapify一个list - O(N)
        从从n//2开始右往左遍历，每次遍历到一个root, 就把这个root的subtree sort成binary heap.
        如何sort呢？ 就用sink的方法把root sink到他该有的位置就可以了
        """
        for k in range(len(arr) - 1, -1, -1):
            self._sink(arr, k)

    def heap_sort(self, arr):
        """
        Sort an input array using heapSort in O(NlogN) time and O(1) space
        The algorithm is actually very similar with heappop: exchange with last item + sink down
        Step 1: heapify the input arr
        Step 2: exchange exchange the min num (arr[0]) with the last num (arr[-1])
                then sink down to find a proper location for the new arr[0]
        """
        self.heapify(arr)
        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            temp_arr = arr[:i]              # 这里必须用辅助数组, so space is O(N)
            self._sink(temp_arr, 0)         # 注意直接self._sink(arr[:i], 0) 并不会modify arr
            arr = temp_arr + arr[i:]        # 可以 modify _sink function as _sink(arr, start_idx, end_idx) 来实现O(1) space

        return arr[::-1]


if __name__ == "__main__":
    heapq = Heapq()
    nums = [2, 4, 1, 9, 5, 0, 8, 7, 3, 6]
    heapq.heapify(nums)
    print(nums)
    heapq.heappush(nums, 8)
    print(nums)
    heapq.heappush(nums, 0)
    print(nums)
    heapq.heappush(nums, 6)
    print(nums)
    for _ in range(len(nums)):
        print(heapq.heappop(nums), nums)

    nums = [2, 4, 1, 9, 5, 0, 8, 7, 3, 6, 3, 5, 2, 8, 6, 4, 0]
    sorted_nums = heapq.heap_sort(nums)
    print(sorted_nums)
