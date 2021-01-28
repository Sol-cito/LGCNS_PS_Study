import sys

# 시간복잡도 : O(N) - 주어진 연산자 넣는 공간 * 연산자 개수

def recursion(arr, operators, arrIdx, res):
    if arrIdx == len(arr) - 1:
        res[0] = max(res[0], arr[-1])
        res[1] = min(res[1], arr[-1])
        return
    for j in range(len(operators)):
        if operators[j] > 0:
            operators[j] -= 1
            temp = arr[arrIdx + 1]
            if j == 0:
                arr[arrIdx + 1] = arr[arrIdx] + temp
            elif j == 1:
                arr[arrIdx + 1] = arr[arrIdx] - temp
            elif j == 2:
                arr[arrIdx + 1] = arr[arrIdx] * temp
            else:
                arr[arrIdx + 1] = int(arr[arrIdx] / temp)
            recursion(arr, operators, arrIdx + 1, res)
            arr[arrIdx + 1] = temp
            operators[j] += 1


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
operators = list(map(int, sys.stdin.readline().split(" ")))
res = [-100000001, 100000001]
recursion(arr, operators, 0, res)
print(res[0])
print(res[1])
