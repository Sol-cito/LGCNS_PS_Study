import sys, heapq


def getDijik(dijik, X):
    heap1, heap2 = [], []
    for i in range(len(dijik)):
        if dijik[X - 1][i] != 0: heapq.heappush(heap1, [dijik[X - 1][i], i])
        if dijik[i][X - 1] != 0: heapq.heappush(heap2, [dijik[i][X - 1], i])
    while heap1:
        pop = heapq.heappop(heap1)
        for i in range(len(dijik)):
            if dijik[pop[1]][i] + pop[0] < dijik[X - 1][i]:
                dijik[X - 1][i] = dijik[pop[1]][i] + pop[0]
                heapq.heappush(heap1, [dijik[X - 1][i], i])
    while heap2:
        pop = heapq.heappop(heap2)
        for i in range(len(dijik)):
            if dijik[i][pop[1]] + pop[0] < dijik[i][X - 1]:
                dijik[i][X - 1] = dijik[i][pop[1]] + pop[0]
                heapq.heappush(heap2, [dijik[i][X - 1], i])


N, M, X = map(int, sys.stdin.readline().split(" "))
dijik = [[100000001] * N for _ in range(N)]
for i in range(N): dijik[i][i] = 0
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    dijik[a - 1][b - 1] = min(dijik[a - 1][b - 1], c)
getDijik(dijik, X)
res = 0
for i in range(N):
    res = max(res, dijik[i][X - 1] + dijik[X - 1][i])
print(res)
