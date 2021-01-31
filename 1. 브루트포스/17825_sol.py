import sys


# 브루트포스
# 재귀의 시간복잡도 : O(4^10) = 약 100만 -> 10번의 턴마다 4개의 말 중 하나를 움직일 수 있음

def move(pieceLocation, steps, valDic, nodeDic, blueSpots):
    # blueSpot에 있으면 그 쪽으로 이동
    for ele in blueSpots:
        if pieceLocation == ele[0]:
            pieceLocation = ele[1]
            steps -= 1
            break
    for i in range(steps):
        # 말이 끝에 도착했으면 바로 리턴
        if pieceLocation == 32: return [pieceLocation, 0]
        pieceLocation = nodeDic.get(pieceLocation)
    return [pieceLocation, valDic.get(pieceLocation)]


def play(turn, arr, pieces, valDic, nodeDic, blueSpots, total, res):
    # 마지막 턴에 종료
    if turn == 10:
        return total
    for i in range(len(pieces)):
        #  체스말이 맨 끝칸에 위치하면 그냥 continue
        if pieces[i] == 32: continue
        originalLocation = pieces[i]
        moveResult = move(pieces[i], arr[turn], valDic, nodeDic, blueSpots)
        pieces[i] = moveResult[0]
        # 놓으려고 하는 곳에 이미 다른 말이 있으면 continue (개수로 판단)
        isAlreadyThere = 0
        for j in range(len(pieces)):
            if pieces[i] == pieces[j] and pieces[i] != 32: isAlreadyThere += 1
        if isAlreadyThere > 1:
            pieces[i] = originalLocation
            continue
        total += moveResult[1]
        res = max(res, play(turn + 1, arr, pieces, valDic, nodeDic, blueSpots, total, res))
        total -= moveResult[1]
        pieces[i] = originalLocation
    return res


arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# 노드 연결 map
board = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5],
         [5, 6], [6, 7], [7, 8], [8, 9], [9, 10],
         [10, 11], [11, 12], [12, 13], [13, 14],
         [14, 15], [16, 17], [17, 18], [18, 19],
         [20, 21], [21, 19], [22, 23], [23, 24],
         [24, 19], [15, 28], [28, 29], [29, 30],
         [30, 31], [31, 27], [19, 25], [25, 26],
         [26, 27], [27, 32]]
# 노드의 value
vals = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30,
        13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 40, 32, 34, 36, 38, 0]
valDic = {}
nodeDic = {}
blueSpots = [[5, 16], [10, 20], [15, 22]]
for i in range(33):
    valDic[i] = vals[i]
for ele in board:
    nodeDic[ele[0]] = ele[1]
pieces = [0, 0, 0, 0]
print(play(0, arr, pieces, valDic, nodeDic, blueSpots, 0, 0))
