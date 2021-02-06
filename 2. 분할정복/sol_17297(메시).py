import sys


def find(idx, M, dp):
    if idx <= 1:
        return "Messi Gimossi"[M - 1]
    if M > dp[idx - 1] + 1:
        res = find(idx - 2, M - dp[idx - 1] - 1, dp)
    elif M < dp[idx - 1]:
        res = find(idx - 1, M, dp)
    else:
        return " "
    return res


M = int(sys.stdin.readline())
dp = [5, 13]
while dp[-1] < M:
    dp.append(dp[-2] + 1 + dp[-1])
res = find(len(dp) - 1, M, dp)
print("Messi Messi Gimossi" if res == " " else res)
