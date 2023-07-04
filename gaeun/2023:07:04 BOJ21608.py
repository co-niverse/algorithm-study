n= int(input())
students = []
room = [[0 for _ in range(n)] for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
studentList = []
likeList = []
result = 0
for _ in range(n*n):
    line = list(map(int,input().split()))
    student = line[0]
    likeStudent = line[1:]
    studentList.append(student)
    likeList.append(likeStudent)
    like = -1
    blank = 0
    r,c = 0,0
    for i in range(n):
        for j in range(n):
            like_s = 0
            blank_s = 0
            #비어있는 칸인지 확인
            if room[i][j] == 0 :
                for k in range(4) :
                    if -1 < dr[k]+i < n and -1 < dc[k]+j < n :
                        #주변 좋아하는 칸
                        if room[dr[k]+i][dc[k]+j] in likeStudent :
                            like_s +=1
                        #주변 빈칸
                        elif room[dr[k]+i][dc[k]+j] == 0 :
                            blank_s +=1
            # 좋아하는 학생이 많은지
            # 좋아하는 사람이 많음
            if like < like_s :
                like = like_s
                blank = blank_s
                r =i
                c =j
            elif like == like_s :
                if blank < blank_s :
                    blank = blank_s
                    r =i
                    c =j
    room[r][c] = student


for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4) :
            if -1 < dr[k]+i < n and -1 < dc[k]+j < n :
               x = dr[k]+i
               y = dc[k]+j
               if room[x][y] in likeList[studentList.index(room[i][j])] :
                    count+=1
        if count == 1 :
            result +=1
        elif count ==2 :
            result+=10
        elif count == 3 :
            result +=100
        elif count == 4 :
            result +=1000

print(result)






# n = int(input())
# # students = [[]for _ in range((n*n)+1)]
# students = []
# room = [[0 for _ in range(n)] for _ in range(n)]
# seatStudent = [False for _ in range((n*n)+1) ]
# # 위 , 오른쪽 , 아래 ,왼쪽
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]
# nope=[]

# for _ in range(n*n):
#     line = list(map(int,input().split()))
#     # students[line[0]] = line[1:]
#     students.append([line[0],line[1:]])

# #첫 학생은 가운데
# # room[n//2][n//2] = students[0][0]
# # seatStudent[students[0][0]] = True

# def findLoveStudent(loveStudent):
#     ix, jx = 0,0
#     for i in range(n):
#         for j in range(n) :
#             if room[i][j] == loveStudent :
#                 ix = i
#                 jx = j
#                 break
#     return ix,jx

# def findNoSeat(r,c):
#     seats = []
#     for i in range(4):
#         if -1<r+i<n and -1<c+i<n :
#             if room[dr[r+i]][dc[c+i]] == 0 :
#                 seats.append([r+i,c+i])
#     return seats




# for studentInfo in students :
#     print("info",studentInfo)
#     student = studentInfo[0]
#     #좋아하는 학생의 위치를 찾음
#     seatList = []
#     seatCount = []
#     for loveStudent in studentInfo[1] :
#         #좋아하는 학생이 자리에 앉았는지 여부 확인
#         if seatStudent[loveStudent]:
#             r , c = findLoveStudent(loveStudent)
#         #좋아하는 학생 자리 주변에 빈 자리 추가
#             for s in findNoSeat(r,c) :
#                 if not s in seatList :
#                     seatList.append(s)
#                     seatCount.append(1)
#                 else :
#                    ind = seatList.index(s)
#                    seatCount[ind]+=1
#                 #    seatCount[seatCount.index(ind)]+=1
#     #좋아하는 학생과 인접한 자리 중 가장 많이 인접한 자리
#     popSeats = []
#     #1번 조건으로 통과 또는 2번 조건으로 넘긴다.
#     if len(popSeats) == 1 :
#         room[popSeats[0][0]][popSeats[0][1]] = studentInfo[0]
#         continue
#     elif len(popSeats) == 0:
#         for i in range(n):
#             for j in range(n):
#                 popSeats.append([i,j])
#     else : 
#         maxNum = max(seatCount)
#         for i,c in enumerate(seatCount) :
#             if c == maxNum :
#                 popSeats.append(seatList[i])

    

#     #많이 인접하는 자리가 여러개이면 인접한 칸 중 비어있는 자리가 많은 곳
#     maxSeat = []
#     maxNum = -1
#     for seat in popSeats :
#         count = 0
#         for i in range(4):
#             if -1<seat[0]+dr[i]<n and -1<seat[1]+dc[i]<n :
#                 rx = seat[0]+dr[i]
#                 dx = seat[1]+dc[i]
#                 if room[rx][dx] == 0 :
#                     count +=1
#         if count > maxNum :
#             maxNum = count
#             maxSeat = []
#             maxSeat.append(seat)
#         elif count == maxNum :
#             maxSeat.append(seat)
#     #가장 행과 열이 가장 작은 칸
#     for i in range(len(maxSeat)):
#         if maxSeat[i] in nope :
#             maxSeat.remove(maxSeat[i])
    
#     maxSeat.sort()
#     r,c = maxSeat[0]
#     room[r][c] = studentInfo[0]
#     seatStudent[studentInfo[0]] = True
#     nope.append([r,c])

# result = 0
# students.sort()
# for i in range(n):
#     for j in range(n):
#         num = room[i][j]
#         count = 0
#         for x in range(4):
#             if -1 < i+dr[x] < n and -1 < j+dc[x] < n :
#                 print("students[num-1][1] :" , students[num-1][1])
#                 if room[i+dr[x]][j+dc[x]]  in students[num-1][1] :
#                     count +=1
#         if count == 1 :
#             result+=1
#         elif count == 2 :
#             result+=10
#         elif count == 3 :
#             result+=100
#         elif count == 4 :
#             result+=1000


# print(result)
        



    

    


       


# #index로 찾음
# #dx,dy로 4방향 중 비었는지 확인
# #빈자리 리스트에 추가
# #리스트에 추가된 자리 중 4방향 비었는지 확인
# #비어있는 자리가 동일하면 r,c순으로 정렬