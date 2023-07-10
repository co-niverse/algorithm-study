import sys
t = int(sys.stdin.readline())
result = []
for _ in range(t):
    n = int(input())
    NumList = []
    for _ in range(n):
        NumList.append(list(map(int,sys.stdin.readline().split())))
    NumList.sort()
    target = NumList[0]
    count = 1
    for arr in NumList[1:] :
        if arr[1] < target[1] :
            count+=1
            target = arr
    result.append(count)
    print(count)
# for i in range(len(result)):
#     print(result[i])