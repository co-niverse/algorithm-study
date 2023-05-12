num = int(input())
answer = 0
for i in range(1, num+1):
    number = list(map(int,str(i)))
    if i < 100:
        answer += 1
    elif number[0]-number[1] == number[1]-number[2]:
        answer += 1
print(answer)
