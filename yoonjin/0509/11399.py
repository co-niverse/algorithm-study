#1
n = int(input())
times = list(map(int,input().split()))
times.sort()
bigSum = 0

for i in range(len(times)+1):
  sum = 0
  for j in range(i):
    sum = sum + times[j]
  bigSum = bigSum + sum

print(bigSum)


#2
n = int(input())
times = list(map(int,input().split()))
times.sort()
bigSum = 0

for i in range(n):
  bigSum += sum(times[:i+1])

print(bigSum)
