import sys
sys.setrecursionlimit(10**9)
# n개의 노드
n = int(input())
#거리 측정
distance = [ 0 for _ in range(n+1)]
# 트리
tree = [[] for _ in range(n+1)]

#트리 저장하기
for _ in range(n-1):
    p , c , w = map(int,input().split())
    tree[p].append((c,w))
    tree[c].append((p,w))

#dfs로 탐색
def dfs(start,sumValue) : 
    #start 노드의 자식 노드 찾기
    nodes = tree[start]

    for node in nodes :
        #방문한 노드인지 확인
        if distance[node[0]] == 0 :
            #거리 구하기
            distance[node[0]] = sumValue + node[1]
            dfs(node[0],distance[node[0]])

#시작 노드 방문 표시
distance[1]= -1
#루트 노드에서 가장 먼 노드를 찾음
dfs(1,0)
firstNode = distance.index(max(distance))

distance = [ 0 for _ in range(n+1)]
distance[firstNode]= -1
#firstNode에서 가장 먼 노드를 찾는다.
dfs(firstNode,0)
print(max(distance))
