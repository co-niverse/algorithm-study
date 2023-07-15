import sys
readline = sys.stdin.readline
N,M,K = map(int,readline().split())
board = [ [ [] for _ in range(N)] for _ in range(N)]
locations = []

#위 , 오른쪽 대각선
dr = [-1,-1,0,+1,+1,+1,0,-1]
dc = [0,+1,+1,+1,0,-1,-1,-1]
nextlovations = {}
def move():
    global nextlovations
    newLovations = {}
    #파이어볼 이동
    for loc in nextlovations :
        r = loc[0]
        c = loc[1]
        for info in nextlovations[loc]:
            m = info[0]
            s = info[1]
            d = info[2]
            nextR = (r + dr[d] * s) % N 
            nextC = (c + dc[d] * s) % N

            if  not (nextR,nextC) in newLovations:
                newLovations[(nextR,nextC)] = [[m,s,d]]
            else :
                newLovations[(nextR,nextC)].append([m,s,d])

    nextlovations = newLovations.copy()

    diviedfireball()


def diviedfireball():
    newLovations = {}
    global nextlovations
    #중복된 파이어볼 나누기
    for loc in nextlovations :
        r = loc[0]
        c = loc[1]
        m = 0
        s = 0
        even = 0
        oddNum = 0
        direct = []
        if len(nextlovations[loc]) > 1 :
            for fb in nextlovations[loc]:
                m+=fb[0]
                s+=fb[1]
                if (fb[2]%2) == 0 :
                    even+=1
                else :
                    oddNum +=1
            #방향 구하기
            if even == len(nextlovations[loc]) or oddNum == len(nextlovations[loc]):
                direct = [0,2,4,6]
            else :
                direct = [1,3,5,7]
            m = m // 5
            s = s // len(nextlovations[loc])
            if m != 0 :
                for dir in direct:
                    # nextR = (r + dr[dir] * s) % N 
                    # nextC = (c + dc[dir] * s) % N
                    # newLovations[(r,c)].append([m,s,dir])
                    if  not (r,c) in newLovations:
                        newLovations[(r,c)] = [[m,s,dir]]
                    else :
                        newLovations[(r,c)].append([m,s,dir])
        else :
            newLovations[(r,c)] = nextlovations[loc]
    
    nextlovations = newLovations.copy()

        

for _ in range(M):
    fireball =list(map(int,readline().split()))
    fireball[0]-=1
    fireball[1]-=1
    r = fireball[0]
    c = fireball[1]
    if  not (r,c) in nextlovations:
        nextlovations[(r,c)] = [[fireball[2],fireball[3],fireball[4]]]
    else :
        nextlovations[(r,c)].append([fireball[2],fireball[3],fireball[4]])

for _ in range(K) :
    move()
sumM = 0
for loc,fireball in nextlovations.items() :
    for fb in fireball:
        sumM+=fb[0]
print(sumM)

