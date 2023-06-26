from collections import deque


n,k = map(int,input().split())
aArray = list(map(int,input().split()))

# 내구도 0 이상인 것 count
zeroCount = aArray.count(0)

#로봇 위치
robbotArray = [False for _ in range(n)]
robbotQ = deque(robbotArray)
#벨트 내구도
queue = deque(aArray)


i = 0
while zeroCount < k  :
    i +=1

    # 벨트와 로봇 같이 회전하기
    lastBelt = queue.pop()
    queue.appendleft(lastBelt)

    lastrobbot = robbotQ.pop()
    robbotQ.appendleft(False)

    #로봇 이동
    for r in range(len(robbotQ)-1,0,-1) :
        #n번째 로봇이 있으면 내리기
        if r == n-1 :
            robbotQ[r] = False
        # 로봇 이동
        elif robbotQ[r] and (queue[r+1] > 0) and robbotQ[r+1]==False  :
            queue[r+1]-=1
            robbotQ[r]= False
            robbotQ[r+1] = True
            if queue[r+1] == 0 :
                zeroCount +=1
    
    #로봇 올리기
    if queue[0] > 0  and robbotQ[0] == False :
        robbotQ[0] = True
        queue[0] -=1
        if queue[0] == 0 :
                zeroCount +=1

print(i)