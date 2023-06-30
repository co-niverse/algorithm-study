n , m = map(int,input().split())
r,c,d = map(int,input().split())
room = []
for _ in range(n):
    room.append(list(map(int,input().split())))

#북,동,남,서
dx = [0,1,0,-1]
dy = [-1,0,+1,0]
room[r][c] = 2
count = 1
while True :
    flag = False
    nextD = d
    for i in range(4):
        nextD = (nextD+3) % 4
        nextR = r+dy[nextD]
        nextC = c+dx[nextD]
        if -1 < nextR < n and -1 < nextC < m : 
            if room[nextR][nextC] == 0 :
                room[nextR][nextC] = 2
                count +=1
                r = nextR
                c = nextC
                d = nextD
                flag = True

    # 4방향 다 청소되어 있을 때 
    if not flag :
        #북쪽을 바라보고 있을 때 
        if d == 0 :
            nextR = r+dy[2]
            nextC = c+dx[2]
            
        # 동쪽
        elif d == 1 :
            nextR = r+dy[3]
            nextC = c+dx[3]
            
        # 남쪽
        elif d == 2 :
            nextR = r+dy[0]
            nextC = c+dx[0]
            
        # 서쪽
        elif d == 3 :
            nextR = r+dy[1]
            nextC = c+dx[1]

        if -1 < nextR < n and -1 < nextC < m :
            if room[nextR][nextC] == 1 :
                print(count)
                break
            # 후진
            else : 
                r = nextR
                c = nextC




     