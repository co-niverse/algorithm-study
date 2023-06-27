import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
op = list()

#operators 변환
for i in range(operators[0]):
    op.append('+')
for i in range(operators[1]):
    op.append('-')
for i in range(operators[2]):
    op.append('*')
for i in range(operators[3]):
    op.append('/')

total_max = -1e9
total_min = 1e9

# operators의 경우 - 순열로 구하기
for op_case in permutations(op, len(op)):
    total = numbers[0]
    # 연산 수행
    for i in range(1, n):
      if op_case[i-1] == '+':
        total += numbers[i]
      elif op_case[i-1] == '-':
        total -= numbers[i]
      elif op_case[i-1] == '*':
        total *= numbers[i]
      elif op_case[i-1] == "/":
        total = int(total / numbers[i])
    # 최대값, 최소값 찾기
    if total_max < total:
        total_max = total
    if total_min > total:
        total_min = total

print(total_max)
print(total_min)
