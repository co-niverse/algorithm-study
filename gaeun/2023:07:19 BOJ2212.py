import sys
from collections import deque
readline = sys.stdin.readline
M = int(readline())
K = int(readline())
sensorList = list(map(int,readline().split()))
if K >= M :
    print(0)
    sys.exit()

distance = []

sensorList.sort()
for s in range(len(sensorList)-1) :
    distance.append(sensorList[s+1]-sensorList[s])

distance.sort()

for c in range(K-1):
    distance.pop()
print(sum(distance))