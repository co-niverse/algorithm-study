# 첫번째 풀이 (시간초과)
n = int(input())

people = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0

for i in range(len(people)):
  people[i] = people[i] - b
  count += 1

for i in range(len(people)):
  while people[i] > 0:
    people[i] = people[i] - c
    count += 1

print(count)

# 두번째 풀이 (for, while 중첩 삭제)
n = int(input())

people = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0

for i in range(len(people)):
  people[i] = people[i] - b
  count += 1
  if people[i] > 0:
    count += people[i] // c
    people[i] = people[i] % c
    if people[i] > 0:
      count += 1

print(count)
