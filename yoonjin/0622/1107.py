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
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
wrong = list(map(int, input().split()))

# + - 만 사용해서 이동하는 경우
count = abs(100 - n)

# 리모컨으로 입력할 수 있는 모든 숫자
for nums in range(1000001):
    nums = str(nums)

    # 한개의 숫자 당 한자리씩
    for j in range(len(nums)):
        # 고장났으면 입력이 안되니까 break
        if int(nums[j]) in wrong:
            break
        # 안 고장났으면 타겟 숫자와의 차이 만큼이 최솟값
        elif j == len(nums) - 1:
            count = min(count, abs(int(nums) - n) + len(nums))

print(count)
