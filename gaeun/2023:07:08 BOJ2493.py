import sys
n = int(sys.stdin.readline())
line = sys.stdin.readline()
topList=list(map(int,line.split()))
stack = []
result = ""
for t in range(n):
    height = topList[t]
    #앞에 다른 탑들이 존재
    if stack :
        
        while stack :
            target = stack[-1][1]
            target_h = stack[-1][0]
            #현재 탑보다 낮다면 
            if target_h < height :
                stack.pop()
                if len(stack) == 0 :
                    print(0, end=' ')
                    break
            #stack[-1][0] >= height일 때
            elif  target_h > height:
                print(target+1, end=' ')
                break
            else :
                print(target+1, end=' ')
                if target_h == height :
                    #이후에 도달할 일이 없음으로 미리 제거
                    stack.pop()
                break
        stack.append([topList[t],t])
    # 이 탑보다 앞에 있는 탑은 없음
    else :
        print(0, end=' ')
        stack.append([topList[t],t])



