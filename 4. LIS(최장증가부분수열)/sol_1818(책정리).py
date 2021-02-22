import sys


def binSearch(target, dp):
    left, right = 0, len(dp) - 1
    while left < right:
        mid = (left + right) // 2
        if target < dp[mid]:
            right = mid
        else:
            left = mid + 1
    dp[left] = target


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
dp = [arr[0]]
for i in range(1, N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        binSearch(arr[i], dp)
print(N - len(dp))
