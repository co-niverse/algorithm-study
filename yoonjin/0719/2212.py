import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# 예외처리
if k >= n:
  print(0)
else:
  sensor = list(map(int, input().split()))

  # 센서 정렬
  sensor.sort()

  # 사이 거리 계산
  mid = []
  for i in range(1,n):
    mid.append(sensor[i]-sensor[i-1])

  # 사이 거리 정렬
  mid.sort(reverse=True)

  # 큰 순서로 k-1개 제외하고 더하기
  for i in range(k-1):
    mid.pop(0)

  # 남은 것들 합 구하기
  print(sum(mid))
