### 1차 풀이
import sys
input = sys.stdin.readline
from itertools import combinations

l,c = map(int, input().split())
words = list(input().split())

# 모음, 자음 분리
aeiou = ['a','e','i','o','u']
first = [] # 모음
second = [] # 자음

# 모음, 자음 분리해서 저장
for i in words:
  if i in aeiou:
    first.append(i)
  else:
    second.append(i)

answer = []

# 모음, 자음 몇 글자씩 들어갈지 결정
for i in range(1,l-1):
  if(i <= len(first) and (l-i) <= len(second)):
    first_num = i
    second_num = l-i
    # 조합 사용해서 문자열 만들기
    for first_str in combinations(first, first_num):
      for second_str in combinations(second, second_num):
        answer.append(first_str + second_str)

answer.sort()

# 출력
for i in answer:
  print(''.join(i))


### 2차 풀이
import sys
input = sys.stdin.readline
from itertools import combinations

l,c = map(int, input().split())
words = list(input().split())
# 입력 받고 나서 바로 정렬
words.sort()

aeiou = ['a','e','i','o','u']

# 조합으로 글자 뽑기
for str in combinations(words,l):
    # 모음, 자음 숫자 확인
    first_cnt = 0
    second_cnt = 0
    for i in str:
      if i in aeiou:
        first_cnt += 1
      else:
        second_cnt += 1
    # 숫자 맞으면 출력
    if(first_cnt >= 1 and second_cnt >=2):
        print(''.join(str))
