import sys

''' 
1. 먼저 트라이 구조를 재귀로 생성한다.
2. 루트에서 출발하여 해당 node의 linkedNodes를 보면서 재귀를 내려가는데,
3. 만약 linkedNodes에 현재 노드(input으로 받은 arr와 arr의 idx로 구분)가 없다면, 새 노드를 만들어 연결해야 한다는 의미이다.
4. 트라이 구조 생성 후 다시 dfs를 타면서 각 노드의 name을 출력해주면 되는데, 
5. 이 때 사전순이 되어야 하므로 sorted()함수로 key값을 lambda로 name으로 설정하여 출력해준다.

시간복잡도 : O(노드 개수 * 노드에 달려있는 linkedNode의 개수) = ?
AC : 72ms
'''


#  트라이 노드
class Node:
    def __init__(self, name, linked):
        self.name = name
        self.linked = linked


#  트라이 구조 생성하는 DFS
def dfs(arr, idx, node):
    for linkedNode in node.linked:
        if linkedNode.name == arr[idx]:
            return dfs(arr, idx + 1, linkedNode)
    return [idx, node]


#  트라이 재귀로 출력 - 출력 시 sorted() 함수로 알파벳 정렬
def printTrie(node, bars):
    if node.name != 0:
        print("--" * bars + node.name)
    node.linked = sorted(node.linked, key=lambda node: node.name)
    for linkedNode in node.linked:
        printTrie(linkedNode, bars + 1)


n = int(sys.stdin.readline())
root = Node(0, [])
for _ in range(n):
    arr = list(map(str, sys.stdin.readline().rstrip().split(" ")))[1:]
    dfsRes = dfs(arr, 0, root)
    nextLinkedNode = dfsRes[1]
    for i in range(dfsRes[0], len(arr)):
        node = Node(arr[i], [])
        nextLinkedNode.linked.append(node)
        nextLinkedNode = node
printTrie(root, -1)
