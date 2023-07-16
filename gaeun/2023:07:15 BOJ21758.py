import sys
readline = sys.stdin.readline
N = int(readline())
honeyArr = list(map(int,readline().split()))
# 꿀통이 가장 왼쪽에 위치했을 때
honeyBox = 0
firstBee = N -1
maxHoney = -1
sumHoneyFirst = sum(honeyArr[:firstBee])
sumHoneySecond = honeyArr[honeyBox]
for i in range(1,N-1):
    maxHoney = max(maxHoney,sumHoneyFirst+sumHoneySecond-honeyArr[i])
    sumHoneySecond+=honeyArr[i]

# 꿀통이 가운데 위치햇을 때
honeyBox = 1
firstBee = 0
secondBee = N -1
sumHoneyFirst = sum(honeyArr[firstBee+1:honeyBox+1])
sumHoneySecond = sum(honeyArr[honeyBox:secondBee])
for i in range(1,N-1):
    maxHoney = max(maxHoney,sumHoneyFirst+sumHoneySecond)
    sumHoneyFirst+=honeyArr[i+1]
    sumHoneySecond-=honeyArr[i]

# 꿀통이 가장 오른쪽에 위치했을 때
honeyBox = N -1
firstBee = 0
sumHoneyFirst = sum(honeyArr[firstBee+1:])
sumHoneySecond = sum(honeyArr[firstBee+2:honeyBox+1])
for i in range(1,N-1):
    maxHoney = max(maxHoney,sumHoneyFirst+sumHoneySecond-honeyArr[i])
    sumHoneySecond-=honeyArr[i+1]
print(maxHoney)