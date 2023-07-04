# 1차 풀이
import sys
input = sys.stdin.readline
from collections import deque

prefix = input()

# 연산자 stack
op = deque()

# 피연산자 stack
num = deque()

# 괄호 stack
op_two = deque()
num_two = deque()

for i in range(len(prefix)):
  if prefix[i] == ")":
    new = num.pop()
    new_two = num.pop() + new # BC
    new_two += op.pop() # BC+
    op.pop() # 
    num.append(new_two)
  elif prefix[i] == "(":
    op.append(prefix[i])
  elif prefix[i] =="*" or prefix[i] == "/":
    if prefix[i+1] == "(":
        op.append(prefix[i])
    else:
        op.append(prefix[i])
        new = num.pop()
        new += prefix[i+1]
        new += op.pop()
        num.append(new)
  elif prefix[i] == "-" or prefix[i] == "+":
    op.append(prefix[i])
  elif prefix[i] == "\n":
    continue
  elif prefix[i-1] == "*" or prefix[i-1] == "/":
    continue
  else:
    num.append(prefix[i])
    
# 다 끝났으면 피연산자 2개, 연산자 1개 , .. 순으로 뽑기
answer = num.popleft()
for i in range(len(num)):
    answer += num.popleft()
    answer += op.popleft()

print(answer)

#### 2차 풀이
import sys
input = sys.stdin.readline

prefix = list(input())
stack = []
answer = ""

for i in prefix:
  if i.isalpha():
    answer += i
  else:
    if i == '(':
      stack.append(i)
    elif i == '*' or i =='/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        answer += stack.pop()
      stack.append(i)
    elif i =='+' or i =='-':
      while stack and (stack[-1] != '('):
        answer += stack.pop()
      stack.append(i)
    elif i == ')':
      while stack and stack[-1] != '(':
        answer += stack.pop()
      stack.pop()
      
while stack:
  answer += stack.pop()

print(answer)
