n = int(input())
tree = list(map(int,input().split()))
layble = [[] for _ in range(n)] 


def findTop(subTree,laybleNum):
    top = len(subTree)//2
    layble[laybleNum].append(subTree[top])
    laybleNum +=1;
    if laybleNum >= n:
        return
    #왼쪽트리
    findTop(subTree[:top],laybleNum)
    #오른쪽트리
    findTop(subTree[top+1:],laybleNum)



laybleNum = 0
findTop(tree,laybleNum)
for numbers in layble:
    result = " ".join(map(str, numbers))
    print(result) 
