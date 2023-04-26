num = int(input())
for i in range(num):
    for j in range(i):
        print(" ",end='')
    for k in range(num-i):
        print("*",end='')
    print()
