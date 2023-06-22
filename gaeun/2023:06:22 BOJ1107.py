import sys
buttonStatus = [ True for i in range(10) ]
#희망하는 채널
num = int(sys.stdin.readline())

#위,아래 버튼만으로 조작
upDownCount = abs(num-100)

#고장난 버튼 수
brokenBttCount = int(sys.stdin.readline())
#고장난 버튼 리스트
if brokenBttCount > 0 :
    brokenBtts = list(map(int,sys.stdin.readline().split()))
else :
    print(min(upDownCount,len(str(num))))
    exit()
    
#고장난 버튼 False로 변경
for i in brokenBtts :
    buttonStatus[i] = False
#100000번까지 숫자를 만들어, +,-로 num 채널까지 이동
for i in range(1000001):
    numStr = str(i)
    for j in range(len(numStr)):
        if not buttonStatus[int(numStr[j])] :
            break
        elif j == len(numStr) -1:
            upDownCount = min(upDownCount,abs(num-i)+len(numStr))

print(upDownCount)