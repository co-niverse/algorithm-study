import sys
readline = sys.stdin.readline
N,T = map(int,readline().split())
study = [0] * (T+1)
for i in range(N) :
    line = list(map(int,readline().split()))
    for node in range(T,line[0]-1,-1) :
        study[node] = max(study[node],study[node-line[0]]+line[1])

print(study[T])
