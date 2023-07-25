import sys
input = sys.stdin.readline

N, K = map(int, input().split())
students = list(map(int, input().split()))

# 차이 저장
sub = []
for i in range(1, N):
    sub.append(students[i] - students[i-1])

# 차이 정렬
sub.sort()

# 큰 숫자 pop
for i in range(K-1):
    sub.pop()

print(sum(sub))
