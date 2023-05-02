def binary(n,k) :
    Max_len=0
    high=max(lines)
    low=0
    mid=high
    while mid>=low and high>=mid :
        count=0
        for value in lines:
            count+=value//mid
        if count<n:
            high=mid-1   
        elif count>=n:
            if Max_len<=mid:
                Max_len=mid
            low=mid+1
        if high>=0 and low>=0:
            mid=(high+low)//2
    return Max_len
    




k,n = map(int, input().split())

lines = []
for i in range(k):
    value = int(input())
    lines.append(value)

          
print(binary(n,k))         