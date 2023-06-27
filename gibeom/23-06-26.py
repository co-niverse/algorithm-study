from sys import stdin
from collections import deque


def decrease(idx):
    global durability
    robot[idx] = True
    belt[idx] -= 1
    if belt[idx] == 0:
        durability += 1


n, k = map(int, stdin.readline().split())
belt = deque(map(int, stdin.readline().split()))
robot = deque([False] * n)
step, durability = 0, 0
while durability < k:
    belt.rotate()
    robot.rotate()
    robot[0] = False

    robot[-1] = False
    for i in range(n - 2, -1, -1):
        if not robot[i + 1] and robot[i] and belt[i + 1] > 0:
            robot[i] = False
            decrease(i + 1)

    if belt[0] > 0:
        decrease(0)
    step += 1

print(step)

##########################
#    memory: 34140KB     #
#    time:   2908ms      #
##########################
