# import sys
# from collections import deque
# readline = sys.stdin.readline
# n = int(readline())
# crains = list(map(int,readline().split()))
# m = int(readline())
# weights = list(map(int,readline().split()))
# crains.sort(reverse=True)
# weights.sort(reverse=True)
# weight=deque(weights)
# count=0
# flag = False


# if weights[0] > crains[0] :
#     print(-1)
#     sys.exit()

# crainBox = [0]*n
# newWeight = []
# minValue = 1e9
# while weight :
#     #새로운 박스
#     w = weight.popleft()
#     nop = 0
#     flag = True
#     # 옮길 크레인
#     for c in range(len(crains)) :
#         #현재 크레인에 옮길 수 있는지 여부
#         if crains[c] >= w  :
#             #두번째 크레인 ~ 마지막 크레인
#             if minValue > crainBox[c]:
#                 crainBox[c]+=1
#                 minValue = crainBox[c]
#                 flag = False
#                 break
#         elif crains[c] < w :
#             break
#     if flag :
#         w = weight.appendleft(w)
#         minValue = max(crainBox)
        



# print(max(crainBox))

import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt = 0

if boxes[0] > cranes[0]: cnt = -1
else:
    while boxes:
        for c in cranes:
            # 무게를 감당하는 크레인이 없을 때 ,
            if boxes and c < boxes[-1]:
                continue
            for b in boxes:
                # 박스 무게를 감당할 수 있는 크레인
                if c >= b:
                    boxes.remove(b)
                    break
        cnt+=1
        
print(cnt)