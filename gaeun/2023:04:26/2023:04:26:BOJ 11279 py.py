import heapq
import sys
N = int(sys.stdin.readline())
heap = []
for i in range(0,N):
    num = int(sys.stdin.readline())
    if num == 0 :
        if heap :
            print(-heapq.heappop(heap))
        else :
            print(0)
    else :
        heapq.heappush(heap,-num)

