num = int(input())

for i in range(num):
    n = int(input())
    d = [0]*(n+1)
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        d[1] = 1
        d[2] = 2
        d[3] = 4
        for i in range(4,n+1):
            d[i] = d[i-3] + d[i-2] + d[i-1]
        print(d[n])
