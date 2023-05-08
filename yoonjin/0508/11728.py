n, m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sumList = []

sumList = a + b
sumList.sort()


answer = ' '.join(map(str,sumList))
print(answer)
