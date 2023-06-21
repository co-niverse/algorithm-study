


from itertools import combinations
arr = []
#집 위치
homeList = []
#치킨집 위치
chickenList = []

n,m = map(int,input().split())
for x in range(n):
    line = list(map(int,input().split()))
    arr.append(line)
    #집, 치킨집 위치 저장
    for  y in  range(len(line)) :
        if line[y] == 1 :
            homeList.append((x,y))
        elif line[y] == 2 :
            chickenList.append((x,y))

#m개의 치킨집 조합
chickenComb = combinations(chickenList,m)


resultDist = 9999999
#각 치킨집과 집의 거리를 합산
#조합별로 반복
for chicken in chickenComb :
    #총 거리 합
    cSum = 0
    for house in homeList :
        houseDist = 99999999999
        # 어떤 집이 가장 가까운 거리인지
        for ind in range(len(chicken)) :
            dist = abs(house[0]-chicken[ind][0])+abs(house[1]-chicken[ind][1])
            houseDist = min(houseDist,dist)
        cSum+=houseDist
    resultDist = min(resultDist,cSum)
print(resultDist)   