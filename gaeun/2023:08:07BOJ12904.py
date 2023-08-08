import sys
S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())
size = len(T)
while size >len(S) :
    if T[size-1] == 'A':
        T.pop()
    else :
        T.pop()
        T.reverse()
    size -=1
if T == S :
    print(1)
else :
    print(0)
