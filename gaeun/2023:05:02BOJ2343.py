import sys
input = sys.stdin.readline

n,m = map(int,input().split())
video = list(map(int,input().split()))



num = sum(video)

start = 0 
end = 99999999999999
result = num

while start<=end:
    mid = (start+end) // 2 
    if mid < max(video):
        start = mid + 1
        continue
    
    cnt = 1
    tmp = 0
    
    for i in range(len(video)):
        # 블루레이 용량이 넉넉한가
        if tmp + video[i] <= mid:
            tmp += video[i]
        # 그렇지 않으면 다음 블루레이에 넣기
        else:
            tmp = video[i]
            cnt += 1
    
    if cnt > m:
        start = mid + 1
        
    else:
        end = mid - 1
        result = min(result,mid)
print(result)
