## 1차 풀이 (오답)
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
success = 0

while(len(S) < len(T)):
  if (S == T):
    print(1)
    break
  S = S + 'A'
  if (S == T):
    print(1)
    success = 1
    break
  S = S[::-1] + 'B'

if success == 0:
  print(0)

## 2차 풀이 (정답)
import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
success = 0

while (len(T) > 0):
  if (S == T):
    print(1)
    success = 1
    break
  if (T[-1] == 'A'):
    T.pop()
  elif (T[-1] == 'B'):
    T.pop()
    T = T[::-1]

if (success == 0):
  print(0)
