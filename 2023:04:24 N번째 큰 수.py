
import heapq
n = int(input())
heap=[]

for i in range(0,n):
    line = list(map(int,input().split()))
    for num in line :
        if len(heap) < n :
            heapq.heappush(heap,num)
            continue
        if heap[0] < num :
            heapq.heappop(heap)
            heapq.heappush(heap,num)
        

print(heapq.heappop(heap))
