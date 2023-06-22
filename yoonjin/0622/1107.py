## 1차
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
wrong = list(map(int, input().split()))

# number에 실행되는 숫자만 담기
for i in wrong:
  number.remove(i)

# n을 리스트로 바꾼다.
target = list(map(int,str(n)))

# target이 number에 있으면 숫자 증가, 없으면 number중 제일 근처 숫자로 대체하고 숫자 증가
count = 0
for i in range(len(target)):
  if target[i] not in number:
    # number에서 제일 가까운 수 찾기
    min = 1e9
    near_num = 0
    for j in number:
      if min > abs(j - target[i]):
        min = abs(j - target[i])
        target[i] = j
  count += 1

# 타겟 숫자까지 가려면 몇번 눌러야하는지 구하기
target_num = ''.join(map(str, target))
target_num = int(target_num)
count = count + abs(target_num - n)

print(count)

## 2차
