import sys
from itertools import combinations
from collections import deque

sys.setrecursionlimit(10000000)


# 브루트포스
# 시간복잡도 : 궁수배치 MC3 * 총 진행 턴 횟수 N = O(M^3 * N)

def attack(arr, D, archerLocation, removeTarget):
    que = deque([archerLocation])
    visit = [[0] * len(arr[0]) for _ in range(len(arr))]
    while que:
        pop = que.pop()
        if pop[2] == D:
            return
        for dx, dy in [0, -1], [-1, 0], [0, 1]:
            if 0 <= pop[0] + dx < len(arr) and 0 <= pop[1] + dy < len(arr[0]) and visit[pop[0] + dx][pop[1] + dy] == 0:
                if arr[pop[0] + dx][pop[1] + dy] == 1:
                    removeTarget.append([pop[0] + dx, pop[1] + dy])
                    arr[pop[0] + dx][pop[1] + dy] = -1
                    return
                elif arr[pop[0] + dx][pop[1] + dy] == -1:
                    return
                else:
                    que.appendleft([pop[0] + dx, pop[1] + dy, pop[2] + 1])
                    visit[pop[0] + dx][pop[1] + dy] = 1


def recursion(arr, D, archers, enemies, res, enemyCnt):
    if enemyCnt == 0:
        return res
    removeTarget = []
    for archer in archers:
        attack(arr, D, [len(arr), archer - 1, 0], removeTarget)
    res += len(removeTarget)
    cnt = 0
    for target in removeTarget:
        arr[target[0]][target[1]] = 0
        cnt += 1
    for i in range(len(enemies)):
        if arr[enemies[i][0]][enemies[i][1]] == 1:
            if enemies[i][0] < len(arr) - 1:
                arr[enemies[i][0]][enemies[i][1]] = 0
                enemies[i] = [enemies[i][0] + 1, enemies[i][1]]
                arr[enemies[i][0]][enemies[i][1]] = 1
            else:
                arr[enemies[i][0]][enemies[i][1]] = 0
                cnt += 1
    return max(res, recursion(arr, D, archers, enemies, res, enemyCnt - cnt))


def arrCopy(arr):
    copied = [[0] * len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            copied[i][j] = arr[i][j]
    return copied


N, M, D = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
res = 0
for archers in list(combinations([i for i in range(1, M + 1)], 3)):
    copied = arrCopy(arr)
    enemies = []
    for i in reversed(range(len(arr))):
        for j in reversed(range(len(arr[0]))):
            if arr[i][j] == 1:
                enemies.append([i, j])
    res = max(res, recursion(copied, D, archers, enemies, 0, len(enemies)))
print(res)
