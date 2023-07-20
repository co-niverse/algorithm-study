import sys
from collections import deque
readline = sys.stdin.readline
N,S,M = map(int,readline().strip().split())
Vol = list(map(int,readline().split()))
volumes = [[False for _ in range(M+1)] for _ in range(N+1)]
result = -1

volumes[0][S] = True


for n in range(N):
    for m in range(0,M+1) :
        if volumes[n][m] :
            value = m + Vol[n]
            if -1 < value <= M:
                volumes[n+1][value] = True
            value = m - Vol[n]
            if -1 < value <= M:
                volumes[n+1][value] = True

for ind in range(M,-1,-1):
    if volumes[N][ind] :
        result = ind
        break
       

print(result)