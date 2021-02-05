import sys


#  분할정복
def DandC(arr, p1, p2, res):
    if p1 == p2: return arr[p1]
    # 왼쪽 조각
    a = DandC(arr, p1, (p1 + p2) // 2, res)
    # 오른쪽 조각
    b = DandC(arr, (p1 + p2) // 2 + 1, p2, res)
    # 양쪽 범위에 끼여있는 경우의 최대 합 구해주기
    mid = (p1 + p2) // 2
    leftSum = rightSum = 0
    p1, p2 = mid, mid + 1
    leftMAX, rightMAX = arr[p1], arr[p2]
    while p1 >= 0:
        leftSum += arr[p1]
        leftMAX = max(leftMAX, leftSum)
        p1 -= 1
    while p2 < len(arr):
        rightSum += arr[p2]
        rightMAX = max(rightMAX, rightSum)
        p2 += 1
    res[0] = max(res[0], a, b, a + b, leftMAX + rightMAX)
    return a + b


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    res = [arr[0], 0]
    DandC(arr, 0, len(arr) - 1, res)
    print(res[0])


#  DP

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split(" ")))
    dp = [arr[0]]
    for i in range(1, len(arr)):
        if dp[-1] + arr[i] > arr[i]:
            dp.append(dp[-1] + arr[i])
        else:
            dp.append(arr[i])
    print(max(dp))
