n = int(input())
d = [[0]*10 for i in range(101)]
for i in range(1,10):
    d[0][i] = 1
for i in range (1,n):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]
    for j in range(1,9):
        d[i][j] = d[i-1][j-1] + d[i-1][j+1]
sum = 0
for i in range(10):
    sum += d[n-1][i]
    
print(sum%1000000000)
