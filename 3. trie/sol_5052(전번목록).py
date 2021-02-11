import sys


class Node:
    def __init__(self, num, linkedArr, isEnd):
        self.num = num
        self.linkedArr = linkedArr
        self.isEnd = isEnd


def searchTrie(node, targetString, idx):
    if idx == len(targetString): return [-2, node]
    for linkedNode in node.linkedArr:
        if int(targetString[idx]) == linkedNode.num:
            if linkedNode.isEnd: return [-2, node]
            return searchTrie(linkedNode, targetString, idx + 1)
    return [idx, node]


for _ in range(int(sys.stdin.readline().rstrip())):
    root = Node(-1, [], False)
    res = "YES"
    n = int(sys.stdin.readline().rstrip())
    arr = []
    [arr.append(sys.stdin.readline().rstrip()) for _ in range(n)]
    for t in range(n):
        targetString = arr[t]
        searchRes = searchTrie(root, targetString, 0)
        if searchRes[0] == -2:
            res = "NO"
            break
        nextNode = searchRes[1]
        for i in range(searchRes[0], len(targetString)):
            node = 0
            if i == len(targetString) - 1:
                node = Node(int(targetString[i]), [], True)
            else:
                node = Node(int(targetString[i]), [], False)
            nextNode.linkedArr.append(node)
            nextNode = node
    print(res)
