h,w = map(int,input().split())
blocks = list(map(int,input().split()))
result = 0
count = 0

for i in range(1,w-1):
    leftMax = max(blocks[:i])
    rightMax = max(blocks[i:])
    minHeight = min(leftMax,rightMax)
    if blocks[i] < minHeight :
        count+= minHeight-blocks[i]

print(count)


#첫번째 방법
# 가장 높이가 큰  블럭이 가운데 존재
start = -1
flag = False
for i in range(w) :
    if start == -1 and blocks[i] == 0 :
        continue
    elif start == -1 and blocks[i] > 0 :
        start = blocks[i]
    elif start != -1 :
        if blocks[i] < start :
            count+=start-blocks[i]
            flag = True
        elif blocks[i] >= start :
            if flag :
                result+=count
                start = blocks[i]
                flag = False
            else :
                start = blocks[i]

print(result)
