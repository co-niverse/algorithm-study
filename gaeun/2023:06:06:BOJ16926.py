import sys
n,m,R = map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    arr.append(line)

value = min(n,m)//2
for _ in range(R):
    for mIndex in range(value): 
        # 좌우
        #이동할 노드
        nodeLeft = arr[mIndex][m-mIndex-1]
        nodeRight = arr[n-1-mIndex][mIndex]
        for r in range(mIndex,m-mIndex):
            #<-
            if r == m-mIndex-1 :
                break
            nextLeftNode = arr[mIndex][m-2-r]
            arr[mIndex][m-2-r] = nodeLeft
            nodeLeft = nextLeftNode
            #->
            if r == m-mIndex-1:
             
                break
            nextRightNode = arr[n-mIndex-1][r+1]
            arr[n-mIndex-1][r+1] = nodeRight
            nodeRight = nextRightNode 

        #상하
        for d in range(mIndex,n-mIndex):
            #아래
            if d == n-mIndex-1:
                # node = arr[d][mIndex]
                break
            nextLeftNode = arr[d+1][mIndex]
            arr[d+1][mIndex] = nodeLeft
            nodeLeft = nextLeftNode
            #위로
            if d == n-mIndex-1 :
                break
            nextRightNode = arr[n-2-d][m-1-mIndex]
            arr[n-2-d][m-1-mIndex] = nodeRight
            nodeRight = nextRightNode


for line in arr:
    print(" ".join(map(str,line)))

