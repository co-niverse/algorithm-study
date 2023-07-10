def go(cnt, rlt):
    global ans
    if cnt == 10:
        ans = max(ans, rlt)
        return
    #중복순열 : 말 4개
    for i in range(4):
        # 말의 위치
        graph, pos = H[i]
        #다음 말 위치 
        nxt_graph, nxt_pos = graph, pos + D[cnt]
        #다음 말 위치 초기화
        #도착지점인 경우
        if graph == -1:
            continue
        #도착지점까지 4번 코스로 경우
        if graph == 4 and len(G[graph]) <= nxt_pos:
            nxt_graph, nxt_pos = -1, -1
        #도착지점까지 0번 코스로 경우
        elif graph == 0 and len(G[graph]) + 1 <= nxt_pos:
            nxt_graph, nxt_pos = -1, -1
        #도착지점까지 1,2,3번 코스로 경우
        elif graph in [1, 2, 3] and pos == len(G[graph]) - 1 and D[cnt] == 5:
            nxt_graph, nxt_pos = -1, -1
        else:
            #다른 코스로 이동하는 경우
            if graph == 0 and (nxt_pos in [5, 10, 15, 20]):
                if nxt_pos == 5:
                    nxt_graph = 1
                    nxt_pos = 0
                elif nxt_pos == 10:
                    nxt_graph = 2
                    nxt_pos = 0
                elif nxt_pos == 15:
                    nxt_graph = 3
                    nxt_pos = 0
                else:
                    nxt_graph = 4
                    nxt_pos = 3
            
            elif graph in [1, 2, 3] and len(G[graph]) <= nxt_pos:
                nxt_graph, nxt_pos = 4, nxt_pos - len(G[graph])
            #다음 위치에 말이 있으면 continue
            if [nxt_graph, nxt_pos] in H:
                continue
        # 위치 이동
        H[i] = [nxt_graph, nxt_pos]
        #도착했을 경우
        if nxt_graph == -1:
            go(cnt + 1, rlt)
        else:
            go(cnt + 1, rlt + G[nxt_graph][nxt_pos])
        H[i] = [graph, pos]


D = list(map(int, input().split()))
H = [[0, 0]] * 4
#전체 다 돌았을 때
G1 = [i for i in range(0, 40, 2)]
#10과 20, 30을 시작점으로 하는 그래프
G2 = [10, 13, 16, 19]
G3 = [20, 22, 24]
G4 = [30, 28, 27, 26]
#공통으로 이동
G5 = [25, 30, 35, 40]
#전체 지도
G = [G1, G2, G3, G4, G5]
ans = 0
go(0, 0)
print(ans)