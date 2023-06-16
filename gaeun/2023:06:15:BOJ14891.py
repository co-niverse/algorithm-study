gears = []


# arrow = -1(왼쪽),0(둘다),1(오른쪽)
def changeGear(num,direct,arrow):
    leftArrow = 0
    rightArrow = 0

    #자신
    if arrow == 2 :
        if direct == 1 :
            rotation.append([num,1])
        else :
            rotation.append([num,-1])


    # 왼쪽
    # 다른 극
    if (arrow ==2 or arrow == -1)and num>0:  
        if gears[num][6] != gears[num-1][2]:
            #시계 방향
            if direct == 1 :
                #반시계 방향으로
                rotation.append([num-1,-1])

                leftArrow = -1
            # 반시계 방향
            else :
                #시계 방향
                rotation.append([num-1,1])

                leftArrow = 1
            changeGear(num-1,leftArrow,-1)
    # 오른쪽
    if (arrow ==2 or arrow == 1) and num < 3 : 
        if gears[num+1][6] != gears[num][2]:
            #시계방향
            if direct == 1:
                #반시계 방향
                rotation.append([num+1,-1])

                rightArrow = -1
            #반시계 방향
            else :
                # 시계 방향
                rotation.append([num+1,+1])
                rightArrow = 1
            changeGear(num+1,rightArrow,1)









for _ in range(4) :
    gear =list(map(int,input()))
    gears.append(gear)
k = int(input())
for _ in range(k):
    rotation = []
    num , direct = map(int,input().split())
    changeGear(num-1,direct,2)
    for g in rotation :
        if g[1] == -1 :
            value = gears[g[0]].pop(0)
            gears[g[0]].append(value)
        else :
            value = gears[g[0]].pop(7)
            gears[g[0]].insert(0,value)

sumNum = 0
for i in range(4):
    if gears[i][0] == 1 :
        sumNum+=(1*(2**i))
print(sumNum)

    

    



