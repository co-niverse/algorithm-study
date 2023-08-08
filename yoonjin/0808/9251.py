## 1차 풀이
import sys
input = sys.stdin.readline

first = list(input().rstrip())
second = list(input().rstrip())

one_first = first
one_second = second

two_first = second.copy()
two_second = first.copy()

first_answer = 0

while len(one_second) > 0 and len(one_first) > 0:
    word = one_second.pop()
    for i in range(len(one_first)-1,-1,-1):
      if word in one_first:
        if one_first[i] == word:
            first_answer += 1
            one_first.pop()
            break
        else:
            one_first.pop()

second_answer = 0

while len(two_second) > 0 and len(two_first) > 0:
    word = two_second.pop()
    for i in range(len(two_first)-1,-1,-1):
      if word in two_first:
        if two_first[i] == word:
            second_answer += 1
            two_first.pop()
            break
        else:
            two_first.pop()

print(max(first_answer, second_answer))




## 2차 풀이
import sys
input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

matrix = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])
