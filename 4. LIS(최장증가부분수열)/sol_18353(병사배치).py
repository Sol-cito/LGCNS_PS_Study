import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
dp = [0] * N
dp[-1] = 1
for i in range(N - 2, -1, -1):
    maxVal = 0
    for j in range(i + 1, N):
        if arr[i] > arr[j]: maxVal = max(maxVal, dp[j])
    dp[i] = maxVal + 1
print(N - max(dp))
