num = int(input())
numbers = list(map(int,input().split()))
min = numbers[0]
max = numbers[0]
for i in numbers:
    if min > i:
        min = i
    if max < i :
        max = i

print(min, max)
