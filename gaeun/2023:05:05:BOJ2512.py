
n = int(input())
numList = list(map(int,input().split()))
money = int(input())
start = 0
end = max(numList)
if sum(numList)>money:
    while start <= end:
        sumNum = 0
        mid = (start+end)//2
        for i in range(n):
            if mid < numList[i] :
                sumNum +=mid
            else :
                sumNum+=numList[i]
        if sumNum > money :
            end = mid -1
        else :
            start = mid +1
                
    print(end)
else :
    print(end)