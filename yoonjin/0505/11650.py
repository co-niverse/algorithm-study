import sys
n = int(sys.stdin.readline())
dots = []

for _ in range(n):
    [x,y] = map(int,input().split())
    dots.append([x,y])

dots.sort()

for i in range(n):
    print(dots[i][0], dots[i][1])
