n = int(input())
array = list(map(int, input().split()))
m = int(input())

start = 0
end = max(array)

while (start <= end):
  mid = (start + end) // 2
  total = 0
  for i in array:
    if i < mid:
      total += i
    else:
      total += mid
  if total > m:
    end = mid - 1
  else:
    start = mid + 1

print(end)
