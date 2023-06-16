from collections import deque

n = int(input())
input_arr = deque()
count = 0
inputNum = ""
for i in range(2*n):
    if i < n :
        input_arr.append(str(input()))
    else :
        if i == n :
            inputNum = input_arr.popleft()
        outNum = str(input())
        if inputNum != outNum :
            count +=1
            input_arr.remove(outNum)
        else :
            if i < (2*n-1) :
                inputNum = input_arr.popleft()
print(count)

