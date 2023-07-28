import sys
input = sys.stdin.readline

N, T = map(int,input().split())
subject = [0]
times = [0]

for i in range(N):
  K, S = map(int, input().split())
  subject.append(S)
  times.append(K)

# score값 저장
score = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, T+1):
    # 시간이 더 많아서 공부할 수 있는 과목이라면
    if times[i] <= j:
      score[i][j] = max(score[i-1][j], score[i-1][j-times[i]] + subject[i])
    # 아니라면
    else:
      score[i][j] = score[i-1][j]

print(score[N][T])
