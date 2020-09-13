def findK(A, B):
    if not A or not B or len(A) <= 1 or len(B) <= 1:
        return 0

    preA, preB = [0 for _ in range(len(A) + 1)], [0 for _ in range(len(B) + 1)]
    for i in range(len(A)):
        preA[i+1] = preA[i] + A[i]
        preB[i+1] = preB[i] + B[i]

    # print(preA)
    # print(preB)

    cnt = 0
    for i in range(1, len(preA) - 1):
        if preA[i] == preA[-1] - preA[i] == preB[i] == preB[-1] - preB[i]:
            cnt += 1
    return cnt


print(findK([4,-1,0,3], [-2,5,0,3]))            # 2
print(findK([2,-2,-3,3], [0,0,4,-4]))           # 1
print(findK([4,-1,0,3], [-2,6,0,4]))            # 0
print(findK([3,2,6], [4,1,6]))                  # 0
print(findK([1,4,2,-2,5], [7,-2,-2,2,5]))       # 2
