import sys
readline = sys.stdin.readline
N,K = map(int,readline().split())
students = list(map(int,readline().split()))

minusTall = [0]*(N-1)

for s in range(len(students)):
    if s == len(students)-1 :
        break
    minusTall[s] = students[s+1]-students[s]
minusTall.sort()
for k in range(K-1):
    minusTall.pop()
print(sum(minusTall))

