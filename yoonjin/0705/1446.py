import sys
input = sys.stdin.readline

n, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
distance = [i for i in range(d+1)]

# 0 부터 고속도로의 길이까지 반복하여 확인
for i in range(d+1):
    # 고속도로로 간 거리와 지름길로 간 거리 비교
    distance[i] = min(distance[i], distance[i-1]+1)

    # graph 돌면서 최단거리 찾아서 distance에 넣기
    for start, end, length in graph:
        if i == start and end <= d and distance[i] + length < distance[end]:
            distance[end] = distance[i] + length

# 맨 끝에꺼 출력
print(distance[d])
