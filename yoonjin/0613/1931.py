n = int(input())
time = []

for i in range(n):
  start, end = map(int, input().split())
  time.append([start, end])

time.sort(key = lambda x: x[0])
time.sort(key = lambda x: x[1])

last_end = 0
count = 0

for start, end in time:
  if start >= last_end:
    count += 1
    last_end = end

print(count)
