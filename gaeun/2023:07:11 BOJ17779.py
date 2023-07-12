
def findScope(x,y,d1,d2):
    global minValue
    # 경계선
    for d1Ind in range(0,d1+1):
        #1번 경계선
        if scope[y-d1Ind][x+d1Ind] != -1 :
            scope[y-d1Ind][x+d1Ind] = -1
            sumPeople[4]+=city[y-d1Ind][x+d1Ind]
        #4번 경계선
        if  scope[y+d2-d1Ind][x+d2+d1Ind] != -1 :
            scope[y+d2-d1Ind][x+d2+d1Ind] = -1
            sumPeople[4]+=city[y+d2-d1Ind][x+d2+d1Ind]
    for d2Ind in range(0,d2+1):
        #2번 경계선
        if scope[y+d2Ind][x+d2Ind] != -1 :
            scope[y+d2Ind][x+d2Ind] = -1
            sumPeople[4]+=city[y+d2Ind][x+d2Ind]
        #3번 경계선
        if scope[y-d1+d2Ind][x+d1+d2Ind] != -1 :
            scope[y-d1+d2Ind][x+d1+d2Ind] = -1
            sumPeople[4]+=city[y-d1+d2Ind][x+d1+d2Ind]
    for r in range(n):
        #경계선이 없는 구역
        if not -1 in scope[r] :
            for c in range(n):
                if r< y-d1 and c <=x+d1 :
                    scope[r][c]=1
                    sumPeople[0]+=city[r][c]
                elif r< y-d1 and c > x+d1 :
                    scope[r][c]=2
                    sumPeople[1]+=city[r][c]
                elif r > y+d2 and c < x+d2 :
                    scope[r][c]=3
                    sumPeople[2]+=city[r][c]
                elif r > y+d2 and c >= x+d2 :
                    scope[r][c]=4
                    sumPeople[3]+=city[r][c]
        else :
        # 0 : 경계선을 아직 지나지 않음 1: 경계선 내부 범위 2 : 경계선 통과
            flag = 0
            for c in range(n):
                if scope[r][c] == -1 :
                    if flag == 0 :
                        flag = 1
                    elif flag == 1 :
                        flag = 2
                        continue
                    #위,아래 경계선 꼭지점
                    if r == y-d1 and c ==x+d1 :
                        flag = 2
                        continue    
                    elif r == y+d2 and c ==x+d2 :
                        flag = 2
                        continue
                    continue
                if flag == 0 :
                    if r < y :
                        scope[r][c] = 1
                        sumPeople[0]+=city[r][c]
                    elif r >= y :
                        scope[r][c] = 3
                        sumPeople[2]+=city[r][c]
                elif flag == 1 :
                    scope[r][c] = 5
                    sumPeople[4]+=city[r][c]
                elif flag == 2 :
                    if r <= y-d1+d2 :
                        scope[r][c] = 2
                        sumPeople[1]+=city[r][c]
                    elif r > y-d1+d2 :
                        scope[r][c] = 4
                        sumPeople[3]+=city[r][c]
    minus = max(sumPeople)-min(sumPeople)
    if minValue > minus :
        minValue = minus

            
            
import sys
readline = sys.stdin.readline
n = int(readline())
city = [[] for _ in range(n)]
scope = [[0 for _ in range(n)]for _ in range(n)]
sumPeople = [0]*5
minValue = 1e9
#도시 인구 입력
for i in range(n):
    city[i]=list(map(int,readline().split()))

#x,y,d1,d2 구함
for y in range(n):
    for x in range(n):
        for d1 in range(n):
            for d2 in range(n):
                if (d1+d2 < n-x) and (0 <= y-d1 <= y <= y+d2 < n ):
                    scope = [[0 for _ in range(n)]for _ in range(n)]
                    sumPeople = [0]*5
                    findScope(x,y,d1,d2)
print(minValue)
