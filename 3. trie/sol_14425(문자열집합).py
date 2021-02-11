import sys

''' 
Trie 솔루션
시간복잡도 : ??
AC : 4544ms(pypy3)
'''


class Node:
    def __init__(self, letter, linked, isEnd):
        self.letter = letter
        self.linked = linked
        self.isEnd = isEnd


def makeTrie(node, word, idx):
    if idx == len(word):
        node.isEnd = True
        return [-1, node]
    for linkedNode in node.linked:
        if word[idx] == linkedNode.letter:
            return makeTrie(linkedNode, word, idx + 1)
    return [idx, node]


def searchTrie(node, targetStr, idx, res):
    if idx + 1 == len(targetStr):
        return node.isEnd
    for linkedNode in node.linked:
        if linkedNode.letter == targetStr[idx + 1]:
            res = searchTrie(linkedNode, targetStr, idx + 1, res)
    return res


def trieSolution():
    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    trieArr = []
    [trieArr.append(sys.stdin.readline().rstrip()) for _ in range(N)]
    rootNode = Node(-1, [], False)
    for word in trieArr:
        trieRes = makeTrie(rootNode, word, 0)
        if trieRes[0] == - 1: continue
        nextLinkedNode = trieRes[1]
        for i in range(trieRes[0], len(word)):
            node = 0
            if i < len(word) - 1:
                node = Node(word[i], [], False)
            else:
                node = Node(word[i], [], True)
            nextLinkedNode.linked.append(node)
            nextLinkedNode = node
    res = 0
    for _ in range(M):
        if searchTrie(rootNode, sys.stdin.readline().rstrip(), -1, False): res += 1
    print(res)


''' 
Set 자료구조 솔루션
시간복잡도 : O(N + M)
AC : 160ms
'''


def setSolution():
    N, M = map(int, sys.stdin.readline().split(" "))
    setArr = set()
    [setArr.add(sys.stdin.readline()) for _ in range(N)]
    res = 0
    for _ in range(M):
        if sys.stdin.readline() in setArr: res += 1
    print(res)


if __name__ == '__main__':
    setSolution()
