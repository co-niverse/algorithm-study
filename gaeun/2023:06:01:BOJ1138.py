n = int(input())
records = list(map(int,input().split()))
result = [0]*n


for ind in range(n):
    big = 0
    for place in range(n):
        if result[place] == 0 and big < records[ind]:
            big +=1
        elif result[place]==0 and big==records[ind]:
            result[place] = ind+1
            break

print(" ".join(map(str,result)))