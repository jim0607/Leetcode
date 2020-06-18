Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Examples:

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
    


from heapq import heapify, heappop, heappush

def sort_k(nums, k):
    hq = []
    for i in range(k):
        hq.append(nums[i])

    heapify(hq)

    target_idx = 0
    for i in range(k, len(nums)):
        nums[target_idx] = heappop(hq)
        target_idx += 1
        heappush(hq, nums[i])

    while hq:
        nums[target_idx] = heappop(hq)
        target_idx += 1

if __name__ == "__main__":
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    sort_k(arr, k)
    print(arr)
