## 1차 풀이
import sys
input = sys.stdin.readline

num = int(input())
top = list(map(int, input().split()))
answer = [0] * num

for i in range(len(top)):
  if i > 0:
    for j in range(i-1,-1,-1):
      if top[i] < top[j]:
        answer[i] = j+1
        break

print(*answer)

## 2차 풀이
import sys
input = sys.stdin.readline

num = int(input())
top = list(map(int, input().split()))
answer = [0] * num
stack = [] #stack에는 [인덱스, 높이]를 저장한다

for i in range(len(top)):
  while stack:
    if stack[-1][1] > top[i]: #stack 마지막에 저장되어 있는게 더 크면 answer에 저장
      answer[i] = (stack[-1][0] + 1)
      break
    else: #stack에 있는게 작으면 pop하고 지나가기 -> 추후 index에 대해서도 현재 높이보다 작은건 의미 없음
      stack.pop()
  stack.append([i, top[i]])

print(*answer)
