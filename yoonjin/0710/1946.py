## 1차(시간초과)
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
  num = int(input())
  score = []
  answer = 0
  for j in range(num):
    write, speak = map(int, input().split())
    score.append((write, speak))
  for write_t, speak_t in score:
    count = 0
    for l in range(num):
      if (write_t > score[l][0]) and (speak_t > score[l][1]):
        break
      else:
        count += 1
    if count == num:
      answer += 1
  print(answer)

## 2차(시간초과)
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
  num = int(input())
  write_score = []
  speak_score = []
  answer = 0
  for j in range(num):
    write, speak = map(int, input().split())
    write_score.append(write)
    speak_score.append(speak)
  for k in range(num):
    write_t = write_score[k]
    speak_t = speak_score[k]
    if (write_t == max(write_score)) and (speak_t == max(speak_score)):
      continue
    else:
      answer += 1
  print(answer)


## 최종
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    num = int(input())
    score = []
    for j in range(num):
        write, speak = map(int, input().split())
        score.append((write, speak))
    score.sort()
    hired = 1
    man = score[0][1]
    for j in range(1,num):
      if score[j][1] < man:
        man = score[j][1]
        hired += 1
    print(hired)
