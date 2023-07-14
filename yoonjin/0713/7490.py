import sys
input = sys.stdin.readline
from itertools import product

T = int(input())
op = ['+','-',' ']

def printAnswer(n):
    line_list = []
    # 식 리스트 만들기
    for j in product(op, repeat=(n-1)): #j는 ['+','-',' ', ..] 리스트
        stack = []
        for i in range(n-1):
            stack.append(i+1)
            stack.append(j[i])
        stack.append(n)
        line = ''
        for i in stack:
            line += str(i)
        if (eval(line.replace(' ','')) == 0):
            line_list.append(line)
    #아스키 순서에 따라 출력
    line_list.sort()
    for i in line_list:
        print(i)
      
for i in range(T):
    n = int(input())
    printAnswer(n)
    print()
