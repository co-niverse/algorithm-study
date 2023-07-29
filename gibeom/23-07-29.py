from sys import stdin
from collections import deque

n, m, r = map(int, stdin.readline().split())
array = [stdin.readline().split() for _ in range(n)]

q = deque()
result = [[0] * m for _ in range(n)]
for i in range(min(n, m) // 2):
    q.extend([row[i] for row in array[i : n - i - 1]])
    q.extend(array[n - i - 1][i : m - i - 1])
    q.extend([row[m - i - 1] for row in array[i + 1 : n - i][::-1]])
    q.extend(array[i][i + 1 : m - i][::-1])
    q.rotate(r)

    for k in range(i, n - i - 1):
        result[k][i] = q.popleft()
    for k in range(i, m - i - 1):
        result[n - i - 1][k] = q.popleft()
    for k in range(n - i - 1, i, -1):
        result[k][m - i - 1] = q.popleft()
    for k in range(m - i - 1, i, -1):
        result[i][k] = q.popleft()

for res in result:
    print(*res)

##########################
#    memory: 38224KB     #
#    time:   128ms       #
##########################
