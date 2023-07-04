from collections import deque
medium = input()
medium = list(medium)
stack = []
openList = []
result = ""
for s in medium :
    # 알파벳이면 문자열 추가
    if s.isalpha():
        result+=s
    elif s == "(":
        stack.append(s)
    elif s == ")" :
        while stack and (stack[-1]!="("):
            result +=stack.pop()
        stack.pop()
    elif s=="*" or s=="/" :
        while stack and (stack[-1]=="*" or stack[-1]=="/"):
            result +=stack.pop()
        stack.append(s)
    #연산자면 stack 추가
    elif s=="+" or s=="-":
        while stack and (stack[-1]=="*" or stack[-1]=="/") :
            result +=stack.pop()
        while stack and (stack[-1]=="+" or stack[-1]=="-") :
            result +=stack.pop()
        stack.append(s)


for _ in range(len(stack)) :
    result += stack.pop()

print(result)




# #괄호
# def findBracket() :
#     for i,s in enumerate(medium) :
#         #괄호 시작
#         if s == "(" :
#             #stack 추가
#             stack.appendleft(s)
#             #괄호 안에 내용 찾기
#             for m in medium[i+1:] :
#                 # 닫힘 괄호인 경우 괄호가 전부 닫히는지 확인
#                 if m == ")" :
#                     stack.popleft()
#                     #괄호가 전부 수거됐으면
#                     if len(stack) == 0 :

#                         medium[i] = findBracket(openList)
#                         break
#                     #괄호 수거가 안됨 , 괄호 안의 내용 추가
#                     else :
#                         openList.append(m)
#                 #괄호 안의 내용
#                 else:
#                     openList.append(m)
# #곱셈 , 나눗셈
# for i,s in enumerate(medium) :
#     if s == "*" or s == "/" :
#         medium[i-1] = [[medium[i-1],medium[i+1]],s]
#         medium.remove(i)
#         medium.remove(i+1)



# def solve(arr):
#     for i,s in enumerate(arr) :
#         #괄호 시작
#         if s == "(" :
#             #stack 추가
#             stack.appendleft(s)
#             #괄호 안에 내용 찾기
#             for m in arr[i+1:] :
#                 # 닫힘 괄호인 경우 괄호가 전부 닫히는지 확인
#                 if m == ")" :
#                     stack.popleft()
#                     #괄호가 전부 수거됐으면
#                     if len(stack) == 0 :
#                         break
#                     #괄호 수거가 안됨 , 괄호 안의 내용 추가
#                     else :
#                         openList.append(m)
#                 #괄호 안의 내용
#                 else:
#                     openList.append(m)
#             solve(openList)      
#         elif s == "*" or s == "/" :
#             medium[i-1] = [[medium[i-1],medium[i+1]],s]
#             medium.remove(i)
#             medium.remove(i+1)
#         elif s == "+" or s == "-" :




