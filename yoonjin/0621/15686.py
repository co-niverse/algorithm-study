##1차 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

# 집 개수, 치킨 집 개수 계산
home_list = []
chicken_list = []
for i in range(n):
  for j in range(n):
    if (city[i][j] == 1):
      home_list.append([i,j])
    elif (city[i][j] == 2):
      chicken_list.append([i,j])

# 치킨 집마다 집에 대한 거리 계산
chicken_length = []
for i in range(len(chicken_list)):
  for j in range(len(home_list)):
    length = abs(chicken_list[i][0] - home_list[j][0]) + abs(chicken_list[i][1] - home_list[j][1])
    chicken_length[i][j] = length


##2차 풀이
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 집 개수, 치킨 집 개수 계산
home_list = []
chicken_list = []
for i in range(n):
  for j in range(n):
    if (city[i][j] == 1):
        home_list.append((i,j))
    elif (city[i][j] == 2):
        chicken_list.append((i,j))

answer = 1e9

for combi in combinations(chicken_list, m):
    total_distance = 0
    for r1, c1 in home_list:
        distance = 1e9
        for r2, c2 in combi:
            distance = min(distance, abs(r1-r2) + abs(c1-c2))
        total_distance += distance
    answer = min(answer, total_distance)

print(answer)
