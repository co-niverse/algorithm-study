from itertools import combinations
from sys import stdin

n, m = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

min_dist = 1e9
for comb in combinations(chicken, m):
    chicken_dist = 0

    for house_r, house_c in house:
        my_dist = 1e9
        for chicken_r, chicken_c in comb:
            my_dist = min(my_dist, abs(house_r - chicken_r) + abs(house_c - chicken_c))
        chicken_dist += my_dist

    min_dist = min(min_dist, chicken_dist)

print(min_dist)

##########################
#    memory: 31256KB     #
#    time:   608ms       #
##########################